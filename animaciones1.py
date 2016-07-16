import pygame

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("fondox.jpg")
        self.rect=self.imagen.get_rect()
    
    def update(self,pantalla,vx,vy):
        self.rect.move_ip(-vx,-vy)
        pantalla.blit(self.imagen,self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2,imagen3,imagen4):
        self.imagenes=[[imagen1, imagen2],[imagen3,imagen4]]
        self.actualD=False                         
        self.actualI=False
        self.imagen=self.imagenes[0][0]
        self.rect=self.imagen.get_rect()
        self.rect.left,self.rect.top=(200,440)
        #(self.rect.centerx,self.rect.centery)=(240,150)
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    
    def update(self,superficie,vx,vy,izq,der,up,down):
        #self.mover(vx,vy)
        if (vx,vy)!=(0,0):
            if der or up or down:
                self.actualD=not self.actualD
                self.imagen=self.imagenes[0][int(self.actualD)]
            elif izq:
                self.actualI=not self.actualI
                self.imagen=self.imagenes[1][int(self.actualI)]
        
        superficie.blit(self.imagen, self.rect)
        
def main():
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj1=pygame.time.Clock()
    
    #pygame.mixer.music.load("mortal.mp3")
    #pygame.mixer.music.play(4)#4: numero de loops
    
    imagen1=pygame.image.load("personaje_gorra6.png")#.convert()
    imagen1=pygame.transform.scale(imagen1,(50,90))
    
    imagen2=pygame.image.load("personaje_gorra5.png")#.convert()
    imagen2=pygame.transform.scale(imagen2,(50,90))
    
    imagen3=pygame.image.load("personaje_gorra7.png")#.convert()
    imagen3=pygame.transform.scale(imagen3,(50,90))
    
    imagen4=pygame.image.load("personaje_gorra8.png")#.convert()
    imagen4=pygame.transform.scale(imagen4,(50,90))
    
    player1=Player(imagen1,imagen2,imagen3,imagen4)    
    fondo1=Fondo()
#     fondo=pygame.image.load("fondo.jpg")
#     fondo=pygame.transform.scale(fondo,(600,480))
    
    vx=0
    vy=0
    velocidad=10
    (left_pre, right_pre, up_pre, down_pre)=(False,False,False,False)

    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            #if colisiono==False:
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    left_pre=True
                    vx=vx-velocidad
                    print "left",vx
                if event.key==pygame.K_RIGHT:
                    right_pre=True
                    vx=vx+velocidad
                if event.key==pygame.K_UP:
                    up_pre=True
                    vy=vy-velocidad
                if event.key==pygame.K_DOWN:
                    down_pre=True
                    vy=vy+velocidad    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    left_pre=False
                    if right_pre: vx=vx+velocidad
                    else: vx=0
                if event.key==pygame.K_RIGHT:
                    right_pre=False
                    if left_pre: vx=vx-velocidad
                    else: vx=0
                if event.key==pygame.K_UP:
                    up_pre=False
                    if down_pre: vy=vy+velocidad
                    else: vy=0
                if event.key==pygame.K_DOWN:
                    down_pre=False
                    if up_pre: vy=vy-velocidad
                    else: vy=0            
                    
        
        reloj1.tick(20)
        fondo1.update(pantalla,vx,vy)
        #pantalla.fill([255,0,100])
        #pantalla.blit(fondo,(0,0))     
            
        #player1.mover(vx, vy)
        player1.update(pantalla,vx,vy,left_pre,right_pre,up_pre,down_pre)
        pygame.display.update()
        
    pygame.quit()

main()          