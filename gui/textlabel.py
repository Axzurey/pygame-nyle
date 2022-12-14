from gui.guiDefaultProperties import LoadDefaultGuiProperties
from gui.textObject import textObject

class textLabel(textObject):
    
    def __init__(self):
        super().__init__()

        LoadDefaultGuiProperties('textLabel', self)

    def update(self, dt: float):
        super().update(dt)
        self.renderText()

