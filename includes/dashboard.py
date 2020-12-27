# @Author: laurent
# @Date:   2020-12-26T18:43:20+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-12-27T10:44:02+01:00

from tkinter import *
import os
from includes.gaugelib import *
from includes.chrono import *
import tkinter.font as font


class Dashboard:
    def __init__(self, master):
        self.master = master

        # set windows dimensions adapted to the screen
        width_screen = self.master.winfo_screenwidth()-150
        height_screen = self.master.winfo_screenheight()-150
        f_size = height_screen/100
        self.master.geometry(f"{width_screen+20}x{height_screen+22}")
        self.master.title("Interface Pilote")
        self.master.configure(highlightbackground="red", highlightcolor="red", highlightthickness=10, padx=0, pady=0, borderwidth=0, relief="flat")
        # get current working directory
        cwd = os.getcwd()
        # Add full path of the .ico image
        self.master.iconbitmap(cwd + "/images/estaca.ico")


        # self.master.columnconfigure(0, pad=width_screen/4)
        # self.master.columnconfigure(1, pad=width_screen/4)
        # self.master.columnconfigure(2, pad=width_screen/4)
        # self.master.columnconfigure(3, pad=width_screen/4)
        #
        # self.master.rowconfigure(0, pad=height_screen/4)
        # self.master.rowconfigure(1, pad=height_screen/4)
        # self.master.rowconfigure(2, pad=height_screen/4)
        # self.master.rowconfigure(3, pad=height_screen/4)


        self.lap_frame = LabelFrame(self.master, text="LAP", bd=3, width=width_screen/6, height=height_screen/4)
        self.lap_frame.grid(column=0, row=0)
        self.lap_frame.configure(bg="black", fg="white")

        self.SOC_frame = LabelFrame(self.master, text="SOC", bd=3, width=5*width_screen/6, height=height_screen/4)
        self.SOC_frame.grid(column=1, row=0, columnspan=5)
        self.SOC_frame.configure(bg="black", fg="white")

        self.others_frame = LabelFrame(self.master, text="EMPTY", bd=3, width=width_screen/6, height=height_screen/4)
        self.others_frame.grid(column=0, row=1)
        self.others_frame.configure(bg="black", fg="white")

        self.deltas_frame = LabelFrame(self.master, text="DELTA", bd=3, width=4*width_screen/6, height=height_screen/4)
        self.deltas_frame.grid(column=1, row=1, columnspan=4)
        self.deltas_frame.configure(bg="black", fg="white")



        self.fuel_frame = Frame(self.master, width=width_screen/6, height=height_screen/4)
        # self.fuel_frame = LabelFrame(self.master, text="FUEL", width=width_screen/6, height=height_screen/4)
        self.fuel_frame.grid(column=5, row=1)
        self.fuel_frame.configure(bg="red")
        self.fuel_frame.pack_propagate(0)

        self.fuel_label = Label(self.fuel_frame, text="FUEL")
        self.fuel_label.pack()
        self.fuel_label.configure(bg="red", fg="white", font=("Helvetica", 44))

        self.state_label = Label(self.fuel_frame, text="ON")
        self.state_label.pack()
        self.state_label.configure(bg="red", fg="yellow", font=("Helvetica", 44))



        self.regen_frame = LabelFrame(self.master, text="REGEN", bd=3, width=3*width_screen/6, height=height_screen/4)
        self.regen_frame.grid(column=0, row=2, columnspan=3)
        self.regen_frame.configure(bg="black", fg="white")

        self.ICE_frame = LabelFrame(self.master, bd=3, width=3*width_screen/6, height=height_screen/4)
        self.ICE_frame.grid(column=3, row=2, columnspan=3)
        self.ICE_frame.configure(bg="black", fg="white")
        self.ICE_frame.grid_propagate(0)

        self.turn_ICE_frame = Frame(self.ICE_frame, width=width_screen/8, height=height_screen/4,)
        self.turn_ICE_frame.grid(column=0, row=0)
        self.turn_ICE_frame.pack_propagate(0)

        self.turn_ICE_label = Label(self.turn_ICE_frame, text='TURN')
        self.turn_ICE_label.configure(font=("Helvetica", 40))
        self.turn_ICE_label.pack()

        self.num_turn_ICE_label = Label(self.turn_ICE_frame, text='2')
        self.num_turn_ICE_label.configure(font=("Helvetica", 48))
        self.num_turn_ICE_label.pack()

        self.speed_ICE_frame = Frame(self.ICE_frame, width=3*width_screen/8, height=height_screen/4, background="black")
        self.speed_ICE_frame.grid(column=1, row=0)
        self.speed_ICE_frame.pack_propagate(0)


        self.speed_ICE_label = Label(self.speed_ICE_frame, text='ICE')
        self.speed_ICE_label.configure(font=("Helvetica", 30), bg='black', fg="white")
        self.speed_ICE_label.pack(anchor='nw')

        self.num_speed_ICE_label = Label(self.speed_ICE_frame, text='10 Km/h')
        self.num_speed_ICE_label.configure(font=("Helvetica", 25), bg='black', fg="white")
        self.num_speed_ICE_label.pack(anchor='s')



        self.breaks_mode_frame = Frame(self.master, width=width_screen/6, height=height_screen/4)
        self.breaks_mode_frame.grid(column=0, row=3)
        self.breaks_mode_frame.pack_propagate(0)
        self.breaks_mode_frame.configure(bg="black")

        self.breaks_label = Label(self.breaks_mode_frame, text="BRK")
        self.breaks_label.place(x=width_screen/6/5, y=height_screen/6/5)
        self.breaks_label.configure(bg="red", fg="white", font=("Helvetica", 44))

        self.mode_label = Label(self.breaks_mode_frame, text="HY")
        self.mode_label.pack(anchor="sw", side=BOTTOM)
        self.mode_label.configure(bg="red", fg="white", font=("Helvetica", 44))




        self.time_frame = LabelFrame(self.master, text="TIME", bd=3, width=3*width_screen/6, height=height_screen/4)
        self.time_frame.grid(column=1, row=3, columnspan=3)
        self.time_frame.configure(bg="black", fg="white")

        self.speed_frame = LabelFrame(self.master, text="SPEED", bd=3, width=2*width_screen/6, height=height_screen/4)
        self.speed_frame.grid(column=4, row=3, columnspan=2)
        self.speed_frame.configure(bg="black", fg="white")
