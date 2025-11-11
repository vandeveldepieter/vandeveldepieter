import pygame as pg
import numpy as np

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Learn Pygame")
clock = pg.time.Clock()
# Per-second example: timer event and accumulator alternative
SECOND_EVENT = pg.USEREVENT + 1
pg.time.set_timer(SECOND_EVENT, 1000)  # fire every 1000 ms (1 second)
per_second_count = 0

# Alternative approach using an accumulator (dt) so you can run logic once per second
accumulator = 0.0

running = True
bpos = [350,250,100,100]
bcol = [255, 0, 0]  # Red color
while running:
    while running:
        # Compute time delta (seconds) at the top of the loop
        dt = clock.tick(60) / 1000.0  # cap to ~60 FPS

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == SECOND_EVENT:
                # This branch is called roughly once per second by SDL/pygame
                per_second_count += 0.5
                print(f"Timer event fired: {per_second_count} s")

        # --- Input handling (keyboard) ---
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            # immediate color change when space is pressed
            bcol = [int(x) for x in np.random.randint(0, 256, size=3)]
        if keys[pg.K_LEFT] and (bpos[0] > 0):
            bpos[0] -= 5
        if keys[pg.K_RIGHT] and (bpos[0] < (800 - bpos[2])):
            bpos[0] += 5
        if keys[pg.K_UP] and (bpos[1] > 0):
            bpos[1] -= 5
        if keys[pg.K_DOWN] and (bpos[1] < (600 - bpos[3])):
            bpos[1] += 5
        if (keys[pg.K_PLUS] or keys[pg.K_KP_PLUS]) and (bpos[2] < 600) and (bpos[3] < 600):
            bpos[0] -= 2
            bpos[1] -= 2
            bpos[2] += 4
            bpos[3] += 4
        if (keys[pg.K_MINUS] or keys[pg.K_KP_MINUS]) and (bpos[2] > 20) and (bpos[3] > 20):
            bpos[0] += 2
            bpos[1] += 2
            bpos[2] -= 4
            bpos[3] -= 4

        # --- Per-second accumulator alternative ---
        accumulator += dt
        if accumulator >= 1.0:
            accumulator -= 1.0
            # This block runs once per second (approx) using dt accumulation
            print("Accumulator tick (1s)")
            # small automatic downward movement each second
            if bpos[1] < (600 - bpos[3]):
                bpos[1] += 5

        # --- Drawing ---
        screen.fill((0, 0, 0))  # clear the screen each frame
        pg.draw.rect(screen, bcol, bpos)  # draw the box
        # draw white fence 100px from the edges
        pg.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400), 5)

        # detect collision with fence
        if bpos[0] < 100:
            bpos[0] = 100
        if bpos[0] + bpos[2] > 700:
            bpos[0] = 700 - bpos[2]
        if bpos[1] < 100:
            bpos[1] = 100
        if bpos[1] + bpos[3] > 500:
            bpos[1] = 500 - bpos[3]

        pg.display.flip()  # Update the display
    pg.display.flip()  # Update the display

pg.quit()
# A simple Pygame window that stays open until closed by the user.
