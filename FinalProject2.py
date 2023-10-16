# @author Esmael Majedi,
# Phantom Choice

# Import necessary libraries
import pygame
import pygame.mixer
import sys
import time
import pyganim
from pygame.locals import *

#Set default screen sizes, have screen scaled
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), SCALED, FULLSCREEN)

# Assigning backgrounds
background0 = pygame.image.load('intro.png')
background1 = pygame.image.load('pic1.png')
background2 = pygame.image.load('pic2.png')
background2scaryface1 = pygame.image.load('pic2scaryface1.png')
background2scaryface2 = pygame.image.load('jumpscary2.jpg')
background3 = pygame.image.load('pic3.png')
background3picright = pygame.image.load('pic3right.png')
background3picdown = pygame.image.load('riverbackground.png')
background3jump = pygame.image.load('background3jump.png')
background4 = pygame.image.load('pic4.png')
background5 = pygame.image.load('pic5.png')
background6 = pygame.image.load('pic6.png')
blackbackground = pygame.image.load('blackbackground.png')

manRoom = pygame.image.load('manRoom.png')

choice1 = pygame.image.load('choice1.png')
choice2 = pygame.image.load('choice2.png')
choiceleft1 = pygame.image.load('choiceleft1.png')
choiceleftDC = pygame.image.load('choiceleftDC.png')
choiceright1 = pygame.image.load('choiceright1.png')
choicerightDC = pygame.image.load('choicerightDC.png')
choicejump = pygame.image.load('choicejump.png')
choicedown = pygame.image.load('choicedown.png')
choicetalk = pygame.image.load('choicetalk.png')
choiceContinue = pygame.image.load('choiceContinue.png')

phantomtalk1 = pygame.image.load('phantomtalk1.png')
phantomtalk2 = pygame.image.load('phantomtalk2.png')
phantomtalk3 = pygame.image.load('phantomtalk3.png')
phantomtalk4 = pygame.image.load('phantomtalk4.png')
phantomtalk5 = pygame.image.load('phantomtalk5.png')
phantomtalk6 = pygame.image.load('phantomtalk6.png')

portaltalk1 = pygame.image.load('portaltalk1.png')
portaltalk2 = pygame.image.load('portaltalk2.png')
portaltalk3 = pygame.image.load('portaltalk3.png')
portaltalk4 = pygame.image.load('portaltalk4.png')
portaltalk5 = pygame.image.load('portaltalk5.png')

choiceGAnswer1 = pygame.image.load('choiceGAnswer1.png')
choiceGAnswer2 = pygame.image.load('choiceGAnswer2.png')
choiceGAnswer3 = pygame.image.load('choiceGAnswer3.png')
choiceGAnswer4 = pygame.image.load('choiceGAnswer4.png')
choiceGAnswer5 = pygame.image.load('choiceGAnswer5.png')
choiceGAnswer6 = pygame.image.load('choiceGAnswer6.png')

choiceBAnswer1 = pygame.image.load('choiceBAnswer1.png')
choiceBAnswer2 = pygame.image.load('choiceBAnswer2.png')
choiceBAnswer3 = pygame.image.load('choiceBAnswer3.png')
choiceBAnswer4 = pygame.image.load('choiceBAnswer4.png')
choiceBAnswer5 = pygame.image.load('choiceBAnswer5.png')
choiceBAnswer6 = pygame.image.load('choiceBAnswer6.png')

choiceManEncounter = pygame.image.load('choiceManEncounter.png')
choiceHelp = pygame.image.load('choiceHelp.png')
choiceRun = pygame.image.load('choiceRun.png')
choiceManAnswer1 = pygame.image.load('manAnswer1.png')

choiceContinueStory = pygame.image.load('continuestory.png')
choiceFInal = pygame.image.load('choiceFinal.png')
choiceWoman = pygame.image.load('choiceWoman.png')
choicePhantom = pygame.image.load('choicePhantom.png')

manTalk1 = pygame.image.load('manTalk1.png')
manTalk2 = pygame.image.load('manTalk2.png')

# Initialize pyganim and sounds
pygame.init()
pygame.mixer.init()

