from classes import Team

player_dict = {
    1: {"name": "David De Gea", "position": "GK", "club": "Man U"},
    2: {"name": "Romelu Lukaku", "position": "FWD", "club": "Chels"},
    3: {"name": "Mo Salah", "position": "MID", "club": "Lpool"},
    4: {"name": "Joao Cancelo", "position": "DEF", "club": "Man C"},
    5: {"name": "Conor Gallagher", "position": "MID", "club": "C Pal"},
    6: {"name": "Kieran Tierney", "position": "DEF", "club": "Arsnl"},
    7: {"name": "Raheem Sterling", "position": "MID", "club": "M City"},
    8: {"name": "Heung-Min Son", "position": "MID", "club": "Spurs"},
    9: {"name": "Callum Wilson", "position": "FWD", "club": "New U"},
    10: {"name": "Jordan Pickford", "position": "GK", "club": "Evrtn"},
    11: {"name": "Teemu Pukki", "position": "FWD", "club": "Nwich"},
    12: {"name": "Zinedine Zidane", "position": "MID", "club": "Legends"},
}

test_team = Team("Stuart")

test_team.add_squad_member(player_dict[1], 5)
test_team.add_squad_member(player_dict[2], 2)
test_team.add_squad_member(player_dict[3], 2)
test_team.add_squad_member(player_dict[4], 2)
test_team.add_squad_member(player_dict[5], 2)
test_team.add_squad_member(player_dict[6], 2)
test_team.add_squad_member(player_dict[7], 2)
test_team.add_squad_member(player_dict[8], 2)
test_team.add_squad_member(player_dict[9], 2)
test_team.add_squad_member(player_dict[10], 2)
test_team.add_squad_member(player_dict[11], 2)

print("Name:", test_team.name)
print("Squad size:", test_team.squad_members_current)
print("Members needed:", test_team.squad_members_needed)
print("Budget:", test_team.budget)
print("Max Spend:", test_team.max_spend)
print("Keeper:", test_team.goalkeeper)
print("Defenders:", test_team.defenders)
print("Midfielders:", test_team.midfielders)
print("Forwards:", test_team.forwards)
