from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.textObject import textObject

class textButton(textObject):

    enabled: bool
    
    def __init__(self):
        super().__init__()

        LoadDefaultGuiProperties('textButton', self)

    def update(self, dt: float):
        super().update(dt)
        self.renderText()

