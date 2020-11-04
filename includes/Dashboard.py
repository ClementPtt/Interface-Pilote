# @Date:   2020-10-15T19:31:27+02:00
# @Last modified time: 2020-11-04T15:52:09+01:00
import tkinter as tk
from tkinter import *
from PIL import *
import os
from includes import gaugelib


class Dashboard:
    def __init__(self, master):
        self.master = master

        # set windows dimensions adapted to the screen
        width_screen = self.master.winfo_screenwidth()
        height_screen = self.master.winfo_screenheight()
        self.master.geometry(f"{width_screen}x{height_screen}")

        # get current working directory
        cwd = os.getcwd()

        self.master.title("Interface Pilote")
        # Add full path of the .ico image
        self.master.iconbitmap(cwd + "/images/estaca.ico")

        # DONNEES MOTEUR
        # - Signal fuel ON (contact voiture)
        # - Température moteur
        # - Temps ouverture injecteur
        # - Pression du carburant
        # - Rotation par minute

        motor_frame = LabelFrame(master, text="DONNÉES MOTEUR", padx=5, pady=5)
        motor_frame.pack(side=LEFT, anchor=NW)

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

        # TEMPS
        # - temps par tour
        # - chronometre depuis le debut du tour

        time_frame = LabelFrame(master, text="TEMPS", padx=5, pady=5)
        time_frame.pack(side=TOP, anchor=E)

        time_round = Label(time_frame, text="Temps par tour")
        time_round.grid(column=0, row=0)
        chrono_round = Label(time_frame, text="Chrono depuis le début du tour")
        chrono_round.grid(column=1, row=0)

        # VITESSES
        # - Vitesse instantanée
        # - Vitesse moyenne tour actuel
        # - Vitesse moyenne tour précédent

        speed_frame = LabelFrame(master, text="VITESSES", padx=5, pady=5)
        speed_frame.place(relx=.5, rely=.5, anchor=CENTER)
        # speed_frame.pack()

        speed_round = Label(speed_frame, text="Vitesse moyenne tour actuel")
        speed_round.grid(column=0, row=0)
        speed = Label(speed_frame, text="Vitesse instantanée")
        speed.grid(column=0, row=1)
        speed_last_round = Label(speed_frame, text="Vitesse moyenne tour précédent")
        speed_last_round.grid(column=0, row=2)

        p1 = gaugelib.DrawGauge2(
            master,
            max_value=100.0,
            min_value=0,
            size=200,
            bg_col='black',
            unit="Vitesse km/h", bg_sel=2)
        p1.pack()

        others_frame = LabelFrame(master, text="AUTRES", padx=5, pady=5)
        others_frame.pack(side=RIGHT, anchor=S)

        battery_tension = Label(others_frame, text="Tension de la batterie")
        battery_tension.grid(column=0, row=0)
        lambda_sens = Label(others_frame, text="Données de la sonde lambda")
        lambda_sens.grid(column=1, row=0)
