from typing import Dict


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
        else:
            self.squad_members_needed = 11

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
                   "Goalkeeper: " + gk + "\n" \
                   "Defenders: " + defs + "\n" \
                   "Midfielders: " + mids + "\n" \
                   "Forwards: " + fwds

        return team_str

    def recalculate_max_spend(self):
        if self.squad_members_needed == 0:
            self.max_spend = 0
        else:
            self.max_spend = self.budget - self.squad_members_needed + 1
        return None

    def add_squad_member(self, member: Dict, price: int):

        position = member["position"]

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
            return

        self.squad_members_current += 1
        self.squad_members_needed -= 1
        self.budget -= price
        self.recalculate_max_spend()
