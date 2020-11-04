from tkinter import *
import tkinter as tk
import time


class Chrono(Frame):
    def __init__(self, master):

        self.titre = Label(master, text="Chronometre")
        self.titre.grid(column=0, row=0)

        self.chronometre = Label(master)
        self.chronometre.grid(column=0, row=1)

        self.play_pause_button = Button(master, text="Play", command=self.play_pause)
        self.play_pause_bin = 0
        self.play_pause_button.grid(column=0, row=2)

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
