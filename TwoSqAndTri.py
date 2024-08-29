from manim import *
import math

config.media_width = "100%"
config.verbosity = "WARNING"
config.frame_size = (1080,1920)
config.frame_width = 7.5
config.background_color=BLACK

def find_intersection(self, line1, line2):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x4, y4 = p4[0], p4[1]

    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det
    intersection_x = x1 + t * (x2 - x1)
    intersection_y = y1 + t * (y2 - y1)

    return np.array([intersection_x, intersection_y, 0])


class AngleInSquare(MovingCameraScene):
    
    
    def construct(self):
        
        A = [0, 0, 0]
        B = [4, 0, 0]
        C = [4, 2, 0]
        D = [2, 1, 0]
        E = [-1, 2, 0]
        F = [1, 3, 0]
        G = [3, 4, 0]
        
        M = [11.9811529405346, 1, 0]
        N = [11.6953167565325, 3.2177235345992, 0]
        O = [10.5088155298863, -0.6829208386628, 0]
        P = [13.6038115438257, -0.5384989623543, 0]
        Q = [9.7450849630348, 1, 0]
        R = [14.2172209180344, 1, 0]
 
        triangle = Polygon(C, A, B, color = WHITE, fill_opacity = 1, fill_color = "#0A47C2", stroke_width=3)
        triangle.joint_type=LineJointType.ROUND 
        X = self.camera.frame.move_to(triangle).scale(1.1)
        self.add(X)
        self.play(DrawBorderThenFill(triangle))
        self.wait(2)
        
        sq1 = Polygon(E, F, D, A, color = WHITE, fill_opacity = 1, fill_color = PINK, stroke_width=3).shift(1.5*UP)
        sq1.joint_type=LineJointType.ROUND 
        sq2 = Polygon(F, G, C, D, color = WHITE, fill_opacity = 1, fill_color = PINK, stroke_width=3).shift(1.5*UP) 
        sq2.joint_type=LineJointType.ROUND 
        self.play(FadeIn(sq1, sq2))
        self.play(sq1.animate.shift(1.5*DOWN), sq2.animate.shift(1.5*DOWN), run_time=1)
        self.wait(2)
        
        line = Line(F, B, stroke_width=3).set_z_index(2)
        
        l = Line(B,A, stroke_width=3).set_z_index(2)
        
        self.play(Create(line), FadeIn(l))
        self.wait()
        
        
        
        sector = Sector(arc_center=B, outer_radius=0.65, 
                    start_angle=line.get_angle(), angle=PI/4, 
                    fill_opacity=1, fill_color="#3DD771", stroke_width = 3).rotate(PI, about_point=B)
        
        #self.play(GrowFromPoint(sector, B))
        self.wait(2)

        angle = MathTex(r"\angle", color="#3DD771").scale(1).set_stroke(width=3)
        eq_to = MathTex(" = ").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(angle, RIGHT, buff=0.3)
        sym = Text(" ? ").scale(0.8).set_color(WHITE).set_stroke(width = 1).next_to(eq_to, RIGHT, buff=0.3)
        eqn = VGroup(angle, eq_to, sym)
        eqn.next_to(triangle, 4*DOWN)
        
        self.play(FadeIn(eqn), GrowFromPoint(sector, B), self.camera.frame.animate.shift(DOWN))
        self.wait(2)

        dot = Circle(radius=0.08, fill_color="#C22300", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(D).set_z_index(3)
        self.play(FadeOut(eqn), FadeIn(dot))
        self.play(Indicate(dot, scale_factor=2, color=None), run_time=1.5)
        self.wait(2)

        radius = Line(D, C, stroke_width = 6, color="#000000").set_z_index(2)
        self.play(Create(radius))
        #self.play(Indicate(radius, scale_factor=1.5, color=None), run_time=1.5)
        self.wait()
        AC = Line(C, A)

        circle = Circle().surround(AC, buffer_factor=1).set_z_index(3)
        circle.set_stroke(width = 5, color=WHITE).rotate(PI/6.775819809273145)
        #circle.start_angle = PI/3
        self.play(Create(circle))
        self.wait(2)
        self.play(FadeOut(radius))
        self.wait(2)

        FD = Line(F, D, stroke_width = 6, color="#000000").set_z_index(2)
        AD = Line(A, D, stroke_width = 6, color="#000000").set_z_index(2)

        self.play(FadeIn(FD, AD))
        
        self.wait(2)
        #FD = Line(F,D)
        sq = Square(side_length=0.5, 
                        stroke_width = 3,
                        fill_color = "#C22300",
                        fill_opacity=1).rotate(angle=PI/6.77581983+PI/2)
        sq.next_to(FD.get_end(), LEFT, buff=0).shift(0.1*UP+0.01*LEFT)

        ninety_degrees = MathTex("90^\circ").scale(0.8).next_to(sq, LEFT).shift(0.1*RIGHT+0.1*UP)

        #ninety = VGroup(sq, ninety_degrees)

        self.play(GrowFromPoint(sq, D))

        self.wait(2)
        self.play(FadeIn(ninety_degrees),
                  FadeOut(triangle, sq2, l, line, AC, sector, dot, circle),
                  self.camera.frame.animate.move_to(sq1).scale(0.75),
                  FD.animate.set_color("#FFBA07"),
                  AD.animate.set_color("#FFBA07"))

        self.wait(5)

        self.play(self.camera.frame.animate.move_to(triangle).scale(1/0.75).shift(DOWN),
                  FadeIn(triangle, sq2, l, line, sector, dot, circle),
                  FD.animate.set_color(BLACK),
                  AD.animate.set_color(BLACK))
        self.wait(2)

        QR = Line( Q, R)

        circleProof = Circle().surround(QR, buffer_factor=1)
        circleProof.set_fill(color = PINK, opacity = 1)
        circleProof.set_stroke(width = 5, color=WHITE)
        circleProof.start_angle = PI/3

        group = VGroup(triangle, sq1, sq2, l, line, sector, dot, FD, AD, circle, sq, ninety_degrees)


        dotP = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(M).set_z_index(3)
        self.play(FadeIn(circleProof, dotP),
                  self.camera.frame.animate.move_to(circleProof).shift(DOWN),
                  FadeOut(group))

        self.wait(2)

        ON = Line(O, N, stroke_width=3).set_z_index(2)
        PN = Line(P, N, stroke_width=3).set_z_index(2)

        self.play(Create(ON), Create(PN))


        angleBlue = MathTex(r"\angle", color="#0A47C2").scale(1).set_stroke(width=3)
        eq = MathTex(" = ").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(angleBlue, RIGHT, buff=0.3)
        #q = Text(" ? ").scale(0.8).set_color(WHITE).set_stroke(width = 1).next_to(eq, RIGHT, buff=0.3)
        half = MathTex(r"\frac{1}{2}").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(eq, RIGHT, buff=0.3)
        times = MathTex("\\times").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(half, RIGHT, buff=0.3)
        angleRed = MathTex(r"\angle", color="#C22300").scale(1).set_stroke(width=3).next_to(times, RIGHT, buff=0.3)
        
        eqnP = VGroup(angleBlue, eq, half, times, angleRed)
        eqnP.next_to(circleProof, 4*DOWN).scale(0.9)

        ONP = Sector(arc_center=N, outer_radius=0.65, 
                    start_angle=ON.get_angle(), angle=PI/4.1045875, 
                    fill_opacity=1, fill_color="#0A47C2", stroke_width = 3).rotate(PI, about_point=N)
        self.play(GrowFromPoint(ONP, N), FadeIn(angleBlue, eq), 
                  )

        OM = Line(O, M, stroke_width=3).set_z_index(2)
        PM = Line(P, M, stroke_width=3).set_z_index(2)
        self.play(Create(OM), Create(PM))
        OMP = Sector(arc_center=M, outer_radius=0.65, 
                    start_angle=OM.get_angle(), angle=2*PI/4.1045875, 
                    fill_opacity=1, fill_color="#C22300", stroke_width = 3).rotate(PI, about_point=M)
        self.play(GrowFromPoint(OMP, M), FadeIn(half, times, angleRed))

        box = SurroundingRectangle(eqnP, color=WHITE, buff=0.4, corner_radius=0.2)
        self.play(Create(box))
        self.wait(2)

        txt = Text("Inscribed Angle Theorem", font='Athletics', weight = BOLD).next_to(circleProof, 2 * UP).scale(0.65)
        self.play(FadeIn(txt))
        self.wait(2)

        pGroup = VGroup(circleProof, eqnP, txt, ONP, OMP, dotP, box, ON, PN, OM, PM)

        self.play(FadeOut(pGroup),
                  self.camera.frame.animate.move_to(triangle).shift(DOWN),
                  FadeIn(group))
        
        self.wait(2)

        eqnP.next_to(circle, 4*DOWN)
        angleBlue.set_color("#3DD771")
        self.play(sq1.animate.set_opacity(0),
                  sq2.animate.set_opacity(0),
                  triangle.animate.set_opacity(0),
                  FD.animate.set_color("#FFBA07"),
                  AD.animate.set_color("#FFBA07"))
        sector.save_state()
        self.play(FadeIn(angleBlue), sector.animate.scale(1.2).shift(0.1*LEFT+0.06*UP),
                  )
        self.play(FadeIn(eq), Restore(sector))
        self.play(FadeIn(half))
        self.play(FadeIn(times))
        sq.save_state()
        self.play(FadeIn(angleRed), sq.animate.shift(0.03*UP+0.07*LEFT).scale(1.2))
        self.play(Restore(sq))

        n = MathTex(" 90^\circ ").scale(0.9).set_color(WHITE).set_stroke(width = 1).next_to(times, RIGHT, buff=0.3)
        ninety_degrees_c = ninety_degrees.copy()

        self.play(ReplacementTransform(ninety_degrees_c, n), FadeOut(angleRed))
        self.wait()
        grp = VGroup(half, times, n)

        ffv = MathTex("45^\circ").scale(0.8).next_to(sector, LEFT).shift(0.1*RIGHT+0.2*UP)

        fv = MathTex(" 45^\circ ").scale(0.9).set_color(WHITE).set_stroke(width = 1).next_to(eq, RIGHT, buff=0.3)
        self.play(FadeTransform(grp, fv), FadeIn(ffv),
                  )

        finaleq = VGroup(angleBlue, eq, fv)
        fBox = SurroundingRectangle(finaleq, color=WHITE, buff=0.4, corner_radius=0.2)

        self.play(Create(fBox),
                  sq1.animate.set_opacity(1),
                  sq2.animate.set_opacity(1),
                  triangle.animate.set_opacity(1),
                  FD.animate.set_color("#000000"),
                  AD.animate.set_color("#000000"))

        fgrp = VGroup(finaleq, fBox)
        self.play(fgrp.animate.next_to(circle, 4*DOWN))

        self.wait(5)


        fsector = Sector(arc_center=A, outer_radius=0.75, 
                    start_angle=l.get_angle(), angle=PI/6.775819809273145, 
                    fill_opacity=1, fill_color="#FF9F6C", stroke_width = 3).rotate(PI, about_point=A)
        angle.set_color("#FF9F6C")
        eqn.next_to(circle, 4*DOWN)

        # Add symbols for equality of the sides of the pentagon
        parallel_symbol_p1 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width=3)
        parallel_symbol_p2 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width=3).next_to(parallel_symbol_p1, DOWN, buff = 0.7)
        AB = Line(A,B)
        FBeq = VGroup(parallel_symbol_p1, parallel_symbol_p2).move_to(AB.get_center()).rotate(PI/2).scale(0.17).set_z_index(20)       

        ABeq = FBeq.copy()
        ABeq.move_to(line.get_center()).rotate(PI/4 + PI/2)

        FB = Line(F, B, stroke_width = 6, color="#C22300").set_z_index(2)
        AB = Line(A, B, stroke_width = 6, color="#C22300").set_z_index(2)
        #sq1.set_fill(color = "#3DD771")
        #sq2.set_fill(color = "#3DD771")
        self.play(FadeOut(FD, AD, fgrp),
                  #FadeIn(FBeq, ABeq),
                  self.camera.frame.animate.shift(UP))
        
        self.wait(2)

        self.play(FadeIn(FB, AB))
        self.wait()
        self.play(FadeIn(FBeq, ABeq))

        self.play(FadeIn(eqn),
                  GrowFromPoint(fsector, A),
                  self.camera.frame.animate.shift(DOWN))
        
        self.wait(4)


