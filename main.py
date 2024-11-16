def main():
    #external libraries
    import pygame
    import sys
    #internal modules
    import planet
    

    planets : list[planet.planet]

    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 1000

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simulador de gravedad")
    print("starting")

    playing = True
    FPS = 60
    G = 6.6743 *(10**(-11))
    print(G)

    #A = planet.planet(190000000000000000,(300,500),(255,255,0),100,(0,100))
    #B = planet.planet(190000000000000000,(700,500),(0,0,255),100,(0,-100))

    #A = planet.planet(300000000000000000,(500,500),(30,129,176),100,(0,0))
    #B = planet.planet(300,(800,500),(135,62,35),20,(10,200))
    C = planet.planet(10000,(90, 200),(0,255,0),20,(-20,-100))
    D = planet.planet(10000,(100,900),(255,255,200),10,(150,0))
    #E = planet.planet(100000000000000000,(200,500),(255,0,100),80,(0,-250))

    planets = [
        A,
        B,
        C,
        D
        
    ]

    while playing:
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        planet.update_velocities(planets,G)
        for entity in planets:
            entity.move(fps = FPS)

        """from planet import calculate_distance
        print(calculate_distance(A,B))"""

        import displayer 
        displayer.display(window,planets)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print(__name__)
    main()