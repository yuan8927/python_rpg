import pygame

tile_size = 32

map_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

tile_image = {}

#タイルファイルの読み込み・格納
def load_tiles():
    tile_image[0] = pygame.image.load("assets/tilesets/grass.png").convert_alpha()
    tile_image[1] = pygame.image.load("assets/tilesets/grassclump.png").convert_alpha()


"""
画像の読み込みが成功しているかの確認
def load_tiles():
    try:
        tile_image[0] = pygame.image.load("assets/tilesets/grass.png").convert()
        print("✅ tile_image[0] 読み込み成功")
    except Exception as e:
        print("❌ tile_image[0] 読み込み失敗:", e)
"""

#タイルの描写
def draw_map(surface):
    for y ,row in enumerate(map_data):
        for x, tile in enumerate(row):
            surface.blit(tile_image[tile],(x*tile_size, y*tile_size))
            
#座標が草むら上かどうか判定
def is_in_bush(x, y):
    tile_x = x // tile_size
    tile_y = y // tile_size
    if 0 <= tile_y < len(map_data) and 0 <= tile_x < len(map_data[0]):
        return map_data[tile_y][tile_x] == 1
    return False

    