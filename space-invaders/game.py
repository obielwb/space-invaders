from time import sleep
import pygame
import sys

from space_invaders import SpaceInvaders
from button import Button

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Space Invaders')

    logo = pygame.image.load('./graphics/red.png')
    pygame.display.set_icon(logo)

    mode = 'menu'
    players = 1

    space_invaders = SpaceInvaders(
        screen, screen_width, screen_height, players)

    button_x = (screen_width / 2) - 240
    button_y = (screen_height / 2) + 40

    button_two_x = screen_width / 2
    button_two_y = (screen_height / 2) + 40

    one_player = Button(screen, (30, 30, 30), (255, 255, 255),
                        button_x, button_y, 240, 60, "1 Player")
    two_player = Button(screen, (30, 30, 30), (255, 255, 255),
                        button_two_x, button_two_y, 240, 60, "2 Player")

    one_player.draw()
    two_player.draw()

    quit_button = Button(screen, (30, 30, 30), (255, 255, 255),
                         screen_width / 2 - 30, screen_height / 2 + 150, 60, 60, "Quit")

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        if mode == 'game':
            if space_invaders.win:
                mode = 'menu'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ALIENLASER:
                    space_invaders.alien_shoot()
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()

                    if space_invaders.restart_button.is_over(x, y):
                        space_invaders = SpaceInvaders(
                            screen, screen_width, screen_height, players)

                        screen.fill((30, 30, 30))

                    if space_invaders.quit_button.is_over(x, y):
                        pygame.quit()
                        sys.exit()

            if space_invaders.running:
                screen.fill((30, 30, 30))

                space_invaders.run()

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
                        players = 1
                        mode = 'game'
                    elif two_player.is_over(x, y):
                        players = 2
                        mode = 'game'
                    elif quit_button.is_over(x, y):
                        pygame.quit()
                        sys.exit()

            sleep(0.1)

            screen.fill((30, 30, 30))

            red = pygame.image.load('./graphics/red.png')
            green = pygame.image.load('./graphics/green.png')
            yellow = pygame.image.load('./graphics/yellow.png')

            screen.blit(red, (screen_width / 2 - 100 - 40, 150))
            screen.blit(green, (screen_width / 2 - 40, 150))
            screen.blit(yellow, (screen_width / 2 + 100 - 40, 150))

            font = pygame.font.Font('./font/Pixeled.ttf', 30)
            space_invaders_text = font.render(
                'SPACE INVADERS', True, (255, 255, 255))

            screen.blit(space_invaders_text, (screen_width / 2 - 200, 240))

            space_invaders = SpaceInvaders(
                screen, screen_width, screen_height, players)

            one_player.draw()
            two_player.draw()
            quit_button.draw()

            pygame.display.flip()

            clock.tick(60)
