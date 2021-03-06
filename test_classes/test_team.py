from classes.team import Team

# Create tests for update_remaining_budget method.
def test_update_remaining_budget():
    test_team = Team("test")
    test_team.remaining_budget = 100  # Set manually here as remaining_budget will be configurable.
    example_bid = 15  # Represents a bid of 15m on a player at auction.

    # Check that the remaining_budget attribute is updated as expected.
    test_team.update_remaining_budget(example_bid)
    assert test_team.remaining_budget == 85

# Create tests for update_max_bid method.
def test_update_max_bid():
    test_team = Team("test")

    # Check that if run immediately, max_bid equals 90.
    test_team.update_max_bid()
    assert test_team.max_bid == 90

    # Check that if there is one team member and no change to the remaining_budget, max bid is now 91.
    test_team.current_team_size = 1
    test_team.update_max_bid()
    assert test_team.max_bid == 91

    # Check that if there is one team member and the remaining_budget is now 10, max bid is now 1.
    test_team.current_team_size = 1
    test_team.remaining_budget = 10
    test_team.update_max_bid()
    assert test_team.max_bid == 1

    # Check that if the team is complete, max_bid is 0.
    test_team.team_complete = True
    test_team.update_max_bid()
    assert test_team.max_bid == 0

# Create tests for check_team_complete method.
def test_check_team_complete():
    test_team = Team("test")

    # Check that team_complete is still False after adding one player.
    test_team.current_team_size = 1

    test_team.update_team_complete()
    assert test_team.team_complete is False

    # Check that team_complete is still False after adding ten players.
    test_team.current_team_size = 10

    test_team.update_team_complete()
    assert test_team.team_complete is False

    # Check that team_complete is True after adding eleven players.
    test_team.current_team_size = 11

    test_team.update_team_complete()
    assert test_team.team_complete is True

