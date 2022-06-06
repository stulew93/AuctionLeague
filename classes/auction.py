import requests
from unidecode import unidecode
from classes.team import Team

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
        # Used in get_player_info_from_api.
        # Takes the positions raw data from the api call and returns the position related to the input id.
        simple_positions = {position["id"]: position["singular_name_short"] for position in positions_list}
        return simple_positions[id]

    def get_club(self, clubs_list, id):
        # Used in get_player_info_from_api.
        # Takes the clubs raw data from the api call and returns the club name related to the input id.
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
            player_formatted = {"simple_name_raw": player["web_name"],
                                "simple_name_eng_chars": unidecode(player["web_name"]), # using unidecode to anglicise
                                # name for easier searching
                                "first_name": player["first_name"],
                                "second_name": player["second_name"],
                                "club": self.get_club(raw_clubs, player["team"]),
                                "position": self.get_position(raw_positions, player["element_type"]),
                                "player_purchased": False
                                }
            # Insert player into the players dict, using the player id as a key.
            self.players[player["id"]] = player_formatted

        print("Player data loaded.")
        return

    def add_team(self, team_name):
        # Add new team to the teams list.
        # Check that the new team name is unique before adding.
        if team_name in [team.name for team in self.teams]:
            print(f'Th team name "{team_name}" is already taken.')
            return
        else:
            new_team = Team(team_name)
            self.teams.append(new_team)
            print(f"Team {team_name} added successfully.")
            return

    def print_teams(self):
        # Method to print the team names out neatly.
        teams_display = "Teams: "
        for team in self.teams:
            teams_display += team.name + ", "
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
    test_auction.add_team("Stuart")

    for team in test_auction.teams:
        print(team)
        print("----------")

    test_auction.show_teams()