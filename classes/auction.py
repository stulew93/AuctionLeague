from typing import Dict

from classes.team import Team
import requests


class Auction:

    def __init__(self, include_managers=False):
        self.teams = []
        self.players = {}
        self.transaction_log = []
        self.include_managers = include_managers
        self.initial_budget = 100

    def get_player_info_from_api(self):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

        r = requests.get(url)
        fpl_data = r.json()

        players = fpl_data['elements']
        positions = fpl_data['element_types']
        teams = fpl_data['teams']

        copy_keys = ["id", "first_name", "second_name", "web_name"]
        for player in players:
            player_formatted = {key: player[key] for key in copy_keys}
            position = next(pos for pos in positions if pos["id"] == player["element_type"])
            team = next(t for t in teams if t["id"] == player["team"])
            player_formatted["position"] = position["singular_name"]
            player_formatted["position_short"] = position["singular_name_short"]
            player_formatted["team"] = team["name"]
            player_formatted["team_short"] = team["short_name"]

            self.players[player_formatted["id"]] = player_formatted

        print('Player data loaded.')
        return None

    def add_team(self, name: str):

        if name in [team.name for team in self.teams]:
            print('Team name already exists.')
            return None
        else:
            new_team = Team(name=name, manager_required=self.include_managers)
            self.teams.append(new_team)
            return None

    def add_member_to_team(self, member_id: int, team: Team, price: int):

        player = self.players[member_id]  # TODO: Add in functionality for managers.
        team.add_squad_member(player, price)

        return None
