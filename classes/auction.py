from typing import Dict
import datetime

from classes.team import Team
import requests


class Auction:

    def __init__(self, include_managers=False):
        self.teams = []
        self.players = {}
        self.transaction_log = []
        self.include_managers = include_managers
        self.initial_budget = 100

    def get_player_info_from_api(self) -> None:
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

        r = requests.get(url)
        fpl_data = r.json()

        players = fpl_data['elements']
        positions = fpl_data['element_types']
        clubs = fpl_data['teams']

        copy_keys = ["id", "first_name", "second_name", "web_name"]
        for player in players:
            player_formatted = {key: player[key] for key in copy_keys}
            position = next(pos for pos in positions if pos["id"] == player["element_type"])
            club = next(c for c in clubs if c["id"] == player["team"])
            player_formatted["position"] = position["singular_name"]
            player_formatted["position_short"] = position["singular_name_short"]
            player_formatted["club"] = club["name"]
            player_formatted["club_short"] = club["short_name"]
            player_formatted["player_purchased"] = 0

            self.players[player_formatted["id"]] = player_formatted

        print('Player data loaded.')
        return None

    def add_team(self, name: str) -> None:

        if name in [team.name for team in self.teams]:
            print('Team name already exists.')
        else:
            new_team = Team(name=name, manager_required=self.include_managers)
            self.teams.append(new_team)

        return None

    def add_member_to_team(self, member_id: int, team: Team, price: int) -> None:

        player = self.players[member_id]  # TODO: Add in functionality for managers.
        team.add_squad_member(player, price)
        self.players[member_id]["player_purchased"] = 1

        timestamp = str(datetime.datetime.utcnow())
        transaction_info = {"player": player["web_name"],
                            "club": player["club_short"],
                            "team": team.name,
                            "price": price,
                            "timestamp": timestamp}
        self.transaction_log.append(transaction_info)
        return None

    def get_club_eligibility(self, member_id: int, team: Team) -> str:
        club_short = self.players[member_id]["club_short"]
        club_long = self.players[member_id]["club"]
        if club_short in team.club_count:
            if team.club_count == 3:
                return "Ineligible. Team already has three players from {}.".format(club_long)
        else:
            return ''

    def get_formation_eligibility(self, member_id: int, team: Team) -> str:
        num_gkp = len(team.goalkeeper)
        num_def = len(team.defenders)
        num_mid = len(team.midfielders)
        num_fwd = len(team.forwards)

        player_position = self.players[member_id]["position_short"]

        eligibility_reason = ''

        if team.squad_members_needed == 0:
            eligibility_reason = 'Ineligible. Squad is complete.'
        elif player_position == 'GKP':
            if num_gkp == 1:
                eligibility_reason = "Ineligible. Team already has a goalkeeper."
        elif player_position == 'DEF':
            if num_def + num_mid + num_fwd == 10:
                eligibility_reason = "Ineligible. Team already has 10 outfield players."
            elif num_def == 5:
                eligibility_reason = "Ineligible. Team already has five defenders."
            elif num_def + num_mid == 9:
                eligibility_reason = "Ineligible. Illegal formation."
        elif player_position == 'MID':
            if num_def + num_mid + num_fwd == 10:
                eligibility_reason = "Ineligible. Team already has 10 outfield players."
            elif num_def == 5:
                eligibility_reason = "Ineligible. Team already has five midfielders."
            elif num_def + num_mid == 9:
                eligibility_reason = "Ineligible. Illegal formation."
            elif num_mid + num_fwd == 7:
                eligibility_reason = "Ineligible. Illegal formation."
        elif player_position == 'FWD':
            if num_def + num_mid + num_fwd == 10:
                eligibility_reason = "Ineligible. Team already has 10 outfield players."
            elif num_fwd == 3:
                eligibility_reason = "Ineligible. Team already has three forwards."
            elif num_mid + num_fwd == 7:
                eligibility_reason = "Ineligible. Illegal formation."

        return eligibility_reason

    def get_team_eligibility(self, member_id: int, team: Team) -> Dict:
        formation_eligibility = self.get_formation_eligibility(member_id, team)
        club_eligibility = self.get_club_eligibility(member_id, team)

        if formation_eligibility != '':
            eligibility_reason = formation_eligibility
            eligibility_flag = 0
        elif club_eligibility != '':
            eligibility_reason = club_eligibility
            eligibility_flag = 0
        else:
            eligibility_reason = 'Eligible.'
            eligibility_flag = 1

        team_eligibility = {"eligibility_flag": eligibility_flag,
                            "eligibility_reason": eligibility_reason}

        return team_eligibility

    def get_teams_eligibility(self, member_id: int) -> Dict:

        teams_eligibility = {}

        for team in self.teams:
            team_eligibility = self.get_team_eligibility(member_id, team)
            teams_eligibility[team.name] = team_eligibility

        return teams_eligibility

    def nominate_player(self, member_id: int):
        if self.players[member_id]["player_purchased"] == 1:
            print("Player has already been purchased.")
        else:
            player = self.players[member_id]
            print("Player nominated: {0} {1} ({2}), {3}, {4}"
                  .format(player["first_name"], player["second_name"], player["web_name"],
                          player["position_short"], player["club"]))
            print(self.get_teams_eligibility(member_id))

        return None