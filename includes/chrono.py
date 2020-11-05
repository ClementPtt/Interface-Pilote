# @Date:   2020-11-04T22:19:22+01:00
# @Last modified time: 2020-11-05T01:42:06+01:00



from tkinter import *
import tkinter as tk
import time


class Chrono(LabelFrame): # use Frame if we dont need LabelFrame
    def __init__(self, master):
        LabelFrame.__init__(self, master, text="widget")
        self.titre = Label(self, text="Chronometre")
        self.titre.pack()

        self.play_pause_bin = 0
        self.play_pause_button = Button(self, text="Play", command=self.play_pause)
        self.play_pause_button.pack()

    def play_pause(self):
        if self.play_pause_bin == 0:
            self.start = time.time()
            self.play_pause_button.config(text="Pause")
            self.play_pause_bin = 1
            self.cunt()
        else:
            self.play_pause_button.config(text="Play")
            self.play_pause_bin = 0
            self.cunt()

    def cunt(self):
        if self.play_pause_bin == 1:
            self.compteur = int(time.time() - self.start)
            self.chronometre.config(text=self.compteur)
            self.chronometre.after(1000, self.cunt)
        else:
            self.chronometre.config(text=self.compteur)
