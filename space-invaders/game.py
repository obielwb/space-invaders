import pygame, sys

from space_invaders import SpaceInvaders

if __name__ == '__main__':
  pygame.init()
  screen_width = 600
  screen_height = 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  clock = pygame.time.Clock()

  space_invaders = SpaceInvaders(screen_width, screen_height)

  ALIENLASER = pygame.USEREVENT + 1
  pygame.time.set_timer(ALIENLASER, 800)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == ALIENLASER:
        space_invaders.alien_shoot()

    screen.fill((30, 30, 30))
    space_invaders.run(screen)

    pygame.display.flip()
    clock.tick(60)
