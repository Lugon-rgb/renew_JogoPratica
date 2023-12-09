import pygame, sys, random, math
from pygame.locals import *

# VARIÁVEIS

# mapa
tile_size = 64
screen_width = tile_size * 12
screen_height = tile_size * 6
mapa = []
tile_quads = []
tiles_pattern = ['G', 'F', 'B', 'T', 'R', 'B', 'A', 'P', 'S']

mapa_config = {
   'mapaSize_x': 36,
   'mapaSize_y': 6,
   'mapaDisplay_x': 12,
   'mapaDisplay_y': 6
}

camera = {
   'pos_x': 0,
   'pos_y': 0,
   'speed': 0.120
}

# jogabilidade
game_over = False
inicio = True

# fontes
font = None
defeat_font = None

# Define a taxa de atualização
clock = pygame.time.Clock()

# Jogador
player_size = 50
player_x = 10 #player_size // 2
player_y = screen_height // 2 - player_size // 2
player_speed = 4


# FUNÇÕES

def comentarios():
  pass
  # #personagem variáveis
  # dino_walk = []
  # dino_frameAnim = 1
  # dino_x = 100
  # dino_y = 300
  # direcao = "direita"
  # dino_TimeAnim = 0

  #load
   #personagem
  # for i in range(1, 11):
  #   dino_walk.append(pygame.image.load("img/Personagem/Walk("+str(i)+").png"))

  #Pontuação
  #  fonte = pygame.font.Font(, 20)

  #UPDATE
  #old_x, old_y = dino_x, dino_y

  #personagem (dino)
  # if keys[pygame.K_RIGHT]:
  #   direcao = "direita"
  #   dino_x = dino_x + (0.1 * dt)
  #   dino_TimeAnim = dino_TimeAnim + dt
  #   if dino_TimeAnim > 100:
  #     dino_frameAnim = dino_frameAnim + 1      
  #     if dino_frameAnim > 9:
  #       dino_frameAnim = 1
  #     dino_TimeAnim = 0

  # if keys[pygame.K_LEFT]:
  #   direcao = "esquerda"
  #   dino_x = dino_x - (0.1 * dt)
  #   dino_TimeAnim = dino_TimeAnim + dt
  #   if dino_TimeAnim > 100:
  #     dino_frameAnim = dino_frameAnim - 1      
  #     if dino_frameAnim < 1:
  #       dino_frameAnim = 9
  #     dino_TimeAnim = 0

  # Alterar escala da imagem
  #dino_walk[dino_frameAnim] = pygame.transform.scale(dino_walk[dino_frameAnim], (210, 210))

  #DRAW
  #personagem (dino)
  #screen.blit(dino_walk[dino_frameAnim], (dino_x, dino_y))
  
def draw_player(x, y):
  pygame.draw.rect(screen, (0, 0, 0), [x, y, player_size, player_size])


# FUNÇÕES
def load_mapa(filename): # Lê o conteúdo do arquivo para a matriz
  global mapa
  file = open(filename,"r")
  for line in file.readlines():
   mapa.append(line)
  file.close()
  
def load_tiles(filename, nx, ny):
  global tileset_image, tile_quads
  
  tileset_image = pygame.image.load(filename)
  for i in range(nx):
    for j in range(ny):
      tile_quads.append((i * tile_size, j * tile_size, tile_size, tile_size))


def load():
  global clock, tile, font, defeat_font
  
  clock = pygame.time.Clock()
  
  #mapa
  load_mapa("mapa.txt")
  load_tiles("platform_tileset.png", 3, 3)

  # Pontuação
  font = pygame.font.Font(None, 36)
  defeat_font = pygame.font.Font(None, 60)  
  
def draw(screen):
  global caixa, chao, game_over, start_following
  
  screen.fill((255,255,255))

  # MAPA
  offset_x = math.floor(camera['pos_x'] % tile_size)
  first_tile_x = math.floor(camera['pos_x'] / tile_size)
  range_x = mapa_config['mapaDisplay_x']

  # antes do fim da fase - mostrar um tile a mais
  if first_tile_x != mapa_config["mapaSize_x"] - mapa_config["mapaDisplay_x"]:
    range_x = mapa_config["mapaDisplay_x"] + 1

  for y in range(mapa_config["mapaDisplay_y"]):
    for x in range(range_x):
      if mapa[y][x + first_tile_x] in tiles_pattern:
        pos = ((x * tile_size) - offset_x,(y * tile_size))
        pattert_index = tiles_pattern.index(mapa[y][x + first_tile_x])
        screen.blit(tileset_image, pos, tile_quads[pattert_index])


  draw_player(player_x, player_y)

  if game_over == True:
        defeat_text = defeat_font.render("Você perdeu!", True, "red")
        text_rect = defeat_text.get_rect(center=(screen_width // 2, (screen_height // 2)))
        screen.blit(defeat_text, text_rect.topleft)
        
        
def movimentacaoPersonagem_Teclado():
  global player_x, player_y, player_size, player_speed
  keys = pygame.key.get_pressed()

  if keys[pygame.K_w]:
    player_y -= player_speed
    
  if keys[pygame.K_a] and player_x > 0:
      player_x -= player_speed
      camera['pos_x'] = camera['pos_x'] - (camera['speed'] * dt)
  
  if keys[pygame.K_d]: #and player_x < screen_width - player_size:
      player_x += player_speed
      camera['pos_x'] = camera['pos_x'] + (camera['speed'] * dt)
      
  if keys[pygame.K_s]:
      player_y += player_speed
      

def movimentacaoPersonagem_Mouse():
  global player_x, player_y
  
  mouse_x, mouse_y = pygame.mouse.get_pos()
  player_x += (mouse_x - player_x) * 1
  player_y += (mouse_y - player_y) * 1
        
 

def movimentoCamera():
  global camera

  keys = pygame.key.get_pressed()

  if keys[pygame.K_d]:
    camera['pos_x'] = camera['pos_x'] + (camera['speed'] * dt)

  elif keys[pygame.K_a]:
    camera['pos_x'] = camera['pos_x'] - (camera['speed'] * dt)

  # verifica os limites da fase e trava a camera
  if camera['pos_x'] < 0:
    camera['pos_x'] = 0
  elif camera['pos_x'] > (mapa_config['mapaSize_x'] - mapa_config['mapaDisplay_x']) * tile_size:
    camera['pos_x'] = (mapa_config['mapaSize_x'] - mapa_config['mapaDisplay_x'] * tile_size)



def update(dt):
  global game_over, start_following
  #movimentacaoPersonagem_Mouse()
  movimentacaoPersonagem_Teclado()
  movimentoCamera()

        
# CÓDIGO PRINCIAPL
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sky Jump")

load()
running = True
while running:
  clock.tick(60)
  dt = clock.get_time()

  draw(screen)
  update(dt)
  

  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
      break

  print(camera['pos_x'])
  pygame.display.update()

pygame.quit()
sys.exit()

