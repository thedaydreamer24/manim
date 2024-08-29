#koch.py
from manim import *

import numpy as np

import math



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


class CheckKoch(MovingCameraScene):
    def construct(self):
        
        koch1 = RegularPolygon(3).scale(2)
        self.play(Write(koch1))
        self.wait(2)

        koch2 = koch1.copy()
        verts = koch2.get_vertices()
        new_verts = []

        for i in range( len(verts) - 1 ):
            new_verts = np.append(new_verts,verts[i])
            new_verts = np.append(new_verts,2/3*verts[i]+1/3*verts[i+1])
            new_verts = np.append(new_verts,1/3*verts[i]+2/3*verts[i+1])
        
        #new_verts.reshape((len(new_verts),3))
        #self.add(Text(str(len(new_verts))))
        
        for v in range(int(len(new_verts)/3)):
            self.play(Write(Dot(np.array([new_verts[3*v],new_verts[3*v+1],new_verts[3*v+2]]))))
        self.wait(2)
        
class NewKoch(Scene):
    def construct(self):
        
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

        points=[LEFT,RIGHT]
        line1 = add_lines(points)
        line2 = add_lines(add_points(points))
        line3 = add_lines(add_points(add_points(points)))
        line4 = add_lines(add_points(add_points(add_points(points))))
        line5 = add_lines(add_points(add_points(add_points(add_points(points)))))

        self.play(Create(line1.shift(2.5*2*LEFT)))
        self.wait()
        self.play(Create(line2.shift(2.5*LEFT)))
        #self.play(AnimationGroup(FadeOut(line1),FadeIn(line2)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line3))
        #self.play(AnimationGroup(FadeOut(line2),FadeIn(line3)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line4.shift(2.5*RIGHT)))
        #self.play(AnimationGroup(FadeOut(line3),FadeIn(line4)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line5.shift(2*2.5*RIGHT)))
        #self.play(AnimationGroup(FadeOut(line4),FadeIn(line5)),lag_ratio=0.5,run_time=2)
        self.wait(5)

class NewKoch2(MovingCameraScene):
    def construct(self):
        
        def add_lines(V):
            W = VGroup()
            for i in range(len(V)-1):
                W.add(Line(V[i],V[i+1]).set_stroke(width=1))
            return W
        
        def add_points(V): #next iteration
            
            for i in range(len(V)-1):
                if(i==0):
                    a=np.array(V[np.mod(i,len(V))])
                else:
                    a=np.vstack([a,V[np.mod(i,len(V))]])
                a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,-PI/3)
                a=np.vstack([a,new_point])
                a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])    
                    
            return np.vstack([a,V[-1]])

        points=[1000*LEFT,1000*RIGHT]

        line1 = add_lines(points).scale(3/1000).move_to(ORIGIN)
        line2 = add_lines(add_points(points)).scale(3/1000).move_to(ORIGIN)
        line3 = add_lines(add_points(add_points(points))).scale(3/1000).move_to(ORIGIN)
        line4 = add_lines(add_points(add_points(add_points(points)))).scale(3/1000).move_to(ORIGIN)
        line5 = add_lines(add_points(add_points(add_points(add_points(points))))).scale(3/1000).move_to(ORIGIN)
        line6 = add_lines(add_points(add_points(add_points(add_points(add_points(points)))))).scale(3/1000).move_to(ORIGIN)

        self.play(Create(line1))
        self.wait()
        self.play(AnimationGroup(FadeOut(line1),FadeIn(line2)),lag_ratio=0.75,run_time=2)
        self.wait(2)
        self.play(AnimationGroup(FadeOut(line2),FadeIn(line3)),lag_ratio=0.75,run_time=2)
        self.wait(2)
        self.play(AnimationGroup(FadeOut(line3),FadeIn(line4)),lag_ratio=0.75,run_time=2)
        self.wait(2)
        self.play(AnimationGroup(FadeOut(line4),FadeIn(line5)),lag_ratio=0.75,run_time=2)
        self.wait(2)
        self.play(AnimationGroup(FadeOut(line5),FadeIn(line6)),lag_ratio=0.75,run_time=2)
        self.wait(2)
        self.play(*[k.animate.set_stroke(width=DEFAULT_STROKE_WIDTH*0.025) for k in line6],self.camera.frame.animate.scale(0.025).move_to(line6.get_top()),run_time=15)
        self.wait()



