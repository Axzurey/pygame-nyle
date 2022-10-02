from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.guiObject import guiObject
from client.renderer import gameLoop
from typing import Literal, Union
from classes.color4 import color4

class textObject(guiObject):

    textFont: str
    textColor: color4
    textSize: int
    text: str
    textAlignX: Union[Literal['left'], Literal['center'], Literal['right']]
    textAlignY: Union[Literal['top'], Literal['center'], Literal['bottom']]

    def __init__(self):
        super().__init__()

        LoadDefaultGuiProperties('textObject', self)

    def renderText(self):

        renderer = gameLoop.getRenderer()

        (textSurf, _) = renderer.fonts[self.textFont].render(self.text, self.textColor.toRGBATuple(), size=self.textSize)

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

        textSize = textSurf.get_size()

        absSize = self.absoluteSize
        absPos = self.absolutePosition
        
        offsetXAbs = absPos.x + (absSize.x - textSize[0]) * textOffsetX
        offsetYAbs = absPos.y + (absSize.y - textSize[1]) * textOffsetY

        renderer.screen.blit(textSurf, (offsetXAbs, offsetYAbs))