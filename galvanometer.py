# @Author: laurent
# @Date:   2020-11-03T18:25:22+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-11-03T19:57:47+01:00

from tkinter import *
from PIL import *
import os
from math import *
import time
import random

class Galva(Canvas):
    def __init__(self, window):
        #Dessin du Galva
        self.canvas = Canvas(window, width=400, height=400)
        self.canvas.create_rectangle(0,0,200,200,fill="white",outline="red")
        self.canvas.grid(column=0, row=3)
