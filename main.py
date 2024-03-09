# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
square_width = 900
screen_height = 900
screen = pygame.display.set_mode((square_width, screen_height))
clock = pygame.time.Clock()
running = True

def generate_starting_postiion():
    range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*range), random.randrange(*range)]

def reset():
    target.center = generate_starting_postiion()
    snake_pixel.center = generate_starting_postiion()
    return [snake_pixel.copy()]

def boundaryConditionBreak():
    return snake_pixel.bottom > screen_height or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width

#  playground
pixel_width = 50

# snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_postiion()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

# target:
target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_postiion()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    # RENDER YOUR GAME HERE
    
    if boundaryConditionBreak():
        snake_length = 1
        snake = reset()

    if snake_pixel.center == target.center:
        target.center = generate_starting_postiion()
        snake_length += 1
        snake.append(snake_pixel.copy())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, - pixel_width)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_LEFT]:
        snake_direction = ( - pixel_width, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "yellow", snake_part)

    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()