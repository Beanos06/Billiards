import numpy as np
from numpy.typing import NDArray

def normalize(vect: NDArray):
    return vect / np.linalg.norm(vect)