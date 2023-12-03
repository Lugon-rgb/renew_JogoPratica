import pygame, sys, random
from pygame.locals import *

# VARIÁVEIS
screen_width = 19 * 77
screen_height = 7 * 77
game_over = False
defeat_font = None

# Define a taxa de atualização
clock = pygame.time.Clock()

#mapa
mapa = []
tile={} # Usando dicionário

# Jogador
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size
player_speed = 15

font = None

inicio = True

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
  pygame.draw.rect( 'white', [x, y, player_size, player_size])


# FUNÇÕES
def load_mapa(filename): # Lê o conteúdo do arquivo para a matriz
  global mapa
  file = open(filename,"r")
  for line in file.readlines():
   mapa.append(line)
  file.close()
  
def load():
  global clock, tile, font, defeat_font
  
  clock = pygame.time.Clock()
  
  #mapa
  load_mapa("mapa.txt")
  tile['G'] = pygame.image.load("img/Tiles/grama.png")
  tile['A'] = pygame.image.load("img/Tiles/aguaMeio.png")

  # Pontuação
  font = pygame.font.Font(None, 36)
  defeat_font = pygame.font.Font(None, 60)  
  
def draw(screen):
  global caixa, chao, game_over, start_following
  
  screen.fill((255,255,255))
  
  #pontuacao()
  
  #mapa
  for i in range(8):
    for j in range(14):
        screen.blit(tile[mapa[i][j]], ((j * 77), (i * 77)))

  draw_player(player_x, player_y)

  if game_over == True:
        defeat_text = defeat_font.render("Você perdeu!", True, "red")
        text_rect = defeat_text.get_rect(center=(screen_width // 2, (screen_height // 2)))
        screen.blit(defeat_text, text_rect.topleft)
        
        
def movimentacaoPersonagem():
  global velocidade_y, jump, player_x, player_y, player_size, player_speed
  keys = pygame.key.get_pressed()

  if keys[pygame.K_w]:
    player_y -= player_speed
    
  if keys[pygame.K_a] and player_x > 0:
      player_x -= player_speed
  
  if keys[pygame.K_d] and player_x < screen_width - player_size:
      player_x += player_speed
      
  if keys[pygame.K_s]:
      player_y += player_speed
        
        
def update(dt):
    global game_over, start_following
    movimentacaoPersonagem()

        
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

  pygame.display.update()

pygame.quit()
sys.exit()
