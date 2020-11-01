# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-11-01T18:23:16+01:00

from tkinter import *
from PIL import *

# Crée une fenêtre
window = Tk()
window.title("Interface Pilote")
# Add full path of the .ico image (not relative path)
window.iconbitmap("/Users/laurent/Desktop/SiERA/PITA/Interface-Pilote/images/estaca.ico")

# set windows dimensions adapted to the screen
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
window.geometry(f"{width_screen}x{height_screen}")




# VITESSES
# - Vitesse instantanée
# - Vitesse moyenne tour actuel
# - Vitesse moyenne tour précédent

speed_frame = LabelFrame(window, text="VITESSES", padx=5, pady=5) #padding
speed_frame.pack(padx=5, pady=5) #margin

speed_round = Label(speed_frame, text="Vitesse moyenne tour actuel")
speed_round.grid(column=0, row=0)
speed = Label(speed_frame, text="Vitesse instantanée")
speed.grid(column=1, row=0)
speed_last_round = Label(speed_frame, text="Vitesse moyenne tour précédent")
speed_last_round.grid(column=2, row=0)

# DONNEES MOTEUR
# - Signal fuel ON (contact voiture)
# - Température moteur
# - Temps ouverture injecteur
# - Pression du carburant
# - Rotation par minute

motor_frame = LabelFrame(window, text="DONNÉES MOTEUR", padx=5, pady=5)
motor_frame.pack(padx=5, pady=5)

fuel_on = Label(motor_frame, text="Signal fuel ON")
fuel_on.grid(column=0, row=4)
motor_temp = Label(motor_frame, text="Température moteur")
motor_temp.grid(column=0, row=1)
injection_op_time = Label(motor_frame, text="Temps ouverture injecteur")
injection_op_time.grid(column=0, row=2)
fuel_pressure = Label(motor_frame, text="Pression carburant")
fuel_pressure.grid(column=0, row=3)
rpm = Label(motor_frame, text="Rotation par minute")
rpm.grid(column=0, row=0)
# TEMPS
# - temps par tour
# - chronometre depuis le debut du tour

# AUTRES
# - Tension de batterie
# - Données de sonde lambda








exit_btn = Button(window, text="Quitter", command=window.quit, fg="red")
exit_btn.pack()

# Boucle Tkinter qui s'interompt quand on ferme la fenêtre
window.mainloop()
