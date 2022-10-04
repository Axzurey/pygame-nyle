from __future__ import annotations

import os
import pathlib
from classes.nyleSignal import NyleSignal
import time
from typing import Dict, Literal, Optional, Tuple, TypedDict, Union
import pygame
import pygame.freetype
from classes.color4 import color4
from classes.nominal import clickable, hoverable
from classes.sharedUtil import rawSet
from gui.instance import instance
from modules.pyKeyMap import keyBuffer, purifyRawKeyBuffer

pygame.init()
pygame.freetype.init()

freeColorTuple = Tuple[int, int, int, Optional[int]]

class rendererListeners(TypedDict):
    keyUp: NyleSignal[keyBuffer]
    keyDown: NyleSignal[keyBuffer]

class actionPassList(TypedDict):
    mouseLifted: bool
    mousePressed: bool
    mouseScrolling: bool
    mouseScrollDirection: pygame.Vector2

class actionOrder(TypedDict):
    at: float
    obj: instance

class actionOrdersT(TypedDict):
    hover: list[actionOrder]
    click: list[actionOrder]

class mouseClickBuffer(TypedDict):
    x: int
    y: int
    clickType: Literal['right'] | Literal['left'] | Literal['middle']

class updateBuffer(TypedDict):
    mouseBuffer: mouseClickBuffer
    actionOrders: actionOrdersT
    actionList: actionPassList
    lastButton: actionOrder | None

class freeFont:

    def render(
        self, text: str, fgcolor: freeColorTuple = (255, 255, 255, 255), bgColor: freeColorTuple = (0, 0, 0, 0),
        rotation: int = 0, size: int = 16
    ) -> Tuple[pygame.Surface, pygame.Rect]: ...

class renderer:
    rendererClosing: bool
    lastUpdate: float
    lastEvents: list[pygame.event.Event]

    listeners: rendererListeners

    children: list[instance]

    fonts: Dict[str, freeFont]

    def __init__(self, resolution: pygame.Vector2, framerate: int, backgroundColor: color4):
        self.rendererClosing = False;
        self.lastUpdate = time.time()
        self.lastEvents = []
        self.children = []
        self.fonts = {}

        self.listeners = {
            "keyUp": NyleSignal[keyBuffer](),
            "keyDown": NyleSignal[keyBuffer]()
        }


        self.backgroundColor = backgroundColor;

        self.framerate = framerate;

        self.resolution = resolution;

        self.screen = pygame.display.set_mode((resolution.x, resolution.y))

        self.loadDefaultFonts()

    def recurseUpdate(self, inst: instance, dt: float, update: updateBuffer):
        inst.update(dt)

        childrenPriority: list[instance] = []
        childrenLast: list[instance] = []

        for child in inst.children:
            if type(child["zindex"]) is int:
                childrenPriority.append(child)
            else:
                childrenLast.append(child)

        childrenPriority.sort(key=lambda x: x["zindex"])

        for child in childrenPriority:
            if issubclass(type(child), clickable):
                update['actionOrders']['click'].append({"obj": child, "at": time.time()})
                t = time.time()
                if child['absolutePosition'] and child['absoluteSize']:

            if issubclass(type(child), hoverable):
                update['actionOrders']['hover'].append({"obj": child, "at": time.time()})
            return self.recurseUpdate(child, dt, update)

        for child in childrenLast:
            if issubclass(type(child), clickable):
                update['actionOrders']['click'].append({"obj": child, "at": time.time()})
            if issubclass(type(child), hoverable):
                update['actionOrders']['hover'].append({"obj": child, "at": time.time()})
            return self.recurseUpdate(child, dt, update)

        return (update['actionOrders'])


    def start(self):
        clock = pygame.time.Clock()

        while (not self.rendererClosing):

            now = time.time()

            dt = now - self.lastUpdate;

            self.lastUpdate = now;

            events = pygame.event.get()
            self.lastEvents = events;

            passList: actionPassList = {
                "mouseLifted": False,
                "mousePressed": False,
                "mouseScrolling": False,
                "mouseScrollDirection": pygame.Vector2(),
            }

            keysUp: list[int] = []
            keysDown: list[int] = []
            modifiers: list[int] = []

            for event in events:
                if event.type == pygame.QUIT:
                    self.rendererClosing = True;
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    passList['mousePressed'] = True;
                elif event.type == pygame.MOUSEBUTTONUP:
                    passList['mouseLifted'] = True
                elif event.type == pygame.MOUSEWHEEL:
                    passList['mouseScrolling'] = True
                    passList["mouseScrollDirection"] = pygame.Vector2(event.x, event.y)
                elif event.type == pygame.KEYDOWN:
                    keysDown.append(event.key)
                    if not event.mod in modifiers:
                        modifiers.append(event.mod)
                elif event.type == pygame.KEYUP:
                    keysUp.append(event.key)
                    if not event.mod in modifiers:
                        modifiers.append(event.mod)

            upKeyBuffer = purifyRawKeyBuffer({
                "keys": keysUp,
                "modifiers": modifiers
            })
            
            downKeyBuffer = purifyRawKeyBuffer({
                "keys": keysDown,
                "modifiers": modifiers
            })

            self.listeners["keyDown"].emit(downKeyBuffer)
            self.listeners['keyUp'].emit(upKeyBuffer)

            self.screen.fill(self.backgroundColor.toRGBTuple())

            mouseBuffer: mouseClickBuffer = {
                'x': 0,
                'y': 0,
                'clickType': 'left'
            }

            for child in self.children:
                (actionOrders, clickTarget) = self.recurseUpdate(child, dt, {
                    "actionOrders": {
                        'hover': [],
                        'click': []
                    },
                    "actionList": passList,
                    "mouseBuffer": mouseBuffer,
                    "lastButton": None
                })

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


class __gameLoop:
    def setRenderer(self, renderer: renderer):
        self.renderer = renderer;

    def getRenderer(self) -> renderer:
        return self.renderer


gameLoop = __gameLoop();