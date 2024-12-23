from abc import abstractmethod
from custom.fc_object.fc_build_object import FCBuildObject
import fullcontrol as fc
import numpy as np
import math
from math import tau
from math import pi

import typing as tp


class VaseObject(FCBuildObject):
    pass


class VaseState:
    h: float
    theta: float
    ANGULAR_RESOLUTION: float


@abstractmethod
class RadiusFunctionInterface:
    def radius(h: float, theta: float, *args, **kwargs) -> tuple[float, float, float]:
        pass


@abstractmethod
class RadiusFunctionDecorator:
    def radius(
        f: function, h: float, theta: float, *args, **kwargs
    ) -> tuple[float, float, float]:
        pass


@abstractmethod
class BaseFunctionInterface:
    def base(h: float, theta: float, *args, **kwargs) -> list[fc.Point]:
        pass


@abstractmethod
class BaseFunctionDecorator:
    def base(f: function, h: float, theta: float, *args, **kwargs) -> list[fc.Point]:
        pass
