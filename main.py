import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

from linear import normalize
from models import Ball, Wall

NUM_BALLS = 10 # Number of balls
size = 8 # Size of balls

# Matplotlib setup
fig, ax = plt.subplots()
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
ax.set_axis_off()
ax.set_title("Billiards Challenge")

def generate_start_pos():
    """Generate starting position of ball"""
    
    return (np.random.rand(1,2) * 10)[0]

def generate_start_vect(speed: float):
    """Generate starting vector of a ball"""
    
    start_vect = normalize((np.random.rand(1,2) * 10)[0]) * speed
    return start_vect

# Generate balls
balls = [Ball(pos=generate_start_pos(), vect=generate_start_vect(speed=4), ax=ax, size=size) for _ in range(NUM_BALLS)]

# Generate walls
top_wall = Wall(
    pos=np.array([0,10]),
    vect=np.array([10, 0]),
    ax=ax
)
bottom_wall = Wall(
    pos=np.array([0, 0]),
    vect=np.array([10,0]),
    ax=ax
)
left_wall = Wall(
    pos=np.array([0, 0]),
    vect=np.array([0, 10]),
    ax=ax
)
right_wall = Wall(
    pos=np.array([10, 0]),
    vect=np.array([0, 10]),
    ax=ax
)

def update(frame):
    for b in balls:
        b.pos += b.vect
        b.update_pos()
        
        if b.pos[1] >= 10:
            b.bounce(top_wall.normal)
        if b.pos[1] <= 0:
            b.bounce(bottom_wall.normal)
        if b.pos[0] >= 10:
            b.bounce(right_wall.normal)
        if b.pos[0] <= 0:
            b.bounce(left_wall.normal)


ani = animation.FuncAnimation(fig=fig, func=update, frames=60, interval=10)
plt.show()