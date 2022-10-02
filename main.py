from classes.color4 import color4
from classes.udim2 import udim2
#from classes.udim2 import udim2
from client.renderer import renderer, gameLoop
import pygame
from gui.guiObject import guiObject
from gui.textLabel import textLabel

#from gui.guiObject import guiObject

mainRenderer = renderer(pygame.Vector2(1000, 700), 0, color4(1, 1, 1))

gameLoop.setRenderer(mainRenderer)

frame = guiObject()

frame.backgroundColor = color4.fromRGBA(0, 255, 255, 200)

frame.size = udim2.fromScale(.8, .6)

frame.position = udim2.fromScale(.1, .1)

frame.dropShadowOffset = udim2.fromOffset(5, 5)

frame.parent = mainRenderer

txt1 = textLabel()
txt1.parent = frame
txt1.zindex = 6
txt1.text = "hello 1"

txt2 = textLabel()
txt2.parent = frame
txt2.zindex = 4
txt2.size = udim2(0, .9, 0, .9)
txt2.position = udim2(0, .05, 0, .05)
txt2.backgroundColor = color4(.5, .3, .7, 1)
txt2.text = "hello 2"
txt2.cornerRadius = 0
txt2.textAlignX = 'center'
txt2.textAlignY = 'center'
txt2.textColor = color4(1, 1, 1, 1)
txt2.textSize = 64

mainRenderer.start()

#next: buttons & gui corners