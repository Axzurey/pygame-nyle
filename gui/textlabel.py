from classes.color4 import color4
from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.guiObject import guiObject
from client.renderer import gameLoop

class textlabel(guiObject):

    textFont: str
    textColor: color4
    textSize: int
    text: str
    
    def __init__(self):
        super().__init__()

        LoadDefaultGuiProperties('textLabel', self)

    def update(self, dt: float):
        super().update(dt)

        renderer = gameLoop.getRenderer()

        textSurf = renderer.fonts[self.textFont].render(self.text, True, self.textColor.toRGBTuple())

        renderer.screen.blit(textSurf, self.absolutePosition)