class Koch_full(Scene):
    def construct(self):
        
        def add_lines(V):
            W = VGroup()
            for i in range(len(V)):
                W.add(Line(V[i],V[np.mod(i+1,len(V))]).set_stroke(width=0.75))
            return W
        
        def add_points(V): #next iteration
            
            for i in range(len(V)):
                if(i==0):
                    a=np.array(V[np.mod(i,len(V))])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                else:
                    a=np.vstack([a,V[np.mod(i,len(V))]])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                    
            return a

        points=[LEFT,RIGHT,math.sqrt(3)*UP]
        line1 = add_lines(points)
        line2 = add_lines(add_points(points))
        line3 = add_lines(add_points(add_points(points)))
        line4 = add_lines(add_points(add_points(add_points(points))))
        line5 = add_lines(add_points(add_points(add_points(add_points(points)))))

        self.play(Create(line1.shift(2.5*2*LEFT)),run_time=2)
        self.wait()
        self.play(Create(line2.shift(2.5*LEFT)),run_time=2)
        #self.play(AnimationGroup(FadeOut(line1),FadeIn(line2)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line3),run_time=2)
        #self.play(AnimationGroup(FadeOut(line2),FadeIn(line3)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line4.shift(2.5*RIGHT)),run_time=3)
        #self.play(AnimationGroup(FadeOut(line3),FadeIn(line4)),lag_ratio=0.5,run_time=2)
        self.wait()
        self.play(Create(line5.shift(2*2.5*RIGHT)),run_time=4)
        #self.play(AnimationGroup(FadeOut(line4),FadeIn(line5)),lag_ratio=0.5,run_time=2)
        self.wait(5)

class Koch_full_main(MovingCameraScene):
    def construct(self):
        
        def add_lines(V):
            W = VGroup()
            for i in range(len(V)):
                W.add(Line(V[i],V[np.mod(i+1,len(V))]).set_stroke(width=0.75))
            return W
        
        def add_points(V): #next iteration
            
            for i in range(len(V)):
                if(i==0):
                    a=np.array(V[np.mod(i,len(V))])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                else:
                    a=np.vstack([a,V[np.mod(i,len(V))]])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                    
            return a

        points=[LEFT,RIGHT,math.sqrt(3)*UP]
        line1 = add_lines(points)
        line2 = add_lines(add_points(points))
        line3 = add_lines(add_points(add_points(points)))
        line4 = add_lines(add_points(add_points(add_points(points))))
        line5 = add_lines(add_points(add_points(add_points(add_points(points)))))
        line6 = add_lines(add_points(add_points(add_points(add_points(add_points(points))))))
        line7 = add_lines(add_points(add_points(add_points(add_points(add_points(add_points(points)))))))

        points = add_points(add_points(add_points(add_points(add_points(add_points(points))))))
        #line8 = add_lines(add_points(add_points(add_points(add_points(add_points(add_points(add_points(points))))))))
        #line9 = add_lines(add_points(add_points(add_points(add_points(add_points(add_points(add_points(add_points(points)))))))))
        #line10 = add_lines(add_points(add_points(add_points(add_points(add_points(add_points(add_points(add_points(add_points(points)))))))))).scale(2)
        axes = Axes()
        x_points = [x[0] for x in points]
        y_points = [x[1] for x in points]
        line = axes.plot_line_graph(x_points,y_points, add_vertex_dots=False)

        
        self.play(FadeIn(line))
        self.wait()
        self.play(self.camera.frame.animate.move_to(axes.c2p(0.5,np.sqrt(3)/2)).scale(0.1),run_time=10)
        #self.play(AnimationGroup(FadeOut(line4),FadeIn(line5)),lag_ratio=0.5,run_time=2)
        self.wait(5)

class CheckMovement(MovingCameraScene):
    def construct(self):
        c=Circle(radius=5)
        d=Dot(5*RIGHT)
        r=5
        t=ValueTracker(0)
        self.add(c,d)
        self.wait()
        self.play(self.camera.frame.animate.scale(0.75).move_to(d.get_center()))
        self.camera.frame.add_updater(lambda x: x.move_to(d.get_center()))
        d.add_updater(lambda x: x.become(Dot([r*np.cos(t.get_value()),r*np.sin(t.get_value()),0])))
        self.play(t.animate.set_value(2*PI),run_time=15,rate_function=rate_functions.ease_in_sine)
        self.wait(2)

from manim import *

class MoveAlongPathExample(MovingCameraScene):
    def construct(self):
        d1 = Dot(LEFT).scale(0.25).set_color(RED)
        l1 = Line(LEFT, RIGHT)
        l2 = Line(RIGHT, RIGHT+UP)
        l3 = Line(RIGHT+UP,UP)
        l4 = Line(UP,ORIGIN)
        self.camera.frame.scale(0.15)
        self.add(d1)
        
        
        
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

        points=[LEFT,RIGHT]
        line1 = add_lines(points)
        line2 = add_lines(add_points(points))
        line3 = add_lines(add_points(add_points(points)))
        line4 = add_lines(add_points(add_points(add_points(points))))
        line5 = add_lines(add_points(add_points(add_points(add_points(points)))))

        #p = Polygon()
        #l2 = VMobject()
        paths = line3
        self.add(*paths)
        self.camera.frame.add_updater(lambda x: x.move_to(d1))
        #self.add(self.camera.frame)
        #l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center())))
        #self.camera.frame.add_updater(lambda x: x.move_to(d1.get_center()))
        for path in paths:
            self.play(MoveAlongPath(d1,path),rate_func=linear,run_time=0.25)
            