# Assigning sound variables
pygame.mixer.music.load("scream1.wav")
pygame.mixer.music.load("scarymusic.ogg")
pygame.mixer.music.load("littlegirlvoice.wav")

mainmusic = pygame.mixer.Sound("scarymusic.ogg")
epicmusic = pygame.mixer.Sound("epicmusic.ogg")
scream1 = pygame.mixer.Sound("scream1.wav")
dooropen = pygame.mixer.Sound('dooropen.wav')

whispersound = pygame.mixer.Sound('whispers.wav')
littlegirlvoice = pygame.mixer.Sound("littlegirlvoice.wav")

phantomsound1 = pygame.mixer.Sound("phantomsound1.wav")
phantomsound2 = pygame.mixer.Sound("phantomsound2.wav")
phantomsound3 = pygame.mixer.Sound("phantomsound3.wav")
phantomsound4 = pygame.mixer.Sound("phantomsound4.wav")
phantomsound5 = pygame.mixer.Sound("phantomsound5.wav")
phantomsound6 = pygame.mixer.Sound("phantomsound6.wav")

phantomScream = pygame.mixer.Sound('phantomScream.wav')

# Set FPS
fpsClock = pygame.time.Clock()

# Set looping picture animations with pyganim
scaryface1Anim = pyganim.PygAnimation([('jumpscary0.jpg',0.1)], loop = False)

dooropenAnim = pyganim.PygAnimation([('dooropen1.png',0.5,),('dooropen2.png',0.1,),
('dooropen3.png',0.1),('dooropen4.png',0.1),('dooropen5.png',3,)], loop = False)

fireAnim = pyganim.PygAnimation([('fire1.png',0.1),('fire2.png',0.1),
('fire3.png',0.1),('fire4.png',0.1)], loop = True)

floatingghost = pyganim.PygAnimation([('ghost1.png',0.3),('ghost2.png',0.3),
('ghost3.png',0.3),('ghost4.png',0.3),('ghost5.png',0.3),('ghost6.png',0.3),
('ghost5.png',0.3),('ghost4.png',0.3),('ghost3.png',0.3),('ghost2.png',0.3)], loop = True)

graveghost = pyganim.PygAnimation([('graveghost1.png',0.3),('graveghost2.png',0.3),
('graveghost3.png',0.3),('graveghost4.png',0.3),('graveghost5.png',0.3),('graveghost6.png',0.3),
('graveghost5.png',0.3),('graveghost4.png',0.3),('graveghost3.png',0.3),('graveghost2.png',0.3)], loop = True)

womanGhost = pyganim.PygAnimation([('womanGhost1.png',0.3),('womanGhost2.png',0.3),
('womanGhost3.png',0.3),('womanGhost4.png',0.3),('womanGhost5.png',0.3),('womanGhost6.png',0.3),
('womanGhost5.png',0.3),('womanGhost4.png',0.3),('womanGhost3.png',0.3),('womanGhost2.png',0.3)], loop = True)

chandelierAnim = pyganim.PygAnimation([('chandelier1.png',0.1),('chandelier2.png',0.1),
('chandelier3.png',0.1),('chandelier4.png',0.1),('chandelier3.png',0.1),('chandelier2.png',0.1),], loop = True)

hallDeathAnim = pyganim.PygAnimation([('falldeath1.png',0.1),('falldeath2.png',0.1),
('falldeath3.png',0.1),('falldeath4.png',0.1),('falldeath5.png',0.1), ('falldeath6.png',0.1),
('falldeath7.png',0.1),('falldeath8.png',0.1), ('falldeath9.png',0.1),('falldeath9.png',10)], loop = False)

riverPhantomAnim = pyganim.PygAnimation([('riverphantom1.png',0.1),('riverphantom2.png',0.1),
('riverphantom3.png',0.1),('riverphantom4.png',0.1),('riverphantom5.png',0.1)], loop = True)

phantomEyesAnim = pyganim.PygAnimation([('phantomeyes1.png',0.1),('phantomeyes2.png',0.1),
('phantomeyes3.png',0.1),('phantomeyes4.png',0.1),('phantomeyes5.png',0.1),('phantomeyes6.png',0.1),
('phantomeyes7.png',0.1),('phantomeyes8.png',0.1)], loop = True)

