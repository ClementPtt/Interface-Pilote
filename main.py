# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-11-01T18:50:22+01:00

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



# DONNEES MOTEUR
# - Signal fuel ON (contact voiture)
# - Température moteur
# - Temps ouverture injecteur
# - Pression du carburant
# - Rotation par minute

motor_frame = LabelFrame(window, text="DONNÉES MOTEUR", padx=5, pady=5) #padding
motor_frame.grid(column=0, row=0)

fuel_on = Label(motor_frame, text="Signal fuel ON")
fuel_on.grid(column=0, row=0)
motor_temp = Label(motor_frame, text="Température moteur")
motor_temp.grid(column=0, row=3)
injection_op_time = Label(motor_frame, text="Temps ouverture injecteur")
injection_op_time.grid(column=0, row=4)
fuel_pressure = Label(motor_frame, text="Pression carburant")
fuel_pressure.grid(column=0, row=2)
rpm = Label(motor_frame, text="Rotation par minute")
rpm.grid(column=0, row=1)


# VITESSES
# - Vitesse instantanée
# - Vitesse moyenne tour actuel
# - Vitesse moyenne tour précédent

speed_frame = LabelFrame(window, text="VITESSES", padx=5, pady=5)
speed_frame.grid(column=1, row=1)

speed_round = Label(speed_frame, text="Vitesse moyenne tour actuel")
speed_round.grid(column=0, row=0)
speed = Label(speed_frame, text="Vitesse instantanée")
speed.grid(column=0, row=1)
speed_last_round = Label(speed_frame, text="Vitesse moyenne tour précédent")
speed_last_round.grid(column=0, row=2)


# TEMPS
# - temps par tour
# - chronometre depuis le debut du tour

time_frame = LabelFrame(window, text="TEMPS", padx=5, pady=5)
time_frame.grid(column=2, row=2)

time_round = Label(time_frame, text="Temps par tour")
time_round.grid(column=0, row=0)
chrono_round = Label(time_frame, text="Chrono depuis le début du tour")
chrono_round.grid(column=1, row=0)


# AUTRES
# - Tension de batterie
# - Données de sonde lambda

others_frame = LabelFrame(window, text="AUTRES", padx=5, pady=5)
others_frame.grid(column=2, row=0)

battery_tension = Label(others_frame, text="Tension de la batterie")
battery_tension.grid(column=0, row=0)
lambda_sens = Label(others_frame, text="Données de la sonde lambda")
lambda_sens.grid(column=1, row=0)






exit_btn = Button(window, text="Quitter", command=window.quit, fg="red")
exit_btn.grid(column=2, row=3)

# Boucle Tkinter qui s'interompt quand on ferme la fenêtre
window.mainloop()
