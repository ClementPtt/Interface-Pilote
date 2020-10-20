# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-10-20T17:05:53+02:00

from tkinter import *

# Crée une fenêtre
window = Tk()
window.title("Interface Pilote")

#set windows dimensions adapted to the screen
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
window.geometry(f"{width_screen}x{height_screen}")




# Note : le premier paramètre passé est l'objet instancié concerné
label = Label(window, text="Voici notre interface SiERA")
label.pack()




frame1 = Frame(window, borderwidth=2, highlightcolor="red", bg="blue")
frame1.pack()

quit_btn = Button(frame1, text="Quitter", command=window.quit)
quit_btn.grid(row=0, column=0)

message = Label(frame1, text="Dans le frame1")
message.grid(row=1, column=1)


# Boucle Tkinter qui s'interompt quand on ferme la fenêtre
mainloop()
