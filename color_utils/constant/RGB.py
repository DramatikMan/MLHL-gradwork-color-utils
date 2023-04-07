import numpy as np
from numpy.typing import NDArray

RGB: dict[str, tuple[int, int, int]] = {
    "#FF0000": (255, 0, 0),  # red
    "#FF8000": (255, 128, 0),
    "#FFFF00": (255, 255, 0),  # yellow
    "#80FF00": (128, 255, 0),
    "#00FF00": (0, 255, 0),  # green
    "#00FF80": (0, 255, 128),
    "#00FFFF": (0, 255, 255),  # cyan
    "#0080FF": (0, 128, 255),
    "#0000FF": (0, 0, 255),  # blue
    "#8000FF": (128, 0, 255),
    "#FF00FF": (255, 0, 255),  # magenta
    "#FF0080": (255, 0, 128),
}

RGBt: dict[str, NDArray[np.uint8]] = {}

for key, value in RGB.items():
    tensor = np.zeros((224, 224, 3), dtype=np.uint8)
    tensor[:, :] = value
    RGBt[key] = tensor
