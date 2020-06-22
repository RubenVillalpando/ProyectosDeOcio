# # Rubén Villalpando Bremont
# # Barnsley Fern
#
# import pygame, math, random
#
# ANCHO = 800
# ALTO = 800
#
# NEGRO = (0, 0, 0)
# BLANCO = (255, 255, 255)
# VERDE = (30, 200, 30)
#
#
#
# def colorear():
#     pygame.init()
#
#     reloj = pygame.time.Clock()
#     ventana = pygame.display.set_mode((ANCHO, ALTO))
#     termina = False
#
#     ventana.fill(NEGRO)
#
#     currentPoint = (0, 0)
#
#
#     while not termina:
#
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 termina = True
#
#         pygame.draw.circle(ventana, VERDE, (int(currentPoint[0])*10 + 400, int(currentPoint[1])*10 + 400), 1)
#
#         lastPoint = currentPoint
#
#         chosenPoint = random.random()
#
#         if chosenPoint <= 0.01:
#             x = 0
#             y = -lastPoint[1]*0.16
#             print("first point")
#         elif chosenPoint <= 0.86:
#             x = 0.85*lastPoint[0] + 0.04*lastPoint[1]
#             y = -0.04*lastPoint[0] - 0.85*lastPoint[1] - 1.6
#             print("second point")
#         elif chosenPoint <= 0.93:
#             x = 0.2*lastPoint[0] - 0.26*lastPoint[1]
#             y = -0.23*lastPoint[0] - 0.22*lastPoint[1] - 1.6
#             print("third point")
#         else:
#             x = -0.15*lastPoint[0] + 0.28*lastPoint[1]
#             y = -0.26*lastPoint[0] - 0.24*lastPoint[1] - 0.44
#             print("fourth point")
#         print("current point: ", currentPoint[0], currentPoint[1])
#         print("last point: ", currentPoint[0], currentPoint[1])
#         currentPoint = (x, y)
#         print("new current point: ", currentPoint)
#
#
#         pygame.display.flip()
#         reloj.tick()
#
#
#
#     pygame.quit()
#
#
#
#
# if __name__ == '__main__':
#     # puntosTotales = int(input("Numero de puntos que va a tener la figura: "))
#     colorear()
import random
import matplotlib.pyplot as plt



X = [0]
Y = [0]
for n in range(100000):
    r = random.uniform(0, 100)
    if r < 1.0:
        x = 0
        y = 0.16*Y[n-1]
    elif r < 86.0:
        x = 0.85*X[n-1] + 0.04*Y[n-1]
        y = -0.04*X[n-1] + 0.85*Y[n-1]+1.6
    elif r < 93.0:
        x = 0.2*X[n-1] - 0.26*Y[n-1]
        y = 0.23*X[n-1] + 0.22*Y[n-1] + 1.6
    else:
        x = -0.15*X[n-1] + 0.28*Y[n-1]
        y = 0.26*X[n-1] + 0.24*Y[n-1] + 0.44
    X.append(x);Y.append(y)

'''Make a plot'''
plt.figure(figsize = [15,15])
plt.scatter(X,Y,color = 'g',marker = '.')
plt.show()