import pygame

class Menu:
  def __init__(self, screen_width, screen_height, screen):
    super().__init__()
    self.font = pygame.font.Font('space-invaders\\font\Pixeled.ttf', 20)

    self.screen_width = screen_width
    self.screen_height = screen_height


  def make_buttons(self, screen):
    mouse = pygame.mouse.get_pos()
    if self.screen_width/2 <= mouse[0] <= self.screen_width/2+140 and self.screen_height/2.5 <= mouse[1] <= self.screen_height/2.5+40:
      pygame.draw.rect(screen,(170, 170, 170),[self.screen_width/2,self.screen_height/2.5,140,40])

    if self.screen_width/2 <= mouse[0] <= self.screen_width/2+140 and self.screen_height/2 <= mouse[1] <= self.screen_height/2+40:
      pygame.draw.rect(screen,(170, 170, 170),[self.screen_width/2,self.screen_height/2,140,40])

    else:
      pygame.draw.rect(screen,(100, 100, 100),[self.screen_width/2,self.screen_height/2.5,140,40])
      pygame.draw.rect(screen,(100, 100, 100),[self.screen_width/2,self.screen_height/2,140,40])

  def run(self, screen):
    victory_surf = self.font.render('1 - Player', False, (255, 255, 255))
    victory_rect = victory_surf.get_rect(center = (self.screen_width / 2, self.screen_height / 2))
    screen.blit(victory_surf, victory_rect)

    self.make_buttons(screen)
