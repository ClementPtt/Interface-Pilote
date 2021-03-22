# @Date:   2021-03-22T12:52:26+01:00
# @Last modified time: 2021-03-22T14:03:57+01:00

from tkinter import *
import os
import math
from includes.chrono import *
import tkinter.font as font

class Dashboard:
    def __init__(self, master):
        self.master = master

        #Variables du menu
        self.engine_rpm=2013 #RPM
        self.engine_torque=2.67 #Nm
        self.engine_temp=84.5 #°C
        self.p_fuel=3.45 #bars
        self.fuel_cons=2.25 #mL
        self.ice_clutch1=False #True si ICE Clutch ON
        self.motor_rpm=0
        self.motor_torque=0
        self.motor_temp=45.6
        self.distance=15.2 #km
        self.efficiency=712 #km/L
        self.ice_clutch2=True #False si ICE Clutch OFF
        self.fuel_mode=True #True si mode FUEL ON
        self.soc=57 #%
        self.lipo=65 #%
        self.connexion=True #True si état de connexion 3g OK
        self.gps=True #True si connexion GPS OK
        self.speed=25 #km/h
        self.hybride_mode=True #False si mode HY pas activé

        # self.speed = 10.5
        self.time = 25320  # en millisecondes
        self.break_value = False
        self.turn_regen = 8
        self.value_regen = 95  # en pourcent
        self.target_speed = 34.5  # en km
        self.turn_ice = 2
        # self.fuel = True = fuel_mode
        # self.mode = True  # True en mode hybride = hybride_mode
        # self.value_soc = 80  # en pourcent = soc
        self.race_delta = -18.5
        self.live_delta = 2.5
        self.n_1_delta = -3.8
        self.target_soc = 85

        #CONDITIONNEMENT

        # Mode Hybride
        if self.hybride_mode==False :
            hy_color="white"
            hy_background="white"
            hy_police="black"
        else:
            hy_color="red"
            hy_background="red"
            hy_police="white"

        # Etat ICE Clutch engine
        if self.ice_clutch1==True :
            clutch1_background="red"
            clutch1_value="ON"
            clutch1_contour="red"
        else:
            clutch1_background="black"
            clutch1_contour="white"
            clutch1_value="OFF"

        # Etat ICE Clutch motor
        if self.ice_clutch2==True :
            clutch2_background="red"
            clutch2_value="ON"
            clutch2_contour="red"
        else:
            clutch2_background="black"
            clutch2_contour="white"
            clutch2_value="OFF"

        # Fuel mode
        if self.fuel_mode == True :
            fuel_mode_value="ON"
            fuel_mode_background="red"
            fuel_mode_contour="red"
        else:
            fuel_mode_value="OFF"
            fuel_mode_background="black"
            fuel_mode_contour="white"

        # Etat connexion 3g
        if self.connexion == True :
            etat_connexion_background="#03FF00"
            etat_connexion_label="black"
        else:
            etat_connexion_background="red"
            etat_connexion_label="white"

        # Etat connexion GPS
        if self.gps == True :
            etat_gps_background="#03FF00"
            etat_gps_label="black"
        else:
            etat_gps_background="red"
            etat_gps_label="white"

        # Etat Breaks
        if self.break_value == False :
            breaks_background="black"
        else:
            breaks_background= "red"





        #Fenêtre qui s'adapte à la taille de l'écran
        width_screen = self.master.winfo_screenwidth()-20 #-20 de highlightthockness=10
        height_screen = self.master.winfo_screenheight()-20 #-20 de highlightthockness=10


        # space = math.ceil(width_screen/50) #variable qui va espacer les différents cadres


        self.master.geometry(f"{width_screen+space}x{height_screen+space}")



        # self.master.title("Menu TEST")




        self.master.configure(bg="black", highlightbackground=hy_background, highlightcolor=hy_background, highlightthickness=10, padx=0, pady=0, borderwidth=0, relief="flat")
        # get current working directory
        cwd = os.getcwd()
        # Add full path of the .ico image
        # self.master.iconbitmap(cwd + "/images/estaca.ico")

        #On définit la taille des différentes font en fonction de la taille de l'écran
        font_titre=("Arial", int(space*0.8),"bold")
        font_titre_donnees=("Arial", int(space*1.5),"bold")
        font_donnees=("Arial", int(space*1.75),"bold")
        font_vitesse=("Arial", int(space*2.5),"bold")
        font_hy=("Arial", int(space*2),"bold")
        font_etat_clutch=("Arial", int(space*1.2),"bold")
        font_titre_signaux=("Arial", int(space*1.2),"bold")
