# Rubén Villalpando
# Visualizing sorting algorithms using pygame

import pygame, random

ANCHO = 800
ALTO = 800

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

def dibujar():

    pygame.init()
    reloj = pygame.time.Clock()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    termina = False

    ventana.fill(NEGRO)

    listaBarras = []

    for n in range(0, 801, 2):
        y = random.randint(0, 800)
        x = n
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        listaBarras.append((x, y, r, g, b))



    while not termina:

        ventana.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        for x in range(0, len(listaBarras)):
            randomColor = (listaBarras[x][2], listaBarras[x][3], listaBarras[x][4])
            pygame.draw.line(ventana, randomColor, (2*x, 800), (2*x, listaBarras[x][1]), 2)

        for x in range(0, len(listaBarras)-1):

            if listaBarras[x][1]<listaBarras[x+1][1]:
                barraMayor = listaBarras[x]
                listaBarras[x] = listaBarras[x+1]
                listaBarras[x+1] = barraMayor


        pygame.display.flip()
        reloj.tick(10)

    pygame.quit()


if __name__ == '__main__':
    dibujar()
