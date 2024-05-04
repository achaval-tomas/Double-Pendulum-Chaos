import pygame
from setup import *
from systems import *

pygame.init()

clock = pygame.time.Clock()
running = True
start = False
dt = 0

def keyActions():
    global sound_on
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        return True
    
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            start = keyActions()      # handle key inputs
            while not pygame.KEYUP:
                continue
    
    screen.fill("black")

    if start is False:
        continue

    # calculate next step on each system
    for s in systems:
        s.updatesystem(canvas, screen)
    
    # once all systems are updated, we display them
    for s in systems:
        s.show(screen)

    pygame.draw.circle(screen, "tan4", pygame.Vector2(p, q), 5)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
