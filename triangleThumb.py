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


        self.add(triangle)
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
        self.add(triangle1, questionText, l1,l2,equality_symbol1, es2, es3,es6,d1,d2,d3,d4,d6,d7), FadeIn(d5,d6_copy,d8,d9,es4,es5,es7,es8,es9)
