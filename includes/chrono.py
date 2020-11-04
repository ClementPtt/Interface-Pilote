from tkinter import *

class Chrono(Frame):
    def __init__(self, master):
        self.frame = LabelFrame(master, text="Chrono", padx=10, pady=10)
        self.frame.pack(side=LEFT, anchor=S)

        self.titre = Label(self.frame, text="Chronometre")
        self.titre.grid(column=0, row=0)

        play = Button(master, text="Play", command=self.play)
        play.pack()

    def play(self):
        self.titre.config(text="test")
