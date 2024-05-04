from math import pi
from pygame import Surface, display

swidth = 1000
sheight = 1000

# CENTER
p = swidth/2
q = sheight/2

canvas = Surface((swidth, sheight))
canvas.fill("black")
screen = display.set_mode((swidth, sheight))
display.set_caption('Double Pendulum Simulation in Python')

# icon = pygame.image.load('pendulum2.png')
# pygame.display.set_icon(icon)