from math import sqrt
import pygame

points = []
rad = int(input())

for y in range(rad):
    for x in range(rad):
        if (rad-0.5) < (sqrt(x**2 + y**2)) < (rad+0.5):
            points.append([x, y])
        else:
            pass

print(points)

# Display in pygame
WIDTH = 200
HEIGHT = 200

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Circle")
screen.fill(WHITE)
pygame.init()
for i in points:
    pygame.draw.line(screen, (0, 0, 0), i, i)
    pygame.display.update()

input()

