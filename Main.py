from Sprite import *
from Screen import *

world_width = 10000
world_height = 10000
screen = Screen(4000,4000, 800, 600)
sprites = []
with open ("sprites.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split(",")
        name = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        width = int(parts[3])
        height = int(parts[4])
        sprite = Sprite(name,x,y,width,height)
        sprites.append(sprite)
for sprite in sprites:
    screen.render(sprite, sprite.x, sprite.y)
# for sprite in sprites:
#     print(f"name: {sprite.name}, x: {sprite.x}, y: {sprite.y},width: {sprite.width}, height: {sprite.height}")
# 1) make a list called rendered
# 2) add each sprite that is inside the screen's boundaries to rendered
# 3) call the screen.render() method on each rendered sprite at the x
#    and y coordinate they'd be on the screen
# 4) CHALLENGE: find all the sprites that collide (overlap) and print
#    the number of collisions