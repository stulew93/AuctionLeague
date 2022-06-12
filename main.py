import tkinter as tk
from classes.auction import Auction
from classes.frame_title import TitleFrame
from classes.frame_team_display import TeamDisplay

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
frame_teams.place(rely=0.05, relwidth=0.33, relheight=0.95)


# frame for selecting player to auction.
frame_auction = tk.Frame(window, bg='green')
frame_auction.place(relx=0.33, rely=0.05, relwidth=0.34, relheight=0.95)

# frame for displaying past purchases.
frame_history = tk.Frame(window, bg='black')
frame_history.place(relx=0.67, rely=0.05, relwidth=0.33, relheight=0.95)

# Run mainloop.
window.mainloop()
