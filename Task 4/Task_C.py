import pygame
import time
import random

pygame.init()


width = 600
height = 400
size = 20
win = pygame.display.set_mode((600,400))

pygame.display.set_caption("SNAKE GAME")

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',25)


def Snake_draw(snake_blocks):
    for blocks in snake_blocks :
        pygame.draw.rect(win,'green',(*blocks , size, size))
        
def Score(score):
    score_txt = font.render("Score : " + str(score) , True, 'blue')
    win.blit(score_txt,[10,10])
    
def game_loop():
    x,y = width // 2, height // 2
    dx,dy = 0,0 
    
    snake = [[x,y]]
    
    while True :
        point_x = random.randrange(0,width, size)
        point_y = random.randrange(0, height, size)
        
        if[point_x, point_y] not in snake :
            break
    
    score = 0
    running = True
    
    while running :
        if score < 25 :
            clock.tick(7 + score // 5)
        else :
            clock.tick(7+5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0 :
                    dx, dy = -size, 0
                    
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx,dy = size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx,dy = 0, -size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx,dy = 0, size
                    
        
        x += dx
        y+= dy
        
        new_head = [x,y]
        
        if(x<0 or x>=width or y<0 or y>= height or (new_head in snake and dx != 0 and dy != 0) ):
            break
        
        
        snake.insert(0,new_head) 
        
        if x== point_x and y == point_y :
            
            score += 1
            
            point_x = random.randrange(0,width,size)
            point_y = random.randrange(0,height,size)
            
        else:
            snake.pop()
        
        win.fill('black')
        
        Snake_draw(snake)
        pygame.draw.circle(win,'red',(point_x + size//2,point_y + size//2),size//2)
        Score(score)
        pygame.display.update()
        
    win.fill('black')
    
    msg = font.render("GAME OVER! SCORE : " + str(score), True, 'white')
    win.blit(msg,[width//6, height//2])
    pygame.display.update()
    time.sleep(10)
    pygame.quit()    
        
        
game_loop()























