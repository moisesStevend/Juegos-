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


if __name__=="__main__":
    pygame.init()
    ventana=pygame.display.set_mode((960,560))#10*70-2*70))#((20*70,10*70))#tamano total de la imagen
    reloj1=pygame.time.Clock()
    salir=False
    
    fondo=Fondo("mapa4",70)
    
    while salir==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
    
        reloj1.tick(20)
        ventana.fill((255,255,255))
        fondo.pintar(ventana)
        pygame.display.update()
        
    pygame.display.quit()
    pygame.quit()
    
        