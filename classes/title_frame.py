import tkinter as tk
from classes.auction import Auction

class TitleFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)

        # create title label:
        self.label_title = tk.Label(self, text="Auction League", font="none 16 bold")
        self.label_title.place(relx=0.5, rely=0.5, anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    frame_title = TitleFrame()
    frame_title.pack(side='top', fill='both', expand=True)
    root.mainloop()