flameAnim = pyganim.PygAnimation([('flame1.png',0.1),('flame2.png',0.1),('flame3.png',0.1),
('flame4.png',0.1)], loop = True)

ghostvisionAnim = pyganim.PygAnimation([('ghostvision1.png',8),('ghostvision2.png',8),
('ghostvision3.png',8),('ghostvision4.png',0.1),('ghostvision5.png',0.1),('ghostvision6.png',0.1),
('ghostvision7.png',0.1),('ghostvision8.png',10),], loop = False)


ghostManAnim = pyganim.PygAnimation([('manghost1.png',0.2),('manghost2.png',0.2),
('manghost3.png',0.2),('manghost4.png',0.2),('manghost5.png',0.2),('manghost6.png',0.2),
('manghost5.png',0.2),('manghost4.png',0.2),('manghost3.png',0.2),('manghost2.png',0.2),], loop = True)

finalPortalAnim = pyganim.PygAnimation([('finalPortal1.png',0.1),('finalPortal2.png',0.1),
('finalPortal3.png',0.1),('finalPortal4.png',0.1),('finalPortal5.png',0.1),('finalPortal6.png',0.1),], loop = True)

phantomDeathAnim = pyganim.PygAnimation([('phantomDeath1.png',0.1),('phantomDeath2.png',0.1),
('phantomDeath3.png',0.1),('phantomDeath4.png',0.1),('phantomDeath5.png',1),('phantomDeath6.png',10),], loop = False)

spiritdestroyingwoman = pyganim.PygAnimation([('spiritdestroyingwoman1.png',0.1),('spiritdestroyingwoman2.png',0.1),
('spiritdestroyingwoman3.png',0.1),('spiritdestroyingwoman4.png',0.1),('spiritdestroyingwoman5.png',0.1),
('spiritdestroyingwoman6.png',0.5),('spiritdestroyingwoman7.png',0.5),('spiritdestroyingwoman8.png',0.5),
('spiritdestroyingwoman9.png',0.5),('spiritdestroyingwoman10.png',0.5),('spiritdestroyingwoman11.png',0.1),
('spiritdestroyingwoman12.png',0.1),], loop = False)

spiritdestroyingman = pyganim.PygAnimation([('spiritdestroyingman1.png',0.1),('spiritdestroyingman2.png',0.1),
('spiritdestroyingman3.png',0.1),('spiritdestroyingman4.png',0.1),('spiritdestroyingman5.png',0.1),
('spiritdestroyingman6.png',0.5),('spiritdestroyingman7.png',0.5),('spiritdestroyingman8.png',0.5),
('spiritdestroyingman9.png',0.5),('spiritdestroyingman10.png',0.5),('spiritdestroyingman11.png',0.1),
('spiritdestroyingman12.png',0.1)], loop = False)

fireAnim.play()
mainClock = pygame.time.Clock()

mainmusic.play(loops= -1)

# Define rooms
def intro():
    screen.blit(background0, (0,0))
    fireAnim.play()
    pygame.display.update()
    mainClock.tick(30)
    while True: # main loop
        fireAnim.blit(screen,(65,110))
        fireAnim.blit(screen,(485,110))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                return

def screen1():
    screen.blit(background2scaryface1,(0,0))
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(background1,(0,0))
                screen.blit(choice1,(50,10))
                screen.blit(choice2, (50, 75))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choice1, (50, 10))
                b = screen.blit(choice2, (50, 75))
                if a.collidepoint(pos):
                    dooropen.play()
                    return
                if b.collidepoint(pos):
                    scaryFace1()

def scaryFace1():
    screen.blit(blackbackground, (0,0))
    dooropenAnim.play()
    pygame.display.update()
    mainClock.tick(30)
    scaryface1Anim.play()
    scream1.play()
    while True: # main loop
        scaryface1Anim.blit(screen,(320,240))
        pygame.display.update()
        time.sleep(0.2)
        screen.blit(background2scaryface2,(0,0))
        pygame.display.update()
        mainClock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                pygame.quit()
                sys.exit()

