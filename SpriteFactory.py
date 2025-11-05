from Sprite import Sprite
from random import randint
from typing import Dict, Tuple, List

types: Dict[str,Tuple[int,int]] = {"blaster":(50, 25),"speeder":(30,20),"destroyer":(50,75),"boss":(100,75)}
def make_sprites(count:int, world_width:int, world_height:int) -> List[Sprite]:
    sprites = []
    for i in range(count):
        type:str = ""
        choose_type:int = randint(0,20)
        if choose_type < 10:
            type = "blaster"
        elif choose_type < 15:
            type = "speeder"
        elif choose_type < 18:
            type = "destroyer"
        else:
            type = "boss"
        entry:Tuple[int,int] = types[type]
        x:int = randint(0,world_width-entry[0])
        y:int = randint(0,world_height-entry[1])
        sprites.append(Sprite(type,x,y,*entry))
    return sprites