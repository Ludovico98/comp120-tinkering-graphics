from PIL import Image
import random

# variables
img = Image.open('tilemap.png')
tiles = []
tile_size = 32
height = 30
width = 60

# used loop to find position of individual tiles from sprite sheet
for i in range(38):
    current_tile = [0, 0, 32, 32]
    current_tile[0] = i * tile_size
    current_tile[2] = i * tile_size + tile_size
    tiles.append(current_tile)

# background image to place my tiles in
map = Image.new('RGB', (width * tile_size, height * tile_size))

# placement of tiles in the map
for x in range(width):
    for y in range(height):
        rand_tile_id = random.randrange(0, len(tiles))
        current_tile = [0, 0]
        current_tile[0] = x * tile_size
        current_tile[1] = y * tile_size
        map.paste(img.crop(tiles[rand_tile_id]), current_tile)
map.show()