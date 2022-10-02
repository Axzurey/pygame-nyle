from __future__ import annotations

import os
import pathlib
import time
from typing import Dict, Optional, Tuple, Union
import pygame
import pygame.freetype
from classes.color4 import color4
from classes.sharedUtil import rawSet
from gui.instance import instance

pygame.init()
pygame.freetype.init()

freeColorTuple = Tuple[int, int, int, Optional[int]]

class freeFont:

    def render(
        self, text: str, fgcolor: freeColorTuple = (255, 255, 255, 255), bgColor: freeColorTuple = (0, 0, 0, 0),
        rotation: int = 0, size: int = 16
    ) -> Tuple[pygame.Surface, pygame.Rect]: ...

class renderer:
    rendererClosing: bool
    lastUpdate: float
    lastEvents: list[pygame.event.Event]

    children: list[instance]

    fonts: Dict[str, freeFont]

    def __init__(self, resolution: pygame.Vector2, framerate: int, backgroundColor: color4):
        self.rendererClosing = False;
        self.lastUpdate = time.time()
        self.lastEvents = []
        self.children = []
        self.fonts = {}


        self.backgroundColor = backgroundColor;

        self.framerate = framerate;

        self.resolution = resolution;

        self.screen = pygame.display.set_mode((resolution.x, resolution.y))

        self.loadDefaultFonts()

    @staticmethod
    def setParent(inst: instance, to: Union[renderer, instance, None]):
        print(inst, to)
        if to:
            if inst in to.children: return;
            rawSet(inst, 'parent', to);
            to.children.append(inst);
            print(id(to.children), id(inst.children))
        else:
            if inst.parent:
                inst.parent.children.remove(inst);
                rawSet(inst, 'parent', None);

    def recurseUpdate(self, inst: instance, dt: float):
        inst.update(dt)

        childrenPriority: list[instance] = []
        childrenLast: list[instance] = []

        for child in inst.children:
            if type(child["zindex"]) is int:
                childrenPriority.append(child)
            else:
                childrenLast.append(child)

        childrenPriority.sort(key=lambda x: x["zindex"])

        print(inst, len(childrenPriority), len(childrenLast), inst.children)

        for child in childrenPriority: self.recurseUpdate(child, dt)

        for child in childrenLast: self.recurseUpdate(child, dt)


    def start(self):
        clock = pygame.time.Clock()

        while (not self.rendererClosing):

            now = time.time()

            dt = now - self.lastUpdate;

            self.lastUpdate = now;

            events = pygame.event.get()
            self.lastEvents = events;

            for event in events:
                if event.type == pygame.QUIT:
                    self.rendererClosing = True;

            self.screen.fill(self.backgroundColor.toRGBTuple())

            for child in self.children:
                self.recurseUpdate(child, dt)

            pygame.display.flip()

            clock.tick(self.framerate);
    
    def loadFont(self, fontAlias: str, fontPath: str, defaultFontSize: int = 20):
        """
        parameter [fontAlias] is automatically made lowercase
        parameter [fontPath] should be the absolute path to the font file
        """
        try:
            if os.path.isfile(fontPath) and fontPath.split('.')[len(fontPath.split('.')) - 1] == 'ttf':
                font: freeFont = pygame.freetype.Font(fontPath, defaultFontSize) #type: ignore

                self.fonts[fontAlias.lower()] = font
            else:
                print(f'[nyle]: Unable to load font "{fontAlias.lower()}" from path {fontPath} as it is not .ttf file')
        except Exception:
            print(f'[nyle]: (Unexpected) Unable to load font "{fontAlias.lower()}" from path {fontPath}')
    
    def loadDefaultFonts(self):
        searchDir = os.path.join(str(pathlib.Path(__file__).parent.parent.resolve()), 'fonts')
        if os.path.isdir(searchDir):
            for p in os.listdir(searchDir):
                self.loadFont(os.path.basename(p.split('.')[0]), os.path.join(searchDir, p))
        else:
            print(f'[nyle]: Unable to load default fonts from {searchDir} as it is not a folder')


class __gameLoop:
    def setRenderer(self, renderer: renderer):
        self.renderer = renderer;

    def getRenderer(self) -> renderer:
        return self.renderer


gameLoop = __gameLoop();