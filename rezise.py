import os
from PIL import Image

path = r'grass_block_side.png'
im = Image.open(path)   
im = im.resize((256, 256) , resample=Image.NEAREST)
im.save('big_grass_block.png')  