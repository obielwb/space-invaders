from time import sleep
import pygame

from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser
from button import Button


class SpaceInvaders:
    def __init__(self, screen, screen_width, screen_height, players=1):
        self.players = players
        if (self.players > 1):
            player_sprite = Player(
                (screen_width / 2, screen_height), screen_width, 5)
            self.player = pygame.sprite.GroupSingle(player_sprite)

            player_two_sprite = Player(
                (screen_width / 2, screen_height), screen_width, 5, is_first_player=False)
            self.player_two = pygame.sprite.GroupSingle(player_two_sprite)
        else:
            player_sprite = Player(
                (screen_width / 2, screen_height), screen_width, 5)
            self.player = pygame.sprite.GroupSingle(player_sprite)

        self.screen = screen

        # health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load(
            './graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - \
            (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('./font/Pixeled.ttf', 20)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.restart_button = Button(screen, (30, 30, 30), (255, 255, 255),
                                     screen_width / 2 - 100, screen_height / 2, 200, 60, "Restart")

        self.quit_button = Button(screen, (30, 30, 30), (255, 255, 255),
                                  screen_width / 2 - 100, screen_height / 2 + 50, 200, 60, "Quit")

        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [
            num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(
            *self.obstacle_x_positions, x_start=screen_width / 15, y_start=480)

        # Aliens setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, columns=8)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()

        self.running = True
        self.win = False

        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio
        music = pygame.mixer.Sound('./audio/music.wav')
        music.set_volume(0.05)
        music.play(loops=-1)

        self.laser_sound = pygame.mixer.Sound(
            './audio/laser.wav')
        self.laser_sound.set_volume(0.1)
        self.explosion_sound = pygame.mixer.Sound(
            './audio/explosion.wav')
        self.explosion_sound.set_volume(0.1)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column == 'x':
                    x = x_start + column_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(
                        self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, columns, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for column_index, column in enumerate(range(columns)):
                x = column_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= self.screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,
                                 6, self.screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left']), self.screen_width))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collisions
                aliens_hit = pygame.sprite.spritecollide(
                    laser, self.aliens, True)
                if aliens_hit:
                    laser.kill()
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.points

                # extra collisions
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.score += 500
                    laser.kill()

        if self.players == 2:
            if self.player_two.sprite.lasers:
                for laser in self.player_two.sprite.lasers:
                    # obstacle collisions
                    if pygame.sprite.spritecollide(laser, self.blocks, True):
                        laser.kill()

                    # alien collisions
                    aliens_hit = pygame.sprite.spritecollide(
                        laser, self.aliens, True)
                    if aliens_hit:
                        laser.kill()
                        self.explosion_sound.play()
                        for alien in aliens_hit:
                            self.score += alien.points

                    # extra collisions
                    if pygame.sprite.spritecollide(laser, self.extra, True):
                        self.score += 500
                        laser.kill()

        # aliens lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.running = False

                if self.players == 2:
                    if pygame.sprite.spritecollide(laser, self.player_two, False):
                        laser.kill()
                        self.lives -= 1
                        if self.lives <= 0:
                            self.running = False

        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, True):
                    self.running = False

    def game_over(self):
        self.running = False
        self.screen.fill((30, 30, 30))

        game_over_surf = self.font.render('Game Over', False, (255, 255, 255))
        score_surf = self.font.render(
            f'Score: {self.score}', False, (255, 255, 255))
        game_over_rect = game_over_surf.get_rect(
            center=(self.screen_width / 2, self.screen_height / 2 - 100))
        score_rect = score_surf.get_rect(
            center=(self.screen_width / 2, self.screen_height / 2 - 50))
        self.screen.blit(game_over_surf, game_over_rect)
        self.screen.blit(score_surf, score_rect)

        self.restart_button.draw()
        self.quit_button.draw()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + \
                (live * (self.live_surf.get_size()[0] + 10))
            self.screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(
            f'Score: {self.score}', False, (255, 255, 255))
        score_rect = score_surf.get_rect(topleft=(10, -10))
        self.screen.blit(score_surf, score_rect)

    def victory_message(self):
        if not self.aliens:
            victory_surf = self.font.render('You win!', False, (255, 255, 255))
            victory_rect = victory_surf.get_rect(
                center=(self.screen_width / 2, self.screen_height / 2))
            self.screen.blit(victory_surf, victory_rect)
            self.win = True

    def run(self):
        self.player.update()
        if self.players == 2:
            self.player_two.update()

        self.aliens.update(self.alien_direction)
        self.alien_lasers.update()
        self.extra.update()

        self.alien_position_checker()
        self.extra_alien_timer()
        self.collision_checks()
        self.display_lives()
        self.display_score()

        self.player.draw(self.screen)
        self.player.sprite.lasers.draw(self.screen)
        if (self.players == 2):
            self.player_two.draw(self.screen)
            self.player_two.sprite.lasers.draw(self.screen)

        self.blocks.draw(self.screen)
        self.aliens.draw(self.screen)
        self.alien_lasers.draw(self.screen)
        self.extra.draw(self.screen)

        self.victory_message()

        if not self.running and not self.win:
            self.game_over()

        if self.win:
            sleep(3)
