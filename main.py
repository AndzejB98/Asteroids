import pygame # type: ignore
from constants import *
from player import *

pygame.init()

clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

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
    pygame.display.flip() # Update the display
    dt = clock.tick(60) / 1000

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()