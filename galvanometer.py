# @Author: laurent
# @Date:   2020-11-03T18:25:22+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-11-03T19:01:39+01:00

from tkinter import *
from PIL import *
import os
from math import *
import time
import random

class Galva(Canvas):
    def __init__(self, frame):
        global valeur, aiguille, txt

        canv = Canvas(frame, bg="white", height=200, width=200)
        #Dessin du Galva
        canv.create_rectangle(0,0,200,200,fill="white",outline="red")
        canv.pack()
