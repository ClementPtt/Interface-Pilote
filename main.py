# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2021-04-11T19:43:49+02:00

from includes.dashboard import *
from includes.test_menu import *
from includes.track_menu import *
from tkinter import *


def main():
    window = Tk()
    dash = Track(window)
    # window.bind("<Left>", lambda dash: Track(window)) #<Left> pour afficher le menu track
    # window.bind("<Right>", lambda dash: Test(window)) #<Right> pour afficher le menu test
    dash.waitForLeft(dash, Test)


if __name__ == '__main__':
    main()