def screen2():
    screen.blit(background2, (0,0))
    dooropenAnim.play()
    pygame.display.update()
    mainClock.tick(30)
    while True: # main loop
        fireAnim.blit(screen,(65,110))
        fireAnim.blit(screen,(485,110))
        dooropenAnim.blit(screen,(220,75))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                return

def screen3():
    pygame.display.update()
    while True:
        floatingghost.blit(screen,(200,20))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(background3,(0,0))
                floatingghost.play()
                screen.blit(choiceleft1,(50,100))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceleft1, (50, 100))
                b = screen.blit(choiceright1,(400, 100))
                c = screen.blit(choicedown,(420, 360))
                if a.collidepoint(pos):
                    floatingghost.stop()
                    pygame.display.update()
                    ChoiceLeft1()
                if b.collidepoint(pos):
                    floatingghost.stop()
                    ChoiceRight1()
                if c.collidepoint(pos):
                    floatingghost.stop()
                    ChoiceDown()

def ChoiceLeft1():
    screen.blit(background4,(0,0))
    flameAnim.play()
    pygame.display.update()
    while True:
        flameAnim.blit(screen,(110,160))
        flameAnim.blit(screen,(480,165))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceContinue,(200,100))
                screen.blit(choicerightDC,(350, 275))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceContinue, (200, 100))
                b = screen.blit(choicerightDC,(350, 275))
                pygame.display.update()
                if a.collidepoint(pos):
                    Graves()
                    pygame.display.update()
                if b.collidepoint(pos):
                    pygame.display.update()
                    return

def ChoiceRight1():
    screen.blit(background3picright,(0,0))
    chandelierAnim.play()
    pygame.display.update()
    while True:
        chandelierAnim.blit(screen,(250,00))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceManEncounter,(150,100))
                screen.blit(choicejump,(250,220))
                screen.blit(choiceleftDC,(0, 310))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choicejump, (250, 220))
                b = screen.blit(choiceleftDC,(0, 310))
                c = screen.blit(choiceManEncounter,(150,100))
                pygame.display.update()
                if a.collidepoint(pos):
                    hallDeath()
                if b.collidepoint(pos):
                    pygame.display.update()
                    return
                if c.collidepoint(pos):
                    manEncounter()

def ChoiceDown():
    screen.blit(background3picdown,(0,0))
    riverPhantomAnim.play()
    whispersound.play()
    pygame.display.update()
    while True:
        riverPhantomAnim.blit(screen,(230,140))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choicetalk,(300,200))
                screen.blit(choiceleftDC,(0, 300))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choicetalk, (300, 200))
                b = screen.blit(choiceleftDC,(0, 300))
                pygame.display.update()
                if a.collidepoint(pos):
                    phantomTalk()
                if b.collidepoint(pos):
                    whispersound.stop()
                    pygame.display.update()
                    return

