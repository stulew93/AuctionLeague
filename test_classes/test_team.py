from classes.team import Team

# Create tests for update_budget_remaining method.
def test_update_budget_remaining():
    test_team = Team()
    test_team.remaining_budget = 100  # Set manually here as remaining_budget will be configurable.
    example_bid = 15  # Represents a bid of 15m on a player at auction.

    # Check that the remaining_budget attribute is updated as expected.
    test_team.update_remaining_budget(example_bid)
    assert test_team.remaining_budget == 85

# Create tests for update_max_bid method.
def test_update_max_bid():
    test_team = Team()

    # Check that if run immediately, max_bid equals 90.
    test_team.update_max_bid()
    assert test_team.max_bid == 90

    # Check that if there is one player in the squad and no change to the remaining_budget, max bid is now 91.
    test_team.squad.current_squad_size = 1
    test_team.update_max_bid()
    assert test_team.max_bid == 91

    # Check that if there is one player in the squad and the remaining_budget is now 10, max bid is now 1.
    test_team.squad.current_squad_size = 1
    test_team.remaining_budget = 10
    test_team.update_max_bid()
    assert test_team.max_bid == 1

    # Check that if the suad is complete, max_bid is 0.
    test_team.squad.squad_complete = True
    test_team.update_max_bid()
    assert test_team.max_bid == 0

# Create tests for check_team_complete method.
def test_check_team_complete():
    pass

pass
