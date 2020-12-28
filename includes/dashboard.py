# @Author: laurent
# @Date:   2020-12-26T18:43:20+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-12-28T16:51:05+01:00

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
        space = width_screen/40
        self.master.geometry(f"{width_screen+20}x{height_screen+22}")
        self.master.title("Interface Pilote")
        self.master.configure(bg="black", highlightbackground="red", highlightcolor="red", highlightthickness=10, padx=0, pady=0, borderwidth=0, relief="flat")
        # get current working directory
        cwd = os.getcwd()
        # Add full path of the .ico image
        self.master.iconbitmap(cwd + "/images/estaca.ico")


        self.master.columnconfigure(0, minsize=width_screen/6)
        self.master.columnconfigure(1, minsize=width_screen/6)
        self.master.columnconfigure(2, minsize=width_screen/6)
        self.master.columnconfigure(3, minsize=width_screen/6)
        self.master.columnconfigure(4, minsize=width_screen/6)
        self.master.columnconfigure(5, minsize=width_screen/6)


        self.master.rowconfigure(0, minsize=height_screen/4)
        self.master.rowconfigure(1, minsize=height_screen/4)
        self.master.rowconfigure(2, minsize=height_screen/4)
        self.master.rowconfigure(3, minsize=height_screen/4)





        self.lap_frame = Frame(self.master, width=width_screen/6-space, height=height_screen/4-space)
        self.lap_frame.grid(column=0, row=0)
        self.lap_frame.configure(bg="black", highlightbackground="white", highlightthickness=2)
        self.lap_frame.pack_propagate(0)

        self.lap_label = Label(self.lap_frame, text="LAP")
        self.lap_label.pack()
        self.lap_label.configure(bg=self.lap_frame["bg"], fg="white", font=("Helvetica", 26))

        self.num_lap_label = Label(self.lap_frame, text="8/11")
        self.num_lap_label.pack(expand=True)
        self.num_lap_label.configure(bg=self.lap_frame["bg"], fg="yellow", font=("Helvetica", 50))





        self.SOC_frame = LabelFrame(self.master, text="SOC", bd=3, width=5*width_screen/6-space, height=height_screen/4-space)
        self.SOC_frame.grid(column=1, row=0, columnspan=5)
        self.SOC_frame.configure(bg="black", fg="white")





        self.others_frame = LabelFrame(self.master, text="EMPTY", bd=3, width=width_screen/6-space, height=height_screen/4-space)
        self.others_frame.grid(column=0, row=1)
        self.others_frame.configure(bg="black", fg="white")




        self.deltas_frame = Frame(self.master, width=4*width_screen/6-space*2, height=height_screen/4-space)
        self.deltas_frame.grid(column=1, row=1, columnspan=4)
        self.deltas_frame.configure(bg="black", highlightbackground="white", highlightthickness=2)
        self.deltas_frame.grid_propagate(0)

        self.liveD_frame = Frame(self.deltas_frame, width=width_screen*2/9-2-2*space/3,
        height=height_screen/4-space-4, bg='white')
        self.liveD_frame.grid(column=1, row=0)
        self.liveD_frame.pack_propagate(0)

        self.liveD_label = Label(self.liveD_frame, text='LIVE DELTA')
        self.liveD_label.configure(font=("Helvetica", 25), bg='white', fg='black')
        self.liveD_label.pack()

        self.num_liveD_label = Label(self.liveD_frame, text='+2.5s')
        self.num_liveD_label.configure(font=("Helvetica", 40), bg='white', fg='red')
        self.num_liveD_label.pack(expand=True)

        self.raceD_frame = Frame(self.deltas_frame, width=width_screen*2/9-2-2*space/3,
        height=height_screen/4-space-4, bg='black')
        self.raceD_frame.grid(column=0, row=0)
        self.raceD_frame.pack_propagate(0)

        self.raceD_label = Label(self.raceD_frame, text='RACE DELTA')
        self.raceD_label.configure(font=("Helvetica", 25), bg=self.deltas_frame["bg"], fg='white')
        self.raceD_label.pack()

        self.num_raceD_label = Label(self.raceD_frame, text='-18 s')
        self.num_raceD_label.configure(font=("Helvetica", 40), bg=self.deltas_frame["bg"], fg='green')
        self.num_raceD_label.pack(expand=True)

        self.nD_frame = Frame(self.deltas_frame, width=width_screen*2/9-2-2*space/3,
        height=height_screen/4-space-4, bg='black')
        self.nD_frame.grid(column=2, row=0)
        self.nD_frame.pack_propagate(0)

        self.nD_label = Label(self.nD_frame, text='N-1 DELTA')
        self.nD_label.configure(font=("Helvetica", 25), bg=self.deltas_frame["bg"], fg='white')
        self.nD_label.pack()

        self.nD_label = Label(self.nD_frame, text='-3.8 s')
        self.nD_label.configure(font=("Helvetica", 40), bg=self.deltas_frame["bg"], fg='green')
        self.nD_label.pack(expand=True)






        self.fuel_frame = Frame(self.master, width=width_screen/6-space, height=height_screen/4-space)
        self.fuel_frame.grid(column=5, row=1)
        self.fuel_frame.configure(bg="black", highlightbackground="white", highlightthickness=2)
        self.fuel_frame.pack_propagate(0)

        self.fuel_label = Label(self.fuel_frame, text="FUEL")
        self.fuel_label.pack()
        self.fuel_label.configure(bg=self.fuel_frame["bg"], fg="white", font=("Helvetica", 25))

        self.state_label = Label(self.fuel_frame, text="ON")
        self.state_label.pack(expand=True)
        self.state_label.configure(bg=self.fuel_frame["bg"], fg="yellow", font=("Helvetica", 50))



        self.regen_frame = Frame(self.master, width=3*width_screen/6-space*2, height=height_screen/4-space)
        self.regen_frame.grid(column=0, row=2, columnspan=3)
        self.regen_frame.configure(bg="black")
        self.regen_frame.grid_propagate(0)

        self.turn_regen_frame = Frame(self.regen_frame, width=width_screen/8-space, height=height_screen/4-space, bg='white')
        self.turn_regen_frame.grid(column=0, row=0)
        self.turn_regen_frame.pack_propagate(0)

        self.turn_regen_label = Label(self.turn_regen_frame, text='TURN')
        self.turn_regen_label.configure(font=("Helvetica", 35), bg=self.turn_regen_frame["bg"])
        self.turn_regen_label.pack()

        self.num_turn_regen_label = Label(self.turn_regen_frame, text='8')
        self.num_turn_regen_label.configure(font=("Helvetica", 80), bg=self.turn_regen_frame["bg"])
        self.num_turn_regen_label.pack(expand=True)

        self.speed_regen_frame = Frame(self.regen_frame, width=3*width_screen/8-space, height=height_screen/4-space, bg=self.regen_frame["bg"])
        self.speed_regen_frame.grid(column=1, row=0)
        self.speed_regen_frame.configure(highlightbackground="white", highlightthickness=2)
        self.speed_regen_frame.pack_propagate(0)

        self.speed_regen_label = Label(self.speed_regen_frame, text='REGEN')
        self.speed_regen_label.configure(font=("Helvetica", 30), bg=self.speed_regen_frame["bg"], fg="white")
        self.speed_regen_label.pack(anchor='nw')

        self.num_speed_regen_label = Label(self.speed_regen_frame, text='85%')
        self.num_speed_regen_label.configure(font=("Helvetica", 50), bg=self.speed_regen_frame["bg"], fg="yellow")
        self.num_speed_regen_label.pack(expand=True)



        self.ICE_frame = Frame(self.master, width=3*width_screen/6-space*2, height=height_screen/4-space, bg='black')
        self.ICE_frame.grid(column=3, row=2, columnspan=3)
        self.ICE_frame.grid_propagate(0)
        # self.ICE_frame.rowconfigure(0, minsize=height_screen/4-30)

        self.turn_ICE_frame = Frame(self.ICE_frame, width=width_screen/8-space, height=height_screen/4-space, bg='white')
        self.turn_ICE_frame.grid(column=0, row=0)
        self.turn_ICE_frame.pack_propagate(0)

        self.turn_ICE_label = Label(self.turn_ICE_frame, text='TURN')
        self.turn_ICE_label.configure(font=("Helvetica", 35), bg=self.turn_ICE_frame["bg"])
        self.turn_ICE_label.pack()

        self.num_turn_ICE_label = Label(self.turn_ICE_frame, text='2')
        self.num_turn_ICE_label.configure(font=("Helvetica", 80), bg=self.turn_ICE_frame["bg"])
        self.num_turn_ICE_label.pack(expand=True)

        self.speed_ICE_frame = Frame(self.ICE_frame, width=3*width_screen/8-space, height=height_screen/4-space,bg=self.ICE_frame["bg"])
        self.speed_ICE_frame.grid(column=1, row=0)
        self.speed_ICE_frame.configure(highlightbackground="white", highlightthickness=2)
        self.speed_ICE_frame.pack_propagate(0)


        self.speed_ICE_label = Label(self.speed_ICE_frame, text='ICE')
        self.speed_ICE_label.configure(font=("Helvetica", 30), bg=self.speed_ICE_frame["bg"], fg="white")
        self.speed_ICE_label.pack(anchor='nw')

        self.num_speed_ICE_label = Label(self.speed_ICE_frame, text='10 Km/h')
        self.num_speed_ICE_label.configure(font=("Helvetica", 50), bg=self.speed_ICE_frame["bg"], fg="yellow")
        self.num_speed_ICE_label.pack(expand=True)



        self.breaks_mode_frame = Frame(self.master, width=width_screen/6, height=height_screen/4)
        self.breaks_mode_frame.grid(column=0, row=3)
        self.breaks_mode_frame.pack_propagate(0)
        self.breaks_mode_frame.configure(bg="black")

        self.breaks_label = Label(self.breaks_mode_frame, text="BRK")
        self.breaks_label.pack(expand=True)
        self.breaks_label.configure(bg="red", fg="white", font=("Helvetica", 30))

        self.mode_label = Label(self.breaks_mode_frame, text="HY")
        self.mode_label.pack(anchor="sw", side=BOTTOM)
        self.mode_label.configure(bg="red", fg="white", font=("Helvetica", 45))




        self.time_frame = Frame(self.master, width=3*width_screen/6, height=height_screen/4-space)
        self.time_frame.grid(column=1, row=3, columnspan=3)
        self.time_frame.configure(bg="black")
        self.time_frame.pack_propagate(0)

        self.time_label = Label(self.time_frame, text="TIME")
        self.time_label.pack(anchor='nw')
        self.time_label.configure(bg=self.time_frame["bg"], fg="white", font=("Helvetica", 26))

        self.num_time_label = Label(self.time_frame, text="00:02:11")
        self.num_time_label.pack(expand=True, anchor='nw')
        self.num_time_label.configure(bg=self.time_frame["bg"], fg="yellow", font=("Helvetica", 90))



        self.speed_frame = Frame(self.master, width=2*width_screen/6, height=height_screen/4-space)
        self.speed_frame.grid(column=4, row=3, columnspan=2)
        self.speed_frame.configure(bg="black")
        self.speed_frame.pack_propagate(0)

        self.speed_label = Label(self.speed_frame, text="SPEED")
        self.speed_label.pack(anchor='nw')
        self.speed_label.configure(bg=self.speed_frame["bg"], fg="white", font=("Helvetica", 26))

        self.num_speed_label = Label(self.speed_frame, text="24 km/h")
        self.num_speed_label.pack(expand=True, anchor='nw')
        self.num_speed_label.configure(bg=self.speed_frame["bg"], fg="yellow", font=("Helvetica", 70))
