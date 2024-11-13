import pygame
import random

GRID_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
SCREEN_WIDTH = GRID_WIDTH * GRID_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * GRID_SIZE


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0, 0
        mole_rect = mole_image.get_rect(topleft=(mole_x * GRID_SIZE, mole_y * GRID_SIZE))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mole was clicked
                    if mole_rect.collidepoint(event.pos):
                        # Move the mole to a random square
                        mole_x = random.randrange(0, GRID_WIDTH)
                        mole_y = random.randrange(0, GRID_HEIGHT)
                        mole_rect.topleft = (mole_x * GRID_SIZE, mole_y * GRID_SIZE)

            screen.fill("light green")

            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))

            screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
