import requests

player_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
root_image_url = "https://resources.premierleague.com/premierleague/photos/players/110x140/p{}.png"
# image_url = root_image_url.format("115918")

player_req = requests.get(player_url)
player_data_raw = player_req.json()["elements"]

for player in player_data_raw:
    image_url = root_image_url.format(player["code"])
    # print(image_url)
    image_req = requests.get(image_url)
    with open(f"player_images/{player['code']}.png", 'wb') as file:
        file.write(image_req.content)
    print(f"Player {player['web_name']} image downloaded.")
