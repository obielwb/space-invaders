import pygame, sys

from space_invaders import SpaceInvaders
from menu import Menu

if __name__ == '__main__':
  pygame.init()
  screen_width = 600
  screen_height = 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  clock = pygame.time.Clock()

  pygame.display.set_caption('Space Invaders')
  pygame.display.set_icon(pygame.image.load('space-invaders\\graphics\\red.png'))

  space_invaders = SpaceInvaders(screen_width, screen_height, players=2)
  menu = Menu(screen_width, screen_height, screen)

  mode = 'game'

  ALIENLASER = pygame.USEREVENT + 1
  pygame.time.set_timer(ALIENLASER, 800)

  while True:
    if mode == 'game':
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

    elif mode == 'menu':
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mode = 'menu'

      screen.fill((30, 30, 30))
      menu.run(screen)
      pygame.display.flip()
      clock.tick(60)


