import pygame as py

class Ball(py.sprite.Sprite):
    def __init__(self,scale_factor):
        #ball design
        super(Ball,self).__init__()
        self.img_list=[py.image.load("ball1.png").convert_alpha(),py.image.load("ball2.png").convert_alpha()]
        self.image_index=0
        self.image=self.img_list[self.image_index].convert_alpha()
        self.rect=self.image.get_rect(center=(250,200))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=True
        
        
    def update(self,dt):
        if self.update_on:
            self.playanimation()
            self.applyGravity(dt)
            
            if self.rect.y<=0 :
                self.rect.y=0
            
            
        
    def applyGravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity 
           
    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt 
        
    def playanimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0:
                self.image_index=1 
            else:
                self.image_index=0
            self.anim_counter=0
        self.anim_counter+=1
                
    def resetPosition(self):
         self.rect.center=(250,200)