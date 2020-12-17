import sys
import numpy as np
import scipy.ndimage

dim = 4

cube = np.array([[p == '#' for p in line.strip()] for line in sys.stdin])
cube = np.expand_dims(cube, axis=tuple(range(dim - 2)))

K = np.ones((3,) * dim)
K[(1,) * dim] = 0

for _ in range(6):
    cube = np.pad(cube, 1).astype(int)
    active_neighbours = scipy.ndimage.convolve(cube, K, mode='constant', cval=0)
    cube = (cube==1) & ((active_neighbours==2) | (active_neighbours==3)) | (cube==0) & (active_neighbours==3)

print(np.sum(cube))