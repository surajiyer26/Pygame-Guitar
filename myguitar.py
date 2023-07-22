import pygame
from pygame import mixer
import sys

pygame.init()
mixer.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('PyGuitar')
clock = pygame.time.Clock()

guitar_surf = pygame.image.load('guitar.jpeg').convert()

e_string_surf = pygame.Surface((10, 480))
e_string_surf.fill('Grey')
e_string_rect = e_string_surf.get_rect(topleft = (150, 0))

a_string_surf = pygame.Surface((9, 480))
a_string_surf.fill('Grey')
a_string_rect = a_string_surf.get_rect(topleft = (190, 0))

d_string_surf = pygame.Surface((8, 480))
d_string_surf.fill('Grey')
d_string_rect = d_string_surf.get_rect(topleft = (230, 0))

g_string_surf = pygame.Surface((6, 480))
g_string_surf.fill('Grey')
g_string_rect = g_string_surf.get_rect(topleft = (260, 0))

b_string_surf = pygame.Surface((4, 480))
b_string_surf.fill('Grey')
b_string_rect = b_string_surf.get_rect(topleft = (290, 0))

E_string_surf = pygame.Surface((3, 480))
E_string_surf.fill('Grey')
E_string_rect = E_string_surf.get_rect(topleft = (320, 0))

e_vibration = 0
a_vibration = 0
d_vibration = 0
g_vibration = 0
b_vibration = 0
E_vibration = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if e_string_rect.collidepoint(event.pos):
                e_vibration = 14
                mixer.music.load('e.wav')
                mixer.music.play()
            if a_string_rect.collidepoint(event.pos):
                a_vibration = 14
                mixer.music.load('a.wav')
                mixer.music.play()
            if d_string_rect.collidepoint(event.pos):
                d_vibration = 14
                mixer.music.load('d.wav')
                mixer.music.play()
            if g_string_rect.collidepoint(event.pos):
                g_vibration = 14
                mixer.music.load('g.wav')
                mixer.music.play()
            if b_string_rect.collidepoint(event.pos):
                b_vibration = 14
                mixer.music.load('b.wav')
                mixer.music.play()
            if E_string_rect.collidepoint(event.pos):
                E_vibration = 14
                mixer.music.load('ee.wav')
                mixer.music.play()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == '1':
                e_vibration = 14
                mixer.music.load('e.wav')
                mixer.music.play()
            if key == '2':
                a_vibration = 14
                mixer.music.load('a.wav')
                mixer.music.play()
            if key == '3':
                d_vibration = 14
                mixer.music.load('d.wav')
                mixer.music.play()
            if key == '4':
                g_vibration = 14
                mixer.music.load('g.wav')
                mixer.music.play()
            if key == '5':
                b_vibration = 14
                mixer.music.load('b.wav')
                mixer.music.play()
            if key == '6':
                E_vibration = 14
                mixer.music.load('ee.wav')
                mixer.music.play()

            if key == 'a':
                e_vibration = 14
                mixer.music.load('e.wav')
                mixer.music.play()
            if key == 's': 
                a_vibration = 14
                mixer.music.load('a.wav')
                mixer.music.play()
            if key == 'd':
                d_vibration = 14
                mixer.music.load('d.wav')
                mixer.music.play()
            if key == 'f':
                g_vibration = 14
                mixer.music.load('g.wav')
                mixer.music.play()
            if key == 'g':
                b_vibration = 14
                mixer.music.load('b.wav')
                mixer.music.play()
            if key == 'h':
                E_vibration = 14
                mixer.music.load('ee.wav')
                mixer.music.play()

    screen.blit(guitar_surf, (0, 0))

    e_string_rect.x += e_vibration
    screen.blit(e_string_surf, e_string_rect)
    e_string_rect.x -= e_vibration
    if e_vibration > 0:
        e_vibration = -1 * e_vibration
    elif e_vibration < 0:
        e_vibration = -1 * e_vibration
        e_vibration -= 1

    a_string_rect.x += a_vibration
    screen.blit(a_string_surf, a_string_rect)
    a_string_rect.x -= a_vibration
    if a_vibration > 0:
        a_vibration = -1 * a_vibration
    elif a_vibration < 0:
        a_vibration = -1 * a_vibration
        a_vibration -= 1

    d_string_rect.x += d_vibration
    screen.blit(d_string_surf, d_string_rect)
    d_string_rect.x -= d_vibration
    if d_vibration > 0:
        d_vibration = -1 * d_vibration
    elif d_vibration < 0:
        d_vibration = -1 * d_vibration
        d_vibration -= 1

    g_string_rect.x += g_vibration
    screen.blit(g_string_surf, g_string_rect)
    g_string_rect.x -= g_vibration
    if g_vibration > 0:
        g_vibration = -1 * g_vibration
    elif g_vibration < 0:
        g_vibration = -1 * g_vibration
        g_vibration -= 1

    b_string_rect.x += b_vibration
    screen.blit(b_string_surf, b_string_rect)
    b_string_rect.x -= b_vibration
    if b_vibration > 0:
        b_vibration = -1 * b_vibration
    elif b_vibration < 0:
        b_vibration = -1 * b_vibration
        b_vibration -= 1

    E_string_rect.x += E_vibration
    screen.blit(E_string_surf, E_string_rect)
    E_string_rect.x -= E_vibration
    if E_vibration > 0:
        E_vibration = -1 * E_vibration
    elif E_vibration < 0:
        E_vibration = -1 * E_vibration
        E_vibration -= 1

    pygame.display.update()
    clock.tick(60)
