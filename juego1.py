import pygame, sys
import random    
import json
import numpy as np
from pprint import pprint


def cuadro(n):
    l=np.arange(1,16).reshape(3,5)
    x=0
    y=0
    coor=[]
    for j in range(len(l)):
        for i in range(len(l[0])):
            coor.append((x,y))
            x+=70
        y+=70
        x=0
    print coor
    return coor[n-1][0],coor[n-1][1]

if __name__=="__main__":
    #20 en X, 8 en Y 
    tamn=None
    with open('mapa1_1.json') as data_file:    
        data = json.load(data_file)
    
    tamn = data["layers"][1]["data2"]
    print tamn,len(tamn)
    print ""
    tamn=np.asarray(tamn)
    print tamn,"\n"
    tamn=tamn.reshape((10,20)) #a = a.reshape((5, 2))
    print tamn,type(tamn)
    #print tamn[2][6]
#     
#     tamn=tamn.tolist()
#     print tamn,type(tamn)
    
    ###########################################
    l=np.arange(1,16).reshape(3,5)
    x=0
    y=0
    coor=[]
    for j in range(len(l)):
        for i in range(len(l[0])):
            coor.append((x,y))
            x+=70
        y+=70
        x=0
    print coor
    #return coor[n-1][0],coor[n-1][1]
    ##############################################
    fondo=pygame.sprite.Sprite()
    imagen=pygame.image.load("tileSet.png")
    fondo.imagen=imagen
    fondo.rect=fondo.imagen.get_rect()
    fondo.rect.left=6*70
    fondo.rect.top=2*70
    img=tamn[2][6]
    print img
    
    pygame.init()
    ventana=pygame.display.set_mode((20*70,10*70))#tamano total de la imagen
    reloj1=pygame.time.Clock()
    salir=False
    
    while salir==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        
        reloj1.tick(20)
        #20,10
        ventana.blit(fondo.imagen,fondo.rect,(coor[img-1][0],coor[img-1][1],70,70))
        pygame.display.update()
        
    pygame.display.quit()
    pygame.quit()
    
        
    
    
    #for item in data["layers"]:
    #    d=item['data2']
    #pprint(data["Posts"]["PostX"])
    #pprint(data["Tags"][1])