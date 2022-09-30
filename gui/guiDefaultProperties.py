from typing import Any, Dict, Literal
import pygame
from classes.color4 import color4
from classes.sharedUtil import rawSet
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
    "dropShadowOffset": lambda: udim2.fromOffset(2, 2),
    "text": lambda: 'Hello World!',
    "textColor": lambda: color4(.5, .5, .5),
    "textSize": lambda: 5,
    "textFont": lambda: "notosansmono-regular",
    "textAlignX": lambda: "left",
    "textAlignY": lambda: "top"
}

GUI_PROPERTY_MAP: dict[str, Dict[Literal['properties'], list[str]]] = {
    "instance": {
        "properties": ["children"],
    },
    "guiObject": {
        "properties": [
            "size", "position", "backgroundColor",
            "borderColor", "borderWidth", "dropShadowColor", 
            "dropShadowRadius", "dropShadowOffset", "absolutePosition",
            "absoluteSize"
        ],
    },
    "textLabel": {
        "properties": ["text", "textColor", "textSize", "textFont", "left", "top"],
    }
}

def LoadDefaultGuiProperties(guiType: str, guiObject: instance):
    print('init for', guiType)
    if GUI_PROPERTY_MAP[guiType]:
        #load own properties
        for propKey in GUI_PROPERTY_MAP[guiType]["properties"]:
            if propKey in GUI_DEFAULT_PROPERTIES:
                rawSet(guiObject, propKey, GUI_DEFAULT_PROPERTIES[propKey]())
            else:
                raise Exception(f"property {propKey} is not a valid property in the Default Properties map!")

    else:
        raise Exception(f"guiType {guiType} is not a valid type in the property map!")
