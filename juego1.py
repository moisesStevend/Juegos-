import pygame,sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.imagen2=pygame.transform.flip(self.imagen,True,False)
        self.rect=self.imagen.get_rect()
        self.rect.left=0
        self.rect.top=454-60-14*5
        
        self.camb=0
        self.camb_img=[(0,13),(13,13),(26,9),(35,15)]#self.x_init, self.x_w
        
        self.camb2=0
        self.camb_img2=[(0,14),(14,9),(23,14),(37,13)]
        
        self.x_init=1###0
        self.y_init=6
        self.x_w=12
        self.y_h=14
        
        self.toggle=False
        #self.rect=pygame.Rect((0, 0, 5*55, 5*70))
        
    def move(self,izq,der,pantalla,arriba,cont_up,mira):        
        if (izq==True) and (der==False) or (arriba  and mira==False):
            self.toggle=True
            #######################################3
            if arriba:
                self.x_init=self.camb_img2[0][0]
                self.x_w=self.camb_img2[0][1]
                
                if cont_up<=7:
                    self.rect.move_ip(0,-10)
                elif cont_up>7 and cont_up<15:
                    self.rect.move_ip(0,10)
                else:
                    self.rect.move_ip(0,0)
                #self.update(pantalla,self.imagen)
            
            #######################################
            else:
                self.rect.move_ip(-10,0)   
                self.camb2=self.camb2+1
                if self.camb2==2 or  self.camb2==4 or self.camb2==6 : 
                    if self.camb2==6:
                        self.camb2=2######0
                    self.x_init=self.camb_img2[self.camb2/2][0]
                    self.x_w=self.camb_img2[self.camb2/2][1]
                    print self.x_init,self.x_w
            
            self.update(pantalla,self.imagen2)
            
        elif (izq==False) and (der==True) or (arriba and mira==True):
            self.toggle=False
            
            #######################################3
            if arriba:
                self.x_init=self.camb_img[3][0]
                self.x_w=self.camb_img[3][1]
                
                if cont_up<=7:
                    self.rect.move_ip(0,-10)
                elif cont_up>7 and cont_up<15:
                    self.rect.move_ip(0,10)
                else:
                    self.rect.move_ip(0,0)
                #self.update(pantalla,self.imagen)
            
            #######################################
            else:
                self.rect.move_ip(10,0)
                self.camb=self.camb+1
                if self.camb==2 or self.camb==4 or  self.camb==6: 
                    if self.camb==6:
                        self.camb=2######0
                    self.x_init=self.camb_img[self.camb/2][0]
                    self.x_w=self.camb_img[self.camb/2][1]
                    print self.x_init,self.x_w
            
            self.update(pantalla,self.imagen)
        else:
            if self.toggle==True:
                self.x_init=self.camb_img2[3][0]
                self.x_w=self.camb_img2[3][1]
                self.rect.move_ip(0,0)
            
                self.update(pantalla,self.imagen2)
                
            elif self.toggle==False:
                self.x_init=self.camb_img[0][0]
                self.x_w=self.camb_img[0][1]
                self.rect.move_ip(0,0)
            
                self.update(pantalla,self.imagen)
            
#             else:
#                 self.x_init=self.camb_img[0][0]
#                 self.x_w=self.camb_img[0][1]
#                 self.rect.move_ip(0,0)
#             
#                 self.update(pantalla,self.imagen)
        

        
    def update(self,pantalla,imagen):
        pantalla.blit(imagen,self.rect,(5*self.x_init, 5*self.y_init,5*self.x_w, 5*self.y_h))
        #self.x_init=self.x_init*2
        #self.x_w=13
        #self.y_h=14
    
if __name__=="__main__":
    pygame.init()
    ventana=pygame.display.set_mode([940,454])
    reloj = pygame.time.Clock()
    salir=False
    
    img_mario1=pygame.image.load("mario_moviendose3.png").convert_alpha()
    mario1=Player(img_mario1)
    
    mundo1=pygame.image.load("mundo.png").convert()
    #variables auxliares
    izq=False
    der=False
    arriba=False
    cont_up=0
    mira=True#der:True, Izqui=False
    
    while salir==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mira=False
                    print "left"
                    izq=True
                    der=False
                if event.key == pygame.K_RIGHT:
                    mira=True
                    print "rght"
                    der=True
                    izq=False
                if event.key==pygame.K_UP:
                    arriba=True
                
            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if der:
                        der=True
                        izq=False
                    else:
                        der=False
                        izq=False
                        
                if event.key == pygame.K_RIGHT:
                    if izq:
                        der=False
                        izq=True
                    else:
                        der=False
                        izq=False
                        
                if event.type==pygame.K_UP:
                    pass
        
        if arriba:
            cont_up+=1
            if cont_up==15:
                cont_up=0
                arriba=False
                #der=False
                #izq=False
                   
        reloj.tick(20)
        ventana.blit(mundo1,(0,0))
        mario1.move(izq,der,ventana,arriba,cont_up,mira)
        #mario1.update(ventana)
        pygame.display.update()
     
    pygame.quit()   