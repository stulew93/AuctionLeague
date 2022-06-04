class Squad:

    def __init__(self):
        self.players = {"GKP": [],
                        "DEF": [],
                        "MID": [],
                        "FWD": []
                        }  # Keeps track of the players in the squad, and their positions.
        self.club_count = {}  # For each club represented within the squad, keeps count of the number of players from
        # that club.
        self.squad_complete = False  # Set to true when number of players equals 11.

    def update_club_count(self, club):
        # If club already exists in club_count, increment count by 1; else add club into club_count with value 1.
        if club in self.club_count:
            self.club_count[club] += 1
        else:
            self.club_count[club] = 1

        print("Squad club count updated.")
        return None

    def check_squad_complete(self):
        # Count the players in the squad; if there are 11 then set squad_complete to True.
        player_count = 0
        for pos in self.players:
            player_count += len(self.players[pos])

        if player_count == 11:
            self.squad_complete = True

        print("Squad complete: {}".format(self.squad_complete))
        return None

    def add_player_to_squad(self, player):
        # Add player into the players dict, under the correct position.
        name, position, club = player["name"], player["position"], player["club"]
        self.players[position].append(name)

        self.update_club_count(club)

        self.check_squad_complete()

        print("Player {} added to squad.".format(name))
        return


if __name__ == "__main__":
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

    for p in players:
        test_squad.add_player_to_squad(players[p])
        print(test_squad.club_count)
        print("----------")

