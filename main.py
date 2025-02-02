import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT
from player import Player
from world import World, world_data1, world_data2, world_data3, water_group , grave_group, rat_group, spike_group
from menu import main_menu, end_menu
pygame.mixer.init()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nine Lives")
clock = pygame.time.Clock()
current_level = world_data1
bg_img = pygame.image.load("img/background.png")
sound_effect = pygame.mixer.Sound("img/gg.mp3")
main_theme = pygame.mixer.Sound("img/main.mp3")

def reset_position():
    global player
    player = Player(100, SCREEN_HEIGHT - 150, 9)

def reset_game():
    global world, lava_group , grave_group
    reset_position()
    water_group.empty()
    grave_group.empty()
    rat_group.empty()
    spike_group.empty()
    world = World(current_level)

def change_level():
    global current_level
    if current_level == world_data1:
        current_level = world_data2
    elif current_level == world_data2:
        current_level = world_data3
    else:
        current_level = world_data1

    reset_game()
    sound_effect.play()

main_theme.play(-1)
main_theme.set_volume(0.05)
main_menu()
reset_game()

running = True
while running:
    screen.blit(bg_img, (0, 0))
    world.draw(screen)
    player.update(world)
    player.draw()
    water_group.draw(screen)
    grave_group.draw(screen)
    rat_group.draw(screen)
    spike_group.draw(screen)

    lives_text = FONT.render(f"Lives: {player.lives}", True, (255, 255, 255))
    screen.blit(lives_text, (SCREEN_WIDTH - 100, 20))

    if player.lives <= 0:
        reset_game()

    if player.end == True:
        if current_level == world_data3:
            main_theme.stop()
            end_menu()
            change_level()
            player.end = False
            main_theme.play(-1)
        else:
            change_level()
            player.end = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_n:
                change_level()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
