from typing import Literal, Union
from classes.color4 import color4
from classes.udim2 import udim2
from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.guiObject import guiObject
from client.renderer import gameLoop

class textlabel(guiObject):

    textFont: str
    textColor: color4
    textSize: int
    text: str
    textAlignX: Union[Literal['left'], Literal['center'], Literal['right']]
    textAlignY: Union[Literal['top'], Literal['center'], Literal['bottom']]
    
    def __init__(self):
        super().__init__()

        LoadDefaultGuiProperties('textLabel', self)

    def update(self, dt: float):
        super().update(dt)

        renderer = gameLoop.getRenderer()

        textSurf = renderer.fonts[self.textFont].render(self.text, True, self.textColor.toRGBTuple())

        textOffsetX = 0
        textOffsetY = 0

        if self.textAlignX == 'right':
            textOffsetX = 1
        elif self.textAlignX == 'center':
            textOffsetX = .5
        else:
            textOffsetX = 0

        if self.textAlignY == 'bottom':
            textOffsetY = 1
        elif self.textAlignY == 'center':
            textOffsetY = .5
        else:
            textOffsetY = 0

        textOffsetUdim = udim2.fromScale(textOffsetX, textOffsetY)

        #multiply ^ by abs pos in screen space?

        renderer.screen.blit(textSurf, self.absolutePosition)