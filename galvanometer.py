# @Author: laurent
# @Date:   2020-11-03T18:25:22+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-11-03T21:04:35+01:00

from tkinter import *
from PIL import *
import os
from math import *
import time
import random

class Galva(Canvas):
    def __init__(self, window, size, value=0, range=0):
        #Dessin du Galva
        canvas = Canvas(window, width=size, height=size)
        window.update()
        canvas.create_oval(4,4,size,size,width=3)
        canvas.grid(column=0, row=3)
