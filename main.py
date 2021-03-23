# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2021-03-23T14:27:30+01:00

from includes.dashboard import *
from tkinter import *

# def

def main():
    window = Tk()
    dash = Dashboard(window)
    dash.DispTRACK()
    window.attributes('-fullscreen',True) #affichage plein écran
    window.bind("<Escape>", lambda e: window.destroy()) #<ESC> pour pouvoir fermer le programe
    window.bind("<Left>", lambda e: dash.DispTRACK()) #<Left> pour afficher le menu track
    window.bind("<Right>", lambda e: dash.DispTEST()) #<Right> pour afficher le menu test
    window.mainloop()

if __name__ == '__main__':
    main()
