from typing import Any

from pygame import Vector2
import pygame
from classes.color4 import color4
from classes.udim2 import udim2

class hoverable: ...

def Corner(DX: float, DY: float, R: float):
    return DX < 0 and DY < 0 and DX * DX + DY * DY > R * R


class clickable:
    def isPointInBounding(self: Any, m: Vector2):

        from gui.guiObject import guiObject
        from client.renderer import gameLoop
        
        if self.boundingRect:
            br: pygame.Rect = self.boundingRect
            r = self.cornerRadius or 0
            if r < 60:
                Top = br.y
                Left = br.x
                X = m.x
                Y = m.y
                (Wdt, Hgt) = br.size
                R = r
                for e in ((Left, Top), (X, Y)):
                    x = guiObject()
                    x.size = udim2.fromOffset(5, 5)
                    x.backgroundColor = color4(1, .5, 1, 1)
                    x.parent = gameLoop.getRenderer()
                    x.position = udim2.fromOffset(e[0], e[1])
            
            """
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
            """
            Top = br.y
            Left = br.x
            X = m.x
            Y = m.y
            (Wdt, Hgt) = br.size
            R = r

            Outside = (X < Left) or (X > Left + Wdt) or (Y < Top) or (Y > Top + Hgt) or Corner(X - Left - R - X, Y - Top - R, R) or Corner(X - Left - R, Top  + Hgt - R - Y, R) or Corner(Left + Wdt - R - X, Top  + Hgt - R - Y, R) or Corner(Left + Wdt - R - X, Y - Top - R, R)

            if Outside: return False
            return True
        else:
            return False