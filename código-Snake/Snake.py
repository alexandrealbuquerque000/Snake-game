import pygame
from random import*
import copy
import os
import time
import sys

def inittest():
    while True:
        try:
            pygame.init()
        except:
            continue
        else:
            break


def presets():
    global white, black, gray, green, red, blue, orange, yellow, pink, brown, colors, padraocor, width, height, proporção, FPS, tamplacar, tamobj, velocidade_x, velocidade_y, clock, fundo, f11

    inittest()

    dirpath=os.getcwd()
    sys.path.append(dirpath)

    if getattr(sys, "frozen", False):
        os.chdir(sys._MEIPASS)

    white=(255,255,255)
    black=(0,0,0)
    gray=(105,105,105)
    green=(0,255,0)
    red=(255,0,0)
    blue=(0,0,255)
    orange=(255, 140, 0)
    yellow=(255,255,0)
    pink=(255,20,147)
    brown=(95, 45, 0)
    colors=[white,black,gray,green,red,blue,orange,yellow,pink,brown]
    padraocor=copy.deepcopy(colors)
        
    width, height=1366, 768
    proporção=35/100
    width=int(width*proporção)
    height=int(height*proporção)
    FPS=15
    tamplacar=int(width*height/3660)
    tamobj=int((width*height-tamplacar)/12806)

    velocidade_x=int(0)
    velocidade_y=int(0)
    clock=pygame.time.Clock()

    fundo=pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    f11=1               


def randomcolors():
    global colors
    global padraocor
    global cor1
    global cor2
    global cor3
    global cor4
    global cor5
    global cor6
    global cor7
    global cor8
    choose=randint(0, (len(colors))-1)
    cor1=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor2=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor3=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor4=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor5=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor6=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor7=colors[choose]
    del(colors[choose])
    choose=randint(0, (len(colors))-1)
    cor8=colors[choose]
    colors=copy.deepcopy(padraocor)

    
def standartcolors():
    global colors
    global cor1
    global cor2
    global cor3
    global cor4
    global cor5
    global cor6
    global cor7
    global cor8
    cor1=black
    cor2=gray
    cor3=red
    cor4=yellow
    cor5=blue
    cor6=green
    cor7=orange
    cor8=white


def poscharacter():
    global pos_x
    global pos_y
    pos_x=randrange(0, int(width-height), tamobj)
    pos_y=randrange(0, int(width-height-tamplacar), tamobj)
    
    
def posapple():
    global pos_xapple
    global pos_yapple
    pos_xapple=randrange(0, int(width-height), tamobj)
    pos_yapple=randrange(0, int(width-height-tamplacar), tamobj)
    while pos_x==pos_xapple and pos_y==pos_yapple:
        pos_xapple=randrange(0, int(width-height), tamobj)
        pos_yapple=randrange(0, int(width-height-tamplacar), tamobj)
        
        
def text(msg, cor, fonte, style, backx, backy, mode):
    font=pygame.font.SysFont(mode, int(fonte))
    texto1=font.render(msg, style, cor)
    fundo.blit(texto1, [int(width/backx), int(height/backy)])
    

def updateeyes3(info):
    global eyesx1
    global eyesy1
    global eyesx2
    global eyesy2
    global xy
    if info=='up':
        eyesx1=0
        eyesy1=0
        eyesx2=int(2.25*tamobj/3)
        eyesy2=0
    elif info=='right':
        eyesx1=int(2.25*tamobj/3)
        eyesy1=0
        eyesx2=int(2.25*tamobj/3)
        eyesy2=int(2.25*tamobj/3)
    elif info=='down':
        eyesx1=0
        eyesy1=int(2.25*tamobj/3)
        eyesx2=int(2.25*tamobj/3)
        eyesy2=int(2.25*tamobj/3)
    elif info=='left':
        eyesx1=0
        eyesy1=0
        eyesx2=0
        eyesy2=int(2.25*tamobj/3)
     

def character():
    global eyesx1
    global eyesy1
    global eyesx2
    global eyesy2
    global xyp
    try:
        eyesx1
        eyesy1
        eyesx2
        eyesy2
    except NameError:
        eyesx1=0
        eyesy1=0
        eyesx2=0
        eyesy2=0
        eyes=randint(1,4)
        if eyes==1:
            updateeyes3('up')
        elif eyes==2:
           updateeyes3('right')
        elif eyes==3:
            updateeyes3('down')
        elif eyes==4:
            updateeyes3('left')
    for xy in cobraxy:
        pygame.draw.rect(fundo, cor1, [xy[0], xy[1], tamobj, tamobj])
    pygame.draw.rect(fundo, cor8, [xy[0]+eyesx1, xy[1]+eyesy1, int(tamobj/3), int(tamobj/3)])
    pygame.draw.rect(fundo, cor8, [xy[0]+eyesx2, xy[1]+eyesy2, int(tamobj/3), int(tamobj/3)])
    

