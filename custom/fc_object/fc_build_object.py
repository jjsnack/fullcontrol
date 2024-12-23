from abc import abstractmethod
import fullcontrol as fc
import numpy as np
import math
from math import tau
from math import pi

import typing as tp

print_settings = {
    "extrusion_width": 0.5,
    "extrusion_height": 0.2,
    "fan_percent": 60,
    "print_speed": 1000,
    "travel_speed": 8000,
    "area_model": "stadium",
    "e_units": "mm",
    "dia_feed": 1.75,
    "relative_e": True,
}


class PrinterSettings:
    printer: str
    extrusion_width: float
    extrusion_height: float
    fan_percent: float
    print_speed: float
    travel_speed: float
    area_model: str
    e_unit: str
    dia_feed: float
    relative_e: bool
    offset_x: float
    offset_y: float

    def __init__(self):
        pass


class FCBuildObject:
    def __init__(self):
        pass

    def printer_setup():
        pass

    @abstractmethod
    def build():
        pass

    def pol2xyz():
        pass

    def xyz2pol():
        pass
