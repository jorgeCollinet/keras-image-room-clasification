#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys, pygame, time, os
from pygame.locals import *
 
# Constants
WIDTH = 840
HEIGHT = 580
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
UNLABELED_DIR = 'unlabelled'
LABELED_DIR = 'labelled'

# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
        try: 
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        except pygame.error as message:
            print("Error in file: " + filename)
            raise message
        image = image.convert()
        if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
        return image

def text_objects(text, text_color=black):
    font = pygame.font.Font("freesansbold.ttf",20)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def button(screen, msg, x, y, w, h, ic, ac, destination_folder):
    global background_image
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        textSurf, textRect = text_objects(msg, white)
        if click[0]==1:
            org = get_first_file(UNLABELED_DIR)
            dest = destination_folder + '/' + org.split('/')[-1]
            move_file(org, dest) 
            background_image = get_first_unlabeled_photo(UNLABELED_DIR)
            screen.blit(background_image, (0, 0))
            print("apreto -> " + destination_folder)
            time.sleep(0.5) 
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        textSurf, textRect = text_objects(msg, black)
    
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def get_first_file(path):
    return path +'/'+ os.listdir(path)[0]

def get_first_unlabeled_photo(path):
    try :
        return load_image(get_first_file(path))
    except:
        os.remove(get_first_file(path))
        return load_image(get_first_file(path))
     
def move_file(org, dest):
	os.rename(org, dest)

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("BrotherEngine with Pygame")
    background_image = get_first_unlabeled_photo(UNLABELED_DIR)
    screen.blit(background_image, (0, 0))

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        button(screen, msg='bathroom',	x=40,  y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/bathroom')
        button(screen, msg='living',	x=140, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/living')
        button(screen, msg='exterior',	x=240, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/exterior')
        button(screen, msg='kitchen',	x=340, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/kitchen')
        button(screen, msg='bedroom',	x=440, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/bedroom')        
        button(screen, msg='plane',	x=540, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/plane')
        button(screen, msg='publicity',	x=640, y=500, w=90, h=30, ic=red, ac=20, destination_folder=LABELED_DIR + '/publicity')
        button(screen, msg='other',	x=740, y=500, w=90, h=30, ic=red, ac=20, destination_folder='./other') # This wont be classified
        
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
