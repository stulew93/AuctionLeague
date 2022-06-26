import requests
import pytz
import csv
from datetime import datetime
from unidecode import unidecode
from classes.team import Team

# TODO: method to change the name of a team.
# TODO: method to add extra players to player list.
# TODO: method to ingest list of transactions.

class Auction:
    '''
    The Auction class orchestrates an auction. It maintains a list of participating Teams, a list of players available
    in the auction, keeps a transaction log throughout the auction, and calls the validation logic when a player
    nomination is made.
    '''

    def __init__(self):
        self.teams = {}  # A dict of participating teams, keyed on their team name.
        self.nomination_seq = []  # List of the teams in order to control who is nominating players.
        self.nomination_index = 0  # Current index in nomination sequence.
        self.next_up_index = 1 # Next up index in nomination sequence.
        self.players = {}  # The players available for auction. Each player is keyed on their ID, paired with an info dict.
        self.clubs = {}  # The clubs that players can play for.
        self.transaction_log = []  # A list of all transactions throughout the auction.
        self.auction_complete = False

        # URL for the FPL api.
        self.url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.get_player_info_from_api()

        # Initialise transaction log csv with headings.
        with open("transaction_log.csv", 'w') as f:
            columns = "Team, Player, Position, Club, Price, Timestamp\n"
            f.write(columns)

    def get_position(self, positions_list, id):
        # Used in get_player_info_from_api.
        # Takes the positions raw data from the api call and returns the position related to the input id.
        simple_positions = {position["id"]: position["singular_name_short"] for position in positions_list}
        return simple_positions[id]

    def get_clubs(self, clubs_data):
        # Saves the club data into a simplified dictionary.
        self.clubs = {club["id"]: club["short_name"] for club in clubs_data}
        return

    def get_player_info_from_api(self):
        '''
        Calls the FPL api and populates the players dict with player information.
        The players dict is keyed on the player ID, which is paired with an info dict with the fields:
        simple_name, first_name, second_name, club, position, player_purchased.
        '''
        # Make call to api, and save raw data in dict fpl_data.
        req = requests.get(self.url)
        fpl_data = req.json()
        # Extract raw player data, from key "elements".
        raw_players = fpl_data["elements"]
        # Extract raw club data, from key "teams"; save in the clubs dictionary.
        raw_clubs = fpl_data["teams"]
        self.get_clubs(raw_clubs)
        # Extract raw position data, from key "element_types".
        raw_positions = fpl_data["element_types"]

        # For each player, format the data points we want and add to the players class attribute.
        for player in raw_players:
            player_formatted = {"id": player["id"],
                                "code": player["code"],
                                "simple_name_raw": player["web_name"],
                                "simple_name_eng_chars": unidecode(player["web_name"]), # using unidecode to anglicise
                                # name for easier searching
                                "first_name": player["first_name"],
                                "second_name": player["second_name"],
                                "club": self.clubs[player["team"]],
                                "position": self.get_position(raw_positions, player["element_type"]),
                                "player_purchased": False
                                }
            # Insert player into the players dict, using the player id as a key.
            self.players[player["id"]] = player_formatted

        print("Player data loaded.")
        return

    def add_players_from_csv(self, file_path):
        # Method which will take a filepath to a .csv file containing details of players which are not in the official
        # FPL game (and hence have not been retrieved by the API call), to be added to the players dict.
        # Input csv should be in the format: simple_name, first_name, second_name, club (3-letter club code),
        # position (3-letter position code).
        # Check file_path is in .csv format.
        if file_path[-4:] != ".csv":
            return 'File type not ".csv".'
        else:
            with open(file_path, 'r') as file:
                new_players = csv.DictReader(file)
                # We need IDs for the new players. Get the max existing id and add 1, and the increment for each new
                # player that we add.
                new_player_id = max(self.players.keys()) + 1
                for player in new_players:
                    # Define new player dict.
                    player_dict = {"id": new_player_id,
                                   "code": None,
                                   "simple_name_raw": player["simple_name"],
                                   "simple_name_eng_chars": unidecode(player["simple_name"]),
                                   # using unidecode to anglicise
                                   # name for easier searching
                                   "first_name": player["first_name"],
                                   "second_name": player["second_name"],
                                   "club": player["club"],
                                   "position": player["position"],
                                   "player_purchased": False
                                   }
                    # Add to the players dict for the auction.
                    self.players[new_player_id] = player_dict
                    # Increment the player id for the next new player.
                    new_player_id += 1
            return "New players added to player list."

    def add_team(self, team_name):
        # Add new team to the teams list.
        # Check that the new team name is unique before adding.
        # if team_name in [team.name for team in self.teams]:
        if team_name in self.teams:
            print(f'The team name "{team_name}" is already taken.')
            return "Team name exists."
        elif team_name == "":  # Flag if team_name is blank.
            return "Team name empty."
        else:
            new_team = Team(team_name)
            # self.teams.append(new_team)
            self.teams[team_name] = new_team
            print(f"Team {team_name} added successfully.")
            return "Team added."

    def delete_team(self, team_name):
        # TODO: Ensure to return any players associated with the team back to the available pool.
        # Delete team from teams list.
        # Check that team exists before deleting.
        # if team_name not in [team.name for team in self.teams]:
        if team_name not in self.teams:
            print(f'Team "{team_name}" does not exist.')
            return "Team name does not exist."
        else:
            # team_to_delete = next(team for team in self.teams if team.name == team_name)
            # self.teams.remove(team_to_delete)
            self.teams.pop(team_name)
            print(f"Team {team_name} deleted successfully.")
            return "Team deleted."

    def initialise_nomination_seq(self):
        self.nomination_seq = list(self.teams.keys())
        print("Initialised nomination sequence.")
        return

    def update_nomination_index(self):
        # If all teams are complete, do nothing.
        if self.auction_complete == True:
            return
        else:
            # Increment nomination index until we find a team that isn't already complete.
            # Add one and take modulus over the number of teams, so we go back to the start of the list.
            self.nomination_index = (self.nomination_index + 1) % len(self.teams)
            while self.teams[self.nomination_seq[self.nomination_index]].team_complete == True:
                # Add one and take modulus over the number of teams, so we go back to the start of the list.
                self.nomination_index = (self.nomination_index + 1) % len(self.teams)

            # Do the same for the next up index but starting from the new nomination index + 1.
            self.next_up_index = (self.nomination_index + 1) % len(self.teams)
            # Increment the next up index until we find a team that isn't already complete.
            while self.teams[self.nomination_seq[self.next_up_index]].team_complete == True:
                # Add one and take modulus over the number of teams, so we go back to the start of the list.
                self.next_up_index = (self.next_up_index + 1) % len(self.teams)

            return

    def create_transaction(self, team, player, price):
        # Takes as input the team (Team), player (dict) and price (INT)
        transaction = {"team": team,
                       "player": player,
                       "price": price,
                       "timestamp": datetime.now(pytz.timezone("Europe/London"))}
        # Add to transaction log.
        self.transaction_log.append(transaction)
        # Add to transaction log csv. Open file in append mode.
        with open("transaction_log.csv", 'a') as f:
            new_line = f"{team.name}, {player['simple_name_raw']}, {player['position']}, {player['club']}, " \
                       f"{price}, {transaction['timestamp']}\n"
            f.write(new_line)
        return

    def display_transaction_log(self):
        display = ""
        for t in self.transaction_log:
            display += f"Team {t['team'].name} bought player {t['player']['simple_name_raw']} for £{t['price']}m.\n"
        print(display)
        return display

    def get_latest_transactions(self):
        # Get last 20 transactions and reverse them so the latest is first.
        latest_transactions_list = self.transaction_log[-20:][::-1]
        # Format them into a string.
        latest_transaction_string = ""
        for t in latest_transactions_list:
            t_formatted = f"Team {t['team'].name} bought player {t['player']['simple_name_raw']} " \
                          f"({t['player']['position']}, {t['player']['club']}) for £{t['price']}m.\n"
            latest_transaction_string += t_formatted
        return latest_transaction_string

    def confirm_purchase(self, team_name, player_id, price):
        # Takes as input the team name (STR), the player id (STR), and the price of the purchase (INT).
        # Get the player from the players dict.
        player = self.players[player_id]

        # Get the team object for the team.
        team = self.teams[team_name]

        # Add player to team.
        team.add_squad_member(player, price)

        # Add the purchase to the transaction log.
        self.create_transaction(team, player, price)

        # Mark the player as purchased so it can't be selected again.
        player['player_purchased'] = True

        # Update the nomination index.
        self.update_nomination_index()

        return

    def can_bid(self, team, player):
        # Method which takes in team (Team) and player (dict), and returns a tuple with a boolean indicating whether
        # the team can bid for the player or not, and a string representing the reason.
        # If team is complete then cannot bid.
        if team.team_complete == True:
            return (False, "Team complete.")
        # If team already has three players from the club, cannot bid.
        elif player["club"] in team.squad.club_count:
            if team.squad.club_count[player["club"]] == 3:
                return (False, f"Already have three players from {player['club']}.")
        # If player is a GKP
        elif player["position"] == "GKP":
            # and team already has a GKP, cannot bid.
            if len(team.squad.players["GKP"]) == 1:
                return (False, "Invalid formation (>1 GKP).")
            else:
                return (True, "Can bid.")
        # If player is not a GK
        else:
            # and already have 10 outfield players, cannot bid.
            if len(team.squad.players["DEF"]) + len(team.squad.players["MID"]) + len(team.squad.players["FWD"]) == 10:
                return (False, "Invalid formation (>10 outfield).")
            # If player is a DEF
            elif player["position"] == "DEF":
                # and team already has 5 DEFs, cannot bid.
                if len(team.squad.players["DEF"]) == 5:
                    return (False, "Invalid formation (>5 DEF).")
                # and team has 4 DEFs
                elif len(team.squad.players["DEF"]) == 4:
                    # and 5 MIDs, cannot bid.
                    if len(team.squad.players["MID"]) == 5:
                        return (False, "Invalid formation (5/5/0).")
                    else:
                        return (True, "Can bid.")
                else:
                    return (True, "Can bid.")
            # If player is a MID
            elif player["position"] == "MID":
                # and the team already has 5 MIDs, cannot bid.
                if len(team.squad.players["MID"]) == 5:
                    return (False, "Invalid formation (>5 MID).")
                # and team has 4 MIDs
                elif len(team.squad.players["MID"]) == 4:
                    # and 5 DEFs, cannot bid.
                    if len(team.squad.players["DEF"]) == 5:
                        return (False, "Invalid formation (5/5/0).")
                    # and 3 FWDs, cannot bid.
                    elif len(team.squad.players["FWD"]) == 3:
                        return (False, "Invalid formation (2/5/3).")
                    else:
                        return (True, "Can bid.")
                else:
                    return (True, "Can bid.")
            # If player is a FWD
            elif player["position"] == "FWD":
                # and the team already has 3 FWDs, cannot bid.
                if len(team.squad.players["FWD"]) == 3:
                    return (False, "Invalid formation (>3 FWD).")
                # and the team has 2 FWDs
                elif len(team.squad.players["FWD"]) == 2:
                    # and 5 MIDs, cannot bid.
                    if len(team.squad.players["MID"]) == 5:
                        return (False, "Invalid formation (2/5/3).")
                    else:
                        return (True, "Can bid.")
                else:
                    return (True, "Can bid.")
            else:
                return (False, "Something went wrong with validation logic!")

    def print_teams(self):
        # Method to print the team names out neatly.
        teams_display = "Teams: "
        for team in self.teams:
            teams_display += team + ", "
        teams_display = teams_display[:-2]
        print(teams_display)
        return


