from classes.squad import Squad

class Team:
    '''
    The Team class is a shell for the Squad - set up like this as in future I hope to add configurable elements
    (such as managers). The Team object will manage the budget for the team, including keeping track of the remaining
    budget, and whether the team is complete.
    '''

    def __init__(self, name, remaining_budget=100, target_team_size=11):
        self.name = name
        self.squad = Squad()
        self.remaining_budget = remaining_budget  # Default 100.
        self.max_bid = remaining_budget - target_team_size + 1
        self.current_team_size = self.squad.current_squad_size
        self.target_team_size = target_team_size  # Default 11.
        self.team_complete = False

    def __str__(self):
        # Printing a Team instance displays the team name, and the playing squad.
        team_str = f"Team: {self.name}\n" \
                   f"Remaining budget: {str(self.remaining_budget)}\n" \
                   f"\n" \
                   f"{str(self.squad)}"
        # If team is complete, say so!
        if self.team_complete == True:
            team_str += "\n" + "Team {} complete!".format(self.name)

        return team_str

    def update_remaining_budget(self, debit):
        # Subtract the bid from the remaining budget.
        self.remaining_budget -= debit
        return

    def update_max_bid(self):
        if self.team_complete:
            self.max_bid = 0
        else:
            self.max_bid = self.remaining_budget - (self.target_team_size - self.current_team_size) + 1
        return

    def update_team_complete(self):
        # Currently the only criteria is that
        if self.current_team_size == self.target_team_size:
            self.team_complete = True
        return

    def get_team_completion(self):
        if self.team_complete == True:
            return "Complete!"
        else:
            return f"{self.current_team_size}/{self.target_team_size}"

    def update_team_size(self):
        self.current_team_size = self.squad.current_squad_size
        return

    def add_squad_member(self, player, cost):
        # Add player to squad.
        self.squad.add_player_to_squad(player)

        # Update team size.
        self.update_team_size()

        # Update team completion.
        self.update_team_complete()

        # Update the team's remaining budget.
        self.update_remaining_budget(cost)

        # Update the team's max bid.
        self.update_max_bid()

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

    print("******************************************")

    test_team_3 = Team("Bob")
    for p in range(1,12):
        test_team_3.add_squad_member(players[p],3)
        print("----------")

    print(test_team_3)
    print("----------")
