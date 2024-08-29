from manim import *

import numpy as np

import math

eq_tri = Polygon(ORIGIN,100*RIGHT,50*RIGHT+50*np.sqrt(3)*UP)

def my_rotate(origin, point, angle):
            """
            Rotate a point counterclockwise by a given angle around a given origin.

            The angle should be given in radians.
            """
            ox, oy, oz = origin
            px, py, pz = point

            qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
            qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
            qz = 0
            return np.array([qx, qy, qz])

def add_lines(V):
            W = VGroup()
            for i in range(len(V)-1):
                W.add(Line(V[i],V[i+1]).set_stroke(width=0.75))
            return W
        
def add_points(V): #next iteration
    
    for i in range(len(V)-1):
        
        if(i==0):
            a = np.array(V[np.mod(i,len(V))])
        else:
            a = np.vstack([a,V[np.mod(i,len(V))]])

        a = np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
        new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,-PI/3)
        a = np.vstack([a,new_point])
        a = np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
            
    return np.vstack([a,V[-1]])


class test(MovingCameraScene):
    def construct(self):
        eq_tri.scale(0.05).move_to(ORIGIN)
        self.add(eq_tri)
        #self.wait()
        l = Line(UP,DR)
        s=Square().rotate(np.arctan(l.get_slope())).align_to(l,DOWN)
        self.add(l,s)