import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 60, 100
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()

# Load car image
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

# Load obstacle image
obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = pygame.transform.scale(obstacle_img, (CAR_WIDTH, CAR_HEIGHT))

# Define car properties
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20
car_speed = 5

# Obstacle properties
obstacle_width = 60
obstacle_height = 100
obstacle_speed = 3
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height

def draw_car(x, y):
    window.blit(car_img, (x, y))

def draw_obstacle(x, y):
    window.blit(obstacle_img, (x, y))

def game_over():
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over", True, RED)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += car_speed

    # Move the obstacle down
    obstacle_y += obstacle_speed

    # Check for collision with the car
    if car_y < obstacle_y + obstacle_height:
        if (car_x > obstacle_x and car_x < obstacle_x + obstacle_width) or (car_x + CAR_WIDTH > obstacle_x and car_x + CAR_WIDTH < obstacle_x + obstacle_width):
            game_over()
            break

    window.fill(WHITE)
    draw_obstacle(obstacle_x, obstacle_y)
    draw_car(car_x, car_y)

    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height

    pygame.display.update()
    clock.tick(60)

pygame.quit()
