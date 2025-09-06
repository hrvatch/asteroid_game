import pygame
from player import *
from asteroid import *
from constants import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()
    # Default screen surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Define the clock object and variable dt which will hold delta time
    clock = pygame.time.Clock()
    dt = 0

    # Pygame groups one wil lbe used for updates and one for drawin
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add Player, Asteroids and AsteroidField to the correct sprite groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        
        # Quit the game if Escape key is pressed or if user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        screen.fill((20, 25, 35))

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                pygame.quit()
                return
            for bullet in shots:
                if bullet.collides(asteroid):
                    bullet.kill()
                    asteroid.split()
       
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
