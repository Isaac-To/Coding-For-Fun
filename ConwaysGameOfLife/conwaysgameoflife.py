import numpy as np
import numba as nb
from os import system as sys, get_terminal_size as t_size
import time

GRID_SIZE = 20
LIFES = 100000000
FPS = 24
DENSITY = 0.05

clear = lambda : sys('cls')

def init():
    import random
    img = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.int0)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.randint(0, GRID_SIZE)<GRID_SIZE*DENSITY:
                img[i, j] = 1
    return img

@nb.njit(nogil=True, parallel=True)
def life(img):
    new_img = img
    for i in nb.prange(GRID_SIZE):
        for j in nb.prange(GRID_SIZE):
            sur = 0
            conn = False
            #direct neighbors
            if i + 1 < GRID_SIZE:
                if img[i + 1, j] == 1:
                    sur += 1
                    conn = True
            else:
                sur += 1
            if i - 1 > 0:
                if img[i - 1, j] == 1:
                    sur += 1
                    conn = True
            else:
                sur += 1
            if j + 1 < GRID_SIZE:
                if img[i, j + 1] == 1:
                    sur += 1
                    conn = True
            else:
                sur += 1
            if j - 1 > 0:
                if img[i, j - 1] == 1:
                    sur += 1
                    conn = True
            else:
                sur += 1
            #corners
            if i + 1 < GRID_SIZE and j + 1 < GRID_SIZE:
                if img[i + 1, j + 1] == 1:
                    sur += 1
            else:
                sur += 1
            if i + 1 < GRID_SIZE and j - 1 > 0:
                if img[i + 1, j - 1] == 1:
                    sur += 1
            else:
                sur += 1
            if i - 1 > 0 and j + 1 < GRID_SIZE:
                if img[i - 1, j + 1] == 1:
                    sur += 1
            else:
                sur += 1
            if i - 1 > 0 and j - 1 > 0:
                if img[i - 1, j - 1] == 1:
                    sur += 1
            else:
                sur += 1
            #flip flopper
            if conn == True:
                if sur == 1:
                    new_img[i, j] = 0
                elif sur == 2:
                    new_img[i, j] = 1
                if sur >= 3:
                    new_img[i, j] = 0
            else:
                new_img[i, j] = 0
    return new_img

def render_image(img):
    grid = ""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if img[i, j] == 1:
                grid += "# "
            else:
                grid += "  "
        grid += "\n"
    clear()
    print(grid)

if __name__ == "__main__":
    img = init()
    for i in range(LIFES):
        start = time.time()
        img = life(img)
        extime = time.time() - start
        sleep_time = (1/FPS) - extime
        if sleep_time > 0:
            time.sleep(sleep_time)
        render_image(img)
        if 1 in img:
            pass
        else:
            import sys
            sys.exit()
