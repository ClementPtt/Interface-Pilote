# @Author: laurent
# @Date:   2020-11-03T18:25:22+01:00
# @Last modified by:   laurent
# @Last modified time: 2020-11-04T09:42:49+01:00

from tkinter import *
from PIL import *
import os
from math import *
import time
import random

class Galva(Canvas):
    def __init__(self, window, size, value=0, range=0, column_=0, row_=3):
        #Dessin du Galva
        canvas = Canvas(window, width=size, height=size)
        window.update()
        canvas.create_oval(4,4,size,size,width=3)
        for i in range(100):
            canvas.create_rectangle(12,60,188,118,fill="black")
        canvas.grid(column=column_, row=row_)
