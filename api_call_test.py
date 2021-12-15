import requests

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)
fpl_data = r.json()

players = fpl_data['elements']
# first_player = players[0]
positions = fpl_data['element_types']
teams = fpl_data['teams']
# print(first_player)
# print(positions)
# for team in teams:
#     print(team)

# for key in first_player:
#     print(key)

# keys = ["id", "first_name", "second_name", "web_name"]
# first_player_formatted = {key: first_player[key] for key in keys}
# position = next(pos for pos in positions if pos["id"] == first_player["element_type"])
# team = next(t for t in teams if t["id"] == first_player["team"])
# first_player_formatted["position"] = position["singular_name"]
# first_player_formatted["position_short"] = position["singular_name_short"]
# first_player_formatted["team"] = team["name"]
# first_player_formatted["team_short"] = team["short_name"]
# print(first_player_formatted)
# print()

players_dict = {}
copy_keys = ["id", "first_name", "second_name", "web_name"]
for player in players:
    player_formatted = {key: player[key] for key in copy_keys}
    position = next(pos for pos in positions if pos["id"] == player["element_type"])
    team = next(t for t in teams if t["id"] == player["team"])
    player_formatted["position"] = position["singular_name"]
    player_formatted["position_short"] = position["singular_name_short"]
    player_formatted["team"] = team["name"]
    player_formatted["team_short"] = team["short_name"]

    players_dict[player_formatted["id"]] = player_formatted

for player in players_dict:
    print(player, ":", players_dict[player])
