from tkinter import *
import time


class Chrono(Frame):
    def __init__(self, master):
        self.frame = LabelFrame(master, text="Chrono", padx=10, pady=10)
        self.frame.pack(side=LEFT, anchor=S)

        self.titre = Label(self.frame, text="Chronometre")
        self.titre.grid(column=0, row=0)

        self.play_pause_button = Button(self.frame, text="Play", command=self.play_pause)
        self.play_pause_bin = 0
        self.play_pause_button.grid(column=0, row=1)

    def play_pause(self):
        if self.play_pause_bin == 0:
            self.play_pause_button.config(text="Pause")
            self.play_pause_bin = 1
        else:
            self.play_pause_button.config(text="Play")
            self.play_pause_bin = 0
