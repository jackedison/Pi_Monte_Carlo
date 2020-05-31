import pygame
import random
from math import hypot


# Initialise the surface
diameter = 700
margin = 60
surface = pygame.display.set_mode(size=(diameter, diameter+margin))
surface.fill((255, 255, 255))

# Draw a circle on the surface (no kwaargs accepted)
pygame.draw.circle(surface,  # Surface object
                   (0, 0, 0),  # Colour
                   (diameter//2, diameter//2),  # Center
                   diameter//2,  # Radius
                   1)  # Width/fill

pygame.draw.rect(surface,
                 (0, 0, 0),
                 pygame.Rect(0, 0, diameter, diameter),
                 1)

# Initialise font
pygame.font.init()
font = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 35)

# Begin computation
num_dots = 0
num_dots_in_circle = 0

running = True
while running:
    # Drop a random dot on the surface
    dot_x = random.random()
    dot_y = random.random()

    # Check if dot is in the circle (assumes circle line width of 0)
    # Do this by checking euclidean distance from centre < r with pythagorus
    if hypot(dot_x, dot_y) < 1:
        num_dots_in_circle += 1
    num_dots += 1

    # Draw dot to surface
    rect = pygame.draw.circle(surface,
                              (0, 0, 255),
                              (round(dot_x*diameter), round(dot_y*diameter)),
                              2,
                              0)

    pygame.display.update(rect)

    # Calculate pi
    pi = 4 * num_dots_in_circle / num_dots

    # Draw to surface - clear old text
    left, top, width, height = 0, diameter, diameter, margin
    surface.fill((255, 255, 255), (left, top, width, height))

    # Draw new text to screen
    string_1 = 'Pi: {:.9f}'.format(pi)
    string_2 = 'Calculation: 4 * {} / {}'.format(num_dots_in_circle,
                                                 num_dots)
    text_1 = font.render(string_1, True, (0, 0, 0))
    text_2 = font_small.render(string_2, True, (0, 0, 0))
    surface.blit(text_1, (left, top))
    surface.blit(text_2, (left, top+35))

    # Check if user has quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
