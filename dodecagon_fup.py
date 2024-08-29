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


class dodec_followUp(MovingCameraScene):

    
    def construct(self):
        M = [0.0681483474219, 3.3460652149512, 0]
        dodecagon = RegularPolygon(n=12, 
                                   fill_color = BLACK,
                                   fill_opacity = 1,
                                   radius = 3.8637033051563, 
                                   color = WHITE, 
                                   stroke_width = 6).move_to(M).set_z_index(4)
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
        #W = [-3.7955549577344, 7.2097685201075, 0]
        
        
        #Zoom out
        X = self.camera.frame.scale(1.9).move_to(dodecagon)
        self.add(X)

        line = Line(M, dodecagon.get_vertices()[0]).set_z_index(10)
        text = MathTex("5").next_to(line, 1.3*DOWN).scale(1.6).set_z_index(10)

        square = Square(side_length = 2*3.8637033051563, color = WHITE, stroke_width = 6, fill_color = "#D68000").set_z_index(2).move_to(M)

        self.play(FadeIn(dodecagon , line, text))
        self.wait(2)
        #A = dodecagon.animate.set_fill(color = "#0A47C2", opacity=1)
        #self.play(A)
        self.wait(2)
        
        equal_to_what = MathTex("A(", "\phantom{xxx}", ")\ =\ ? ").scale(2).set_color(WHITE).set_stroke(width = 1).next_to(dodecagon, DOWN, buff=2)
        dodecagon_copy = dodecagon.copy()
        square_copy = square.copy()
        followUp = VGroup(dodecagon_copy, square_copy)

        #dodecagon_copy.set_fill(color = "#0A47C2", opacity=1)

        self.play(A)
        self.play( FadeIn(equal_to_what), followUp.animate.scale(0.175).move_to(equal_to_what).shift(0.71*LEFT), self.camera.frame.animate.shift(2*DOWN))
        self.wait(2)
        #self.play(FadeOut(line, text, dodecagon_copy, equal_to_what))
        self.wait(2)