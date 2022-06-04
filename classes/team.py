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

        return

