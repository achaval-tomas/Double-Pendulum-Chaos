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
start = False
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

for s in systems :
    s['x1'] = p + s['r1']*sin(s['a1'])
    s['y1'] = q + s['r1']*cos(s['a1'])
    s['x2'] = s['x1'] + s['r2']*sin(s['a2'])
    s['y2'] = s['y1'] + s['r2']*cos(s['a2'])

def keyActions():
    global sound_on
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        return 1
    
    return 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            start = keyActions()      # handle key inputs to select sorting algorithm
            while not pygame.KEYUP:
                continue
    
    screen.fill("black")

    if not start:
        continue

# DOUBLE PENDULUM SIMULATION
    for s in systems :
        s['cvs'].set_colorkey((0, 0, 0))
        s['cvs'].fill((0, 0, 0))
        
        s['px2'] = s['x2']
        s['py2'] = s['y2']

        s['x1'] = p + s['r1']*sin(s['a1'])
        s['y1'] = q + s['r1']*cos(s['a1'])
        s['x2'] = s['x1'] + s['r2']*sin(s['a2'])
        s['y2'] = s['y1'] + s['r2']*cos(s['a2'])

        # PENDULUM PATH TRACING
        pygame.draw.line(canvas, s['color'], pygame.Vector2(s['px2'], s['py2']), pygame.Vector2(s['x2'], s['y2']), 2)
        screen.blit(canvas, (0,0))

        # PENDULUM DRAWING
        intensity = 50 + int(dist((s['px2'],s['py2']), (s['x2'], s['y2'])))*4
        line_color = pygame.Color(intensity, intensity, intensity)
        pygame.draw.line(s['cvs'], line_color, pygame.Vector2(p,q), pygame.Vector2(s['x1'], s['y1']), 5)
        pygame.draw.line(s['cvs'], line_color, pygame.Vector2(s['x1'],s['y1']), pygame.Vector2(s['x2'], s['y2']), 5)
        pygame.draw.circle(s['cvs'], s['color'], pygame.Vector2(s['x1'], s['y1']), s['m1']/4)
        pygame.draw.circle(s['cvs'], s['color'], pygame.Vector2(s['x2'], s['y2']), s['m2']/4)

        num1 = -1 * s['g'] * (2 * s['m1'] + s['m2']) * sin(s['a1'])
        num2 = -1 * s['m2'] * s['g'] * sin(s['a1'] - 2*s['a2'])
        num3 = -2 * sin(s['a1'] - s['a2']) * s['m2']
        num4 = s['v2']*s['v2'] * s['r2'] + s['v1']*s['v1'] * s['r1'] * cos(s['a1'] - s['a2'])
        den  = s['r1'] * (2*s['m1'] + s['m2'] - s['m2'] * cos(2*s['a1'] - 2*s['a2']))
        acc1 = (num1 + num2 + num3*num4) / den

        num1 = 2 * sin(s['a1'] - s['a2'])
        num2 = s['v1']*s['v1'] * s['r1'] * (s['m1'] + s['m2'])
        num3 = s['g'] * (s['m1'] + s['m2']) * cos(s['a1'])
        num4 = s['v2']*s['v2'] * s['r2']  * s['m2'] * cos(s['a1'] - s['a2'])
        den  = s['r2'] * (2*s['m1'] + s['m2'] - s['m2'] * cos(2*s['a1'] - 2*s['a2']))
        acc2 = ( num1*(num2 + num3 + num4) ) / den

        s['v1'] += acc1;
        s['v2'] += acc2;
        s['a1'] += s['v1'];
        s['a2'] += s['v2'];
    
    for s in systems :
        screen.blit(s['cvs'], (0,0))

    pygame.draw.circle(screen, "tan4", pygame.Vector2(p, q), 5)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
