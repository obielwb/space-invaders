import pygame, sys

from space_invaders import SpaceInvaders
from button import Button

if __name__ == '__main__':
  pygame.init()
  screen_width = 600
  screen_height = 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  clock = pygame.time.Clock()

  pygame.display.set_caption('Space Invaders')

  logo = pygame.image.load('space-invaders\\graphics\\red.png')
  pygame.display.set_icon(logo)

  mode = 'menu'
  players = 1

  space_invaders = SpaceInvaders(screen_width, screen_height, players)

  button_x = (screen_width / 2) - 240
  button_y = (screen_height / 2) - 30

  button_two_x = screen_width / 2
  button_two_y = (screen_height / 2) - 30

  one_player = Button(screen, (30, 30, 30), (255, 255, 255), button_x, button_y, 240, 60, "1 Player")
  two_player = Button(screen, (30, 30, 30), (255, 255, 255), button_two_x, button_two_y, 240, 60, "2 Player")

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
        if pygame.mouse.get_pressed()[0]:
          x, y = pygame.mouse.get_pos()

          if one_player.is_over(x, y):
            print("1 Player")
            players = 1
            mode = 'game'
          if two_player.is_over(x, y):
            print("2 Player")
            players = 2
            mode = 'game'

      one_player.draw()
      two_player.draw()

      space_invaders = SpaceInvaders(screen_width, screen_height, players)
      screen.fill((30, 30, 30))
      pygame.display.flip()
      clock.tick(60)
