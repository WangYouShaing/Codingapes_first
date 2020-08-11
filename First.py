# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:36:08 2020

@author: USER
"""

#zdbsdzblkrflizdclkfblifcslzdfjblf
"""
lskmv;onv;ozsdvnjrn;dzjnv
zsdvzdv
zdvzvzv
"""
#hdgcjhSGSDvjsgdcvajsevakjsckaj
"""
kjfnvlzkdjfnv
"""
"Minecraft"
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
print(mc.player.getTilePos())
mc.player.setTilePos(100,20,50)
time.sleep(5)

mc.player.setPos(150,150,120)
a=0
while a<10:
    mc.setBlock(x,y-1,z)
    mc.setBlock(x+1,y+1,z)
    mc.setBlock(x+1+1,y-1,z)
    mc.setBlock(x+1+1,y-1,z-1)
    mc.setBlock(x+1+1,y-1,z-1-1)
    mc.setBlock(x+1,z-1-1,y-1)
    mc.setBlock(x,y-1,z-1-1)
    mc.setBlock(x,y-1,z-1)
    y=y+1
    a=a+1