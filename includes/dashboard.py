# @Author: laurent
# @Date:   2020-12-26T18:43:20+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-12-26T21:34:11+01:00

from tkinter import *
import os
from includes.gaugelib import *
from includes.chrono import *


class Dashboard:
    def __init__(self, master):
        self.master = master

        # set windows dimensions adapted to the screen
        width_screen = self.master.winfo_screenwidth()-150
        height_screen = self.master.winfo_screenheight()-150
        self.master.geometry(f"{width_screen+10}x{height_screen+13}")
        self.master.title("Interface Pilote")
        self.master.configure(bg="black", highlightbackground="black", highlightcolor="red", highlightthickness=5)
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

        self.fuel_frame = LabelFrame(self.master, text="FUEL", bd=3, width=width_screen/6, height=height_screen/4)
        self.fuel_frame.grid(column=5, row=1)
        self.fuel_frame.configure(bg="black", fg="white")

        self.regen_frame = LabelFrame(self.master, text="REGEN", bd=3, width=3*width_screen/6, height=height_screen/4)
        self.regen_frame.grid(column=0, row=2, columnspan=3)
        self.regen_frame.configure(bg="black", fg="white")

        self.ICE_frame = LabelFrame(self.master, text="ICE", bd=3, width=3*width_screen/6, height=height_screen/4)
        self.ICE_frame.grid(column=3, row=2, columnspan=3)
        self.ICE_frame.configure(bg="black", fg="white")

        self.breaks_mode_frame = LabelFrame(self.master, text="BREAKS_MODE", bd=3, width=width_screen/6, height=height_screen/4)
        self.breaks_mode_frame.grid(column=0, row=3)
        self.breaks_mode_frame.configure(bg="black", fg="white")

        self.time_frame = LabelFrame(self.master, text="TIME", bd=3, width=3*width_screen/6, height=height_screen/4)
        self.time_frame.grid(column=1, row=3, columnspan=3)
        self.time_frame.configure(bg="black", fg="white")

        self.speed_frame = LabelFrame(self.master, text="SPEED", bd=3, width=2*width_screen/6, height=height_screen/4)
        self.speed_frame.grid(column=4, row=3, columnspan=2)
        self.speed_frame.configure(bg="black", fg="white")
