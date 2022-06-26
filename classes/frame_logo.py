import tkinter as tk
from PIL import ImageTk, Image

class LogoFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='green')

        # Create canvas for logo
        self.canvas = tk.Canvas(self)
        self.canvas.place(relwidth=1, relheight=1)
        # Add image to canvas.
        self.image_loc = "images_repo/auction_league_logo.png"
        self.img = Image.open(self.image_loc)
        self.canvas.image = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        self.canvas.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        # print(new_height)
        self.img = self.img.resize((new_width, new_height), Image.ANTIALIAS)
        self.canvas.image = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
