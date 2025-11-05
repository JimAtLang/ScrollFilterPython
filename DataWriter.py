from typing import List
from Sprite import Sprite


def write_sprites(sprites:List[Sprite]):
    with open("sprites.txt","w") as f:
        for sprite in sprites:
            line: str = ",".join([
                sprite.type,
                str(sprite.x),
                str(sprite.y),
                str(sprite.width),
                str(sprite.height)
            ])
            f.write(line + "\n")