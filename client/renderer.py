from __future__ import annotations

import os
import pathlib
import time
from typing import Dict, Union
import pygame
from pygame import freetype
from classes.color4 import color4
from classes.sharedUtil import rawSet

from gui.instance import instance

pygame.init()
freetype.init()

class renderer:
    rendererClosing: bool
    lastUpdate: float
    lastEvents: list[pygame.event.Event]

    children: list[instance]

    fonts: Dict[str, pygame.font.Font]

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
        if to:
            if inst in to.children: return;
            rawSet(inst, 'parent', to);
            to.children.append(inst);
        else:
            if inst.parent:
                inst.parent.children.remove(inst);
                rawSet(inst, 'parent', None);

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
                child.update(dt)

            pygame.display.flip()

            clock.tick(self.framerate);
    
    def loadFont(self, fontAlias: str, fontPath: str, defaultFontSize: int = 20):
        """
        parameter [fontAlias] is automatically made lowercase
        parameter [fontPath] should be the absolute path to the font file
        """
        try:
            if os.path.isfile(fontPath) and fontPath.split('.')[len(fontPath.split('.')) - 1] == 'ttf':
                font = pygame.font.Font(fontPath, defaultFontSize)

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