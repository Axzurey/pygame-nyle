from typing import Any

from pygame import Vector2


class hoverable: ...

class clickable:
    def isPointInBounding(self: Any, point: Vector2):
        #https://math.stackexchange.com/questions/3630329/how-to-check-if-a-point-px-y-lies-inside-a-rounded-rectangle
        if self.absolutePosition and self.absoluteSize:
            cornerRadius = self.cornerRadius or 0
            pos: Vector2 = self.absolutePosition
            size: Vector2 = self.absoluteSize

            if point.x > pos.x + size.x or point.x < pos.x: return False #not in the bounding rectangle
            if point.y > pos.y + size.y or point.y < pos.y: return False #not in the bounding rectangle
            pass    