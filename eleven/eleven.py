import sys
import numpy as np
from scipy import ndimage
import cv2
import time

with open(sys.argv[1],'r') as infile:
    lines = infile.readlines()

array = np.zeros([10,10],dtype=int)

for i,line in enumerate(lines):
    for j,char in enumerate(line.rstrip()):
        array[i,j] = int(char)

kernel = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]], dtype=int)

flash_count = 0
flash_step = None

for step in range(9999):
    # First each octopus gains energy
    array += 1

    # Then each octopus with an energy greater than 9 flashes:
    while((array>9).sum()>0):
        already_flashed = (array==0)
        flashers = (array>9).astype(int)
        array += ndimage.convolve(flashers,kernel,
                                  mode='constant',
                                  cval=0)
        array[np.where(flashers)] = 0
        array[np.where(already_flashed)] = 0
    
    cv2.namedWindow("Jellyfish", cv2.WINDOW_AUTOSIZE)
    initialtime = time.time()

    cv2.startWindowThread()

    img = (255.*array.astype(float)/9.).astype(np.uint8)
    img = cv2.resize(img, (500,500), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Jellyfish', np.tile(img[...,np.newaxis],[1,1,3]))
    time.sleep(0.1)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        break

    if np.allclose(array,0):
        break

    if step < 100:
        flash_count += (array==0).sum()

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)

print("Total flashes at 100 steps: {}".format(flash_count))
print('All flashed at step {}'.format(step+1))