if __name__ == "__main__":
    test_auction = Auction()
    # test_auction.get_player_info_from_api()
    # print(test_auction.players[1])
    # print(test_auction.players)

    # for player in test_auction.players:
    #     print(player, ":", test_auction.players[player])
    test_auction.add_team("Stuart")
    test_auction.add_team("Alex")
    # test_auction.add_team("Stuart")
    # test_auction.delete_team("Alex")
    # test_auction.delete_team("Alex")
    #
    # for team in test_auction.teams:
    #     print(team)
    #     print("----------")
    #
    # test_auction.print_teams()
    #
    # print(test_auction.clubs)

    # zones = pytz.all_timezones
    # print(zones)  # Europe/London

    # print()
    #
    # test_auction.confirm_purchase("Stuart", 1, 2)
    #
    # print(test_auction.teams['Stuart'])
    #
    # test_auction.display_transaction_log()

    for p in test_auction.players:
        print(test_auction.players[p])

    result = test_auction.can_bid(test_auction.teams["Stuart"], test_auction.players[1])
    print(result)

    result = test_auction.add_players_from_csv("C:/Users/stuar/Documents/PythonFiles/AuctionLeaguev2/new_players_test.csv")
    print(result)

    mci_players = [player['simple_name_raw'] for player in test_auction.players.values() if player['club'] == 'MCI']
    print(mci_players)