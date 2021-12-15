from typing import Dict
import requests


class Team:

    def __init__(self, name: str, manager_required: bool = 0):
        self.name = name
        self.budget = 100

        if manager_required == 1:
            self.max_spend = 89
        else:
            self.max_spend = 90

        self.squad_members_current = 0

        if manager_required == 1:
            self.squad_members_needed = 12
            self.final_squad_size = 12
        else:
            self.squad_members_needed = 11
            self.final_squad_size = 11

        if manager_required == 1:
            self.manager = []
        self.goalkeeper = []
        self.defenders = []
        self.midfielders = []
        self.forwards = []

    def __str__(self):

        gk = ', '.join([g["name"] for g in self.goalkeeper])
        defs = ', '.join([d["name"] for d in self.defenders])
        mids = ', '.join([m["name"] for m in self.midfielders])
        fwds = ', '.join([f["name"] for f in self.forwards])

        team_str = "Name: " + self.name + "\n" \
                   "Budget Remaining: £" + str(self.budget) + "m\n" \
                   "Squad Completion: " + str(self.squad_members_current) + "/" + str(self.final_squad_size) + "\n" \
                   "Goalkeeper: " + gk + "\n" \
                   "Defenders: " + defs + "\n" \
                   "Midfielders: " + mids + "\n" \
                   "Forwards: " + fwds

        return team_str

    def recalculate_max_spend(self):
        if self.squad_members_needed == 0:
            self.max_spend = 0
        else:
            self.max_spend = self.budget - (self.squad_members_needed - 1)
        return None

    def add_squad_member(self, member: Dict, price: int):

        position = member["position_short"]

        if position == 'MGR':
            self.manager.append(member)
        elif position == 'GK':
            self.goalkeeper.append(member)
        elif position == 'DEF':
            self.defenders.append(member)
        elif position == 'MID':
            self.midfielders.append(member)
        elif position == 'FWD':
            self.forwards.append(member)
        else:
            return None

        self.squad_members_current += 1
        self.squad_members_needed -= 1
        self.budget -= price
        self.recalculate_max_spend()

        print("Player added to squad.")
        return None


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
