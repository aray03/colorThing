from turtle import Screen
import pygame
import time
import random
import math

from tqdm import tqdm



#def show(image):
#    screen = pygame.display.get_surface()
 #   screen.fill((255,255,0))
  #  screen.blit(image, (0, 0))
#

def main():

   # pygame.init()


   # pygame.display.set_mode ((255, 255))
  #  surface = pygame.Surface ((255, 255))
  #  pygame.display.flip ()
    
  #  show(surface)
   
   # import pygame

    pygame.init()
    width = 1
    height = 1
    
    screen = pygame.display.set_mode((width, height ))
    penguinImage = pygame.image.load("goomba.png").convert()
    height = penguinImage.get_height()
    width = penguinImage.get_width()
    
    
  #  width=350
  #  height=300
    screen = pygame.display.set_mode((width, height ))
    pygame.display.set_caption('Display an image')
    penguinImage = pygame.image.load("goomba.png").convert()

  #  penguinImage.get_height

  #  x = 20; # x coordnate of image
  #  y = 30; # y coordinate of image
    screen.blit(penguinImage, (0,0)) # paint to screen
    pygame.display.flip() # paint screen one time

    pxarray = pygame.PixelArray(screen)

 #   pxarray[::1, :] = (0, 0, 0)
  #  pxarray[::2] = (0, 0, 0)
    
  #  for z in range(100):
   #     pxarray[x+z, y+z] = (255, 0, 255)

   # print(pxarray.extract())
    
    r = 0
    g = 0
    b = 0
    
    rgbList = set()
    
    for ix in tqdm(range(width)):
        for iy in range(height):
            rgbLoop = True
            for curCol in rgbList:
                if pxarray[ix, iy] == screen.map_rgb((curCol)):
                    rgbLoop = False
                
            if rgbLoop:
                if pxarray[ix, iy] == screen.map_rgb((255, 255, 255)):
                    rgbList.add((255, 255, 255)) 
                    print("Black")
                if pxarray[ix, iy] == screen.map_rgb((0, 0, 0)):
                    rgbList.add((0, 0, 0)) 
                    print("White")
                    
                for r in range(256):
                    for g in range(256):
                        for b in range(256):
                            if pxarray[ix, iy] == screen.map_rgb((r, g, b)):
                                rgbList.add((r, g, b)) 
                                print(r,g,b)
                                rgbLoop = False
                                break
                            if not rgbLoop:
                                break
                        if not rgbLoop:
                                break
                    if not rgbLoop:
                                break
    
    for i in range(len(rgbList)):
        print(rgbList.pop())
    
    print(rgbList)
    
   # if pxarray[x+3, y+3] == screen.map_rgb((0, 0, 255)):
   #    print("Helo there")
   # elif pxarray[x+3, y+3] == screen.map_rgb((255, 0, 255)):
   #    print("Gneral Kenobi")
   

    pygame.display.flip()

    running = True
    while (running): # loop listening for end of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #loop over, quite pygame
    pygame.quit()
    
    
    
    
main()