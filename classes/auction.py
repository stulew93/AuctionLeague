import requests

class Auction:
    '''
    The Auction class orchestrates an auction. It maintains a list of participating Teams, a list of players available
    in the auction, keeps a transaction log throughout the auction, and calls the validation logic when a player
    nomination is made.
    '''

    def __init__(self):
        self.teams = []  # A list of participating teams.
        self.players = {}  # The players available for auction. Each player is keyed on their ID, paired with an info dict.
        self.transaction_log = []  # A list of all transactions throughout the auction.
        self.auction_complete = False

        # URL for the FPL api.
        self.url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.get_player_info_from_api()

    def get_position(self, positions_list, id):
        # Takes the positions raw data and returns the position related to the input id.
        simple_positions = {position["id"]: position["singular_name_short"] for position in positions_list}
        return simple_positions[id]

    def get_club(self, clubs_list, id):
        # Takes the clubs raw data and returns the club name related to the input id.
        simple_clubs = {club["id"]: club["short_name"] for club in clubs_list}
        return simple_clubs[id]

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
        # Extract raw club data, from key "teams".
        raw_clubs = fpl_data["teams"]
        # Extract raw position data, from key "element_types".
        raw_positions = fpl_data["element_types"]

        # For each player, format the data points we want and add to the players class attribute.
        for player in raw_players:
            player_formatted = {"simple_name": player["web_name"],
                                "first_name": player["first_name"],
                                "second_name": player["second_name"],
                                "club": self.get_club(raw_clubs, player["team"]),
                                "position": self.get_position(raw_positions, player["element_type"]),
                                "player_purchased": False
                                }
            # Insert player into the players dict, using the player id as a key.
            self.players[player["id"]] = player_formatted

        print("Player data loaded.")


if __name__ == "__main__":
    test_auction = Auction()
    # test_auction.get_player_info_from_api()
    print(test_auction.players[1])
    pass
