'''
1)import
2)take width,height and now we need to display display with w,h and caption for it
3)main function creation and run a while loop
'''
import math
import random
import pygame
import time
pygame.init()

w,h = 800,600 #2 # width , height of display 
TARGET_INCREMENT = 400 # in crement in millie second
TARGET_EVENT = pygame.USEREVENT #creating custom event

TARGET_PADDING = 30
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans",24)


Lives = 3

BG_COLOR = (0,25,40) #This can be picked in 0-255 0-red, 25-blue , 40-green

WIN = pygame.display.set_mode((w,h)) #2 #displaying in built pygame display with w,h size
pygame.display.set_caption("AIM Building") #2 #display name

class Target:
    MAX_SIZE = 30 #maximun radius
    GROWTH_RATE = 0.2 # radius increment per certain time
    color = "red"
    second_color = "white"

    def __init__(self,x,y): #x,y are cordinates in display
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    
    def update(self): # circle radius increment and decrement
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self,win): # Drawing a circle with white and red colour from 1 , 0.8 , 0.6 , 0.4
        pygame.draw.circle(win,self.color,(self.x,self.y),self.size)
        pygame.draw.circle(win,self.second_color,(self.x,self.y),self.size*0.8)
        pygame.draw.circle(win,self.color,(self.x,self.y),self.size*0.6)
        pygame.draw.circle(win,self.second_color,(self.x,self.y),self.size*0.4)

    def collide(self,x,y):
        dis = math.sqrt((self.x-x)**2+(self.y-y)**2)
        return dis<=self.size


def draw(win,targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win) #this draw is class draw function

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win,elapsed_time,targets_pressed,misses):
    pygame.draw.rect(win,"grey",(0,0,w,TOP_BAR_HEIGHT))

    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}" , 1 , "black")

    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed: {speed}t/s" , 1 , "black")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}" , 1 , "black")

    lives_label = LABEL_FONT.render(f"lives: {Lives - misses}" , 1 , "black")

    win.blit(time_label,(50,5))
    win.blit(speed_label,(270,5))
    win.blit(hits_label,(500,5))
    win.blit(lives_label,(650,5))

def end_screen(win,elapsed_time,targets_pressed,clicks):
    win.fill(BG_COLOR)

    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}" , 1 , "white")

    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed: {speed}t/s" , 1 , "white")

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}" , 1 , "white")

    accuracy = round(targets_pressed / clicks * 100 , 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%" , 1 , "white")

    win.blit(time_label,(get_middle(time_label),100))
    win.blit(speed_label,(get_middle(speed_label),200))
    win.blit(hits_label,(get_middle(hits_label),300))
    win.blit(accuracy_label,(get_middle(accuracy_label),400))

    pygame.display.update()

    run = True
    while run:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return w/2 - surface.get_width()/2

def main():
    run = True

    targets = [] 
    clicks = 0
    targets_pressed = 0
    start_time = time.time()
    misses = 0

    

    clock = pygame.time.Clock() #clock for circle apperance in frame rates
    pygame.time.set_timer(TARGET_EVENT,TARGET_INCREMENT) # running custom event called target event for target increment seconds

    while run:
        clock.tick(60)  # frames speed
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time
        

        for event in pygame.event.get(): #loop in event
            if event.type == pygame.QUIT: #if quit quit
                run = False
                break
            if event.type == TARGET_EVENT: # x,y cordinates picking in random asined value
                x = random.randint(TARGET_PADDING , w-TARGET_PADDING) 
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT,h-TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets: #updating target in targets
            target.update()

            if target.size <= 0 :
                targets.remove(target)
                misses += 1
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                targets_pressed += 1

        if misses>=Lives:
            end_screen(WIN,elapsed_time,targets_pressed,clicks)
            
        draw(WIN,targets) #calling draw function to draw circle on display
        draw_top_bar(WIN,elapsed_time,targets_pressed,misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()