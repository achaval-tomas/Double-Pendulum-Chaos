from pygame import Surface, Color, Vector2, draw
from setup import *
from math import sin, cos, dist, pow

class System:
    def __init__(self, g=1, m1=50, m2=75, r1=100, r2=250, a1=3*pi/4, a2=3*pi/4, color="goldenrod1"):
        self.cvs = Surface((swidth, sheight))
        self.g = g
        self.m1 = m1
        self.m2 = m2
        self.a1 = a1
        self.a2 = a2
        self.r1 = r1
        self.r2 = r2
        self.color = color
        
        self.x1 = p + r1*sin(a1)
        self.y1 = q + r1*cos(a1)
        self.x2 = self.x1 + r2*sin(a2)
        self.y2 = self.y1 + r2*cos(a2)
        self.v1 = 0
        self.v2 = 0
        self.px2 = 0
        self.py2 = 0

    def updatesystem(self, canvas, screen):
        self.cvs.set_colorkey((0, 0, 0))
        self.cvs.fill((0, 0, 0))
        
        self.px2 = self.x2
        self.py2 = self.y2

        self.x1 = p + self.r1*sin(self.a1)
        self.y1 = q + self.r1*cos(self.a1)
        self.x2 = self.x1 + self.r2*sin(self.a2)
        self.y2 = self.y1 + self.r2*cos(self.a2)

        # PENDULUM PATH TRACING
        draw.line(canvas, self.color, Vector2(self.px2, self.py2), Vector2(self.x2, self.y2), 2)
        screen.blit(canvas, (0,0))

        # PENDULUM DRAWING
        intensity = 50 + int(dist((self.px2,self.py2), (self.x2, self.y2)))*4
        line_color = Color(intensity, intensity, intensity)
        draw.line(self.cvs, line_color, Vector2(p,q), Vector2(self.x1, self.y1), 5)
        draw.line(self.cvs, line_color, Vector2(self.x1,self.y1), Vector2(self.x2, self.y2), 5)
        draw.circle(self.cvs, self.color, Vector2(self.x1, self.y1), self.m1/4)
        draw.circle(self.cvs, self.color, Vector2(self.x2, self.y2), self.m2/4)

        num1 = -1 * self.g * (2 * self.m1 + self.m2) * sin(self.a1)
        num2 = -1 * self.m2 * self.g * sin(self.a1 - 2*self.a2)
        num3 = -2 * sin(self.a1 - self.a2) * self.m2
        num4 = pow(self.v2,2) * self.r2 + pow(self.v1, 2) * self.r1 * cos(self.a1 - self.a2)
        den  = self.r1 * (2*self.m1 + self.m2 - self.m2 * cos(2*self.a1 - 2*self.a2))
        acc1 = (num1 + num2 + num3*num4) / den

        num1 = 2 * sin(self.a1 - self.a2)
        num2 = pow(self.v1, 2) * self.r1 * (self.m1 + self.m2)
        num3 = self.g * (self.m1 + self.m2) * cos(self.a1)
        num4 = pow(self.v2,2) * self.r2  * self.m2 * cos(self.a1 - self.a2)
        den  = self.r2 * (2*self.m1 + self.m2 - self.m2 * cos(2*self.a1 - 2*self.a2))
        acc2 = ( num1*(num2 + num3 + num4) ) / den

        self.v1 += acc1
        self.v2 += acc2
        self.a1 += self.v1
        self.a2 += self.v2
    
    def show(self, screen):
        screen.blit(self.cvs, (0,0))