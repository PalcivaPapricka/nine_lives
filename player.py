import pygame
from settings import screen, SCREEN_WIDTH, SCREEN_HEIGHT
from world import water_group, grave_group, Grave, rat_group, spike_group
pygame.mixer.init()

class Player:
    def __init__(self, x, y, lives):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.flipping = False
        self.flip_angle = 0
        self.flip_speed = 20
        self.dead_img = pygame.image.load(f'img/rip.png')
        self.lives = lives
        self.end = False
        self.sound_effect = pygame.mixer.Sound("img/jump1.mp3")
        self.sound_effect2 = pygame.mixer.Sound("img/jump2.mp3")
        self.sound_effect3 = pygame.mixer.Sound("img/death.mp3")
        self.sound_effect.set_volume(0.5)
        self.sound_effect3.set_volume(0.5)

        for num in range(1, 3):
            img_right = pygame.image.load(f'img/cat{num}.png')
            img_right = pygame.transform.scale(img_right, (100, 100))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = pygame.Rect(x, y, 40, 80)
        self.offset_x = (100 - 40) // 2
        self.offset_y = (100 - 80) // 2
        self.vel_y = 0
        self.jumped = False
        self.jump_count = 0
        self.direction = 1
        self.gravity_multiplier = 1

    def update(self, world):
        dx, dy = 0, 0
        walk_cooldown = 5

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jumped and self.jump_count < 2:
            self.vel_y = -15
            self.jumped = True
            self.jump_count += 1

            if self.jump_count == 2:
                self.flipping = True
                self.flip_angle = 0
                self.sound_effect2.play()
            else:
                self.sound_effect.play()

        if not key[pygame.K_SPACE]:
            self.jumped = False

        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1

        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.counter = 0
            self.index = 0
            self.image = self.images_right[self.index] if self.direction == 1 else self.images_left[self.index]

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images_right)
            self.image = self.images_right[self.index] if self.direction == 1 else self.images_left[self.index]

        if self.vel_y >= 0:
            self.gravity_multiplier = min(self.gravity_multiplier + 0.1, 3)
        else:
            self.gravity_multiplier = 1

        self.vel_y += self.gravity_multiplier
        self.vel_y = min(self.vel_y, 15)
        dy += self.vel_y

        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y < 0:  # Ceiling hit
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:  # Landing
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.jump_count = 0
                    self.flipping = False
                    self.gravity_multiplier = 1

        if grave_group:
            for grave in grave_group:
                if grave.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0

                if grave.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    if self.vel_y < 0:
                        dy = grave.rect.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = min(dy, grave.rect.top - self.rect.bottom)
                        self.vel_y = 0
                        self.jump_count = 0
                        self.flipping = False
                        self.gravity_multiplier = 1



        if self.rect.x + dx < 0:
            dx = -self.rect.x
        if self.rect.x + dx + self.rect.width > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.width - self.rect.x

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
            self.jump_count = 0
            self.flipping = False

        if pygame.sprite.spritecollide(self, water_group, False) or pygame.sprite.spritecollide(self, spike_group, False):
            global lives
            grave = Grave(self.rect.x, self.rect.y)
            grave_group.add(grave)
            self.rect.x=100
            self.rect.y=850
            self.lives-=1
            self.sound_effect3.play()

        if pygame.sprite.spritecollide(self, rat_group, False):
           self.end=True


    def draw(self):
        if self.flipping:
            self.flip_angle += self.flip_speed
            if self.flip_angle >= 360:
                self.flipping = False
                self.flip_angle = 0

            rotated_image = pygame.transform.rotate(
                self.images_right[self.index] if self.direction == 1 else self.images_left[self.index],
                self.flip_angle * self.direction
            )
            screen.blit(rotated_image, (self.rect.x - self.offset_x, self.rect.y - self.offset_y))
        else:
            screen.blit(self.image, (self.rect.x - self.offset_x, self.rect.y - self.offset_y))
