import tkinter as tk
from classes.auction import Auction


def display_teams():
    # For each team, add a label and display the team name.
    num_teams = len(auction.teams)
    for i in range(num_teams):
        team_name = auction.teams[i].name
        # row=i+3 as start adding these to the grid after the title, team entry box, button and subtitle.
        tk.Label(window, text=team_name, font="none 10").grid(row=i+4, column=0, sticky='w')
    return


def create_team():
    # TODO: Pop up message if name is taken or is invalid (e.g. blank entry box).
    new_team_name = entry_create_team.get()
    auction.add_team(new_team_name)
    display_teams()
    return


# main:
window = tk.Tk()
window.title("Auction League")

# create title label:
title = tk.Label(window, text="Auction League", font="none 12 bold")
title.grid(row=0, column=0, columnspan=3)

# Add a text entry box for new team names, and a button to create team.
entry_create_team = tk.Entry(window, bg='white', text="Enter a team name:")
entry_create_team.grid(row=1, column=0, sticky='ew')

# Add a button to add the team, using the name in the entry box.
button_create_team = tk.Button(window, text="CREATE TEAM", command=create_team)
button_create_team.grid(row=2, column=0, sticky='w')

# Display a list of teams on the left hand side.
# Add subtitle label:
teams_subtitle = tk.Label(window, text="Teams:", font="none 10 bold")
teams_subtitle.grid(row=3, column=0, sticky='w')
# Create some teams:
auction = Auction()
# auction.add_team("Stuart")
# auction.add_team("Alex")
# auction.add_team("Stef")
# For each team, add a label and display the team name.
display_teams()

# Run mainloop.
window.mainloop()
