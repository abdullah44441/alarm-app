import pygame
import sys
from datetime import datetime

pygame.init()
pygame.mixer.init()

# Load and set volume
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(1.0)

# Create a screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Alarm app")

# Variables
white = (255, 255, 255)
red = (255, 0, 0)
alarm = ""
clock = pygame.time.Clock()
Fps = 60

# Fonts
Font = pygame.font.SysFont("comicsansms",55)
Font2 = pygame.font.SysFont("comicsansms", 40)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    text_rect = img.get_rect(center=(x, y))
    screen.blit(img, text_rect)

def draw_alarm(text, font, color, x, y):
    img = font.render(text, True, color)
    text_rect = img.get_rect(topleft=(x, y))
    screen.blit(img, text_rect)

# Loop
run = True
while run:
    screen.fill(white)
    
    width, height = screen.get_size()
    time = datetime.now().strftime("%H:%M")
    
    draw_text("Current timing: "+time, Font, red, width // 2, height // 3)  # Centered horizontally, placed near top
    draw_alarm("Set alarm: " + alarm, Font2, red, 20, height - 60)  # Positioned near bottom left
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.TEXTINPUT:
            alarm += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                alarm = alarm[:-1]    
        if time == alarm:
            pygame.mixer.music.play(1) 
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

pygame.quit()