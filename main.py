import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

from models import Ball, Wall

fig, ax = plt.subplots()

size = 8

ball_1 = Ball(
    pos=[5.0,0.0], 
    vect=[1.0,3.0],
    ax=ax,
    size=size
)

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

ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
ax.set_axis_off()
ax.set_title("Billiards Challenge")

top_wall.show()
bottom_wall.show()
left_wall.show()
right_wall.show()

ball = ball_1.show()

def update(frame):
    ball_1.pos += ball_1.vect
    ball.set_xdata([ball_1.pos[0]])
    ball.set_ydata([ball_1.pos[1]])
    # print(ball_1.pos)
    
    if ball_1.pos[1] >= 10:
        ball_1.bounce(np.array([0, 1]))
    if ball_1.pos[1] <= 0:
        ball_1.bounce(np.array([0, 1]))
    if ball_1.pos[0] >= 10:
        ball_1.bounce(np.array([1, 0]))
    if ball_1.pos[0] <= 0:
        ball_1.bounce(np.array([1, 0]))

ani = animation.FuncAnimation(fig=fig, func=update, frames=60, interval=10)
plt.show()