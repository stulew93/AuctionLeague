import PIL
import requests
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from classes.auction import Auction
from classes.frame_team_display import TeamDisplay
from classes.frame_transaction_display import TransactionDisplay

class AuctionLot(tk.Frame):

    def __init__(self, parent, auction, team_display, transaction_display):
        tk.Frame.__init__(self, parent)
        self.auction = auction
        self.frame_team_display = team_display
        self.frame_transaction_display = transaction_display

        # Variable to control padding across all widgets.
        self.FRAME_AUCTION_LOT_X_PAD = 10

        # Create frame for nominating team info.
        self.frame_nomination = tk.Frame(self)
        self.frame_nomination.place(relwidth=1, relheight=0.1)

        # Create label for heading "Currently nominating:"
        label_currently_header = tk.Label(self.frame_nomination, text="Currently nominating:", font="none 10 bold")
        label_currently_header.grid(row=0, column=1, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for heading "Next up:"
        label_next_header = tk.Label(self.frame_nomination, text="Next up:", font="none 10 bold")
        label_next_header.grid(row=0, column=2, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create button to initialise nominations.
        button_init_nom = tk.Button(self.frame_nomination, text="Initialise Nominations")
        button_init_nom.grid(row=1, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for the currently nominating team
        label_currently_nom = tk.Label(self.frame_nomination, font="none 10", bg='red')
        label_currently_nom.grid(row=1, column=1, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for the next nominating team
        label_next_nom = tk.Label(self.frame_nomination, font="none 10")
        label_next_nom.grid(row=1, column=2, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create frame for player selection.
        self.frame_player_selection = tk.Frame(self)
        self.frame_player_selection.place(rely=0.1, relwidth=1, relheight=0.15)
        self.columnconfigure((0, 1), weight=1)

        # Create label for heading "Select player below:"
        label_select_player = tk.Label(self.frame_player_selection, text="Player for auction:", font="none 10 bold")
        label_select_player.grid(row=0, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for heading "Filter by club:"
        label_club_filter = tk.Label(self.frame_player_selection, text="Filter by club:", font="none 10 bold")
        label_club_filter.grid(row=0, column=1, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create a combobox to select a player.
        self.player_list = [f"({player['club']}) {player['simple_name_eng_chars']} ({player['id']})"
                            for player in self.auction.players.values()
                            if player['player_purchased'] == False]
        self.combobox_players = ttk.Combobox(self.frame_player_selection, values=sorted(self.player_list), width=40)
        self.combobox_players.set("Select player from dropdown:")
        self.combobox_players.grid(row=1, column=0, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)
        self.combobox_players.bind("<<ComboboxSelected>>", self.display_player)

        # Create combobox to select a club as a filter.
        self.club_list = [self.auction.clubs[club] for club in self.auction.clubs]
        self.combobox_clubs = ttk.Combobox(self.frame_player_selection, values=self.club_list, width=10)
        self.combobox_clubs.set("Select club:")
        self.combobox_clubs.grid(row=1, column=1, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)
        self.combobox_clubs.bind("<<ComboboxSelected>>", self.filter_players_by_club)

        # Create frame to display player image.
        self.frame_player_image = tk.Frame(self)
        self.frame_player_image.place(rely=0.25, relwidth=0.35, relheight=0.4)

        # Create canvas for image
        self.canvas = tk.Canvas(self.frame_player_image)
        self.canvas.place(relwidth=1, relheight=1)

        # Create frame to display player info.
        self.frame_player_info = tk.Frame(self)
        self.frame_player_info.place(relx=0.40, rely=0.25, relwidth=0.4, relheight=0.4)

        # Create label for player info.
        self.label_player_info = tk.Label(self.frame_player_info, font="none 10 bold", justify=tk.LEFT)
        self.label_player_info.grid(row=0, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create frame for team selection and winning bid.
        self.frame_winning_team = tk.Frame(self)
        self.frame_winning_team.place(rely=0.65, relwidth=1, relheight=0.35)

        # Create label for heading "Select winning team:"
        label_select_winning_team = tk.Label(self.frame_winning_team, text="Winning team:", font="none 10 bold")
        label_select_winning_team.grid(row=0, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for heading "Enter winning bid:"
        label_winning_bid = tk.Label(self.frame_winning_team, text="Enter winning bid:", font="none 10 bold")
        label_winning_bid.grid(row=0, column=1, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create combobox to select Team.
        self.teams_list = [self.team.name for team in self.auction.teams]
        self.combobox_teams = ttk.Combobox(self.frame_winning_team, values=self.teams_list, width=25)
        self.combobox_teams.set("Select winning team:")
        self.combobox_teams.bind("<Button>", self.update_teams_list)
        self.combobox_teams.grid(row=1, column=0, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create entry box to enter winning bid.
        self.entry_winning_bid = tk.Entry(self.frame_winning_team, bg='white')
        self.entry_winning_bid.grid(row=1, column=1, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create button to confirm player purchase.
        self.button_confirm_purchase = tk.Button(self.frame_winning_team, text="Confirm", command=self.confirm_purchase)
        self.button_confirm_purchase.grid(row=1,column=2, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)


    def update_teams_list(self, event):
        teams_list = [team for team in self.auction.teams]
        self.combobox_teams['values'] = teams_list
        return

    def update_players_list(self, event=None):
        player_list = [f"({player['club']}) {player['simple_name_eng_chars']} ({player['id']})"
                       for player in self.auction.players.values() if player['player_purchased'] == False]
        self.combobox_players['values'] = sorted(player_list)
        return

    def filter_players_by_club(self, event):
        club = self.combobox_clubs.get()
        filtered_player_list = [f"{player['simple_name_eng_chars']} ({player['id']})"
                                for player in self.auction.players.values()
                                if player['club'] == club and player['player_purchased'] == False]
        self.combobox_players["values"] = sorted(filtered_player_list)
        print(f"Filtered players of {club}.")
        return

    def display_player_image(self, player_code):
        image_loc = f"C:/Users/stuar/Documents/PythonFiles/AuctionLeaguev2/images_repo/player_images/{player_code}.png"

        try:
            if __name__ == "__main__":
                image_loc = f"../images_repo/player_images/{player_code}.png"
            else:
                image_loc = f"images_repo/player_images/{player_code}.png"
            img = Image.open(image_loc)
        except (FileNotFoundError, PIL.UnidentifiedImageError):
            if __name__ == "__main__":
                image_loc = "../images_repo/question_mark.png"
            else:
                image_loc = "images_repo/question_mark.png"
            img = Image.open(image_loc)
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

    def display_player_info(self, player_id):
        player = self.auction.players[player_id]
        player_info = f"FPL name: {player['simple_name_raw']}\n" \
                      f"\n" \
                      f"Full name: {player['first_name'] + ' ' + player['second_name']}\n" \
                      f"\n" \
                      f"Position: {player['position']}\n" \
                      f"\n" \
                      f"Club: {player['club']}"
        self.label_player_info['text'] = player_info

    def display_player(self, event):
        player_name = self.combobox_players.get()
        if player_name[0] == '(':  # if player has club in brackets in front of the name
            player_name = player_name[6:]  # drop the first six characters.
        # Get player_id from the end of the combobox input.
        player_id = int(player_name[player_name.index('(')+1:player_name.index(')')])

        player_code = self.auction.players[player_id]["code"]
        self.display_player_image(player_code)

        self.display_player_info(player_id)
        return

    def reset_auction_lot(self):
        self.update_players_list()
        self.combobox_players.set("Select player from dropdown:")
        self.combobox_clubs.set("Select club:")
        self.combobox_teams.set("Select winning team:")
        self.entry_winning_bid.delete(0, tk.END)
        self.canvas.image = None
        self.label_player_info['text'] = ""
        return

    def confirm_purchase(self):
        player_name = self.combobox_players.get()
        team_name = self.combobox_teams.get()
        price = int(self.entry_winning_bid.get())

        # player_name comes as formatted in the list, with the player is after the name and possibly with the club
        # before the name. Remove the club if it exists before the name and then get the player id.
        if player_name[0] == '(':  # if player has club in brackets in front of the name
            player_name = player_name[6:]  # drop the first six characters.
        # Get player_id from the end of the combobox input.
        player_id = int(player_name[player_name.index('(')+1:player_name.index(')')])

        # Confirm the purchase.
        self.auction.confirm_purchase(team_name, player_id, price)

        # Update/reset frame ready for next auction lot.
        self.reset_auction_lot()

        # Update team display in frame_team_display.
        self.frame_team_display.display_teams()

        # Update the transaction display in frame_transaction_display.
        self.frame_transaction_display.get_latest_transactions()

        print(f"{player_name[:player_name.index('(')-1]} added to team {team_name} for £{price}m.")
        return


if __name__ == "__main__":
    root = tk.Tk()
    auction = Auction()
    frame_team_display = TeamDisplay(root, auction)
    frame_transaction_display = TransactionDisplay(root, auction)
    frame_auction_lot = AuctionLot(root, auction, frame_team_display, frame_transaction_display)
    frame_auction_lot.pack(side='top', fill='both', expand=True)
    auction.add_team("Stuart")
    auction.add_team("Alex")
    print(auction.players[4])
    root.mainloop()

    # frame_auction_lot.display_player_image()
