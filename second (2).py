from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

time.sleep(1)

x,y,z = mc.player.getTilePos()

blockType = int(input("Block id:"))

mc.setBlock(x,y,z, blockType)

try:
    BlockType = int(input(Block id))
    mc.setBlock(x,y,z, blocktype)
except:
    print("Invalid")