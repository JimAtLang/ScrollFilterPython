from SpriteFactory import make_sprites
from DataWriter import write_sprites

sprites = make_sprites(1500, 8000, 10000)
write_sprites(sprites)