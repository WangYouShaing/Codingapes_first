# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:38:38 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
"""
def plantTree(x,y,z):
    print(x)
    print(y)
    print(z)
    
plantTree("save the earth", "I am y", 0)
"""
x,y,z = mc.player.getPos()
def plantTree (x,y,z):
    mc.setBlocks(x-1,y+3,z+1,y+5,z+1,leaves)
    
for i in range(10):
    plantTree (x + i, y, z)