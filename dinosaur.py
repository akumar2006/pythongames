import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dinosaur Game!")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)

# Classes

class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/Dino1.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/Dino2.png"), (80, 100)))

        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/DinoDucking1.png"), (110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("assets/DinoDucking2.png"), (110, 60)))

        self.x = x_pos
        self.y = y_pos

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.velocity = 50
        self.gravity = 4.5
        self.ducking = False

        self.jump_height = 50
        self.jumping = False

    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0

        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        else:
            self.image = self.running_sprites[int(self.current_image)]

    def duck(self):
        self.ducking = True
        self.rect.centery = 380

    def unduck(self):
        self.ducking = False
        self.rect.centery = 360

    def apply_gravity(self):
        if self.rect.centery <= 360:
            self.rect.centery += self.gravity

    # def jump(self):



        # self.Jumping = True
        # if self.Jumping:
        #     if self.jump_count >= -10:
        #         sign = 1
        #     if self.jump_count <= 0:
        #         sign = -1
        #     self.y -= self.jump_count**2 * 0.1 * sign
        #     self.jump_count -= 1
        # else:
        #     self.Jumping = False
        #     self.jump_count = 10


        # if self.rect.centery >= 360:
        #     self.jumping = True
        #     if self.jumping and self.rect.centery - self.velocity > 40:
        #         self.rect.centery -= 1
        #     else: self.jumping = False

# Variables

game_speed = 5
game_score = 0
tick = 0

# Surfaces

ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (1280, 20))
ground_x = 0
ground_rect = ground.get_rect(center = (640, 400))

# Groups

dino_group = pygame.sprite.GroupSingle()

# Objects

dinosaur = Dino(50, 360)
dino_group.add(dinosaur)

while True:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dinosaur.duck()
    else:
        if dinosaur.ducking:
            dinosaur.unduck()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if dinosaur.jumping == False and (event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w):
                dinosaur.jumping = True
                # dinosaur.jump()
    if dinosaur.jumping:
        if (dinosaur.jump_height > 0 and dinosaur.rect.centery >= 360):
            # dinosaur.rect.centery -= (dinosaur.jump_height ** 2) * 0.05
            dinosaur.rect.centery -= (dinosaur.jump_height * abs(dinosaur.jump_height)) * 0.1
            dinosaur.jump_height -= 1
        else:
            dinosaur.jumping = False
            dinosaur.jump_height = 50
    screen.fill("white")

    dino_group.update()
    dino_group.draw(screen)

    game_speed += 0.0025
    tick += 1
    if tick % 12 == 0:
        game_score += 1

    ground_x -= 1

    scoretext = game_font.render('Score: ' + str(game_score), True, "black", "white")
    scoretextRect = scoretext.get_rect()
    scoretextRect.center = (1100,50)

    screen.blit(ground, (ground_x, 360))
    screen.blit(ground, (ground_x + 1280, 360))
    screen.blit(scoretext,scoretextRect)

    if ground_x <= -1280:
        ground_x = 0

    pygame.display.update()
    clock.tick(120)