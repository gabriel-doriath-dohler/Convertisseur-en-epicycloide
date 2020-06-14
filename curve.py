import numpy as np
from PIL import Image


def curve(arr, N=100_000, diag=True):
    '''
    return un chemin passant par tout les pixels noirs si possible.
    '''
    ymax, xmax = arr.shape
    xmax -= 1
    ymax -= 1

    for y, line in enumerate(arr):
        for x, val in enumerate(line):
            if not val:
                X = x
                Y = y
                break

    y, x = Y, X
    arr[y][x] = 1
    n = 0
    coords = [(x, y)]

    while (X != x or Y != y and n <= N) or not n:
        n += 1
        if x < xmax and not arr[y][x+1]:
            x += 1
        elif x > 0 and not arr[y][x-1]:
            x -= 1
        elif y < ymax and not arr[y+1][x]:
            y += 1
        elif y > 0 and not arr[y-1][x]:
            y -= 1
        elif y < ymax and x < xmax and not arr[y+1][x+1] and diag:
            x += 1
            y += 1
        elif y < ymax and x > 0 and not arr[y+1][x-1] and diag:
            x -= 1
            y += 1
        elif y > 0 and x < xmax and not arr[y-1][x+1] and diag:
            x += 1
            y -= 1
        elif y > 0 and x > 0 and not arr[y-1][x-1] and diag:
            x -= 1
            y -= 1
        else:
            break
        coords.append((x, y))
        arr[y][x] = 1

    if n > N:
        print('infinite loop?')

    return coords

