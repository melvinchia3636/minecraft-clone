from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np
import noise
from matplotlib import pyplot as plt

print(help(noise.pnoise2))

shape = (32, 32)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = round(noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=42)*100)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=None):
        super().__init__(
			parent= scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture if texture else grass_block,
			color = color.white,
			highlight_color = color.lime,
			scale = 0.5
		)
        
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

app = Ursina()

grass_block = load_texture('assets/grass_block.png')
dirt_block = load_texture('assets/dirt_block.png')

def get_neighbour(i, j):
		neighbour = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
		neighbour = [i for i in neighbour if 0<=i[0]<32 and 0<=i[1]<32]
		return neighbour

for z in range(32):
	for x in range(32):
		diff = int(world[x][z])-int(min([world[i][j] for i,j in get_neighbour(x, z)]))
		if diff > 1:
			for y in range(int(world[x][z])-diff+1, int(world[x][z])):
				voxel = Voxel(position=(x, y, z), texture=dirt_block)
			voxel = Voxel(position=(x, int(world[x][z]), z))
		else: voxel = Voxel(position=(x, int(world[x][z]), z))

player = FirstPersonController()

app.run()