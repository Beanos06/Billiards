from numpy.typing import NDArray
import numpy as np
from matplotlib.axes import Axes

K = 20 #constant to shrink the vector of ball for correct speed

class Ball():
    def __init__(self, pos: list[float], vect: list[float], ax: Axes, size: int):
        self.pos = np.array(pos)
        self.vect = np.array(vect) / K
        self.ax = ax
        self.size = size
        
        self.show() # Show on screen
        
    def show(self):
        """Render the ball on screen"""
        
        self.ball_on_screen = self.ax.plot(self.pos[0], self.pos[1], 'o', markersize=self.size)[0]
        
    def bounce(self, normal_vect: NDArray):
        """Reflects ball's vector about a given normal vector (of the wall)"""
        
        proj_self_on_n = (np.dot(normal_vect, self.vect) / np.linalg.norm(normal_vect) ** 2) * normal_vect
        orth_self_on_n = self.vect - proj_self_on_n
        self.vect = orth_self_on_n - proj_self_on_n
        
    def update_pos(self):
        """Update ball's position on screen"""
        self.ball_on_screen.set_xdata([self.pos[0]])
        self.ball_on_screen.set_ydata([self.pos[1]])

class Wall():
    def __init__(self, pos: NDArray, vect: NDArray, ax: Axes):
        self.pos = pos
        self.vect = vect
        self.ax = ax
        self.normal = np.array([vect[1], -vect[0]])
        
        self.show() # Render wall on screen
    
    def show(self):
        """Render wall on screen"""
        self.ax.plot(
            [self.pos[0], self.pos[0] + self.vect[0]],
            [self.pos[1], self.pos[1] + self.vect[1]],
            color='black'
        )