import pygame , sys , random


#INITIAL
pygame.init()

screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
width , height = screen.get_size()
pygame.display.set_caption("Missionaries and Cannibals")