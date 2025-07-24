import sys
import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

pygame.init()

clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


asteroidfield = AsteroidField()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Fill the screen with black

    for obj in drawable:
        obj.draw(screen)

    updatable.update(dt)  # Update the player state

    for obj in asteroids:
        for bullet in shots:
            if obj.collision_check(bullet) == True:
                obj.split()

        if obj.collision_check(player) == True:
            print("Game over!")
            pygame.time.wait(5)
            sys.exit()
    
        

    pygame.display.flip() # Update the display
    dt = clock.tick(60) / 1000

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()