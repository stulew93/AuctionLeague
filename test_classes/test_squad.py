from classes.squad import Squad


# Create tests for update_club_count method.
def test_update_club_count():
    test_squad = Squad()
    test_squad.update_club_count("TOT")
    test_squad.update_club_count("LIV")

    assert test_squad.club_count == {"TOT": 1,
                                     "LIV": 1}

    test_squad.update_club_count("TOT")

    assert test_squad.club_count == {"TOT": 2,
                                     "LIV": 1}


def test_check_squad_complete():
    test_squad = Squad()
    test_squad.players = {"GKP": [],
                          "DEF": [],
                          "MID": ["Son"],
                          "FWD": []
                          }

    test_squad.check_squad_complete()

    assert test_squad.squad_complete is False

    test_squad.players = {"GKP": ["Martinez"],
                          "DEF": ["Trent", "Targett", "Cancelo", "Sessegnon"],
                          "MID": ["Son", "Salah", "Diaz", "Gallagher", "Brownhill"],
                          "FWD": ["Ronaldo"]
                          }

    test_squad.check_squad_complete()

    assert test_squad.squad_complete is True

    # players = {1: {"name": "Son", "position": "MID", "club": "TOT"},
    #            2: {"name": "Salah", "position": "MID", "club": "LIV"},
    #            3: {"name": "Ronaldo", "position": "FWD", "club": "MUN"},
    #            4: {"name": "Trent", "position": "DEF", "club": "LIV"},
    #            5: {"name": "Martinez", "position": "GKP", "club": "AVL"},
    #            6: {"name": "Targett", "position": "DEF", "club": "NEW"},
    #            7: {"name": "Cancelo", "position": "DEF", "club": "MCI"},
    #            8: {"name": "Sessegnon", "position": "DEF", "club": "TOT"},
    #            9: {"name": "Diaz", "position": "MID", "club": "LIV"},
    #            10: {"name": "Gallagher", "position": "MID", "club": "CRY"},
    #            11: {"name": "Brownhill", "position": "MID", "club": "BUR"},
    #            }
    #
    # for p in range(2, 12):
    #     test_squad.add_player_to_squad(players[p])


# Create tests for add_player method.
def test_add_player_to_squad():
    test_squad = Squad()
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

    test_squad.add_player_to_squad(players[1])

    assert test_squad.players == {"GKP": [],
                                  "DEF": [],
                                  "MID": ["Son"],
                                  "FWD": []}

    for p in range(2, 12):
        test_squad.add_player_to_squad(players[p])

    assert test_squad.players == {"GKP": ["Martinez"],
                                  "DEF": ["Trent", "Targett", "Cancelo", "Sessegnon"],
                                  "MID": ["Son", "Salah", "Diaz", "Gallagher", "Brownhill"],
                                  "FWD": ["Ronaldo"]
                                  }
