from typing import Protocol

import numpy as np
from numpy.typing import NDArray

from . import constant as const


class Base(Protocol):
    _colors: dict[str, NDArray[np.uint8]]

    @classmethod
    def get_dominant_color(cls, image: NDArray[np.uint8]) -> str:
        dominant_color, min_distance = "", float("+inf")

        for color_hex, color_array in cls._colors.items():
            score = np.mean(
                np.sqrt(
                    np.sum(
                        np.square(np.subtract(image, color_array)),
                        axis=2,
                    )
                )
            )

            if score < min_distance:
                min_distance = score
                dominant_color = color_hex

        return dominant_color


class RGB(Base):
    _colors = const.RGB


class RYB(Base):
    _colors = const.RYB
