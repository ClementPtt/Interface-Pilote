# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2021-04-11T17:54:53+02:00

from includes.dashboard import *
from includes.test_menu import *
from includes.track_menu import *
from tkinter import *


def main():
    window = Tk()
    dash = Track(window)
    # dash.DispTRACK()
    window.attributes('-fullscreen',True) #affichage plein écran
    window.bind("<Escape>", lambda e: window.destroy()) #<ESC> pour pouvoir fermer le programe
    window.bind("<Left>", lambda dash: Track(window)) #<Left> pour afficher le menu track
    window.bind("<Right>", lambda dash: Test(window)) #<Right> pour afficher le menu test
    i = 0
    while(i<20):
        dash.speed = i
        i = i+1
    window.mainloop()

if __name__ == '__main__':
    main()
