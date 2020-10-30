# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-10-30T13:05:50+01:00

from tkinter import *

# Crée une fenêtre
window = Tk()
window.title("Interface Pilote")
window.iconbitmap("SiERA_logo.ico")

# set windows dimensions adapted to the screen
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
window.geometry(f"{width_screen}x{height_screen}")


def start_click():
    # Note : le premier paramètre passé est l'objet instancié concerné
    label = Label(window, text="Voici notre interface SiERA")
    label.pack()

def print_name():
    if (input.get() == "mdp"):
        name = Label(window, text="je m'appelle CaCa")
        name.pack()

input = Entry(window)
input.pack()

start_btn = Button(window, text="Commencer", command=start_click, bg="green")
start_btn.pack()

name_btn = Button(window, text="mot de passe", command=print_name)
name_btn.pack()

# Boucle Tkinter qui s'interompt quand on ferme la fenêtre
window.mainloop()
