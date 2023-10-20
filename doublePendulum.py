import pygame
from math import *

pygame.init()

swidth = 1000
sheight = 1000

canvas = pygame.Surface((swidth, sheight))
canvas.fill("black")
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Double Pendulum Simulation in Python')

# icon = pygame.image.load('pendulum2.png')
# pygame.display.set_icon(icon)

clock = pygame.time.Clock()
running = True
dt = 0

# CENTER
p = swidth/2
q = sheight/2

system1 = {
    'g' : 1, # gravitational constant

    'm1' : 50     , 'm2' : 75,        # masses
    'r1' : 100    , 'r2' : 250,       # rod lentghs
    'a1' : 3*pi/4 , 'a2' : 3*pi/4,    # pendulum angles (0 down, positive counter-clockwise)
    'v1' : 0      , 'v2' : 0,         # initial velocity of blocks
    'x1' : 0      , 'y1' : 0,         # initialize x,y of first mass in 0
    'x2' : 0      , 'y2' : 0,         # initialize x,y of second mass in 0
    'px2' : 0     ,'py2' : 0,         # previous cords (for path tracing)

    'color' : "goldenrod1",           # system's color
    'cvs' : pygame.Surface((swidth, sheight))   # system's individual canvas
}

system2 = {
    'g' : 1, # gravitational constant

    'm1' : 50     , 'm2' : 75,        # masses
    'r1' : 100    , 'r2' : 250,       # rod lentghs
    'a1' : 3*pi/4.00001 , 'a2' : 3*pi/4,    # pendulum angles (0 down, positive counter-clockwise)
    'v1' : 0      , 'v2' : 0,         # initial velocity of blocks
    'x1' : 0      , 'y1' : 0,         # initialize x,y of first mass in 0
    'x2' : 0      , 'y2' : 0,         # initialize x,y of second mass in 0
    'px2' : 0     ,'py2' : 0,         # previous cords (for path tracing)

    'color' : "mediumpurple3",        # system's color
    'cvs' : pygame.Surface((swidth, sheight))    # system's individual canvas
}

system3 = {
    'g' : 1, # gravitational constant

    'm1' : 50     , 'm2' : 75,        # masses
    'r1' : 100    , 'r2' : 250,       # rod lentghs
    'a1' : 3*pi/4 , 'a2' : 3*pi/3.9999,    # pendulum angles (0 down, positive counter-clockwise)
    'v1' : 0      , 'v2' : 0,              # initial velocity of blocks
    'x1' : 0      , 'y1' : 0,         # initialize x,y of first mass in 0
    'x2' : 0      , 'y2' : 0,         # initialize x,y of second mass in 0
    'px2' : 0     ,'py2' : 0,         # previous cords (for path tracing)

    'color' : "indianred2",           # system's color
    'cvs' : pygame.Surface((swidth, sheight))    # system's individual canvas
}

systems = [system1, system2, system3]

for system in systems :
    system['x1'] = p + system['r1']*sin(system['a1'])
    system['y1'] = q + system['r1']*cos(system['a1'])
    system['x2'] = system['x1'] + system['r2']*sin(system['a2'])
    system['y2'] = system['y1'] + system['r2']*cos(system['a2'])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

# DOUBLE PENDULUM SIMULATION
    for system in systems :
        system['cvs'].set_colorkey((0, 0, 0))
        system['cvs'].fill((0, 0, 0))
        
        system['px2'] = system['x2']
        system['py2'] = system['y2']

        system['x1'] = p + system['r1']*sin(system['a1'])
        system['y1'] = q + system['r1']*cos(system['a1'])
        system['x2'] = system['x1'] + system['r2']*sin(system['a2'])
        system['y2'] = system['y1'] + system['r2']*cos(system['a2'])

        # PENDULUM PATH TRACING
        pygame.draw.line(canvas, system['color'], pygame.Vector2(system['px2'], system['py2']), pygame.Vector2(system['x2'], system['y2']), 2)
        screen.blit(canvas, (0,0))

        # PENDULUM DRAWING
        intensity = 50 + int(dist((system['px2'],system['py2']), (system['x2'], system['y2'])))*4
        line_color = pygame.Color(intensity, intensity, intensity)
        pygame.draw.line(system['cvs'], line_color, pygame.Vector2(p,q), pygame.Vector2(system['x1'], system['y1']), 5)
        pygame.draw.line(system['cvs'], line_color, pygame.Vector2(system['x1'],system['y1']), pygame.Vector2(system['x2'], system['y2']), 5)
        pygame.draw.circle(system['cvs'], system['color'], pygame.Vector2(system['x1'], system['y1']), system['m1']/4)
        pygame.draw.circle(system['cvs'], system['color'], pygame.Vector2(system['x2'], system['y2']), system['m2']/4)

        num1 = -1 * system['g'] * (2 * system['m1'] + system['m2']) * sin(system['a1'])
        num2 = -1 * system['m2'] * system['g'] * sin(system['a1'] - 2*system['a2'])
        num3 = -2 * sin(system['a1'] - system['a2']) * system['m2']
        num4 = system['v2']*system['v2'] * system['r2'] + system['v1']*system['v1'] * system['r1'] * cos(system['a1'] - system['a2'])
        den  = system['r1'] * (2*system['m1'] + system['m2'] - system['m2'] * cos(2*system['a1'] - 2*system['a2']))
        acc1 = (num1 + num2 + num3*num4) / den

        num1 = 2 * sin(system['a1'] - system['a2'])
        num2 = system['v1']*system['v1'] * system['r1'] * (system['m1'] + system['m2'])
        num3 = system['g'] * (system['m1'] + system['m2']) * cos(system['a1'])
        num4 = system['v2']*system['v2'] * system['r2']  * system['m2'] * cos(system['a1'] - system['a2'])
        den  = system['r2'] * (2*system['m1'] + system['m2'] - system['m2'] * cos(2*system['a1'] - 2*system['a2']))
        acc2 = ( num1*(num2 + num3 + num4) ) / den

        system['v1'] += acc1;
        system['v2'] += acc2;
        system['a1'] += system['v1'];
        system['a2'] += system['v2'];
    
    for system in systems :
        screen.blit(system['cvs'], (0,0))

    pygame.draw.circle(screen, "tan4", pygame.Vector2(p, q), 5)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
