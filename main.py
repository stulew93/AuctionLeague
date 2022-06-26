import tkinter as tk
from PIL import ImageTk, Image
from classes.auction import Auction
from classes.frame_title import TitleFrame
from classes.frame_team_display import TeamDisplay
from classes.frame_auction_lot import AuctionLot
from classes.frame_transaction_display import TransactionDisplay
from classes.frame_logo import LogoFrame

HEIGHT = 600
WIDTH = 800

# main:
window = tk.Tk()
window.title("Auction League")

# Initialise Auction:
auction = Auction()

# canvas; used to set the initial window size.
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame for window title.
frame_title = TitleFrame(window)
frame_title.place(relwidth=1, relheight=0.05)

# Team section; the left hand column in the main display.
frame_teams = TeamDisplay(window, auction)
frame_teams.place(rely=0.05, relwidth=0.30, relheight=0.95)

# frame for displaying past purchases.
frame_transactions = TransactionDisplay(window, auction)
frame_transactions.place(relx=0.7, rely=0.05, relwidth=0.3, relheight=0.95)

# frame for selecting player to auction.
frame_auction = AuctionLot(window, auction, frame_teams, frame_transactions)
frame_auction.place(relx=0.32, rely=0.05, relwidth=0.36, relheight=0.95)

# border frames
frame_border_1 = tk.Frame(window, bg='black')
frame_border_2 = tk.Frame(window, bg='black')
frame_border_1.place(relx=0.305, rely=0.05, relwidth=0.01, relheight=0.95)
frame_border_2.place(relx=0.685, rely=0.05, relwidth=0.01, relheight=0.95)

# Logo frame
frame_logo = LogoFrame(window)
frame_logo.place(relx=0.7, rely=0.675, relwidth=0.295, relheight=0.3)

# Run mainloop.
window.mainloop()
