import pygame,sys ,random,time,os
from pygame.locals import*

pygame.init()

GAMEWINDOW=pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Closest pair')
obj=pygame.font.Font('freesansbold.ttf',35)

black=( 0, 0, 0)
red=(255, 0, 0)
grey=(169,169,169)
white = (255, 255, 255)
blue = (0, 0 , 255)


points = []
def terminate():
    pygame.quit()
    sys.exit()

def draw_grid(l):
    GAMEWINDOW.fill(white)    
    a = 0
    b = 0
    c = 0
    d = 800
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a,b), (c,d), 1)
        a+=16
        c+=16
        
    a = 0
    b = 0
    c = 800
    d = 0
    for i in range(50):
        pygame.draw.line(GAMEWINDOW, grey, (a,b), (c,d), 1)
        b+=16
        d+=16
        
    for i in l:    
        pygame.draw.rect(GAMEWINDOW,red,(i[0]*16, abs((49 - i[1])*16), 16, 16))

def display_points(l):
    obj=pygame.font.Font('freesansbold.ttf',20)
    
    for i in l:
        s = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        surf=obj.render(s,True,black)
        GAMEWINDOW.blit(surf,(i[0]*16 + 16,abs((49 - i[1])*16 + 16)))

def draw_line(a, b, color):

    x1 = a[0]; y1 = a[1]
    x2 = b[0]; y2 = b[1]
    y1 = abs(50 - y1)
    y2 = abs(50 - y2)
    pygame.draw.line(GAMEWINDOW, color, (x1*16,y1*16), (x2*16,y2*16), 5)

def sleep():
    t_end = time.time() + 2
    while time.time() < t_end:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate() 
        
        pygame.display.update() 

def points_with_distance(a, b, l1, l2, l3):
    draw_grid(points)
    display_points(points)
    obj1=pygame.font.Font('freesansbold.ttf',20)
    s = 'D = ' + str(round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2))
    surf=obj1.render(s,True,red)
    dist_x_coor = (a[0]*16 + b[0]*16)//2
    dist_y_coor = (800 - a[1]*16 + 800 - b[1]*16)//2
    GAMEWINDOW.blit(surf,(dist_x_coor, dist_y_coor))
    
    draw_line(a,b, (0, 255, 0))
    draw_line((l1, 0), (l1, 50), blue)
    draw_line([l2, 0], [l2, 50], blue)

    sleep()
   

draw_grid(points)
display_points(points)

############################################################################################################

def call_pygame(a, b, l1, l2, l3):
    points_with_distance(a, b, l1, l2, l3)
        
def distance(a, b):
    return ( (b[1] - a[1])**2 + (b[0] - a[0])**2 )**(1/2)

