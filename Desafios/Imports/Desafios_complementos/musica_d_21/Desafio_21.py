import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer_music.load('smoke.mp3')
pygame.mixer_music.play(loops=0, start=0.0)

pygame.event.wait()
