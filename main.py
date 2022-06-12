import tkinter as tk
from classes.auction import Auction


def display_teams():
    # For each team, add a label and display the team name.
    num_teams = len(auction.teams)
    for i in range(num_teams):
        # Display team name.
        team_name = auction.teams[i].name
        # row=i+1 as start adding these to the grid in frame_teams_info after the subtitle "Teams:".
        label_team_name = tk.Label(frame_teams_info, text=team_name, font="none 10")
        label_team_name.grid(row=i+1, column=0, sticky='w', padx=FRAME_TEAM_X_PAD)
        # Display team completion.
        team_completion = auction.teams[i].get_team_completion()
        label_team_completion = tk.Label(frame_teams_info, text=team_completion, font="none 10")
        label_team_completion.grid(row=i+1, column=1, sticky='ew', padx=FRAME_TEAM_X_PAD)
        # Display budget info.
        # In the form "(Remaining budget) / (Max single bid)"
        remaining_budget = auction.teams[i].remaining_budget
        max_bid = auction.teams[i].max_bid
        team_budget_info = f"£{remaining_budget}m / £{max_bid}m"
        label_team_budget_info = tk.Label(frame_teams_info, text=team_budget_info, font="none 10")
        label_team_budget_info.grid(row=i+1, column=2, sticky='ew', padx=FRAME_TEAM_X_PAD)
        # Create "View" button.
        button_view = tk.Button(frame_teams_info, text='VIEW')
        button_view.grid(row=i+1, column=3, sticky='w', padx=FRAME_TEAM_X_PAD, pady=2)
    return


def create_team():
    # TODO: Pop up message if name is taken or is invalid (e.g. blank entry box).
    new_team_name = entry_team_name.get()
    auction.add_team(new_team_name)
    display_teams()
    entry_team_name.delete(0, 'end')
    return

def delete_team():
    team_to_delete = entry_team_name.get()
    auction.delete_team(team_to_delete)
    for label in frame_teams_info.grid_slaves(column=0):
        if int(label.grid_info()["row"]) > 0:
            label.grid_forget()
    display_teams()
    return

HEIGHT = 600
WIDTH = 800
FRAME_TEAM_X_PAD = 10

# main:
window = tk.Tk()
window.title("Auction League")

# canvas; used to set the initial window size.
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame for window title.
frame_title = tk.Frame(window)
frame_title.place(relwidth=1, relheight=0.05)

# create title label:
label_title = tk.Label(frame_title, text="Auction League", font="none 16 bold")
label_title.place(relx=0.5, rely=0.5, anchor='center')


## Create structure for the Teams section, which sits on the left hand side of the app.
# Overall frame for teams.
frame_teams = tk.Frame(window, bg='pink')
frame_teams.place(rely=0.05, relwidth=0.33, relheight=0.95)

# Frame for team creation and deletion.
frame_teams_entry = tk.Frame(frame_teams)
frame_teams_entry.place(relwidth=1, relheight=0.15)
# frame_teams_entry.rowconfigure(tuple(range(2)), weight=1)
frame_teams_entry.columnconfigure(tuple(range(2)), weight=1)

# Add label with text "Enter team name below:"
label_team_name = tk.Label(frame_teams_entry, text="Enter team name below:", font="none 10 bold")
label_team_name.grid(row=0, column=0, columnspan=2, sticky='w', padx=FRAME_TEAM_X_PAD)

# Add a text entry box for new team names, and a button to create team.
entry_team_name = tk.Entry(frame_teams_entry, bg='white', text="Enter a team name:")
entry_team_name.grid(row=1, column=0, columnspan=2, sticky='ew', padx=FRAME_TEAM_X_PAD, pady=2)

# Add a button to add the team, using the name in the entry box.
button_create_team = tk.Button(frame_teams_entry, text="CREATE TEAM", command=create_team)
button_create_team.grid(row=2, column=0, sticky='ew', padx=FRAME_TEAM_X_PAD)

# Add a button to delete a team, using the name in the entry box.
button_delete_team = tk.Button(frame_teams_entry, text="DELETE TEAM", command=delete_team)
button_delete_team.grid(row=2, column=1, sticky='ew', padx=FRAME_TEAM_X_PAD)

# Frame for team information.
frame_teams_info = tk.Frame(frame_teams)
# frame_teams_entry.grid(row=0, column=0, columnspan=2)
frame_teams_info.place(rely=0.15, relwidth=1, relheight=0.85)
frame_teams_info.columnconfigure(0, weight=3)
frame_teams_info.columnconfigure((1, 2), weight=2)
frame_teams_info.columnconfigure(3, weight=1)

# Create column headings for list of teams.
# Specify desired headings:
headings = [("Teams:", 'w'),
            ("Completion:", 'ew'),
             ("Budget/MaxBid:", 'ew')]

for i in range(len(headings)):
    label_heading = tk.Label(frame_teams_info, text=headings[i][0], font="none 10 bold")
    label_heading.grid(row=0, column=i, sticky=headings[i][1], padx=FRAME_TEAM_X_PAD, pady=2)

# "Teams:"
# label_heading_teams = tk.Label(frame_teams_info, text="Teams:", font="none 10 bold")
# label_heading_teams.grid(row=0, column=0, sticky='w', padx=FRAME_TEAM_X_PAD, pady=2)

# Display team completion.

# Diplay remaining budget/max bid.

# Add button to view team.


# frame for selecting player to auction.
frame_auction = tk.Frame(window, bg='green')
frame_auction.place(relx=0.33, rely=0.05, relwidth=0.34, relheight=0.95)

# frame for displaying past purchases.
frame_history = tk.Frame(window, bg='black')
frame_history.place(relx=0.67, rely=0.05, relwidth=0.33, relheight=0.95)

# Initialise Auction:
auction = Auction()

# Run mainloop.
window.mainloop()
