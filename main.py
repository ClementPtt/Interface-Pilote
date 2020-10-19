# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-10-20T00:12:44+02:00

from tkinter import *

# On crée une fenêtre
window = Tk()
window.title("Interface Pilote")

#set windows dimensions adapted to the screen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")

# Note : le premier paramètre passé est l'objet instancié concerné
label = Label(window, text="Test de Label")
label.pack()

quit_btn = Button(window, text="Quitter", command=window.quit)
quit_btn.pack()

frame1 = Frame(window, width=width, height=height, borderwidth=1, bg="blue")
frame1.pack()

message = Label(frame1, text="Siera window")
message.pack(side="top", fill=X)


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
mainloop()
