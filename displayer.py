import planet
import pygame

def display(window ,planets: list[planet.planet])-> None:
    for planet in planets:
        pygame.draw.circle(window, planet.color, planet.position, planet.radius)