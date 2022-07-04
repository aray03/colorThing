import pygame
import time
import random
import math

#Pygame Start Variables
pygame.init()
clock = pygame.time.Clock()
#display_width = 800
#display_height = 600

display_width = 1800
display_height = 900


white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Tetris")

randcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


def block(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def xWork(x):
    if(x < 0):
        return 0
    elif(x > display_width):
        return display_width
    else:
        return x

def yWork(y):
  #  y+=random.randint(-1,1)*10
    if(y < 0):
        return 0
    elif(y > display_height):
        return display_height
    else:
        return y

def game_loop():
    gameDisplay.fill(black)
  #  print("Hello")
    dotS = 10

    rows, cols = ((int)(display_width/dotS), (int)(display_height/dotS))
  #  print(rows)

   
   # arr = [ [(0, 0, 0, 0)]*cols for i in range(rows)]
    arr = [ [0]*cols for i in range(rows)]
   # print(arr)

    x = 10
    y = 10
    x1 = display_width - 10
    y1 = display_height - 10
    x2 = 10
    y2 = display_height - 10
    x3 = display_width - 10
    y3 = 10
    x4 = 10
    y4 = display_height/2
    x5 = display_width - 10
    y5 = display_height/2
    x6 = 20
    y6 = 20
    check = 0
    while True:
        
        
        randcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
        block(x6, y6, dotS, dotS, white)
        block(x1, y1, dotS, dotS, white)
        block(x2, y2, dotS, dotS, white)
        block(x3, y3, dotS, dotS, white)
        block(x4, y4, dotS, dotS, white)
        block(x5, y5, dotS, dotS, white)
        pygame.display.update()
       # clock.tick(60)
        
     
        #This part adds the various colors to a 2D List to keep track of them all.
        block(x6, y6, dotS, dotS, (255, 0, 0))
        try:
            arr[(int)(math.fabs(x6/dotS))].pop((int)(math.fabs(y6/dotS)))
            arr[(int)(x6/dotS)].insert(((int)(y6/dotS)), "red")
        except:
            pass
        block(x1, y1, dotS, dotS, (255, 120, 0))
        try:
            arr[(int)(math.fabs(x1/dotS))].pop((int)(math.fabs(y1/dotS)))
            arr[(int)(x1/dotS)].insert(((int)(y1/dotS)), "orange")
        except:
            pass
        block(x2, y2, dotS, dotS, (255, 255, 0))
        try:
            arr[(int)(math.fabs(x2/dotS))].pop((int)(math.fabs(y2/dotS)))
            arr[(int)(x2/dotS)].insert(((int)(y2/dotS)), "yellow")
        except:
            pass
        block(x3, y3, dotS, dotS, (0, 255, 0))
        try:
            arr[(int)(math.fabs(x3/dotS))].pop((int)(math.fabs(y3/dotS)))
            arr[(int)(x3/dotS)].insert(((int)(y3/dotS)), "green")
        except:
            pass
        block(x4, y4, dotS, dotS, (0, 0, 255))
        try:
            arr[(int)(math.fabs(x4/dotS))].pop((int)(math.fabs(y4/dotS)))
            arr[(int)(x4/dotS)].insert(((int)(y4/dotS)), "blue")
        except:
           pass
        block(x5, y5, dotS, dotS, (255, 0, 130))
        try:
            arr[(int)(math.fabs(x5/dotS))].pop((int)(math.fabs(y5/dotS)))
            arr[(int)(x5/dotS)].insert(((int)(y5/dotS)), "purple")
        except:
            pass
        #print(arr[0])

        x6+=random.randint(-1,1)*dotS
        x6 = xWork(x6)

        y6+=random.randint(-1,1)*dotS
        y6 = yWork(y6)

        x1+=random.randint(-1,1)*dotS
        x1 = xWork(x1)

        y1+=random.randint(-1,1)*dotS
        y1 = yWork(y1)

        x2+=random.randint(-1,1)*dotS
        x2 = xWork(x2)

        y2+=random.randint(-1,1)*dotS
        y2 = yWork(y2)

        x3+=random.randint(-1,1)*dotS
        x3 = xWork(x3)

        y3+=random.randint(-1,1)*dotS
        y3 = yWork(y3)

        x4+=random.randint(-1,1)*dotS
        x4 = xWork(x4)

        y4+=random.randint(-1,1)*dotS
        y4 = yWork(y4)

        x5+=random.randint(-1,1)*dotS
        x5 = xWork(x5)

        y5+=random.randint(-1,1)*dotS
        y5 = yWork(y5)

        #Color checker
        check+=1
        if check % 1000 == 0:
            pygame.display.update()
            clock.tick(1)
        if check % 100000 == 0:
        #    arr[(int)(x/dotS)].insert(((int)(y/dotS)), "red")
            
            re = 0
            ora = 0
            yel = 0
            gre = 0
            blu = 0
            pup = 0
            zero = 0
         #   print("Hello there")
            for i in range((int)(display_width/dotS)):
             #   for z in range[((int)(display_height/dotS))]:
                for z in range((int)(display_height/dotS)):  
                   # print("Hello thereafdadsfasdf")
                    test = arr[i][z]
                    if test == 'red':
                        re+=1
                    elif test == 'orange':
                        ora+=1
                    elif test == 'yellow':
                        yel+=1
                    elif test == 'green':
                        gre+=1
                    elif test == 'blue':
                        blu+=1
                    elif test == 'purple':
                        pup+=1
                    elif test == 0:
                        zero+=1
                        
                        
            totalColor = re+ora+yel+gre+blu+pup
            print("\n\n\n---Without Empty Space------------")
            print("Red:", re, (str)(round(re/totalColor, 3)*100) + "%")
            print("Orange:", ora, (str)(round(ora/totalColor, 3)*100) + "%")
            print("Yellow:", yel, (str)(round(yel/totalColor, 3)*100) + "%")
            print("Green:", gre, (str)(round(gre/totalColor, 3)*100) + "%")
            print("Blue:", blu, (str)(round(blu/totalColor, 3)*100) + "%")
            print("Purple:", pup, (str)(round(pup/totalColor, 3)*100) + "%")
           
            
            totalColor = re+ora+yel+gre+blu+pup+zero
            print("\n\n\n---With Empty Space------------")
            print("Red:", re, (str)(round(re/totalColor, 3)*100) + "%")
            print("Orange:", ora, (str)(round(ora/totalColor, 3)*100) + "%")
            print("Yellow:", yel, (str)(round(yel/totalColor, 3)*100) + "%")
            print("Green:", gre, (str)(round(gre/totalColor, 3)*100) + "%")
            print("Blue:", blu, (str)(round(blu/totalColor, 3)*100) + "%")
            print("Purple:", pup, (str)(round(pup/totalColor, 3)*100) + "%")
            print("Empty:", zero, (str)(round(zero/totalColor, 3)*100) + "%")
            
           # arr[]
            
           # arr[]
            
     #   for i in range((int)(display_height/dotS)):
       #     for z in range((int)(display_width/dotS)):
            
            #  if(pygame.Surface.get_at(gameDisplay, (i,10)) == (255, 0, 0, 255)):
                #  print("Red")
            #    if(pygame.Surface.get_at(gameDisplay, (i,z)) == (255, 120, 0, 255)):
            #        print("Orange")
             #       time.sleep(10)
            # print(pygame.Surface.get_at(gameDisplay, (600,400)))


        #time.sleep(1)
game_loop()
pygame.quit()
quit()
