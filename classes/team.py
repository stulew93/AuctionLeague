from classes.squad import Squad

class Team:
    '''
    The Team class is a shell for the Squad - set up like this as in future I hope to add configurable elements
    (such as managers). The Team object will manage the budget for the team, including keeping track of the remaining
    budget, and whether the team is complete.
    '''

    def __init__(self, name, remaining_budget=100, target_squad_size=11):
        self.name = name
        self.squad = Squad()
        self.remaining_budget = remaining_budget  # Default 100.
        self.target_squad_size = target_squad_size  # Default 11.
        self.team_complete = False

    def __str__(self):
        # Printing a Team instance displays the team name, and the playing squad.
        team_str = "Team: " + self.name + "\n" \
                   + "Remaining budget: " + str(self.remaining_budget) + "\n" \
                   + str(self.squad)
        return team_str

    def update_remaining_budget(self, debit):
        # Subtract the bid from the remaining budget.
        self.remaining_budget -= debit
        return

    def check_team_complete(self):
        # Currently the only criteria is that
        if self.squad.current_squad_size == self.target_squad_size:
            self.team_complete = True
        return

    def add_squad_member(self, player, cost):
        # Add player to squad.
        self.squad.add_player_to_squad(player)

        # Update the team's remaining budget.
        self.update_remaining_budget(cost)

        # Check whether the team is complete.
        self.check_team_complete()

        print("Squad member added to team {}.".format(self.name))
        return

if __name__ == "__main__":
    test_team_1 = Team("Stuart")
    test_team_2 = Team("Alex")

    print(test_team_1)
    print("----------")

    players = {1: {"name": "Son", "position": "MID", "club": "TOT"},
               2: {"name": "Salah", "position": "MID", "club": "LIV"},
               3: {"name": "Ronaldo", "position": "FWD", "club": "MUN"},
               4: {"name": "Trent", "position": "DEF", "club": "LIV"},
               5: {"name": "Martinez", "position": "GKP", "club": "AVL"},
               6: {"name": "Targett", "position": "DEF", "club": "NEW"},
               7: {"name": "Cancelo", "position": "DEF", "club": "MCI"},
               8: {"name": "Sessegnon", "position": "DEF", "club": "TOT"},
               9: {"name": "Diaz", "position": "MID", "club": "LIV"},
               10: {"name": "Gallagher", "position": "MID", "club": "CRY"},
               11: {"name": "Brownhill", "position": "MID", "club": "BUR"},
               }

    test_team_1.add_squad_member(players[1], 23)
    print("----------")

    print(test_team_1)
    print("----------")

    for p in range(2,6):
        test_team_1.add_squad_member(players[p],3)
        print("----------")

    for p in range(6,12):
        test_team_2.add_squad_member(players[p],3)
        print("----------")

    print(test_team_1)
    print("----------")
    print(test_team_2)
    print("----------")
