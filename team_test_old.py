from class_file import Team

player_dict = {
    1: {"name": "David De Gea", "position_short": "GK", "club": "Man U"},
    2: {"name": "Romelu Lukaku", "position_short": "FWD", "club": "Chels"},
    3: {"name": "Mo Salah", "position_short": "MID", "club": "Lpool"},
    4: {"name": "Joao Cancelo", "position_short": "DEF", "club": "Man C"},
    5: {"name": "Conor Gallagher", "position_short": "MID", "club": "C Pal"},
    6: {"name": "Kieran Tierney", "position_short": "DEF", "club": "Arsnl"},
    7: {"name": "Raheem Sterling", "position_short": "MID", "club": "M City"},
    8: {"name": "Heung-Min Son", "position_short": "MID", "club": "Spurs"},
    9: {"name": "Callum Wilson", "position_short": "FWD", "club": "New U"},
    10: {"name": "Jordan Pickford", "position_short": "GK", "club": "Evrtn"},
    11: {"name": "Teemu Pukki", "position_short": "FWD", "club": "Nwich"},
    12: {"name": "Zinedine Zidane", "position_short": "MID", "club": "Legends"},
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

# print("Name:", test_team.name)
# print("Squad size:", test_team.squad_members_current)
# print("Members needed:", test_team.squad_members_needed)
# print("Budget:", test_team.budget)
# print("Max Spend:", test_team.max_spend)
# print("Keeper:", test_team.goalkeeper)
# print("Defenders:", test_team.defenders)
# print("Midfielders:", test_team.midfielders)
# print("Forwards:", test_team.forwards)

print(test_team)
