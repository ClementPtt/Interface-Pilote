# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2021-03-22T12:07:20+01:00

from includes.dashboard import *
from includes.test import *
from tkinter import *

def main():
    window = Tk()
    dash = Test(window) #Pour l'instant, choisir Dashboard ou Test pour lancer un des deux menus
    window.attributes('-fullscreen',True) #affichage plein écran
    window.bind("<Escape>", lambda e: window.destroy()) #<ESC> pour pouvoir fermer le programe
    window.mainloop()

if __name__ == '__main__':
    main()
