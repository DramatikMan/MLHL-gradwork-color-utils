from typing import Protocol
from . import constant as const

import numpy as np
from numpy.typing import NDArray


class Base(Protocol):
    colors: dict[str, NDArray[np.uint8]]

    @classmethod
    def get_dominant_color(cls, image: NDArray[np.uint8]) -> str:
        dominant_color, min_distance = "", float("+inf")

        for color_hex, color_array in cls.colors.items():
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
    colors = const.RGBt


class RYB(Base):
    colors = const.RYBt