def bruteForce(points, n, mid):
    obj1=pygame.font.Font('freesansbold.ttf',20)
    s = 'n = ' + str(n)
    surf=obj1.render(s,True,black)
    GAMEWINDOW.blit(surf,(810, 10))
    s = 'So, Bruteforce'
    surf=obj1.render(s,True,black)
    GAMEWINDOW.blit(surf,(810, 50))
    mini = sys.maxsize
    sleep()
    for i in range(n-1):
        for j in range(i+1, n):
            call_pygame(points[i], points[j], mid,-1,-1)

            if(distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini            
    
def stripClosest(points, n, prevMin, left, right):
    obj1=pygame.font.Font('freesansbold.ttf',20)
    s = 'Strip Closest'
    surf=obj1.render(s,True,black)
    GAMEWINDOW.blit(surf,(810, 10))
    sleep()
    
    mini = prevMin
    for i in range(n-1):
        for j in range(i+1, n):
            if points[j][1] - points[i][1] > mini:
                break
            call_pygame(points[i], points[j], left, right, -1)
            
            if(distance(points[i], points[j]) < mini):
                mini = distance(points[i], points[j])
    return mini            
def closestPair(x_sorted, y_sorted, n, midpoint):
    if n<=3:
        return bruteForce(x_sorted, n, midpoint)
    
    middle = n//2
    midpoint = x_sorted[middle]

    draw_grid(points)
    display_points(points)
    draw_line((midpoint[0], 0), (midpoint[0], 50), blue)
    sleep()
    
    left_x = x_sorted[ : middle]
    right_x = x_sorted[middle : ]
    
    left_y = y_sorted[ : middle]
    right_y = y_sorted[middle : ]
    
    dl = closestPair(left_x, left_y, middle, midpoint[0])
    dr = closestPair(right_x, right_y, n-middle, midpoint[0])

    d = min(dl, dr)

    strip = []
    for i in range(n):
        if abs(y_sorted[i][0] - midpoint[0]) < d:
            strip.append(y_sorted[i])
            
    strip_left = midpoint[0] - d
    strip_right  = midpoint[0] + d
    
    if strip_left<0:
        strip_left = 0
    if strip_right>800:
        strip_right = 800
    
    return stripClosest(strip, len(strip), d, strip_left, strip_right)       

def number_input_intro():
    k=1
    num = '0'
    while k:
        
        GAMEWINDOW.fill(white)
        pygame.draw.rect(GAMEWINDOW, [0, 0, 255], [390, 90 , 250, 40] , 3)
        obj1=pygame.font.Font('freesansbold.ttf',20)
        s = 'Enter a Number : ' + num
        surf=obj1.render(s,True,black)
        GAMEWINDOW.blit(surf,(400, 100))

        s = 'Press enter after entering the number of inputs!'
        surf=obj1.render(s,True,black)
        GAMEWINDOW.blit(surf,(300, 150))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                inp = event.key-256
                
                if inp== -253 or inp==15:
                    k=0
                    
                if k and inp>=0 and inp<=9:
                    num = str(int(num)*10 + inp)
                elif k and inp == -248 and len(num):
                    num = num[:-1]
                    if not len(num):
                        num = '0'
            if event.type == QUIT:
                terminate()
    return int(num) 
def get_random_points(f):
    n = number_input_intro()       
    while n:

        points = []
        for i in range(n):
            x = random.randint(0,49)
            y = random.randint(0,49)
            points.append((x,y))
            f =1
        while f:
            draw_grid(points)
            display_points(points)
            pygame.draw.rect(GAMEWINDOW, [0, 0, 255], [803, 97 , 196, 30] , 3)
            obj1=pygame.font.Font('freesansbold.ttf',20)
            s = 'New Random points'
            surf=obj1.render(s,True,black)
            GAMEWINDOW.blit(surf,(805, 100))
            pygame.draw.rect(GAMEWINDOW, [0, 0, 255], [803, 397, 196, 55] , 3)
            obj1=pygame.font.Font('freesansbold.ttf',20)
            s = 'Click here to '
            surf=obj1.render(s,True,black)
            GAMEWINDOW.blit(surf,(810, 400))

            obj1=pygame.font.Font('freesansbold.ttf',20)
            s = 'find closest'
            surf=obj1.render(s,True,black)
            GAMEWINDOW.blit(surf,(810, 430))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                if event.type == QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    xpos,ypos = event.pos
                    if xpos>800 and ypos>400 and ypos<430:
                       return points
                    if xpos>800 and ypos>100 and ypos<130:
                       f=0
    return []            
# If you want to give specific points, comment the below line and uncomment the next points list and enter you points in the points list
points = get_random_points(1)

#points = [(20, 43), (21, 21), (28, 39), (2, 10), (11, 47), (35, 46), (36, 3), (44, 41), (13, 5), (40, 19)]

if not len(points):
    terminate()

      

n = len(points)
x_sorted = sorted(points)
y_sorted = sorted(points, key = lambda x : x[1])

minimum = closestPair(x_sorted, y_sorted, n, -1)
print(minimum)


while 1:
    obj1=pygame.font.Font('freesansbold.ttf',20)
    s = 'overall min = ' + str(round(minimum,2))
    surf=obj1.render(s,True,black)
    GAMEWINDOW.blit(surf,(810, 100))
    sleep()
