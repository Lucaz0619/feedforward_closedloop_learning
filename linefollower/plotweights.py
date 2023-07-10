#!/usr/bin/python3

import sys
import threading
import math
import time

from matplotlib import pyplot as plt
import numpy as np

plt.ion()
plt.show()
ln = [False,False,False,False,False,False]


def plotOneMatrix(i):
    global ln
    if ln[i]:
        ln[i].remove()
    plt.title(str(i))
    w1 = np.loadtxt("layer"+str(i)+".dat");
    ln[i] = plt.imshow(w1,cmap='gray',interpolation='none')


while True:
    plt.subplot(231)
    plotOneMatrix(0)   
    plt.subplot(232)
    plotOneMatrix(1)   
    plt.subplot(233)
    plotOneMatrix(2)   
    plt.subplot(234)
    plotOneMatrix(3)
    plt.subplot(235)
    plotOneMatrix(4)
    # plt.subplot(236)
    # plotOneMatrix(5)
    # plt.subplot(227)
    # plotOneMatrix(6) 
    plt.draw()   
    plt.pause(10)     

