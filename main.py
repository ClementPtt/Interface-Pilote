# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-11-01T16:19:18+01:00

from tkinter import *

# Crée une fenêtre
window = Tk()
window.title("Interface Pilote")
# Add full path of the .ico image (not relative path)
window.iconbitmap("/Users/laurent/Desktop/SiERA/PITA/Interface-Pilote/images/estaca.ico") #l'image n'est pas au bon format encore je crois

# set windows dimensions adapted to the screen
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
window.geometry(f"{width_screen}x{height_screen}")


def start_click():
    # Note : le premier paramètre passé est l'objet instancié concerné
    label = Label(window, text="Voici notre interface SiERA")
    label.pack()

def pwd_ft():
    if (input.get() == "root"):
        msg = Label(window, text="tu as trouvé le mdp !")
        msg.pack()

input = Entry(window)
input.pack()

start_btn = Button(window, text="Commencer", command=start_click, bg="green")
start_btn.pack()

pwd_btn = Button(window, text="mot de passe", command=pwd_ft)
pwd_btn.pack()

# Boucle Tkinter qui s'interompt quand on ferme la fenêtre
window.mainloop()
