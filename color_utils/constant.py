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

RYB: dict[str, tuple[int, int, int]] = {
    "#FE2712": (254, 39, 18),  # red
    "#FC600A": (252, 96, 10),  # red-orange
    "#FB9902": (251, 153, 2),  # orange
    "#FCCC1A": (252, 204, 26),  # yellow-orange
    "#FEFE33": (254, 254, 51),  # yellow
    "#B2D732": (178, 215, 50),  # yellow-green
    "#66B032": (102, 176, 50),  # green
    "#347C98": (52, 124, 152),  # blue-green
    "#0247FE": (2, 71, 254),  # blue
    "#4424D6": (68, 36, 214),  # blue-purple
    "#8601AF": (134, 1, 175),  # purple
    "#C21460": (194, 20, 96),  # red-purple
}

RGBt: dict[str, NDArray[np.uint8]] = {}
RYBt: dict[str, NDArray[np.uint8]] = {}

for kRGB, vRGB in RGB.items():
    tensor = np.zeros((224, 224, 3), dtype=np.uint8)
    tensor[:, :] = vRGB
    RGBt[kRGB] = tensor

for kRYB, vRYB in RYB.items():
    tensor = np.zeros((224, 224, 3), dtype=np.uint8)
    tensor[:, :] = vRYB
    RYBt[kRYB] = tensor