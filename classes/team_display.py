import tkinter as tk
from classes.auction import Auction

class TeamDisplay(tk.Frame):
    def __init__(self, parent, auction):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.auction = auction

        self.FRAME_TEAM_X_PAD = 10

        # Frame for team creation and deletion.
        self.frame_teams_entry = tk.Frame(self)
        self.frame_teams_entry.place(relwidth=1, relheight=0.15)
        # self.frame_teams_entry.rowconfigure(tuple(range(2)), weight=1)
        self.frame_teams_entry.columnconfigure(tuple(range(2)), weight=1)

        # Add label with text "Enter team name below:"
        label_team_name = tk.Label(self.frame_teams_entry, text="Enter team name below:", font="none 10 bold")
        label_team_name.grid(row=0, column=0, columnspan=2, sticky='w', padx=self.FRAME_TEAM_X_PAD)

        # Add a text entry box for new team names, and a button to create team.
        self.entry_team_name = tk.Entry(self.frame_teams_entry, bg='white', text="Enter a team name:")
        self.entry_team_name.grid(row=1, column=0, columnspan=2, sticky='ew', padx=self.FRAME_TEAM_X_PAD, pady=2)

        # Add a button to add the team, using the name in the entry box.
        button_create_team = tk.Button(self.frame_teams_entry, text="CREATE TEAM", command=self.create_team)
        button_create_team.grid(row=2, column=0, sticky='ew', padx=self.FRAME_TEAM_X_PAD)

        # Add a button to delete a team, using the name in the entry box.
        button_delete_team = tk.Button(self.frame_teams_entry, text="DELETE TEAM", command=self.delete_team)
        button_delete_team.grid(row=2, column=1, sticky='ew', padx=self.FRAME_TEAM_X_PAD)

        # Frame for team information.
        self.frame_teams_info = tk.Frame(self)
        self.frame_teams_info.place(rely=0.15, relwidth=1, relheight=0.85)
        self.frame_teams_info.columnconfigure(0, weight=3)
        self.frame_teams_info.columnconfigure((1, 2), weight=2)
        self.frame_teams_info.columnconfigure(3, weight=1)

        # Create column headings for list of teams.
        # Specify desired headings and sticky values:
        headings = [("Teams:", 'w'),
                    ("Completion:", 'ew'),
                    ("Budget/MaxBid:", 'ew')]

        for i in range(len(headings)):
            label_heading = tk.Label(self.frame_teams_info, text=headings[i][0], font="none 10 bold")
            label_heading.grid(row=0, column=i, sticky=headings[i][1], padx=self.FRAME_TEAM_X_PAD, pady=2)

    def create_team(self):
        # TODO: Pop up message if name is taken or is invalid (e.g. blank entry box).
        new_team_name = self.entry_team_name.get()
        self.auction.add_team(new_team_name)
        self.display_teams()
        self.entry_team_name.delete(0, 'end')
        return

    def delete_team(self):
        team_to_delete = self.entry_team_name.get()
        self.auction.delete_team(team_to_delete)
        for label in self.frame_teams_info.grid_slaves():
            if int(label.grid_info()["row"]) > 0:
                label.grid_forget()
        self.display_teams()
        return

    def display_teams(self):
        # For each team, add a label and display the team name.
        num_teams = len(self.auction.teams)
        for i in range(num_teams):
            # Display team name.
            team_name = self.auction.teams[i].name
            # row=i+1 as start adding these to the grid in frame_teams_info after the column headings (row 0).
            label_team_name = tk.Label(self.frame_teams_info, text=team_name, font="none 10")
            label_team_name.grid(row=i + 1, column=0, sticky='w', padx=self.FRAME_TEAM_X_PAD)

            # Display team completion.
            team_completion = self.auction.teams[i].get_team_completion()
            label_team_completion = tk.Label(self.frame_teams_info, text=team_completion, font="none 10")
            label_team_completion.grid(row=i + 1, column=1, sticky='ew', padx=self.FRAME_TEAM_X_PAD)

            # Display budget info.
            # In the form "(Remaining budget) / (Max single bid)"
            remaining_budget = self.auction.teams[i].remaining_budget
            max_bid = self.auction.teams[i].max_bid
            team_budget_info = f"£{remaining_budget}m / £{max_bid}m"
            label_team_budget_info = tk.Label(self.frame_teams_info, text=team_budget_info, font="none 10")
            label_team_budget_info.grid(row=i + 1, column=2, sticky='ew', padx=self.FRAME_TEAM_X_PAD)

            # Create "View" button.
            button_view = tk.Button(self.frame_teams_info, text='VIEW')
            button_view.grid(row=i + 1, column=3, sticky='w', padx=self.FRAME_TEAM_X_PAD, pady=2)
        return

if __name__ == "__main__":
    root = tk.Tk()
    auction = Auction()
    team_display_test = TeamDisplay(root, auction)
    team_display_test.pack(side='top', fill='both', expand=True)
    root.mainloop()