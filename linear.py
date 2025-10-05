import numpy as np
from numpy.typing import NDArray

def normalize(vect: NDArray):
    """Turns a vector into a unit vector"""
    
    return vect / np.linalg.norm(vect)