def apple():
    pygame.draw.rect(fundo, cor3, [pos_xapple,pos_yapple, tamobj,tamobj])
    

def placar():
    global tamplacar
    pygame.draw.rect(fundo, cor5, [0,height-tamplacar, width,tamplacar])
    
    
def inforestartgame():
    global FPS
    global pos_x
    global pos_y
    global velocidade_x
    global velocidade_y
    global cobraxy
    global cobracomp
    global sair
    global gameover
    global points
    global nextpass
    sair=True
    gameover=False
    poscharacter()
    posapple()
    velocidade_x=int(0)
    velocidade_y=int(0)
    cobraxy=[]
    cobracomp=1
    FPS=15
    points=0
    nextpass=False
    
def jogo():
    global FPS
    global pos_x
    global pos_y
    global velocidade_x
    global velocidade_y
    global cobraxy
    global fundo
    global f11
    
    poscharacter()
    posapple()

    sair=True
    gameover=False
    telainicio=True
    cobraxy=[]
    cobracomp=1
    points=0
    nextpass=False
    eyesx=tamobj
    eyesy=tamobj
    seta=None
    
    while telainicio:
        cor1i=red
        cor2i=yellow
        cor3i=brown
        cor4i=blue
        cor5i=black
        cor7i=orange
        fundo.fill(cor2i)
        text("Snake Game", cor5i, int(width*height/2290), True, 5.6, 29.6, 'bahnschrift')
        text("Snake Game", cor1i, int(width*height/2329), True, 5.5, 30, 'bahnschrift')
        text("Mode:", cor5i, int(width*height/3200), True, 2.73, 4.65, 'comicsansms')
        text("Mode:", cor1i, int(width*height/3202.6), True, 2.7, 4.6, 'comicsansms')
        pygame.draw.rect(fundo, cor5i, [width/3.060,height/2.4, int(width*height/900),float(width*height/3030)])
        pygame.draw.rect(fundo, cor5i, [width/3.060,height/1.58, int(width*height/900),float(width*height/3030)])
        classicbox=pygame.draw.rect(fundo, cor3i, [width/3,height/2.45, int(width*height/915),float(width*height/3014.2)])
        freebox=pygame.draw.rect(fundo, cor3i, [width/3,height/1.6, int(width*height/915),float(width*height/3014.2)])
        if seta=='up' or classicbox.collidepoint( pygame.mouse.get_pos()):
            text("Classic", cor5i, int(width*height/3660), True, 2.73, 2.45, 'cambria')
            text("Free", cor4i, int(width*height/3660), True, 2.44, 1.6, 'cambria')
        if seta=='down' and classicbox.collidepoint( pygame.mouse.get_pos()):
            text("Classic", cor5i, int(width*height/3660), True, 2.73, 2.45, 'cambria')
            text("Free", cor4i, int(width*height/3660), True, 2.44, 1.6, 'cambria')
            seta='up'
        if seta=='down'or freebox.collidepoint(pygame.mouse.get_pos()):
            text("Free", cor5i, int(width*height/3660), True, 2.44, 1.6, 'cambria')
            text("Classic", cor4i, int(width*height/3660), True, 2.73, 2.45, 'cambria')
        if seta=='up' and freebox.collidepoint( pygame.mouse.get_pos()):
            text("Classic", cor4i, int(width*height/3660), True, 2.73, 2.45, 'cambria')
            text("Free", cor5i, int(width*height/3660), True, 2.44, 1.6, 'cambria')
            seta='down'
        if seta==None and freebox.collidepoint( pygame.mouse.get_pos())==False and classicbox.collidepoint( pygame.mouse.get_pos())==False:
            text("Classic", cor4i, int(width*height/3660), True, 2.73, 2.45, 'cambria')
            text("Free", cor4i, int(width*height/3660), True, 2.44, 1.6, 'cambria')
        text("Program by Mastef", cor7i, int(width*height/6500), True, 1.55, 1.1, 'constantia')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=False
                telainicio=False
                nextpass=False
                sair=False
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if ( classicbox.collidepoint( pygame.mouse.get_pos()) ):
                    colisaotela=True
                    nextpass=True
                    telainicio=False
                    pass
                if ( freebox.collidepoint( pygame.mouse.get_pos()) ):
                    colisaotela=False
                    nextpass=True
                    telainicio=False
                    pass
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and freebox.collidepoint( pygame.mouse.get_pos())==False:
                    seta='up'
                if event.key==pygame.K_DOWN and classicbox.collidepoint( pygame.mouse.get_pos())==False:
                    seta='down'
                if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    if seta=='up':
                        colisaotela=True
                        nextpass=True
                        telainicio=False
                        seta=None
                    elif seta=='down':
                        colisaotela=False
                        nextpass=True
                        telainicio=False
                        seta=None
                    else:
                        pass
                if event.key==pygame.K_F11:
                    f11=f11+1
                    if f11%2==0:
                        fundo=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        fundo=pygame.display.set_mode((width, height))
                if event.key==pygame.K_ESCAPE:
                    fundo=pygame.display.set_mode((width, height))
        while nextpass:
            fundo.fill(cor1i)
            text("Theme:", cor5i, int(width*height/2846.7), True, 3.13, 8.8, 'comicsansms')
            text("Theme:", cor2i, int(width*height/2846.7), True, 3.18, 9, 'comicsansms')
            pygame.draw.rect(fundo, cor5i, [width/3.030,height/2.54, int(width*height/920),float(width*height/3300)])
            pygame.draw.rect(fundo, cor5i, [width/3.030,height/1.64, int(width*height/920),float(width*height/3300)])
            standartbox=pygame.draw.rect(fundo, cor4i, [width/3,height/2.7, int(width*height/915),float(width*height/3014.2)])
            randombox=pygame.draw.rect(fundo, cor4i, [width/3,height/1.7, int(width*height/915),float(width*height/3014.2)])
            if seta=='up' or classicbox.collidepoint( pygame.mouse.get_pos()):
                text("Standart", cor5i, int(width*height/4200), True, 2.8, 2.68, 'cambria')
                text("Random", cor2i, int(width*height/4200), True, 2.78, 1.68, 'cambria')
            if seta=='down' and classicbox.collidepoint( pygame.mouse.get_pos()):
                text("Standart", cor5i, int(width*height/4200), True, 2.8, 2.68, 'cambria')
                text("Random", cor2i, int(width*height/4200), True, 2.78, 1.68, 'cambria')
                seta='up'
            if seta=='down'or freebox.collidepoint(pygame.mouse.get_pos()):
                text("Random", cor5i, int(width*height/4200), True, 2.78, 1.68, 'cambria')
                text("Standart", cor2i, int(width*height/4200), True, 2.8, 2.68, 'cambria')
            if seta=='up' and freebox.collidepoint( pygame.mouse.get_pos()):
                text("Standart", cor2i, int(width*height/4200), True, 2.8, 2.68, 'cambria')
                text("Random", cor5i, int(width*height/4200), True, 2.78, 1.68, 'cambria')
                seta='down'
            if seta==None and freebox.collidepoint( pygame.mouse.get_pos())==False and classicbox.collidepoint( pygame.mouse.get_pos())==False:
                text("Standart", cor2i, int(width*height/4200), True, 2.8, 2.68, 'cambria')
                text("Random", cor2i, int(width*height/4200), True, 2.78, 1.68, 'cambria')
            text("Program by Mastef", cor3i, int(width*height/6500), True, 1.55, 1.1, 'constantia')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    nextpass=False
                    sair=False
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if ( standartbox.collidepoint( pygame.mouse.get_pos()) ):
                        standartcolors()
                        nextpass=False
                    if ( randombox.collidepoint( pygame.mouse.get_pos()) ):
                        randomcolors()
                        nextpass=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP and randombox.collidepoint( pygame.mouse.get_pos())==False:
                        seta='up'
                    if event.key==pygame.K_DOWN  and standartbox.collidepoint( pygame.mouse.get_pos())==False:
                        seta='down'
                    if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                        if seta=='up':
                            standartcolors()
                            nextpass=False
                            seta=None
                        elif seta=='down':
                            randomcolors()
                            nextpass=False
                            seta=None
                        else:
                            pass
                    if event.key==pygame.K_F11:
                        f11=f11+1
                        if f11%2==0:
                            fundo=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        else:
                            fundo=pygame.display.set_mode((width, height))
                    if event.key==pygame.K_ESCAPE:
                        fundo=pygame.display.set_mode((width, height))
    pygame.display.update()
    hack=False
    while sair:
        while gameover:
            fundo.fill(cor2)
            if int((width*(height-tamplacar))/tamobj)==points+1:
                text("You Won!", cor1, int(width*height/2846.7), True, 3.45, 17.3, 'impact')
                text("You Won!", cor4, int(width*height/2846.7), True, 3.4, 17.5, 'impact')
            else:
                text("Game Over", cor1, int(width*height/2846.7), True, 3.68, 17.6, 'impact')
                text("Game Over", cor4, int(width*height/2846.7), True, 3.6, 18, 'impact')
            text("Points: "+str(points), cor1, 32.5, True, 2.78, 3.82, 'carlito')
            text("Points: "+str(points), cor4, 32.5, True, 2.75, 3.85, 'carlito')
            text("Press 'R' to restart or 'Q' to quit", cor1, int(width*height/4500), True, 10.3, 1.59, 'tahoma')
            text("Press 'R' to restart or 'Q' to quit", cor4, int(width*height/4500), True, 10, 1.6, 'tahoma')
            pygame.draw.rect(fundo, cor1, [width/3.027,height/2.437, float(width*height/948.9),float(width*height/4270.1)])
            continuebox=pygame.draw.rect(fundo, cor4, [width/3,height/2.5, float(width*height/948.9),float(width*height/4270.1)])
            if ( continuebox.collidepoint( pygame.mouse.get_pos()) ) or seta=='up' or seta=='down':
                text("Continue", cor1, float(width*height/4200.1), True, 2.88, 2.57, 'cambria')
            else:
                text("Continue", cor2, float(width*height/4200.1), True, 2.88, 2.57, 'cambria')
            text("Program by Mastef", cor4, int(width*height/6500), True, 1.55, 1.1, 'constantia')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sair=False
                    gameover=False
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        inforestartgame()
                        jogo()
                    if event.key==pygame.K_q:
                        sair=False
                        gameover=False
                        sys.exit()
                    if event.key==pygame.K_UP and continuebox.collidepoint( pygame.mouse.get_pos())==False:
                        seta='up'
                    if event.key==pygame.K_DOWN  and continuebox.collidepoint( pygame.mouse.get_pos())==False:
                        seta='down'
                    if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                        if seta=='up' or seta=='down':
                            inforestartgame()
                            jogo()
                            seta=None
                        else:
                            pass
                    if event.key==pygame.K_F11:
                        f11=f11+1
                        if f11%2==0:
                            fundo=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        else:
                            fundo=pygame.display.set_mode((width, height))
                    if event.key==pygame.K_ESCAPE:
                        fundo=pygame.display.set_mode((width, height))
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if ( continuebox.collidepoint( pygame.mouse.get_pos()) ):
                        inforestartgame()
                        jogo()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sair=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and velocidade_x != tamobj:
                    velocidade_x=-tamobj
                    velocidade_y=0
                    updateeyes3('left')
                if event.key==pygame.K_RIGHT and velocidade_x != -tamobj:
                    velocidade_x=tamobj
                    velocidade_y=0
                    updateeyes3('right')
                if event.key==pygame.K_UP and velocidade_y != tamobj:
                    velocidade_x=0
                    velocidade_y=-tamobj
                    updateeyes3('up')
                if event.key==pygame.K_DOWN and velocidade_y !=- tamobj:
                    velocidade_x=0
                    velocidade_y=tamobj
                    updateeyes3('down')
                if event.key==pygame.K_LALT:
                    hack=True
                if event.key==pygame.K_SPACE and hack:
                    cobracomp=cobracomp+1
                    points=points+1
                if event.key==pygame.K_F11:
                    f11=f11+1
                    if f11%2==0:
                        fundo=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        fundo=pygame.display.set_mode((width, height))
                if event.key==pygame.K_ESCAPE:
                    fundo=pygame.display.set_mode((width, height))
        if sair:
            fundo.fill(cor2)
            pos_x=pos_x+velocidade_x
            pos_y=pos_y+velocidade_y

            if pos_x==pos_xapple and pos_y==pos_yapple:
                posapple()
                cobracomp=cobracomp+1
                points=points+1
                FPS=FPS+0.01
            
            if pos_x + tamobj>width:
                if colisaotela==True:
                    gameover=True
                    continue
                pos_x=0
            if pos_x<0:
                if colisaotela==True:
                    gameover=True
                    continue
                pos_x=width-tamobj
            if pos_y + tamobj>height-tamplacar:
                if colisaotela==True:
                    gameover=True
                    continue
                pos_y=0
            if pos_y<0:
                if colisaotela==True:
                    gameover=True
                    continue
                pos_y=height-tamobj-tamplacar
                
            cobrainicio=[]
            cobrainicio.append(pos_x)
            cobrainicio.append(pos_y)
            cobraxy.append(cobrainicio)
            if len(cobraxy)>cobracomp:
                del (cobraxy[0])
            if any(bloco==cobrainicio for bloco in cobraxy[:-1]):
                gameover=True          
            
            placar()
            
            text("Points: "+str(points), cor6, int(width*height/6200), True, width*0.1, 1.125, 'ebrima')
            text("Program by Mastef", cor7, int(width*height/6500), True, 1.55, 1.1, 'constantia')
            
            character()
                
            apple()
            
            pygame.display.update()

            clock.tick(float(FPS))


def run():
    presets()
    jogo()
    pygame.quit()
    quit()


run()
