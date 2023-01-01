# Author: Larz60+ Nov 2019

from screeninfo import get_monitors


class GetGeometry:
    def __init__(self):
        self.geometry = []

    def get_tkinter_geometry(self, percent_of_screen, xpad=None, ypad=None):
        '''
        Given percent of monitor size in floating point eg: 10 % = 10.0, calculates
        tkinter geometry for each monitor attached to computer
        requires screeninfo "pip install screeninfo"

        returns: list holding tkinter geometry strings padded with xpad and ypad
        or centered if xpad is None.
        None if bad pct passed
        '''

        if not isinstance(percent_of_screen, float):
            print("requires float percent eg: 10.0 for 10%")
            return

#import GetTkGeometry
from GetGeometry import *

gg = GetGeometry()
# padding specified 10 % of screen dimensions
gg.get_tkinter_geometry(10.0, 10, 10)
geometry = gg.geometry
print(f"\ngeometry - 10% of monitor size 10 pixel x and y padding:\n{geometry}")

# padding not specified 60 % of screen dimensions
gg.get_tkinter_geometry(60.0)
geometry = gg.geometry
print(f"\ngeometry - 60% of monitor size centered (no pading specified):\n{geometry}")