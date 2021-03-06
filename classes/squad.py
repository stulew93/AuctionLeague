class Squad:
    '''
    The Squad class represents a group of players who will form the basis of a team. It deals with adding players to
    the players dict, keeps track of their positions, and records the number of players in the squad from each club.
    '''

    def __init__(self):
        self.current_squad_size = 0  # Keeps track of the number of players in the squad.
        self.players = {"GKP": [],
                        "DEF": [],
                        "MID": [],
                        "FWD": []
                        }  # Keeps track of the players in the squad, and their positions.
        self.club_count = {}  # For each club represented within the squad, keeps count of the number of players from
        # that club.
        self.squad_complete = False  # Set to true when number of players equals 11.

    def __str__(self):
        # Printing a Squad instance prints out the names of the players in the squad, split by their positions.
        gk = '; '.join([player for player in self.players["GKP"]])
        defs = '; '.join([player for player in self.players["DEF"]])
        mids = '; '.join([player for player in self.players["MID"]])
        fwds = '; '.join([player for player in self.players["FWD"]])

        squad_str = "Goalkeeper: " + gk + " (" + str(len(self.players["GKP"])) + ")\n" \
                   "Defenders: " + defs + " (" + str(len(self.players["DEF"])) + ")\n" \
                   "Midfielders: " + mids + " (" + str(len(self.players["MID"])) + ")\n" \
                   "Forwards: " + fwds + " (" + str(len(self.players["FWD"])) + ")"

        return squad_str

    def update_club_count(self, club):
        # If club already exists in club_count, increment count by 1; else add club into club_count with value 1.
        if club in self.club_count:
            self.club_count[club] += 1
        else:
            self.club_count[club] = 1

        print("Squad club count updated.")
        return None

    # def check_squad_complete(self):
    #     if self.current_squad_size == 11:
    #         self.squad_complete = True
    #
    #     print("Squad complete: {}".format(self.squad_complete))
    #     return None

    def add_player_to_squad(self, player):
        # Add player into the players dict, under the correct position.
        name, position, club = player["simple_name_raw"], player["position"], player["club"]
        self.players[position].append(name + ", " + club)

        # Increment the squad size.
        self.current_squad_size += 1

        # Update the club count.
        self.update_club_count(club)

        # Check for squad completion.
        # self.check_squad_complete()

        print("Player {} added to squad.".format(name))
        return


if __name__ == "__main__":
    test_squad = Squad()

    print(test_squad)
    print("----------")

    players = {1: {"simple_name_raw": "Son", "position": "MID", "club": "TOT"},
               2: {"simple_name_raw": "Salah", "position": "MID", "club": "LIV"},
               3: {"simple_name_raw": "Ronaldo", "position": "FWD", "club": "MUN"},
               4: {"simple_name_raw": "Trent", "position": "DEF", "club": "LIV"},
               5: {"simple_name_raw": "Martinez", "position": "GKP", "club": "AVL"},
               6: {"simple_name_raw": "Targett", "position": "DEF", "club": "NEW"},
               7: {"simple_name_raw": "Cancelo", "position": "DEF", "club": "MCI"},
               8: {"simple_name_raw": "Sessegnon", "position": "DEF", "club": "TOT"},
               9: {"simple_name_raw": "Diaz", "position": "MID", "club": "LIV"},
               10: {"simple_name_raw": "Gallagher", "position": "MID", "club": "CRY"},
               11: {"simple_name_raw": "Brownhill", "position": "MID", "club": "BUR"},
               }

    for p in players:
        test_squad.add_player_to_squad(players[p])
        print(test_squad.club_count)
        print("----------")

    print(test_squad)
