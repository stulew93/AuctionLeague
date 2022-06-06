from classes.auction import Auction

def test_get_player_info_from_api():
    # Check that the player info is returned in the correct format.
    test_auction = Auction()
    # Look at player ID 1 for tests.
    test_player = test_auction.players[1]
    print(test_player)
    assert "simple_name" in test_player.keys()
    assert "first_name" in test_player
    assert "second_name" in test_player
    assert "club" in test_player
    assert "position" in test_player
    assert "player_purchased" in test_player
