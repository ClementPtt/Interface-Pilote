# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2020-12-26T18:44:01+01:00

from includes.dashboard import *
from includes.test import *
from tkinter import *

def main():
    window = Tk()
    dash = Dashboard(window) #Pour l'instant, choisir Dashboard ou Test pour lancer un des deux menus
    window.mainloop()

if __name__ == '__main__':
    main()
