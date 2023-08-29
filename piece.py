
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

import pygame 

class Piece:
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color):
        self.row= row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.calc_pos()


        #if self.color == RED:
        #    self.direction = -1
        #else: self.direction = 1


        


    def calc_pos(self):
        #x,y should be in middle of square
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def make_king(self):
        self.king = True

    def draw (self, win):
        radius= SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        #blit just sticks an image onto the screen
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    #just moves pos 
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    #debugging method to identify object w/eror
    def __repr__(self):
        return str(self.color)


        