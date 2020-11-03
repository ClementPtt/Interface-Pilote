# @Author: laurent
# @Date:   2020-11-03T18:25:22+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-11-03T18:56:16+01:00

from tkinter import *
from PIL import *
import os
from math import *
import time
import random

class Galva(Canvas):
    def __init__(self):
        global valeur, aiguille, txt

        Canvas.__init__(self)
        #Dessin du Galva
        self.create_rectangle(0,0,200,200,fill="white",outline="red")
