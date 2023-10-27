import pygame
import sys
import random
# Inicializar Pygame
pygame.init()
# Definir los colores

ventana = pygame.display.set_mode((500, 400))
# Definir las dimensiones de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load('fondo_2.png')
# Colocar la imagen de fondo en la pantalla
screen.blit(background_image, (-150, -70))
pygame.display.set_caption("Fast memory")
# Definir la velocidad del jugador
PLAYER_SPEED = 3
# Definir el tamaño del jugador
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
# Crear el jugador
player = pygame.Rect(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
# Crear los puntos
score=0
RED = (255, 0, 0)
points = []
POINTS_NUM = 1
for _ in range(POINTS_NUM):
    point = pygame.Rect(random.randint(0, SCREEN_WIDTH - 15),
                        random.randint(0, SCREEN_HEIGHT - 15), 25, 25)
    points.append(point)
BLUE=(0,0,200)
pointes = []
POINTS_NUM = 1
for _ in range(POINTS_NUM):
    pointu = pygame.Rect(random.randint(0, SCREEN_WIDTH - 55),
                        random.randint(0, SCREEN_HEIGHT - 55), 25, 25)
    pointes.append(pointu)
WHITE = (255, 255, 255)
pointeD = []
POINTS_NUM = 1
for _ in range(POINTS_NUM):
    pointW = pygame.Rect(random.randint(0, SCREEN_WIDTH - 25),
                        random.randint(0, SCREEN_HEIGHT - 25), 25, 25)
    pointeD.append(pointW)
# Crear el marcador de puntosww
vidas=3
puntaje = 0
font = pygame.font.Font(None, 36)
# Crear la gravedad
GRAVITY = 1
is_jumping = False
jump_count = 10
# Crear el bucle principal
run=True
while run:
    if score==100:
      break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    # Movimiento del jugador
    if keys[pygame.K_w] and not is_jumping:
        player.y -= PLAYER_SPEED    
    if keys[pygame.K_a]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player.y += PLAYER_SPEED
    if keys[pygame.K_d]:
        player.x += PLAYER_SPEED
    if is_jumping:
        player.y -= jump_count
        jump_count -= 1
        if jump_count < -5:
            is_jumping = False
            jump_count = 5
    # Gravedad


    # Comprobar si el jugador ha tocado un punto
    for point in points:
        if player.colliderect(point):
            points.remove(point)
            score += 10
            if score==100:
                score="You"
    for pointu in pointes:
        if player.colliderect(pointu):
            pointes.remove(pointu)
            run=False
    for pointW in pointeD:
        if player.colliderect(pointW):
            pointeD.remove(pointW)
            run=False
    # Dibujar la pantalla
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player)
    for point in points:
        pygame.draw.rect(screen, RED, point)
    for pointu in pointes:
        pygame.draw.rect(screen, BLUE, pointu)
    for pointW in pointeD:
        pygame.draw.rect(screen, WHITE, pointW)
    # Dibujar el marcador de puntos
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(background_image, (10, 10))
    # Actualizar la pantalla
    pygame.display.update()

    #colores de los botones

    #rojo
    #morado
    #azul
    #verde
    #naranja
    #amarillo
    #blanco
