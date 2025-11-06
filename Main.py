from Sprite import *
from Screen import *

world_width = 10000
world_height = 10000
screen = Screen(4000,4000, 800, 600)

# 1) read the sprites.txt file into a list
# 2) create a list called sprites
# 3) convert each line of the sprites.txt file into a Sprite object
#    and add it to the sprites list
# 4) make a list called rendered
# 5) add each sprite that is inside the screen's boundaries to rendered
# 6) call the screen.render() method on each rendered sprite at the x
#    and y coordinate they'd be on the screen