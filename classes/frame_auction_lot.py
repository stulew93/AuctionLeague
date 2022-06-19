import PIL
import requests
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from classes.auction import Auction

class AuctionLot(tk.Frame):

    def __init__(self, parent, auction):
        tk.Frame.__init__(self, parent)
        self.auction = auction

        # Variable to control padding across all widgets.
        self.FRAME_AUCTION_LOT_X_PAD = 10

        # Create frame for player selection.
        self.frame_player_selection = tk.Frame(self)
        self.frame_player_selection.place(relwidth=1, relheight=0.15)
        self.columnconfigure((0, 1), weight=1)

        # Create label for heading "Select player below:"
        label_select_player = tk.Label(self.frame_player_selection, text="Player for auction:", font="none 10 bold")
        label_select_player.grid(row=0, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create label for heading "Filter by club:"
        label_club_filter = tk.Label(self.frame_player_selection, text="Filter by club:", font="none 10 bold")
        label_club_filter.grid(row=0, column=1, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create a combobox to select a player.
        # self.player_list = [self.auction.players[player]['simple_name_eng_chars'] for player in self.auction.players]
        self.player_list = [f"({self.auction.players[player]['club']}) " \
                             f"{self.auction.players[player]['simple_name_eng_chars']}"
                             for player in self.auction.players]
        self.combobox_players = ttk.Combobox(self.frame_player_selection, values=sorted(self.player_list), width=40)
        self.combobox_players.set("Select player from dropdown:")
        self.combobox_players.grid(row=1, column=0, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)
        self.combobox_players.bind("<<ComboboxSelected>>", self.display_player_image)

        # Create combobox to select a club as a filter.
        self.club_list = [self.auction.clubs[club] for club in self.auction.clubs]
        self.combobox_clubs = ttk.Combobox(self.frame_player_selection, values=self.club_list, width=10)
        self.combobox_clubs.set("Select club:")
        self.combobox_clubs.grid(row=1, column=1, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)
        self.combobox_clubs.bind("<<ComboboxSelected>>", self.filter_players_by_club)

        # Create frame to display player image.
        self.frame_player_image = tk.Frame(self)
        self.frame_player_image.place(rely=0.15, relwidth=0.35, relheight=0.4)

        # Create canvas for image
        self.canvas = tk.Canvas(self.frame_player_image)
        self.canvas.place(relwidth=1, relheight=1)

        # Create frame to display player info.
        self.frame_player_info = tk.Frame(self, bg='red')
        self.frame_player_info.place(relx=0.35, rely=0.15, relwidth=0.4, relheight=0.4)

        # Create label for player info.
        info_text = "Text that will describe the player"
        # TODO: function to update player text when player is selected.
        label_player_info = tk.Label(self.frame_player_info, text=info_text, font="none 10 bold")
        label_player_info.grid(row=0, column=0, sticky='w', padx=self.FRAME_AUCTION_LOT_X_PAD)

        # Create frame for team selection and winning bid.
        self.frame_winning_team = tk.Frame(self, bg='green')
        self.frame_winning_team.place(rely=0.6, relwidth=1, relheight=0.4)

        # Create combobox to select Team.
        self.teams_list = [self.team.name for team in self.auction.teams]
        self.combobox_teams = ttk.Combobox(self.frame_winning_team, values=self.teams_list, width=25)
        self.combobox_teams.set("Select winning team:")
        self.combobox_teams.bind("<Button>", self.update_teams_list_for_combobox)
        self.combobox_teams.grid(row=0, column=0, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)


    def update_teams_list_for_combobox(self, event):
        teams_list = [team.name for team in self.auction.teams]
        self.combobox_teams['values'] = teams_list
        return

    def filter_players_by_club(self, event):
        club = self.combobox_clubs.get()
        filtered_player_list = [self.auction.players[player]['simple_name_eng_chars'] for player in self.auction.players
                                if self.auction.players[player]['club'] == club]
        self.combobox_players["values"] = sorted(filtered_player_list)
        print(f"Filtered players of {club}.")
        return

    def display_player_image(self, event):
        player_name = self.combobox_players.get()
        if player_name[0] == '(':  # if player has club in brackets in front of the name
            player_name = player_name[6:]  # drop the first six characters.
        player_code = [player["code"] for player in self.auction.players.values()
                       if player["simple_name_eng_chars"] == player_name
                       ][0]
        image_loc = f"C:/Users/stuar/Documents/PythonFiles/AuctionLeaguev2/images_repo/player_images/{player_code}.png"

        # root_image_url = "https://resources.premierleague.com/premierleague/photos/players/110x140/p{}.png"
        # image_url = root_image_url.format(player_code)
        # # print(image_url)
        # image_req = requests.get(image_url)
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
        # self.canvas.image = ImageTk.PhotoImage(image_req.content)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        # image_label = tk.Label(self.frame_player_image, image=player_image)


if __name__ == "__main__":
    root = tk.Tk()
    auction = Auction()
    frame_auction_lot = AuctionLot(root, auction)
    auction.add_team("Stuart")
    auction.add_team("Alex")
    frame_auction_lot.pack(side='top', fill='both', expand=True)
    root.mainloop()

    # frame_auction_lot.display_player_image()