def Graves():
    screen.blit(background5,(0,0))
    graveghost.play()
    pygame.display.update()
    littlegirlvoice.play()
    while True:
        graveghost.blit(screen,(553,70))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choicetalk,(380,200))
                screen.blit(choiceleft1,(10, 400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choicetalk, (380, 200))
                b = screen.blit(choiceleft1,(10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    ghostVision()
                    pygame.display.update()
                if b.collidepoint(pos):
                    screen.blit(background4,(0,0))
                    pygame.display.update()
                    return

def manEncounter():
    screen.blit(manRoom,(0,0))
    ghostManAnim.play()
    pygame.display.update()
    while True:
        ghostManAnim.blit(screen,(553,70))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choicetalk,(380,200))
                screen.blit(choiceleft1,(10, 400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choicetalk, (380, 200))
                b = screen.blit(choiceleft1,(10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    manVision()
                    pygame.display.update()
                if b.collidepoint(pos):
                    screen.blit(background3picright,(0,0))
                    pygame.display.update()
                    return

def manVision():
    screen.blit(blackbackground,(0,0))
    screen.blit(manTalk1,(0,0))
    pygame.display.update()
    while True:
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceManAnswer1,(10,400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceManAnswer1, (10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    pygame.display.update()
                    manVision2()
                    return

def manVision2():
    screen.blit(blackbackground,(0,0))
    screen.blit(manTalk2,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceHelp,(10,380))
                screen.blit(choiceRun,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceHelp, (10, 380))
                b = screen.blit(choiceRun,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    finalPortal()
                    pygame.display.update()
                if b.collidepoint(pos):
                    screen.blit(blackbackground,(0,0))
                    screen.blit(manRoom,(0,0))
                    pygame.display.update()
                    return

def ghostVision():
    screen.blit(blackbackground,(0,0))
    ghostvisionAnim.play()
    pygame.display.update()
    while True:
        ghostvisionAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceHelp, (10, 380))
                b = screen.blit(choiceRun,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    littlegirlvoice.stop()
                    finalPortal()
                    pygame.display.update()
                    return
                if b.collidepoint(pos):
                    screen.blit(background5,(0,0))
                    pygame.display.update()
                    return

def finalPortal():
    screen.blit(blackbackground,(0,0))
    ghostManAnim.play()
    womanGhost.play()
    screen.blit(portaltalk1,(0,0))
    pygame.display.update()
    while True:
        ghostManAnim.blit(screen,(555,100))
        womanGhost.blit(screen,(10,120))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceContinueStory,(10,400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceContinueStory, (10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    pygame.display.update()
                    finalPortal2()
                    finalPortal3()
                    finalPortal4()
                    finalPortal5()
                    finalPortal6()
                    return

def finalPortal2():
    screen.blit(portaltalk2,(0,0))
    ghostManAnim.play()
    womanGhost.play()
    pygame.display.update()
    while True:
        womanGhost.blit(screen,(10,120))
        ghostManAnim.blit(screen,(555,100))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceContinueStory,(10,400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceContinueStory, (10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    return

def finalPortal3():
    screen.blit(portaltalk3,(0,0))
    ghostManAnim.play()
    womanGhost.play()
    pygame.display.update()
    while True:
        womanGhost.blit(screen,(10,120))
        ghostManAnim.blit(screen,(555,100))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceContinueStory,(10,400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceContinueStory, (10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    return

def finalPortal4():
    screen.blit(portaltalk4,(0,0))
    ghostManAnim.play()
    womanGhost.play()
    pygame.display.update()
    while True:
        womanGhost.blit(screen,(10,120))
        ghostManAnim.blit(screen,(555,100))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceContinueStory,(10,400))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceContinueStory, (10, 400))
                pygame.display.update()
                if a.collidepoint(pos):
                    screen.blit(blackbackground,(0,0))
                    screen.blit(portaltalk5,(0,0))
                    pygame.display.update()
                    return

def finalPortal5():
    screen.blit(portaltalk5,(0,0))
    ghostManAnim.play()
    womanGhost.play()
    pygame.display.update()
    while True:
        womanGhost.blit(screen,(10,120))
        ghostManAnim.blit(screen,(555,100))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceFInal,(350,375))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceFInal,(350,375))
                pygame.display.update()
                if a.collidepoint(pos):
                    screen.blit(blackbackground,(0,0))
                    screen.blit(portaltalk5,(0,0))
                    pygame.display.update()
                    return

def finalPortal6():
    screen.blit(blackbackground,(0,0))
    mainmusic.stop()
    epicmusic.play()
    finalPortalAnim.play()
    ghostManAnim.play()
    womanGhost.play()
    pygame.display.update()
    while True:
        finalPortalAnim.blit(screen,(0,0))
        ghostManAnim.blit(screen,(555,100))
        womanGhost.blit(screen,(10,120))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceWoman,(10,350))
                screen.blit(choicePhantom,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceWoman,(10,350))
                b = screen.blit(choicePhantom,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    choiceManFinal()
                    pygame.display.update()
                if b.collidepoint(pos):
                    choiceWomanFinal()

def hallDeath():
    screen.blit(background3jump, (0,0))
    pygame.display.update()
    mainClock.tick(30)
    hallDeathAnim.play()
    scream1.play()
    while True: # main loop
        hallDeathAnim.blit(screen,(0,0))
        pygame.display.update()
        time.sleep(0.2)
        pygame.display.update()
        mainClock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                pygame.quit()
                sys.exit()

def phantomTalk():
    screen.blit(phantomtalk1,(0,0))
    phantomEyesAnim.play()
    whispersound.stop()
    phantomsound1.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer1,(10,400))
                screen.blit(choiceBAnswer1,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer1, (10, 400))
                b = screen.blit(choiceBAnswer1,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    pygame.display.update()
                    phantomTalk2()
                    phantomTalk3()
                    phantomTalk4()
                    phantomTalk5()
                    phantomTalk6()
                    return
                if b.collidepoint(pos):
                    phantomDeath()

def phantomTalk2():
    screen.blit(phantomtalk2,(0,0))
    phantomEyesAnim.play()
    phantomsound2.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer2,(10,400))
                screen.blit(choiceBAnswer2,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer2, (10, 400))
                b = screen.blit(choiceBAnswer2,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    return
                if b.collidepoint(pos):
                    phantomDeath()

def phantomTalk3():
    screen.blit(phantomtalk3,(0,0))
    phantomEyesAnim.play()
    phantomsound3.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer3,(10,400))
                screen.blit(choiceBAnswer3,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer3, (10, 400))
                b = screen.blit(choiceBAnswer3,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    return
                if b.collidepoint(pos):
                    phantomDeath()

def phantomTalk4():
    screen.blit(phantomtalk4,(0,0))
    phantomEyesAnim.play()
    phantomsound4.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer4,(10,400))
                screen.blit(choiceBAnswer4,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer4, (10, 400))
                b = screen.blit(choiceBAnswer4,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    return
                if b.collidepoint(pos):
                    phantomDeath()

def phantomTalk5():
    screen.blit(phantomtalk5,(0,0))
    phantomEyesAnim.play()
    phantomsound5.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer5,(10,400))
                screen.blit(choiceBAnswer5,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer5, (10, 400))
                b = screen.blit(choiceBAnswer5,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    return
                if b.collidepoint(pos):
                    phantomDeath()

def phantomTalk6():
    screen.blit(phantomtalk6,(0,0))
    phantomEyesAnim.play()
    phantomsound6.play()
    pygame.display.update()
    while True:
        phantomEyesAnim.blit(screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                screen.blit(choiceGAnswer6,(10,400))
                screen.blit(choiceBAnswer6,(10, 435))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = screen.blit(choiceGAnswer6, (10, 400))
                b = screen.blit(choiceBAnswer6,(10, 435))
                pygame.display.update()
                if a.collidepoint(pos):
                    screen.blit(background3picdown,(0,0))
                    pygame.display.update()
                    whispersound.play()
                    return
                    pygame.display.update()
                if b.collidepoint(pos):
                    phantomDeath()

def phantomDeath():
    screen.blit(blackbackground, (0,0))
    pygame.display.update()
    mainClock.tick(30)
    phantomDeathAnim.play()
    phantomScream.play()
    while True: # main loop
        phantomDeathAnim.blit(screen,(0,0))
        pygame.display.update()
        time.sleep(0.2)
        pygame.display.update()
        mainClock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                pygame.quit()
                sys.exit()

def choiceManFinal():
    screen.blit(blackbackground, (0,0))
    pygame.display.update()
    mainClock.tick(30)
    spiritdestroyingman.play()
    scream1.play()
    while True: # main loop
        spiritdestroyingman.blit(screen,(0,0))
        pygame.display.update()
        time.sleep(0.2)
        pygame.display.update()
        mainClock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                pygame.quit()
                sys.exit()

def choiceWomanFinal():
    screen.blit(blackbackground, (0,0))
    pygame.display.update()
    mainClock.tick(30)
    spiritdestroyingwoman.play()
    scream1.play()
    while True: # main loop
        spiritdestroyingwoman.blit(screen,(0,0))
        pygame.display.update()
        time.sleep(0.2)
        pygame.display.update()
        mainClock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                phantomDeath()

FPS = 30

# Primary gameplay functions called here
intro()
screen1()
screen2()
screen3()
finalPortal()