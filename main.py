# @Date:   2020-11-04T16:21:54+01:00
# @Last modified time: 2020-11-04T17:38:55+01:00

from includes.dashboard import *
from tkinter import *

def main():
    window = Tk()
    dash = Dashboard(window)
    window.mainloop()

if __name__ == '__main__':
    main()
