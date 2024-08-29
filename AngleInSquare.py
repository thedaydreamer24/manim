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


class AngleInSquare(MovingCameraScene):
    
    
    def construct(self):
        
        A = [0, 0, 0]
        B = [4, 0, 0]
        C = [4, 4, 0]
        D = [0, 4, 0]
        E = [4, 2, 0]
        F = [2, 4, 0]
        G = [1.6, 3.2, 0]
        
        N = [3.2, 6.4, 0]
        O = [1.6, 3.2, 0]
        P = [4.8, 1.6, 0]
        Q = [6.4, 4.8, 0]
        
        square = Polygon(A, B, C, D, color = WHITE, fill_opacity = 0.4, fill_color = "#0A47C2", stroke_width=3)
        X = self.camera.frame.move_to(square).scale(1.1)
        self.add(X)
        self.play(DrawBorderThenFill(square))
        self.wait(2)
        
        DF = Line(D,F)
        FC = Line(F,C)
        CE = Line(C,E)
        EB = Line(E,B)
        
        equality_symbol_p1 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width = 2.5)
        equality_symbol_p2 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE, stroke_width = 2.5).next_to(equality_symbol_p1, DOWN, buff = 0.7)
        eq_sym = VGroup(equality_symbol_p1, equality_symbol_p2).move_to(DF.get_center()).scale(0.175).set_z_index(6).rotate(PI/2)
        eq_sym_c1 = eq_sym.copy().move_to(FC.get_center())
        eq_sym_c2 = eq_sym.copy().move_to(CE.get_center()).rotate(PI/2)
        eq_sym_c3 = eq_sym.copy().move_to(EB.get_center()).rotate(PI/2)
        
        
        l1 = Line(A, F, stroke_width = 3).set_z_index(4)
        l2 = Line(D, E, stroke_width = 3).set_z_index(4)
        l3 = Line(C, G, stroke_width = 3).set_z_index(4)
        
        #self.play(FadeIn(eq_sym, eq_sym_c1, eq_sym_c2, eq_sym_c3))
        self.play(Create(l1), Create(l2), FadeIn(eq_sym, eq_sym_c1, eq_sym_c2, eq_sym_c3))
        self.wait()
        self.play(Create(l3))
        self.wait(2)
        
        angle = MathTex(r"\angle", color="#FFBA07").scale(1).set_stroke(width=3)
        eq_to = MathTex(" = ").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(angle, RIGHT, buff=0.3)
        sym = Text(" ? ").scale(0.8).set_color(WHITE).set_stroke(width = 1).next_to(eq_to, RIGHT, buff=0.3)
        eqn = VGroup(angle, eq_to, sym)
        eqn.next_to(square, 4*DOWN)
            
        
        GF = Line(G, F)
        GC = Line(G, C)
        
        sector = Sector(arc_center=GC.get_start(), outer_radius=0.6, 
                    start_angle=GC.get_angle(), angle=PI/4, 
                    fill_opacity=1, fill_color="#FFBA07").set_z_index(1)
        self.play(GrowFromPoint(sector, G), FadeIn(eqn), self.camera.frame.animate.shift(1.5*DOWN))
        self.wait(5)
        group = VGroup(l1,l2,l3,square, eq_sym, eq_sym_c1, eq_sym_c2, eq_sym_c3)
        group_c1 = group.copy()
        group_c1.set_fill(color = "#005E2C")
        
        dot = Circle(radius=0.08, fill_color="#C22300", fill_opacity=1, stroke_width=2, stroke_color=WHITE).move_to(C).set_z_index(12)
        
        self.play(FadeOut(sector, eqn), FadeIn(dot))
        self.play(Indicate(dot, scale_factor=2, color=None), run_time=1.5)
        self.play(Rotate(group_c1, about_point = C, angle = -PI/2),
                  self.camera.frame.animate.shift(2*UP),
                  FadeOut(dot), run_time=1.5)
        self.wait()
        self.play(self.camera.frame.animate.move_to(C).scale(2).shift(3*DOWN), run_time=2)
        self.wait(2)
        
        group_c2 = group_c1.copy()
        self.play(Rotate(group_c2, about_point = C, angle = -PI/2), run_time=1.5)
        self.wait(2)
        
        group_c3 = group_c2.copy()
        self.play(Rotate(group_c3, about_point = C, angle = -PI/2), run_time=1.5)
        self.wait(2)

        R = [4, 8, 0]
        S = [8, 4, 0]

        line1 = Line(R, B).set_z_index(10)
        line2 = Line(D, S).set_z_index(10)
        everything = VGroup(line1, line2)
        
        final_square = Polygon(N, O, P, Q, color = WHITE, fill_opacity = 1, fill_color = "#850F85", stroke_width=3).set_z_index(1)
        self.play(FadeIn(final_square, everything))
        self.play(Indicate(final_square, color = None), run_time = 1.5)
        self.wait(2)
        
        diagonal = Line(G, Q, stroke_width = 7, color = "#000000").set_z_index(20)
        self.play(FadeIn(diagonal))
        #self.play(Indicate(diagonal, color = None))
        self.wait(3)
        #angle.shift(0.3*LEFT)
        #eq_to.shift(0.3*LEFT)
        GE = Line(G,E)
        sector_square = Sector(arc_center=GE.get_start(), outer_radius=0.8, 
                    start_angle=GE.get_angle(), angle=PI/2, 
                    fill_opacity=1, fill_color="#3DD771").set_z_index(1)
        
        sector_ninety = Square(stroke_width=3, stroke_color =WHITE, fill_opacity=1, 
                               fill_color="#3DD771").set_z_index(1).move_to(sector_square).scale(0.35)
        sector_ninety.rotate(-PI/6.77581983).shift(0.07*RIGHT+0.022*DOWN)
        self.play(GrowFromPoint(sector_ninety, G))
        self.wait(2)
        
        forty_five = MathTex(" 45^\circ ").scale(1).set_color(WHITE).set_stroke(width = 1).next_to(eq_to, RIGHT, buff=0.3)
        final_eq = VGroup(angle, eq_to, forty_five)
        final_eq.next_to(square, 4*DOWN)
        self.play(self.camera.frame.animate.move_to(square).scale(0.5).shift(1.5*DOWN), 
                  FadeIn(sector, angle, eq_to),
                  FadeOut(everything, group_c1, group_c2, group_c3, 
                          final_square, diagonal, sector_ninety), run_time=2)
        self.wait()
        
        self.play(FadeIn(forty_five))
        self.wait(2)
        
        square.set_fill(color = "#850F85")
        angle.set_color("#3DD771")
        fsector = Sector(arc_center=GF.get_start(), outer_radius=0.5, 
                    start_angle=GF.get_angle(), angle=PI/2, 
                    fill_opacity=1, fill_color="#3DD771").set_z_index(1).rotate(angle = PI, about_point = G)
        
        self.play(FadeOut(sector, final_eq), self.camera.frame.animate.shift(1.5*UP))
        self.wait(3)
        eqn.arrange(buff = 0.3)
        eqn.next_to(square, 4*DOWN)
        self.play(GrowFromPoint(fsector, G), FadeIn(eqn), self.camera.frame.animate.shift(1.5*DOWN))
        
        self.wait(3)