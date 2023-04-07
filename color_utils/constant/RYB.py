import numpy as np
from numpy.typing import NDArray

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

RYBt: dict[str, NDArray[np.uint8]] = {}


for key, value in RYB.items():
    tensor = np.zeros((224, 224, 3), dtype=np.uint8)
    tensor[:, :] = value
    RYBt[key] = tensor
