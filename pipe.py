import pygame as py
from random import randint

class Pipe:
    def __init__(self,scale_factor,move_speed):
        self.img_up=py.transform.scale_by(py.image.load("pipeup.png").convert_alpha(),scale_factor)
        self.img_down=py.transform.scale_by(py.image.load("pipedown.png").convert_alpha(),scale_factor)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.pipe_distance=200
        self.rect_up.y=randint(250,520)
        self.rect_up.x=1200
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=1200
        self.move_speed=move_speed
        
    def drawPipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)
        
    def update(self,dt):
        self.rect_up.x-=int(self.move_speed*dt)
        self.rect_down.x-=int(self.move_speed*dt)