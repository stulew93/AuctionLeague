import tkinter as tk
from tkinter import ttk
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

        # Create combobox to select a club as a filter.
        self.club_list = [self.auction.clubs[club] for club in self.auction.clubs]
        self.combobox_clubs = ttk.Combobox(self.frame_player_selection, values=self.club_list, width=10)
        self.combobox_clubs.set("Select club:")
        self.combobox_clubs.grid(row=1, column=1, sticky='ew', padx=self.FRAME_AUCTION_LOT_X_PAD)
        self.combobox_clubs.bind("<<ComboboxSelected>>", self.filter_players_by_club)


    def filter_players_by_club(self, event):
        club = self.combobox_clubs.get()
        filtered_player_list = [self.auction.players[player]['simple_name_eng_chars'] for player in self.auction.players
                                if self.auction.players[player]['club'] == club]
        self.combobox_players["values"] = sorted(filtered_player_list)
        print("filter players by club")


if __name__ == "__main__":
    root = tk.Tk()
    auction = Auction()
    frame_auction_lot = AuctionLot(root, auction)
    frame_auction_lot.pack(side='top', fill='both', expand=True)
    root.mainloop()