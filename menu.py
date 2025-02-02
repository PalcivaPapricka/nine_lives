import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nine Lives")

# Load background image
background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load default font
title_font = pygame.font.SysFont(None, 72)  # Default font, size 72
button_font = pygame.font.SysFont(None, 36)  # Default font, size 36

# Colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
HOVER_COLOR = (100, 100, 100)

# Create title text
title_text = title_font.render("Nine Lives", True, WHITE)
title_text2 = title_font.render("Well done", True, WHITE)
title_x = (SCREEN_WIDTH - title_text.get_width()) // 2  # Center title
title_y = 150

# Button properties
button_width = 300
button_height = 60
button_spacing = 20  # Space between buttons
button_x = (SCREEN_WIDTH - button_width) // 2  # Center buttons horizontally
button_y = 400  # Start position for first button

buttons = [
    {"text": "Play", "rect": pygame.Rect(button_x, button_y, button_width, button_height)},
    {"text": "Quit", "rect": pygame.Rect(button_x, button_y + button_height + button_spacing, button_width, button_height)}
]

buttons2 = [
    {"text": "Play-again", "rect": pygame.Rect(button_x, button_y, button_width, button_height)},
    {"text": "Quit", "rect": pygame.Rect(button_x, button_y + button_height + button_spacing, button_width, button_height)}
]


# Main menu loop
def main_menu():
    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text, (title_x, title_y))

        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            color = HOVER_COLOR if button["rect"].collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, button["rect"], border_radius=10)

            # Render button text
            text_surface = button_font.render(button["text"], True, WHITE)
            text_x = button["rect"].x + (button["rect"].width - text_surface.get_width()) // 2
            text_y = button["rect"].y + (button["rect"].height - text_surface.get_height()) // 2
            screen.blit(text_surface, (text_x, text_y))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Play":
                            return  # Transition to game
                        elif button["text"] == "Quit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()


def end_menu():
    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text2, (title_x, title_y))

        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons2:
            color = HOVER_COLOR if button["rect"].collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, button["rect"], border_radius=10)

            # Render button text
            text_surface = button_font.render(button["text"], True, WHITE)
            text_x = button["rect"].x + (button["rect"].width - text_surface.get_width()) // 2
            text_y = button["rect"].y + (button["rect"].height - text_surface.get_height()) // 2
            screen.blit(text_surface, (text_x, text_y))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons2:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Play-again":
                            return  # Transition to game
                        elif button["text"] == "Quit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()