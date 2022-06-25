from classes.auction import Auction

def test_get_player_info_from_api():
    # Check that the player info is returned in the correct format.
    test_auction = Auction()
    # Look at player ID 1 for tests.
    test_player = test_auction.players[1]
    print(test_player)
    assert "simple_name_raw" in test_player.keys()
    assert "simple_name_eng_chars" in test_player.keys()
    assert "first_name" in test_player
    assert "second_name" in test_player
    assert "club" in test_player
    assert "position" in test_player
    assert "player_purchased" in test_player

def test_can_bid():
    # Check correct results are returned.
    auction = Auction()
    auction.add_team("Stuart")
    auction.add_team("Alex")
    auction.initialise_nomination_seq()

    # Add eleven players to Stuart.
    for id in list(auction.players.keys())[:12]:
        auction.confirm_purchase("Stuart", id, 1)
    team = team = auction.teams["Stuart"]
    player = auction.players[13]
    # Check that if team has 11 players, can_bid returns False.
    assert auction.can_bid(team, player)[0] == False

    # Add three players from same team to Alex.
    for id in [1, 2, 3]:
        auction.confirm_purchase("Alex", id, 1)
    # Check that if team has 3 players from same team, can_bid returns False.
    team = team = auction.teams["Alex"]
    player = auction.players[4]
    assert auction.can_bid(team, player)[0] == False

    # Test for formations.
