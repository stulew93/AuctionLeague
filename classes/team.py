from typing import Dict


class Team:

    def __init__(self, name: str, manager_required: bool = 0):
        self.name = name
        self.manager_required = manager_required
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

        self.club_count = {}

        self.formation = [len(self.defenders),
                          len(self.midfielders),
                          len(self.forwards)]

    def __str__(self):

        if self.manager_required == 1:
            mgr = ', '.join([m for m in self.manager])
            manager_str = "Manager: " + mgr + "\n"
        else:
            manager_str = ''

        gk = ', '.join([g["first_name"] + ' ' + g["second_name"] for g in self.goalkeeper])
        defs = ', '.join([d["first_name"] + ' ' + d["second_name"] for d in self.defenders])
        mids = ', '.join([m["first_name"] + ' ' + m["second_name"] for m in self.midfielders])
        fwds = ', '.join([f["first_name"] + ' ' + f["second_name"] for f in self.forwards])

        team_str = "Name: " + self.name + "\n" \
                   "Budget Remaining: £" + str(self.budget) + "m\n" \
                   "Squad Completion: " + str(self.squad_members_current) + "/" + str(self.final_squad_size) + "\n" \
                   "Formation: " + str(self.formation) + "\n" \
                   + manager_str + \
                   "Goalkeeper: " + gk + " (" + str(len(self.goalkeeper)) + ")\n" \
                   "Defenders: " + defs + " (" + str(len(self.defenders)) + ")\n" \
                   "Midfielders: " + mids + " (" + str(len(self.midfielders)) + ")\n" \
                   "Forwards: " + fwds + " (" + str(len(self.defenders)) + ")"

        return team_str

    def recalculate_max_spend(self):
        if self.squad_members_needed == 0:
            self.max_spend = 0
        else:
            self.max_spend = self.budget - (self.squad_members_needed - 1)
        return None

    def update_formation(self):
        self.formation = [len(self.defenders),
                          len(self.midfielders),
                          len(self.forwards)]
        return None

    def increment_club_count(self, club: str):
        if club not in self.club_count:
            self.club_count[club] = 1
        else:
            self.club_count[club] += 1
        return None

    def add_squad_member(self, member: Dict, price: int):

        position = member["position_short"]

        if position == 'MGR':
            self.manager.append(member)
        elif position == 'GKP':
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
        self.update_formation()
        self.increment_club_count(member["club_short"])

        print("Player added to squad.")
        return None