class MoveAlongPathExample2(MovingCameraScene):
    def construct(self):
        d1 = Dot().set_color(ORANGE)
        d2 = d1.copy()
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        
        def updater_cam(x):
            x.scale(0.5)
            
        d2.add_updater(lambda x: x.move_to(d1.get_center()))
        self.camera.frame.add_updater(lambda x: x.move_to(d1.get_center()))
        
        self.add(d2, l1, l2,d1)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(d1.animate.shift(RIGHT),run_time=2)
        #self.play(MoveAlongPath(d1, l1), rate_func=linear,run_time=3)
        
class MoveAlongPathExample3(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane())
        d = Dot()
        self.add(d)
        self.wait()
        self.camera.frame.add_updater(lambda x,dt: x.move_to(d.get_center()))
        self.add(self.camera.frame)
        self.play(d.animate.shift(5*RIGHT),run_time=5)

class Check(MovingCameraScene):
    def construct(self):
        axes = Axes()
        x = [0, 1, 2, 3, 4]
        y = [1, 2, 4, 2, 3]
        line = axes.plot_line_graph(x, y, add_vertex_dots=False)
        self.add(axes, line)
        self.wait()
        self.play(self.camera.frame.animate.scale(0.05).move_to(axes.c2p(2,4)),run_time=5)

class Koch_full2(Scene):
    def construct(self):
        
        def add_lines(V):
            W = VGroup()
            for i in range(len(V)):
                W.add(Line(V[i],V[np.mod(i+1,len(V))]).set_stroke(width=0.75))
            return W
        
        def add_points(V): #next iteration
            
            for i in range(len(V)):
                if(i==0):
                    a=np.array(V[np.mod(i,len(V))])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                else:
                    a=np.vstack([a,V[np.mod(i,len(V))]])
                    a=np.vstack([a,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3])
                    new_point = my_rotate((V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3,(2*V[np.mod(i,len(V))]+V[np.mod(i+1,len(V))])/3,PI/3)
                    a=np.vstack([a,new_point])
                    a=np.vstack([a,(V[np.mod(i,len(V))]+2*V[np.mod(i+1,len(V))])/3])
                    
            return a

        points=[2*LEFT,2*RIGHT,2*math.sqrt(3)*UP]
        line1 = add_lines(points)
        line2 = add_lines(add_points(points))
        line3 = add_lines(add_points(add_points(points)))
        line4 = add_lines(add_points(add_points(add_points(points))))
        line5 = add_lines(add_points(add_points(add_points(add_points(points)))))
        #line6 = add_lines(add_points(add_points(add_points(add_points(add_points(points))))))
        #line6.move_to(ORIGIN)
        #self.play(Create(line1.shift(2.5*2*LEFT)),run_time=2)
        #self.wait()
        #self.play(Create(line2.shift(2.5*LEFT)),run_time=2)
        #self.play(AnimationGroup(FadeOut(line1),FadeIn(line2)),lag_ratio=0.5,run_time=2)
        #self.wait()
        #self.play(Create(line3),run_time=2)
        #self.play(AnimationGroup(FadeOut(line2),FadeIn(line3)),lag_ratio=0.5,run_time=2)
        #self.wait()
        #self.play(Create(line4.shift(2.5*RIGHT)),run_time=3)
        #self.play(AnimationGroup(FadeOut(line3),FadeIn(line4)),lag_ratio=0.5,run_time=2)
        #self.wait()
        line5.move_to(ORIGIN)
        self.play(FadeIn(line5))
        
        self.wait(10)
        #self.play(Polygon(*line))
        #self.play(AnimationGroup(FadeOut(line4),FadeIn(line5)),lag_ratio=0.5,run_time=2)
        #self.wait(5)

class rot_create(Scene):
    def construct(self):
        s=3 #scale factor
        points = [ORIGIN,s*RIGHT,s*np.sin(PI/3)*UP+s*np.cos(PI/3)*RIGHT]
        def add_lines2(V):
            W = VGroup()
            for i in range(len(V)):
                W.add(Line(V[i],V[np.mod(i+1,len(V))]).set_stroke(width=0.75))
            return W
        
        
        p = add_lines2(points).move_to(ORIGIN)
        self.play(FadeIn(p))
        for k in p:
            
            self.play(FadeOut(k))
        self.wait(2)
        
        