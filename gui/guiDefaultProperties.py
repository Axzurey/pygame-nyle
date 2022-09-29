from typing import Any, Dict, Literal, Union
import pygame
from classes.color4 import color4
from classes.udim2 import udim2
from gui.instance import instance

def blankAnyTypedList() -> list[Any]:
    return []

GUI_DEFAULT_PROPERTIES = {
    "parent": lambda: None,
    "children": lambda: blankAnyTypedList(),
    "absoluteSize": lambda: pygame.Vector2(),
    "absolutePosition": lambda: pygame.Vector2(),
    "size": lambda: udim2.fromOffset(150, 50),
    "position": lambda: udim2.fromOffset(0, 0),
    "backgroundColor": lambda: color4(.8, .8, 0),
    "borderColor": lambda: color4(1, 0, 1),
    "borderRadius": lambda: udim2.fromOffset(15, 15),
    "borderWidth": lambda: 5,
    "dropShadowColor": lambda: color4(.2, .2, .2),
    "dropShadowRadius": lambda: 5,
    "dropShadowOffset": lambda: udim2.fromOffset(5, 5),
    "text": lambda: 'Hello World!',
    "textColor": lambda: color4(1, 1, 1),
    "textSize": lambda: 5,
    "textFont": lambda: "NotoSansMono"
}

GUI_PROPERTY_MAP: dict[str, Dict[Union[Literal['properties'], Literal["inherits"]], list[str]]] = {
    "instance": {
        "properties": ["children"],
        "inherits": []
    },
    "guiObject": {
        "properties": [
            "size", "position", "backgroundColor",
            "borderColor", "borderWidth", "dropShadowColor", 
            "dropShadowRadius", "dropShadowOffset", "absolutePosition",
            "absoluteSize"
        ],
        "inherits": ["instance"],
    },
    "textObject": {
        "properties": ["text", "textColor", "textSize", "textFont"],
        "inherits": ["guiObject"]
    }
}

def LoadDefaultGuiProperties(guiType: str, guiObject: instance):
    if GUI_PROPERTY_MAP[guiType]:
        #load inherited properties
        for inh in GUI_PROPERTY_MAP[guiType]["inherits"]:
            LoadDefaultGuiProperties(inh, guiObject)

        #load own properties
        for propKey in GUI_PROPERTY_MAP[guiType]["properties"]:
            if propKey in GUI_DEFAULT_PROPERTIES:
                guiObject[propKey] = GUI_DEFAULT_PROPERTIES[propKey]()
            else:
                raise Exception(f"property {propKey} is not a valid property in the Default Properties map!")

    else:
        raise Exception(f"guiType {guiType} is not a valid type in the property map!")
