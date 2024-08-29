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

    
def create_glow(x, rad=0.4, col=WHITE):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius=rad*(1.0023**(idx**2))/600, stroke_opacity=0, fill_color=col,
        fill_opacity=0.2-idx/300).move_to(x)
        glow_group.add(new_circle)
    return glow_group


class tri(MovingCameraScene):

    
    def construct(self):
        # Define the points
        A = [1.5, 2.598076211353, 0]
        B = [0,0,0]
        C = [3,0,0]
        D = [1, 1.7320508075689, 0]
        E = [0.5, 0.8660254037844, 0]
        F = [1,0,0]
        G = [2,0,0]
        H = [2.5, 0.8660254037844, 0]
        I = [2, 1.7320508075689, 0]
        J = [1.5, 0.8660254037844, 0]
        
        triangle = Polygon(A, B, C, color = WHITE).set_z_index(10)
        triangle.joint_type=LineJointType.ROUND 

        #Zoom out
        X = self.camera.frame.scale(0.8).move_to(triangle)
        self.add(X)


        # Create the segments
        f = Line(A, B, color=WHITE, stroke_width=2)
        g = Line(B, C, color=WHITE, stroke_width=2)
        h = Line(C, A, color=WHITE, stroke_width=2)

        # Create the star polygon
        tri_points = [A, B, C]
        s = Polygon(*tri_points, color=WHITE, stroke_width=2).set_z_index(2)
        s.joint_type=LineJointType.ROUND 
        
        line = []

        for k in range(3):
            l = Line(s.point_from_proportion(k/3), s.point_from_proportion((k+1)/3), stroke_width=2).set_color(WHITE)
            line.append(l)

        dot = Dot(s.point_from_proportion(0), radius = 0.02).set_color(WHITE)
        b = TracedPath(dot.get_center, dissipating_time=0.00005, stroke_opacity=[0, 1]).set_color(WHITE)

        self.add(dot, b)
        def glows():
            return VGroup(*[create_glow(x) for x in [dot]])
        glow_all = always_redraw(lambda: glows())
        self.add(glow_all)
        self.play(LaggedStart(MoveAlongPath(dot, s),  FadeIn(f),FadeIn(g),FadeIn(h), FadeIn(triangle), lag_ratio=0.1, run_time=1.6))
        self.play(FadeOut(dot, glow_all))
        
        #Add symbols for equality
        AD = Line(A,D)
        DE = Line(D,E)
        EB = Line(E,B)
        BF = Line(B,F)
        FG = Line(F,G)
        GC = Line(G,C)
        AI = Line(A,I)
        IH = Line(I,H)
        HC = Line(H,C)
        
        equality_symbol_p1 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width = 1.5)
        equality_symbol_p2 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width = 1.5).next_to(equality_symbol_p1, DOWN, buff = 0.7)
        equality_symbol1 = VGroup(equality_symbol_p1, equality_symbol_p2).move_to(AD.get_center()).rotate(PI/3+PI/2).scale(0.09).set_z_index(12)       
        es2 = equality_symbol1.copy().move_to(DE.get_center()).set_z_index(12)       
        es3 = equality_symbol1.copy().move_to(EB.get_center()).set_z_index(12)
        es4 = equality_symbol1.copy().move_to(BF.get_center()).set_z_index(12).rotate(-(PI/3+PI/2)+PI/2)
        es5 = es4.copy().move_to(FG.get_center()).set_z_index(12)
        es6 = es4.copy().move_to(GC.get_center()).set_z_index(12)
        es7 = es4.copy().move_to(AI.get_center()).set_z_index(12).rotate(-PI/3)
        es8 = es4.copy().move_to(IH.get_center()).set_z_index(12).rotate(-PI/3)
        es9 = es4.copy().move_to(HC.get_center()).set_z_index(12).rotate(-PI/3)
        
        
        #Add dots
        d1 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(A).set_z_index(12)
        d2 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(D).set_z_index(12)
        d3 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(E).set_z_index(12)
        d4 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(B).set_z_index(12)
        d5 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(F).set_z_index(12)
        d6 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(G).set_z_index(12)
        d7 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(C).set_z_index(12)
        d8 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(H).set_z_index(12)
        d9 = Circle(radius=0.05, fill_color="#052361", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(I).set_z_index(12)     
        
        
        #Original triangle movement
        triangle1 =Polygon(G,A,E, color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_opacity = 1, stroke_color = WHITE)
        triangle1.joint_type=LineJointType.ROUND
        
        questionText = Text("Shaded Area?", color = WHITE, font='Athletics', t2c={"Shaded": "#0A80D5"}).next_to(A, UP, buff=1).scale(0.55)
        
        l1 = Line(A, G, stroke_width = 2, color = WHITE)
        l2 = Line(E, G, stroke_width = 2, color = WHITE)
        #self.play(AnimationGroup(AnimationGroup(FadeIn(equality_symbol1, es2, es3,es6,d1,d2,d3,d4,d6)), 
        #                         AnimationGroup(Create(l1), Create(l2)),
        #                         lag_ratio = 0.3, 
        #                         run_time=1.5))
        d6_copy = d6.copy().move_to(G)
        self.play(FadeIn(equality_symbol1, es2, es3,es6,d1,d2,d3,d4,d6,d7), FadeIn(d5,d6_copy,d8,d9,es4,es5,es7,es8,es9))
        self.wait()
        self.play(Create(l1), Create(l2), run_time=1.5)
        self.wait()
        self.play(FadeIn(triangle1, questionText))
        self.wait(4)
        
        dl = DashedLine(H, G, stroke_width = 1)
        
        dl1 = DashedLine(D, G, stroke_width = 1)
        dl2 = DashedLine(E, F, stroke_width = 1)
        dl3 = DashedLine(I, F, stroke_width = 1)
        dl4 = DashedLine(D, I, stroke_width = 1)
        dl5 = DashedLine(E, H, stroke_width = 1)
        
        d6.set_z_index(20)
        
        self.play(AnimationGroup(AnimationGroup(Create(dl4),Create(dl5)), 
                                 AnimationGroup(Create(dl1), Create(dl2)), 
                                 AnimationGroup(Create(dl), Create(dl3)),
                                lag_ratio=1))
        
        l3 = Line(A,B, stroke_width = 4, color = "#C22300").set_z_index(11)
        l4 = Line(G,H, stroke_width = 4, color = "#C22300").set_z_index(11)
        self.play(FadeIn(l3, l4), FadeOut(l1, l2))
        self.play(Indicate(l3), Indicate(l4, scale_factor = 1.5), color = None)
        dlc = DashedLine(G, H, stroke_width = 1)
        arrow2 = Arrow(start=dlc.get_start(), end=dlc.get_center(), color=WHITE,stroke_width=0.1,max_tip_length_to_length_ratio=0.36,max_stroke_width_to_length_ratio=0).set_z_index(12).shift(0.1*UP+0.057*RIGHT)
        arrow1 = arrow2.copy().move_to(l3.get_center())

        self.play(FadeOut(l3,l4), FadeIn(arrow1, arrow2))
        self.wait()
        
        R = Dot(G, radius = 0)      
        S = Dot(H)     
        
        line1 = Line(A,G)
        line2 = Line(E,G)
        
        
        triangle1.add_updater(lambda x:x.become(Polygon(d6.get_center(),line1.get_start(),line2.get_start(), color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_opacity = 1, stroke_color = WHITE)))
        self.wait()
        self.play(d6.animate.set_fill(color = "#C22300"))
        self.play(Indicate(d6, color = None, scale_factor = 2), run_time=2)
        self.play(FadeIn(l4))
        self.wait(4)
        self.play(d6.animate.move_to(S), run_time=2)
        self.play(d6.animate.set_fill(color = "#052361"),
                 FadeOut(arrow1, arrow2,l4))
        #self.wait()
        #self.play(FadeOut(arrow1, arrow2,l4))
        
        self.wait(4)
        
        p1 = Polygon(A,D,I, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p2 = Polygon(D,E,J, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p3 = Polygon(D,I,J, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p4 = Polygon(I,J,H, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p5 = Polygon(B,F,E, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p6 = Polygon(E,F,J, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p7 = Polygon(J,F,G, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p8 = Polygon(J,H,G, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        p9 = Polygon(H,G,C, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = "#ED6CEF", stroke_opacity = 1).set_z_index(6)
        
        p10 = Polygon(A,D,I, color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_color = "#0A80D5", stroke_opacity = 1).set_z_index(6)
        p11 = Polygon(D,E,J, color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_color = "#0A80D5", stroke_opacity = 1).set_z_index(6)
        p12 = Polygon(D,I,J, color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_color = "#0A80D5", stroke_opacity = 1).set_z_index(6)
        p13 = Polygon(I,J,H, color = "#052361", fill_opacity = 1, stroke_width = 2, stroke_color = "#0A80D5", stroke_opacity = 1).set_z_index(6)

        t1 = MathTex("1").move_to(p1.get_center()).set_z_index(8).scale(0.5)
        t2 = MathTex("2").move_to(p2.get_center()).set_z_index(8).scale(0.5)
        t3 = MathTex("3").move_to(p3.get_center()).set_z_index(8).scale(0.5)
        t4 = MathTex("4").move_to(p4.get_center()).set_z_index(8).scale(0.5)
        t5 = MathTex("5").move_to(p5.get_center()).set_z_index(8).scale(0.5)
        t6 = MathTex("6").move_to(p6.get_center()).set_z_index(8).scale(0.5)
        t7 = MathTex("7").move_to(p7.get_center()).set_z_index(8).scale(0.5)
        t8 = MathTex("8").move_to(p8.get_center()).set_z_index(8).scale(0.5)
        t9 = MathTex("9").move_to(p9.get_center()).set_z_index(8).scale(0.5)
        fraction = MathTex(r"\frac{\hphantom{ll.}}{9}").next_to(triangle, DOWN, buff= 1.25).scale(0.725)
        self.play(AnimationGroup(AnimationGroup(AnimationGroup(AnimationGroup(FadeIn(p1, t1)), 
                                 AnimationGroup(FadeIn(p2, t2)),
                                 AnimationGroup(FadeIn(p3, t3)),
                                 AnimationGroup(FadeIn(p4, t4)),
                                 AnimationGroup(FadeIn(p5, t5)),
                                 AnimationGroup(FadeIn(p6, t6)),
                                 AnimationGroup(FadeIn(p7, t7)),
                                 AnimationGroup(FadeIn(p8, t8)),
                                 AnimationGroup(FadeIn(p9, t9)),lag_ratio = 0.3)),

                                 AnimationGroup(FadeIn(fraction), self.camera.frame.animate.shift(DOWN)),lag_ratio=1)
                 )
        
        
        
        #self.play()
        
        fractionB = t4.copy()
        
        #self.wait(2)
        
        self.play(FadeOut(p1,t1,p2,t2,p3,t3,p4,t4,p5,t5,p6,t6,p7,t7,p8,t8,p9,t9))

        t1.move_to(p10.get_center())
        t2.move_to(p11.get_center())
        t3.move_to(p12.get_center())
        t4.move_to(p13.get_center())
        
        self.play(AnimationGroup(AnimationGroup(FadeIn(p10, t1)), 
                                 AnimationGroup(FadeIn(p11, t2)),
                                 AnimationGroup(FadeIn(p12, t3)),
                                 AnimationGroup(FadeIn(p13, t4)),lag_ratio = 0.3))
        self.play(fractionB.animate.next_to(fraction, 0.65*UP).scale(1.64594595))
        eqn = VGroup(fraction, fractionB)
        box = SurroundingRectangle(eqn, color=WHITE, buff=0.2, corner_radius=0.1, stroke_width=3)
        self.wait()
        self.play(Create(box))
        self.wait()
        self.wait(3)
        
        self.play(FadeOut(box, fraction, fractionB, t1,t2,t3,t4, p10,p11,p12,p13, triangle1), 
                  self.camera.frame.animate.move_to(triangle))
        triangle.set_stroke(color = WHITE).set_z_index(10)
        dl.set_z_index(8)
        dl1.set_z_index(8)
        dl2.set_z_index(8)
        dl3.set_z_index(8)
        dl4.set_z_index(8)
        dl5.set_z_index(8)
        d1.set_fill(color ="#763677" )
        d2.set_fill(color ="#763677" )
        d3.set_fill(color ="#763677" )
        d4.set_fill(color ="#763677" )
        d5.set_fill(color ="#763677" )
        d6.set_fill(color ="#763677" )
        d7.set_fill(color ="#763677" )
        d8.set_fill(color ="#763677" )
        d9.set_fill(color ="#763677" )
        d6_copy.set_fill(color ="#763677" )
        self.wait()
        
        p14 = Polygon(A,E,I, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = WHITE, stroke_opacity = 1).set_z_index(0)
        p15 = Polygon(G,C,E, color = "#763677", fill_opacity = 1, stroke_width = 2, stroke_color = WHITE, stroke_opacity = 1).set_z_index(0)
        questionTextF = Text("Shaded Area?", color = WHITE, font='Athletics', t2c={"Shaded": "#ED6CEF"}).next_to(A, UP, buff=1).scale(0.55)
        
        self.play(FadeIn(p14,p15,questionTextF,equality_symbol1,es2,es3,es4,es5,es6,es7,es8,es9,d1,d2,d3,d4,d5,d6,d7,d8,d9,d6_copy))
        self.wait(6)