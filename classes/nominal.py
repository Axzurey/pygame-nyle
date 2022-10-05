from typing import Any

from pygame import Vector2
import pygame

class hoverable: ...

class clickable:
    def isPointInBounding(self: Any, m: Vector2):
        #https://math.stackexchange.com/questions/3630329/how-to-check-if-a-point-px-y-lies-inside-a-rounded-rectangle
        if self.boundingRect:
            r = self.cornerRadius or 0
            br: pygame.Rect = self.boundingRect
            
            (a, b, c, d) = (Vector2(br.topleft), Vector2(br.topright), Vector2(br.bottomright), Vector2(br.bottomleft))

            (x1, y1) = (a.x, a.y)
            (x2, y2) = (b.x, b.y)
            (x3, y3) = (c.x, c.y)
            (x4, y4) = (d.x, d.y)
            (xp, yp) = (m.x, m.y)

            D1 = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1)
            D2 = (x3 - x2) * (yp - y2) - (xp - x2) * (y3 - y2)
            D3 = (x4 - x3) * (yp - y3) - (xp - x3) * (y4 - y3)
            D4 = (x1 - x4) * (yp - y4) - (xp - x4) * (y1 - y4)

            if D1 > 0 and D2 > 0 and D3 > 0 and D4 > 0:
                sq1c1 = pos + size - Vector2(r, r)
                sq1c2 = pos + size

                sq2c1 = pos
                sq2c2 = pos + Vector2(r, r)

                sq3c1 = pos + Vector2(0, size.y)
                sq3c2 = pos + Vector2(0, size.y) + Vector2(r, -r)

                sq4c1 = pos + Vector2(size.x, 0)
                sq4c2 = pos + Vector2(size.x, 0) + Vector2(-r, r)
                
            else:
                return False