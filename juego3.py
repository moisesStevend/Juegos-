#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
import random    
import json
import numpy as np
from pprint import pprint

class Fondo(pygame.sprite.Sprite):
    def __init__(self,mapa,pixeles):#"mapa1_1",70
        imagen=pygame.image.load("tileSet3.png")
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        
        self.pixelesXimagen=pixeles
        self.imagenJason(mapa)#filas de la imagen pos, columna de la imagen pos
        self.coordenadasImagen(15,(3,5))#len, (filas, columnas).........tamaño de la matriz main, reparticion de la matriz en Y X del tiled Main

    def update(self,ventana,posY,posX):#filas vs columnas
        self.rect.left=posX*self.pixelesXimagen
        self.rect.top=posY*self.pixelesXimagen
        ventana.blit(self.imagen, self.rect, (self.coor[self.tamn[posY][posX]-1][0],self.coor[self.tamn[posY][posX]-1][1],self.pixelesXimagen,self.pixelesXimagen))
        
    def pintar(self,ventana):
        for j in range(self._height):
            for i in range(self._width):
                self.update(ventana,j,i)
    
    def imagenJason(self,mundo):
        with open(mundo+'.json') as data_file:    
            data = json.load(data_file)
        
        #self._height=data["layers"][1]["height"] #10
        self._height=data["layers"][0]["height"] #10
        self._width=data["layers"][0]["width"]  #20
    
        self.tamn = data["layers"][0]["data"]
        #self.tamn = data["layers"][1]["data2"]
        self.tamn=np.asarray(self.tamn).reshape((self._height, self._width))
    
    def coordenadasImagen(self,tamano,(partY,partX)):
        l=np.arange(1,tamano+1).reshape(partY,partX)
        x=0
        y=0
        self.coor=[]
        for j in range(len(l)):
            for i in range(len(l[0])):
                self.coor.append((x,y))
                x+=self.pixelesXimagen
            y+=self.pixelesXimagen
            x=0


class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.imagen2=pygame.transform.flip(self.imagen,True,False)
        self.rect=self.imagen.get_rect()
        self.rect.left=0
        #self.rect.top=454-60-14*5
        self.rect.top=454-60-14*5-40
        
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
        
    def move(self,izq,der,pantalla,arriba,cont_up,mira,arriba_con_salto,cont_up2):        
        if (izq==True) and (der==False) or (arriba  and mira==False) or (arriba_con_salto and mira==False):
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
            ###########################################
            elif arriba_con_salto:
                self.x_init=self.camb_img2[0][0]
                self.x_w=self.camb_img2[0][1]
                
                if cont_up2<=7:
                    self.rect.move_ip(-10,-10)
                elif cont_up2>7 and cont_up2<15:
                    self.rect.move_ip(-10,10)
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
            
        elif (izq==False) and (der==True) or (arriba and mira==True)  or (arriba_con_salto and mira==True):
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
            ########################################
            elif arriba_con_salto:
                self.x_init=self.camb_img[3][0]
                self.x_w=self.camb_img[3][1]
                
                if cont_up2<=7:
                    self.rect.move_ip(10,-10)
                elif cont_up2>7 and cont_up2<15:
                    self.rect.move_ip(10,10)
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
        
    def update(self,pantalla,imagen):
        pantalla.blit(imagen,self.rect,(5*self.x_init, 5*self.y_init,5*self.x_w, 5*self.y_h))
    
if __name__=="__main__":
    pygame.init()
    ventana=pygame.display.set_mode([940,454])
    reloj = pygame.time.Clock()
    salir=False
    
    img_mario1=pygame.image.load("mario_moviendose3.png").convert_alpha()
    mario1=Player(img_mario1)
    
    #mundo1=pygame.image.load("mundo.png").convert()
    #variables auxliares
    izq=False
    der=False
    arriba=False
    cont_up=0
    mira=True#der:True, Izqui=False
    arriba_con_salto=False
    cont_up2=0
    
    fondo=Fondo("mapa4",70)
    
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
                    if izq:
                        arriba_con_salto=True
                        arriba=False
                    elif der:
                        arriba_con_salto=True
                        arriba=False
                    else:
                        arriba_con_salto=False
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
        
        if arriba_con_salto:
            cont_up2+=1
            if cont_up2==15:
                cont_up2=0
                arriba_con_salto=False
        
        
                #der=False
                #izq=False
                   
        reloj.tick(20)
        #ventana.blit(mundo1,(0,0))
        fondo.pintar(ventana)
        mario1.move(izq,der,ventana,arriba,cont_up,mira,arriba_con_salto,cont_up2)
        #mario1.update(ventana)
        pygame.display.update()
     
    pygame.quit() 