# Rubén Villalpando
# Chaos game using pygame

import pygame, random, math


ANCHO = 800
ALTO = 800

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)



def colorear(puntos, distancia):
    pygame.init()

    reloj = pygame.time.Clock()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    termina = False

    ventana.fill(NEGRO)


    xP, yP = random.randint(20, ANCHO-20), random.randint(20, ALTO-20)

    listaEsquinas = []


    # copo de nieve con 5 esquinas

    for angulo in range(0,361, 72):
        x = int(400 + 400*math.cos(math.radians(angulo)))
        y = int(400 + 400*math.sin(math.radians(angulo)))
        listaEsquinas.append((x, y))
        pygame.draw.circle(ventana, BLANCO, (x, y), 5)

    currentChosenVertex = -1

    diccionarioColores = {}

    for x in listaEsquinas:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        diccionarioColores[x] = (r, g, b)



    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        punto = random.randint(1, puntos)

        while punto == currentChosenVertex:
            punto = random.randint(1, puntos)


        for k in range(1, len(listaEsquinas)+1):
            coordenadas = listaEsquinas[k-1]
            if k == punto:
                currentChosenVertex = punto
                color = diccionarioColores[coordenadas]
                x = coordenadas[0]
                y = coordenadas[1]
                if xP > x:
                    xP -= int(abs((xP-x)*distancia))
                    if yP > y:
                        yP -= int(abs((yP-y)*distancia))
                    else:
                        yP += int(abs((yP-y)*distancia))
                else:
                    xP += int(abs((xP - x)*distancia))
                    if yP > y:
                        yP -= int(abs((yP - y)*distancia))
                    else:
                        yP += int(abs((yP - y)*distancia))

        pygame.draw.circle(ventana, color, (xP, yP), 1)



        pygame.display.flip()
        reloj.tick()



    pygame.quit()




if __name__ == '__main__':
    # puntosTotales = int(input("Numero de puntos que va a tener la figura: "))
    colorear(5, 0.5)
