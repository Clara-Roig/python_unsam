#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:27:59 2021

@author: clara
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()



def experimento_randomwalk(times):
    N = 100000
    plt.subplot(2, 1, 1)
    for i in range(times):
        plt.plot(randomwalk(N))
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.title("12 trayectorias random")
    plt.legend()
    plt.subplot(2, 2, 3)
    plt.subplot(2, 2, 4)
    plt.show()
    
    
if __name__ == "__main__":  
    experimento_randomwalk(12)