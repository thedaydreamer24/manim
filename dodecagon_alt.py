from manim import *
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


class tri(MovingCameraScene):

    
    def construct(self):
        M = [0.0681483474219, 3.3460652149512, 0]
        dodecagon = RegularPolygon(n=12, radius = 3.8637033051563, color = WHITE, stroke_width = 6).move_to(M)
        dodecagon.joint_type=LineJointType.ROUND 
        
        A = dodecagon.get_vertices()[9]
        B = dodecagon.get_vertices()[10]
        C = dodecagon.get_vertices()[11]
        D = dodecagon.get_vertices()[0]
        E = dodecagon.get_vertices()[1]
        F = dodecagon.get_vertices()[2]
        G = dodecagon.get_vertices()[3]
        H = dodecagon.get_vertices()[4]
        I = dodecagon.get_vertices()[5]
        J = dodecagon.get_vertices()[6]
        K = dodecagon.get_vertices()[7]
        L = dodecagon.get_vertices()[8]
       
        N = [3.9318516525781, 7.2097685201075, 0]
        O = [3.9318516525781, -0.517638090205, 0]
        P = [-3.7955549577344, -0.517638090205, 0]
        Q = [-3.5367359126319, 4.3119910412403, 0]
        R = [-2.5708100863428, 5.9850236487159, 0]
        S = [0.8977774788672, 6.950949475005, 0]
        T = [-1.8637033051563, 3.8637033051563, 0]
        U = [-1.3460652149512, 4.7602787773243, 0]
        V = [-0.4494897427832, 5.2779168675294, 0]
        
        
        
        #Zoom out
        X = self.camera.frame.scale(1.9).move_to(dodecagon)
        self.add(X)

        line = Line(M, dodecagon.get_vertices()[0]).set_z_index(10)
        text = MathTex("10").next_to(line, 1.3*DOWN).scale(1.6).set_z_index(10)
        self.play(FadeIn(dodecagon , line, text))
        self.wait(2)
        A = dodecagon.animate.set_fill(color = "#0A47C2", opacity=1)
        #self.play(A)
        self.wait(2)
        
        equal_to_what = MathTex("A(", "\phantom{xxx}", ")\ =\ ? ").scale(2).set_color(WHITE).set_stroke(width = 1).next_to(dodecagon, DOWN, buff=2)
        dodecagon_copy = dodecagon.copy()
        dodecagon_copy.set_fill(color = "#0A47C2", opacity=1)
        self.play(A)
        self.play( FadeIn(equal_to_what), dodecagon_copy.animate.scale(0.175).move_to(equal_to_what).shift(0.71*LEFT), self.camera.frame.animate.shift(2*DOWN))
        self.wait(2)
        self.play(FadeOut(line, text, dodecagon_copy, equal_to_what))
        self.wait(2)
        
        l1 = Line(dodecagon.get_vertices()[3], dodecagon.get_vertices()[9])
        l2 = Line(dodecagon.get_vertices()[2], dodecagon.get_vertices()[8])
        l3 = Line(dodecagon.get_vertices()[1], dodecagon.get_vertices()[7])
        l4 = Line(dodecagon.get_vertices()[0], dodecagon.get_vertices()[6])
        l5 = Line(dodecagon.get_vertices()[11], dodecagon.get_vertices()[5])
        l6 = Line(dodecagon.get_vertices()[10], dodecagon.get_vertices()[4])
        
        lines_g = VGroup(l1,l2,l3,l4,l5,l6)
        
        self.play(Create(l1),Create(l2),Create(l3),Create(l4),Create(l5),Create(l6), run_time = 2.5)
        self.wait(2)
        self.play(FadeOut(lines_g))
        self.wait(2)
        
        GA = Line(dodecagon.get_vertices()[3],dodecagon.get_vertices()[9]).set_z_index(4)
        JD = Line(dodecagon.get_vertices()[6],dodecagon.get_vertices()[0]).set_z_index(4)
        self.play(Create(GA), Create(JD))
        self.wait()
        
        MG = Line(M, dodecagon.get_vertices()[3])
        MV = Line(M, V)
        MH = Line(M, dodecagon.get_vertices()[4])
        MU = Line(M, U)
        MI = Line(M, dodecagon.get_vertices()[5])
        MT = Line(M, T)
        MJ = Line(M, dodecagon.get_vertices()[6])
        
        lines_g2 = VGroup(MG, MV, MH, MU, MI, MT, MJ)
        
        self.play(Create(MG),
                 Create(MV),
                 Create(MH),
                 Create(MU),
                 Create(MI),
                 Create(MT),
                 Create(MJ))
        
        TI = Line(T, dodecagon.get_vertices()[5])
        TJ = Line(T, dodecagon.get_vertices()[6])
        UH = Line(U, dodecagon.get_vertices()[4])
        UI = Line(U, dodecagon.get_vertices()[5])
        VH = Line(V, dodecagon.get_vertices()[4])
        VG = Line(V, dodecagon.get_vertices()[3])
        
        lines_g3 = VGroup(TI, TJ, UH, UI, VH, VG)
        
        self.play(Create(TI), 
                 Create(TJ),
                 Create(UH),
                 Create(UI),
                 Create(VH),
                 Create(VG))
        self.wait()
        
        #Polygons
        
        p1 = Polygon(I, J, T, fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(5)
        p2 = Polygon(I, U, H, fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(5)
        p3 = Polygon(H, V, G, fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(5)
        
        p4 = Polygon(J, T, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p5 = Polygon(I, T, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p6 = Polygon(I, U, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p7 = Polygon(H, U, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p8 = Polygon(H, V, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p9 = Polygon(G, V, M, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        
        p10 = Polygon(dodecagon.get_vertices()[9],
                      dodecagon.get_vertices()[10],
                      dodecagon.get_vertices()[11], 
                      dodecagon.get_vertices()[0],
                      dodecagon.get_vertices()[1],
                      dodecagon.get_vertices()[2],
                      dodecagon.get_vertices()[3], 
                      M, 
                      dodecagon.get_vertices()[6],
                      dodecagon.get_vertices()[7],
                      dodecagon.get_vertices()[8], 
                      fill_color = "#0A47C2", 
                      fill_opacity=1, 
                      stroke_width = 6, stroke_color = WHITE).set_z_index(3)
        
        p1.joint_type=LineJointType.ROUND 
        p2.joint_type=LineJointType.ROUND 
        p3.joint_type=LineJointType.ROUND 
        p4.joint_type=LineJointType.ROUND 
        p5.joint_type=LineJointType.ROUND 
        p6.joint_type=LineJointType.ROUND 
        p7.joint_type=LineJointType.ROUND 
        p8.joint_type=LineJointType.ROUND 
        p9.joint_type=LineJointType.ROUND 
        
        p10.joint_type=LineJointType.ROUND 
        
        self.play(FadeIn(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10))
        self.play(FadeOut(dodecagon, lines_g2, lines_g3))
        self.wait(2)
        
        p1_pos = Polygon(dodecagon.get_vertices()[7], dodecagon.get_vertices()[8], P, fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p2_pos = Polygon(dodecagon.get_vertices()[11], dodecagon.get_vertices()[10], O, fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p3_pos = Polygon(dodecagon.get_vertices()[2], N, dodecagon.get_vertices()[1], fill_color = "#005E2C", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p4_pos = Polygon(dodecagon.get_vertices()[6], dodecagon.get_vertices()[7], P, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p5_pos = Polygon(P, dodecagon.get_vertices()[8], dodecagon.get_vertices()[9], fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p6_pos = Polygon(dodecagon.get_vertices()[9], dodecagon.get_vertices()[10], O, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p7_pos = Polygon(dodecagon.get_vertices()[0], dodecagon.get_vertices()[11], O, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p8_pos = Polygon(dodecagon.get_vertices()[0], dodecagon.get_vertices()[1], N, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        p9_pos = Polygon(dodecagon.get_vertices()[3], dodecagon.get_vertices()[2], N, fill_color = "#3DD771", fill_opacity = 1, stroke_color = WHITE).set_z_index(4)
        
        #Moving p1, p2, p3
        
        self.play(p1.animate.move_to(p1_pos), p2.animate.move_to(p2_pos), p3.animate.move_to(p3_pos), run_time=2)
        
        p4.set_z_index(5)
        p5.set_z_index(5)
        p6.set_z_index(5)
        p7.set_z_index(5)
        p8.set_z_index(5)
        p9.set_z_index(5)
        self.wait()
        # Moving p4
        self.play(Rotate(p4, angle = -PI/2, about_point = J),
                  Rotate(p9, angle = PI/2, about_point = G),
                  Rotate(p7, angle = -PI/1.5, about_point = M),
                  Rotate(p8, angle = PI/3, about_point = M),
                  Rotate(p6, angle = PI/1.5, about_point = M),
                  Rotate(p5, angle = -PI/3, about_point = M),
                  )
        #self.wait()
        
        # Moving p9
        #self.play()
        #self.wait()
        
        
        #Moving p7
        #self.play(Rotate(p7, angle = -PI/1.5, about_point = M))
        self.play(p7.animate.move_to(p6_pos),
                  p8.animate.move_to(p5_pos),
                  p6.animate.move_to(p7_pos),
                  p5.animate.move_to(p8_pos),
                  )
        #self.wait()
        
        #Moving p8
        #self.play()
        #self.play()
        #self.wait()
        
        #Moving p6
        #self.play()
        #self.play()
        #self.wait()
        
        #Moving p5
        #self.play()
        #self.play()
        self.wait(4)
        
        #Final squares
        square1 = Polygon(M, dodecagon.get_vertices()[6], P, dodecagon.get_vertices()[9], fill_color = "#D68000", fill_opacity = 1, stroke_color = WHITE).set_z_index(7)
        square2 = Polygon(M, dodecagon.get_vertices()[0], O, dodecagon.get_vertices()[9], fill_color = "#D68000", fill_opacity = 1, stroke_color = WHITE).set_z_index(7)
        square3 = Polygon(M, dodecagon.get_vertices()[3], N, dodecagon.get_vertices()[0], fill_color = "#D68000", fill_opacity = 1, stroke_color = WHITE).set_z_index(7)
        
        t1 = MathTex("1").move_to(square3.get_center()).set_z_index(8).scale(2)
        t2 = MathTex("3").move_to(square2.get_center()).set_z_index(8).scale(2)
        t3 = MathTex("2").move_to(square1.get_center()).set_z_index(8).scale(2)
        
        self.play(AnimationGroup(AnimationGroup(FadeIn(square3, t1)), 
                                 AnimationGroup(FadeIn(square1, t3)),
                                 AnimationGroup(FadeIn(square2, t2)),
                                 lag_ratio = 0.3))
        
        self.wait(2)

        GA.set_z_index(21)
        JD.set_z_index(21)
        t1.set_z_index(21)
        t2.set_z_index(21)
        t3.set_z_index(21)

        dodec_copy = dodecagon.copy()
        dodec_copy.set_z_index(20)
        text_copy = text.copy()
        text_copy.set_color(WHITE).set_z_index(20)
        line_copy = line.copy()
        line_copy.set_color(WHITE).set_z_index(30)

        self.play(FadeIn(dodec_copy, text_copy, line_copy, GA, JD), FadeOut(t1, t2, t3))
        self.play(Indicate(text_copy, color = RED, scale_factor=1.3), Indicate(line_copy, color = RED, scale_factor=1), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(dodec_copy, text_copy, line_copy, GA, JD), FadeIn(t1, t2, t3))
        self.wait(2)
        
        equal_to = MathTex("A(", "\phantom{xxx}", ")\ = \  ").scale(2).set_color(WHITE).set_stroke(width = 1).next_to(dodecagon, DOWN, buff=2)
        dodecagon_copy.shift(0.4*RIGHT)
        eqn = VGroup(equal_to, dodecagon_copy).shift(2.4*LEFT).scale(0.8)
        
        
        
        self.play(FadeIn(eqn))
        three = MathTex("3").next_to(eqn, buff = 0.6).scale(2)
        mul = MathTex("\\times").next_to(three, buff = 0.6).scale(2)
        
        equal_to_c = MathTex("A(", "\phantom{xxx}", ")\  \  ").scale(2).set_color(WHITE).set_stroke(width = 1).next_to(dodecagon, DOWN, buff=2)
        equal_to_c.scale(0.8)
        equal_to_c.next_to(mul, buff = 0.5)
         
        self.play(FadeIn(three))
        self.play(FadeIn(mul))
        square1_copy = square3.copy()
        self.play(FadeIn(equal_to_c), square1_copy.animate.move_to(equal_to_c).scale(0.225).shift(0.325*RIGHT))
        self.wait(2)
        fivesq = MathTex("5^2").next_to(mul, buff = 0.6).scale(1.9).shift(0.1*UP)
        
        grp = VGroup(equal_to_c, square1_copy)
        
        final = VGroup(equal_to, three, mul, fivesq, dodecagon_copy)
        
        self.play(FadeTransform(grp, fivesq))
        self.play(final.animate.next_to(dodecagon, DOWN, buff=2))
        self.wait()
        sevfive = MathTex("75").next_to(eqn, buff = 0.6).scale(2)
        
        grp2 = VGroup(three, mul, fivesq)
        self.play(FadeTransform(grp2, sevfive))
        
        finalans = VGroup(equal_to, dodecagon_copy, sevfive)
        box = SurroundingRectangle(finalans, color="#D68000", buff=0.5, corner_radius=0.1, stroke_width=6)
        
        fin_ans = VGroup(equal_to, box, dodecagon_copy, sevfive)
        
        self.play(Create(box))
        self.play(fin_ans.animate.next_to(dodecagon, DOWN, buff=2))
       
        self.wait(2)
        
        self.play(FadeOut(p1,p2,p3,p4,p5,p6,p7,p8,p9, p10, GA, JD))
        
        g = VGroup(square1, square2, square3, t1, t2, t3)
        
        r = MathTex("r").next_to(line, 1.3*DOWN).scale(1.6)
        
        dodecagon_g = VGroup(dodecagon, r, line)
        self.play(FadeTransform(g, dodecagon_g), Uncreate(box), FadeOut(sevfive), eqn.animate.shift(1.1*LEFT))
        self.wait(2)
        three.next_to(eqn, buff = 0.6)
        mul.next_to(three, buff = 0.6)
        
        rsq = MathTex("r^2").next_to(mul, buff = 0.6).scale(1.9).shift(0.1*UP+0.1*RIGHT)
        
        
        self.play(FadeIn(three))
        self.play(FadeIn(mul))
        r_copy = r.copy()
        
        self.play(Transform(r_copy, rsq))
        
        feq = VGroup(equal_to, three, mul, rsq)
        
        fbox = SurroundingRectangle(feq, color=WHITE, buff=0.5, corner_radius=0.1, stroke_width=6)
        self.play(Create(fbox))
        
        self.wait(2)
        
        dodecagon.set_z_index(2)
        square = Square(side_length = 2*3.8637033051563, fill_opacity=1, color = WHITE, stroke_width = 6, fill_color = "#D68000").set_z_index(2).move_to(M).set_z_index(1)
        self.play(FadeOut(dodecagon_copy, fbox, feq, r, r_copy),  self.camera.frame.animate.shift(2*UP), 
                  FadeIn(square, text), 
                  dodecagon.animate.set_fill(color = BLACK))
        self.wait(2)

        square_c = square.copy()
        square_c.set_stroke(width = 4)
        dodecagon_c = dodecagon.copy()
        dodecagon_c.set_stroke(width = 4)
        f = VGroup(square_c, dodecagon_c)

        self.play(FadeIn(equal_to_what), f.animate.scale(0.15).move_to(equal_to_what).shift(0.71*LEFT), self.camera.frame.animate.shift(2*DOWN))
        

        self.wait(2)