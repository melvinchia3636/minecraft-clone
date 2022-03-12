import noise

x_range = (32, 64)
z_range = (32, 64)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = []
for i in range(*x_range):
    world.append([])
    for j in range(*z_range):
        world[-1].append(round(noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=42)*100))
        
print(world)