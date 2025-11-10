import pygame as pg
import numpy as np

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Learn Pygame")
clock = pg.time.Clock()
running = True
bpos = [350,250,100,100]
bcol = [255, 0, 0]  # Red color
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #drawing code goes here
    pg.draw.rect(screen, bcol, bpos)  # Draw a red box
    # pg.draw.circle(screen, (0, 255, 0), (400, 300), 50)  # Draw a green circle

    #keyboard input handling
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        print("Space key is pressed")
        bcol[0] = np.random.randint(0,256)
        bcol[1] = np.random.randint(0,256)
        bcol[2] = np.random.randint(0,256)
    if keys[pg.K_LEFT] & (bpos[0]>0):
        print("Left arrow key is pressed")
        bpos[0] -= 50
        screen.fill((0, 0, 0))  # Fill the screen with black
    if keys[pg.K_RIGHT] & (bpos[0]<(800 - bpos[2])):
        print("Right arrow key is pressed")        
        bpos[0] += 50
        screen.fill((0, 0, 0))  # Fill the screen with black
    if keys[pg.K_UP] & (bpos[1]>0):
        print("Up arrow key is pressed")        
        bpos[1] -= 50
        screen.fill((0, 0, 0))  # Fill the screen with black
    if keys[pg.K_DOWN] & (bpos[1]<(600 - bpos[3])):
        print("Down arrow key is pressed")        
        bpos[1] += 50
        screen.fill((0, 0, 0))  # Fill the screen with black
    if keys[pg.K_PLUS] | keys[pg.K_KP_PLUS] & (bpos[2]<600) & (bpos[3]<600):
        print("Plus key is pressed")        
        bpos[0] -= 2
        bpos[1] -= 2
        bpos[2] += 4
        bpos[3] += 4
        screen.fill((0, 0, 0))  # Fill the screen with black
    if keys[pg.K_MINUS] | keys[pg.K_KP_MINUS] & (bpos[2]>20) & (bpos[3]>20):
        print("Minus key is pressed")        
        bpos[0] += 2
        bpos[1] += 2        
        bpos[2] -= 4
        bpos[3] -= 4
        screen.fill((0, 0, 0))  # Fill the screen with black+-

    #draw white fence 100px from the edges
    pg.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400), 5)

    #detect collision with fence
    if bpos[0] < 100:
        bpos[0] = 100
    if bpos[0] + bpos[2] > 700:
        bpos[0] = 700 - bpos[2]
    if bpos[1] < 100:
        bpos[1] = 100
    if bpos[1] + bpos[3] > 500:
        bpos[1] = 500 - bpos[3]
    
    #if bpos[1]<(600 - bpos[3]):       
    #    bpos[1] += 1
    #    pg.draw.rect(screen, (0, 0, 0), (bpos[0], bpos[1], bpos[2], bpos[3]))  # paint black where the box was

    # reset the screen
    # screen.fill((0, 0, 0))  # Fill the screen with black
    pg.display.flip()  # Update the display
    dt = clock.tick(60) / 1000.0 # Limit to 60 frames per second

pg.quit()
# A simple Pygame window that stays open until closed by the user.
