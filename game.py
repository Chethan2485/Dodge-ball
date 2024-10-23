import pygame as py 
import sys,time
from ball import Ball
from pipe import Pipe

#initaializing pygame

py.init()
class Game:
    def __init__(self): 
        #screen
        self.width=1202
        self.height=801
        self.win=py.display.set_mode((self.width, self.height))

        self.scale=1.5
        self.clock=py.time.Clock()
        self.speed=250
        self.startmonitoring=False   #for calculating score
        self.score=0  #intial score
        self.font=py.font.Font("font.ttf",24)
        self.font1=py.font.Font("font.ttf",12)
        self.score_text=self.font.render(f"Score:{self.score} ",True,(127, 255, 0))
        self.score_text_rect=self.score_text.get_rect(center=(150,50))
        self.is_game_started=True
        self.ball=Ball(self.scale)
        self.is_enter_pressed=False      #checking if player is ready
        self.pipes=[]
        self.pipe_generate_counter=101    #distance betwwen 2 pipes
        self.setupbackground()
        
              
        self.gameloop()
         
    def gameloop(self):
        #calculating delta time
        last_time=time.time()

        while True:
            new_time=time.time()   
            dt=new_time-last_time
            last_time=new_time
            
            #mouse and button actions

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN and self.is_game_started:
                    if event.key == py.K_RETURN or event.key ==py.K_SPACE:
                       self.is_enter_pressed=True
                    if event.key == py.K_SPACE or event.key == py.K_UP:
                        self.ball.flap(dt)
                if event.type==py.MOUSEBUTTONUP :
                    if self.restart_rect.collidepoint(py.mouse.get_pos()):
                        self.restartgame()
                       
                       
            self.updateEverthing(dt)
            self.checkCollison()
            self.drawEverthing()
            self.checkScore()
            py.display.update()
            self.clock.tick(60)
    
    def restartgame(self):
        self.score=0
        self.score_text=self.font.render(f"Score:{self.score} ",True,(127, 255, 0))
        self.is_enter_pressed=False   #checking whetr=her player is ready
        self.is_game_started=True
        self.ball.resetPosition()      #bringing ball to intial position
        self.pipes.clear()
        self.pipe_generate_counter=101
        self.ball.update_on=True       #for animation and applying gravity
        
        #CALCULATING SCORE
    def checkScore(self):
        if len(self.pipes)>0:
            if (self.ball.rect.left>self.pipes[0].rect_down.left and self.ball.rect.right < self.pipes[0].rect_down.right and not self.startmonitoring):
                self.startmonitoring=True
            if self.ball.rect.left > self.pipes[0].rect_down.right and self.startmonitoring:
                self.startmonitoring=False
                self.score=self.score+1
                self.score_text=self.font.render(f"Score: {self.score} ",False,(127, 255, 0))


    
    def checkCollison(self):
        if len(self.pipes):
            if (self.ball.rect.bottom>715 or self.ball.rect.colliderect(self.pipes[0].rect_down) or
                self.ball.rect.colliderect(self.pipes[0].rect_up)):
                  self.ball.update_on=False
                  self.is_enter_pressed=False
                  self.is_game_started=False
            
        #updating movements
    def updateEverthing(self,dt):
        if self.is_enter_pressed:
            self.ground1_rect.x-=int(self.speed*dt)
            self.ground2_rect.x-=int(self.speed*dt)
            #creation of moving ground 
            if self.ground1_rect.right<0:
                self.ground1_rect.x=self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x=self.ground1_rect.right
            #generating obstacle
            if self.pipe_generate_counter>100:
                 self.pipes.append(Pipe(self.scale,self.speed))
                 self.pipe_generate_counter=0
                 print("pipe created")
            self.pipe_generate_counter+=1     
            #obstacles moving 
            for pipe in self.pipes:
                pipe.update(dt)  
            #removing extra obstacles
            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)
                    print("pipe removed")
                
             #moving the ball   
            self.ball.update(dt)
        
        
        
               
     #background and ground image
    def setupbackground(self):
        self.back_ground=py.image.load("background.jpg").convert()
        self.ground1=py.image.load("ground2.jpg").convert()
        self.ground2=py.image.load("ground2.jpg").convert()
        self.ground1_rect=self.ground1.get_rect()
        self.ground2_rect=self.ground2.get_rect()
        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=700
        self.ground2_rect.y=700
        self.restart=py.image.load("restart.png").convert()
        self.restart_rect=self.restart.get_rect(center=(600,400))
        
        
    #to display loaded image on screen
    def drawEverthing(self):
        self.win.blit(self.back_ground,(0,0))
        for pipe in self.pipes:
            pipe.drawPipe(self.win)
        self.win.blit(self.ground1,self.ground1_rect)
        self.win.blit(self.ground2,self.ground2_rect)
        self.win.blit(self.ball.image,self.ball.rect)
        self.win.blit(self.score_text,self.score_text_rect)
        
        #restart button
        if not self.is_game_started:
            self.win.blit(self.restart,self.restart_rect)    
           
    
game=Game()

