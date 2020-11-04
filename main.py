# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2020-11-04T17:46:39+01:00

from includes.dashboard import *
from tkinter import *

def main():
    window = Tk()
    dash = Dashboard(window)
    dash.draw_gauge()
    window.mainloop()

if __name__ == '__main__':
    main()
