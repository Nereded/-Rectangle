import pygame
import sys


def is_valid_input(input_str):
    try:
        int_values = [int(val) for val in input_str.split()]
        return len(int_values) == 2
    except ValueError:
        return False


input_str = input("Введите два целых числа, разделенных пробелом: ")
if not is_valid_input(input_str):
    print("Неправильный формат ввода")
    sys.exit()
width, height = map(int, input_str.split())
pygame.init()
window = pygame.display.set_mode((width, height))
black = (0, 0, 0)
red = (255, 0, 0)
window.fill(black)
rect_width = width - 2
rect_height = height - 2
pygame.draw.rect(window, red, (1, 1, rect_width, rect_height))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
