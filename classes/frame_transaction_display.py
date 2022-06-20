import tkinter as tk
from classes.auction import Auction

class TransactionDisplay(tk.Frame):

    def __init__(self, parent, auction):
        tk.Frame.__init__(self, parent, bg='blue')
        self.auction = auction

    pass
