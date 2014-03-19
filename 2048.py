from __future__ import division
import pygame

class Tile(object):
    def __init__(self, x, y, draw_size, value=0):
        self.x = x
        self.y = y
        self.draw_size = draw_size
        self.value = value

class Board(object):
    def __init__(self,x,y,draw_size):
        self.test=0
        self.draw_size = draw_size
        self.x = x
        self.y = y
        self.tiles = [Tile(x, y, self.draw_size / 4, 0) for y in range(4) for x in range(4)]
        self.rect = (self.x, self.y, self.draw_size, self.draw_size)
        
    def left(self):
        print "moving left"
        
    def right(self):
        print "moving right"
        
    def up(self):
        print "moving up"
        
    def down(self):
        print "moving down"
        
    def move(self,pressed):
        if pressed[pygame.K_UP]:
            self.up()
        if pressed[pygame.K_RIGHT]:
            self.right()
        if pressed[pygame.K_DOWN]:
            self.down()
        if pressed[pygame.K_LEFT]:
            self.left()
            
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect)
        
def read_keyboard():
    x = pygame.key.get_pressed()
    if x[pygame.K_ESCAPE] or x[pygame.K_q] or x[pygame.K_BREAK]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    return x
    
def main():
    pygame.init()
    size = 800
    screen = pygame.display.set_mode((size,size))
    black = 0, 0, 0
    board_size = size//5*4
    
    board = Board(size//5, size//5, board_size)
    done = False
    
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYDOWN:
                x = read_keyboard()
                board.move(x)
                
        screen.fill(black)
        board.draw(screen)
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()