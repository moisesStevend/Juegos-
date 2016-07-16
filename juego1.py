import pygame
import random

class Recs():
    def __init__(self,n_inicial):
        self.lista=[]
        for x in range(n_inicial):
            left_random=random.randrange(2,560)
            top_random=random.randrange(-580,-10)
            width_random=random.randrange(10,30)
            height_random=random.randrange(15,30)
            self.lista.append(pygame.Rect(left_random,top_random,width_random,height_random))

    def reagregar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>490:
                left_random=random.randrange(2,560)
                top_random=random.randrange(-580,-10)
                width_random=random.randrange(10,30)
                height_random=random.randrange(15,30)
                self.lista[x]=(pygame.Rect(left_random,top_random,width_random,height_random))
            
    def agregarotro(self):
        pass
            
    def mover(self):
        for r in self.lista:
            r.move_ip(0,2)
            
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(200,100,2),rectangulo)

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        #(self.rect.left,self.rect.top)=(240,150)
        #(self.rect.centerx,self.rect.centery)=(240,150)
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    
    def update(self,superficie):
        superficie.blit(self.imagen, self.rect)
###########################################################
###########################################################
def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    reloj1=pygame.time.Clock()
    
    pygame.mixer.music.load("mortal.mp3")
    pygame.mixer.music.play(4)#4: numero de loops
    
    imagen1=pygame.image.load("nave_buena.png")#.convert()
    imagen1=pygame.transform.scale(imagen1,(50,50))
    player1=Player(imagen1)
    
    imagen2=pygame.image.load("bala2.png")#.convert()
    imagen2=pygame.transform.scale(imagen2,(50,50))
    player2=Player(imagen2)
    
    explosion1=pygame.image.load("explosion_planeta.png")#.convert()
    explosion1=pygame.transform.scale(explosion1,(50,50))
    
    fondo=pygame.image.load("fondo.jpg")
    fondo=pygame.transform.scale(fondo,(600,480))
    
    recs1=Recs(25)
    
    vx=0
    vy=0
    velocidad=10
    (left_pre, right_pre, up_pre, down_pre)=(False,False,False,False)
    colisiono=False
    
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
        #pantalla.fill([255,0,100])
        pantalla.blit(fondo,(0,0))     
        
        player2.mover(0,0)
        player2.update(pantalla)
   
        if colision(player1, recs1):
            colisiono=True
            player1.imagen=explosion1
            pygame.mixer.music.stop()
            
        if colisiono==False:
            recs1.mover()
            player1.mover(vx, vy)
        
        player1.update(pantalla)
        recs1.pintar(pantalla)
        pygame.display.update()
        
        recs1.reagregar()
    pygame.quit()

main()    
    