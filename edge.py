from PIL import Image
import numpy as np


def edge(path):
    '''
    Cherche le bord de l'image dans path.
    Stocke le bord dans edge.png.

    return la matrice du bord.
    '''
    img = Image.open(path)

    arr = np.array(np.asarray(img))
    arr = np.flip(arr, 0)  # Correct the y inversion.

    arr2 = np.ones(arr.shape)

    Y, X = arr.shape
    for y, line in enumerate(arr):
        for x, val in enumerate(line):
            if val == 0 and 0 < x < X - 1 and 0 < y < Y - 1:
                if sum([arr[y][x+1], arr[y][x-1], arr[y+1][x], arr[y-1][x]]) > 0:
                    arr2[y][x] = 0

    # Create and save as an image.
    im = Image.fromarray(np.flip(arr2, 0) * 255).convert('L')
    # im.show()
    im.save('edge.png')
    return arr2

