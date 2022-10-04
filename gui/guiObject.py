from typing import Literal, Union
from classes.color4 import color4
from classes.nominal import hoverable
from classes.sharedUtil import create_neon
from client.renderer import gameLoop
from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.instance import instance
from classes.udim2 import udim2
from pygame import Vector2
import pygame
import classes.mathf as mathf

class guiObject(instance, hoverable):
    position: udim2
    size: udim2

    absolutePosition: pygame.Vector2
    absoluteSize: pygame.Vector2

    boundingRect: pygame.Rect
    
    rotation: float

    backgroundColor: color4

    borderWidth: int
    borderColor: color4
    
    zindex: int

    cornerRadius: int

    dropShadowColor: color4
    dropShadowRadius: int
    dropShadowOffset: udim2

    def __init__(self):

        super().__init__()

        self.__internal = {
            
        }

        LoadDefaultGuiProperties('guiObject', self);

    def udim2RelativeToSelfSize(self, udim: udim2, relative: Union[Literal['xx'], Literal['xy'], Literal['yy']] = 'xy'):
        size = self.absoluteSize

        fS = udim.toScale()
        fsO = udim.toOffset()

        size = Vector2(mathf.lerp(0, size.x, fS.x) + fsO.x, mathf.lerp(0, size.y, fS.y) + fsO.y)

        if relative == 'xx':
            size.y = size.x
        elif relative == 'yy':
            size.x = size.y
        
        return size

    def getSizeAndPositionFromUdim2(self, positionUdim: udim2, sizeUdim: udim2):
        """
        Returns: (position, size)
        """
        if self.parent and isinstance(self.parent, instance):
            pPos = self.parent.absolutePosition
            pSize = self.parent.absoluteSize

            fP = positionUdim.toScale()
            fpO = positionUdim.toOffset()
            fS = sizeUdim.toScale()
            fsO = sizeUdim.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)
            
            return (position, size)
        
        else:
            container = gameLoop.getRenderer().resolution

            pPos = Vector2(0, 0)
            pSize = Vector2(container.x, container.y)

            fP = positionUdim.toScale()
            fpO = positionUdim.toOffset()
            fS = sizeUdim.toScale()
            fsO = sizeUdim.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)

            return (position, size)

    def update(self, dt: float):

        screen = gameLoop.getRenderer().screen

        #background

        (position, size) = self.getSizeAndPositionFromUdim2(self.position, self.size)

        self.absolutePosition = position
        self.absoluteSize = size

        realSurf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        backgroundRect = pygame.Rect(position.x, position.y, size.x, size.y)

        borderRect = pygame.Rect(position.x - self.borderWidth, position.y - self.borderWidth, size.x + self.borderWidth * 2, size.y + self.borderWidth * 2)

        #borderSurf = pygame.Surface(borderRect.size, pygame.SRCALPHA)

        pygame.draw.rect(realSurf, self.borderColor.toRGBATuple(), borderRect, 0, border_radius=self.cornerRadius)

        pygame.draw.rect(realSurf, self.backgroundColor.toRGBATuple(), backgroundRect, 0, border_radius=self.cornerRadius)

        dropOffset = self.udim2RelativeToSelfSize(self.dropShadowOffset, 'xx')

        dropPos = Vector2(position.x + dropOffset.x,
            position.y + dropOffset.y)

        dropSize = Vector2(size.x + self.dropShadowRadius,
            size.y + self.dropShadowRadius)

        dropNeonRect = pygame.Rect(dropPos, dropSize)

        scrSize = screen.get_size()

        dropShadowSurface = pygame.Surface((scrSize[1], scrSize[0]), pygame.SRCALPHA)

        pygame.draw.rect(dropShadowSurface, self.dropShadowColor.toRGBTuple(), (dropNeonRect.y, dropNeonRect.x, dropNeonRect.h, dropNeonRect.w), border_radius=self.cornerRadius)

        dropNeonSurface = create_neon(dropShadowSurface)

        screen.blit(dropNeonSurface, (0, 0), special_flags = pygame.BLEND_PREMULTIPLIED)

        #screen.blit(borderSurf, borderRect)

        #screen.blit(backSurf, backgroundRect)

        screen.blit(realSurf, (0, 0), special_flags = pygame.BLEND_PREMULTIPLIED)

        self.boundingRect = backgroundRect

        super().update(dt)