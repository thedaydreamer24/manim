from manim import *

config.frame_size = (1080,1920)
config.frame_width = 7.5

def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1[0:2],a2[0:2],b1[0:2],b2[0:2]])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return np.array([x/z, y/z,0])

class OctAreaFinal(MovingCameraScene):
    def construct(self):
        
        octagon = RegularPolygon(n=8, stroke_color=WHITE, stroke_width=6, fill_opacity = 1, color = '#0B47C2').scale(3).set_z_index(1)
        octagon.joint_type=LineJointType.ROUND 
        
        octagon_c = RegularPolygon(n=8, stroke_color=WHITE, stroke_width=6, fill_opacity = 0, color = '#0B47C2').scale(3).set_z_index(14)
        octagon_c.joint_type=LineJointType.ROUND 
        #with register_font("C:/Users/payal/Downloads/font/Athletics-Regular.ttf"):
        txt = Text("Octagon  Area  Proof",font='Athletics', color = TEAL_E).next_to(octagon, 5 * UP)
        A = self.camera.frame.animate.scale(1.3).shift(0.75*DOWN).save_state()
        self.play(A)
        vertices = octagon.get_vertices()
        
        
        
        ld = Line(vertices[4],vertices[0], stroke_color='#71DF96', stroke_width=6).set_z_index(10)
        sd = Line(vertices[3],vertices[5], stroke_color='#FF7E3B', stroke_width=6).set_z_index(9)
        
        label1 = MathTex("d_{1}", color = '#71DF96').next_to(ld, UP, buff = 0.25).scale(1.1).set_z_index(10)
        label2 = MathTex("d_{2}", color = '#FF7E3B').next_to(sd, RIGHT, buff = 0.25).shift(DOWN).scale(1.1).set_z_index(10)
        
        
        self.play(GrowFromCenter(octagon_c))
        self.wait(2)
        self.play(FadeIn(octagon))
        self.wait(2)
        self.play(FadeIn(ld), FadeIn(label1))
        self.wait(0.5)
        self.play(FadeIn(sd), FadeIn(label2))
        self.wait(1.5)
        self.play(FadeOut(sd), FadeOut(ld), FadeOut(octagon_c, label1, label2))
        
        #self.play(FadeIn(txt))
        self.wait(1)
        poly1 = Polygon(vertices[2],vertices[3],get_intersect(vertices[2], vertices[6], vertices[3], vertices[1]), fill_color=TEAL_E, fill_opacity=1, color=WHITE, stroke_width = 6).set_z_index(4)
        poly2 = Polygon(vertices[2],vertices[1],get_intersect(vertices[2], vertices[6], vertices[3], vertices[1]), fill_color=TEAL_E, fill_opacity=1, color=WHITE, stroke_width = 6).set_z_index(4)
        poly3 = Polygon(vertices[6],vertices[5],get_intersect(vertices[2], vertices[6], vertices[5], vertices[7]), fill_color=TEAL_E, fill_opacity=1, color=WHITE, stroke_width = 6).set_z_index(4)
        poly4 = Polygon(vertices[6],vertices[7],get_intersect(vertices[2], vertices[6], vertices[5], vertices[7]), fill_color=TEAL_E, fill_opacity=1, color=WHITE, stroke_width = 6).set_z_index(4)
        polyInOct = Polygon(vertices[3],vertices[4],vertices[5],vertices[7],vertices[0],vertices[1], stroke_color=WHITE, stroke_width=6, fill_opacity = 1, color = '#0B47C2').set_z_index(3)
        polyInOct.joint_type=LineJointType.ROUND 
               
        #Copy of polygons
        poly1_copy = poly1.copy().set_fill(BLACK, opacity = 1).set_stroke(width = 4, color = WHITE).set_z_index(2)
        poly2_copy = poly2.copy().set_fill(BLACK, opacity = 1).set_stroke(width = 4, color = WHITE).set_z_index(2)
        poly3_copy = poly3.copy().set_fill(BLACK, opacity = 1).set_stroke(width = 4, color = WHITE).set_z_index(2)
        poly4_copy = poly4.copy().set_fill(BLACK, opacity = 1).set_stroke(width = 4, color = WHITE).set_z_index(2)
        
        poly1_copy.joint_type=LineJointType.ROUND 
        poly2_copy.joint_type=LineJointType.ROUND 
        poly3_copy.joint_type=LineJointType.ROUND 
        poly4_copy.joint_type=LineJointType.ROUND 
        
        poly1.joint_type=LineJointType.ROUND
        poly2.joint_type=LineJointType.ROUND
        poly3.joint_type=LineJointType.ROUND
        poly4.joint_type=LineJointType.ROUND
        
        #Split the octagon
        line1 = Line(vertices[3], vertices[1], stroke_color=WHITE, stroke_width = 6).set_z_index(4)
        line2 = Line(vertices[5], vertices[7], stroke_color=WHITE, stroke_width = 6).set_z_index(4)
        line3 = Line(vertices[2], get_intersect(vertices[2], vertices[6], vertices[3], vertices[1]), stroke_color=WHITE, stroke_width = 6).set_z_index(4)
        line4 = Line(vertices[6], get_intersect(vertices[2], vertices[6], vertices[5], vertices[7]), stroke_color=WHITE, stroke_width = 6).set_z_index(4)
        self.wait()
        #self.play(Indicate(txt, scale_factor = 1), run_time = 1.2)
        self.play(FadeIn(txt))
        self.wait(0.5)
        self.play(FadeOut(txt))
        self.wait(2)
        self.play(Create(line1), Create(line2))
        self.wait(0.5)
        self.play(Create(line3), Create(line4), run_time = 0.5)
        self.wait(0.5)
        
        self.play(FadeIn(poly1, poly2, poly3, poly4), FadeOut(line1, line2, line3, line4))
        self.add(polyInOct)
        self.play(FadeIn(poly1_copy, poly2_copy,poly3_copy,poly4_copy), FadeOut(octagon))
        
        self.wait()
        
        #self.play(FadeOut(octagon))
        #self.wait(2)
        self.play(Rotate(poly3,about_point=get_intersect(vertices[2], vertices[6], vertices[5], vertices[7]),angle= -PI/2),run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(poly3.animate.shift(3*RIGHT),run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(Rotate(poly4, angle = PI/2,about_point=get_intersect(vertices[2], vertices[6], vertices[5], vertices[7])),run_time=4.4/6, rate_func=rate_functions.ease_in_out_sine)
        self.play(poly4.animate.shift(3*LEFT),run_time=4.4/6, rate_func=rate_functions.ease_in_out_sine)
        self.play(Rotate(poly2, angle=-PI/2, about_point=get_intersect(vertices[2], vertices[6], vertices[3], vertices[1])),run_time=1.7/3, rate_func=rate_functions.ease_in_out_sine)
        self.play(poly2.animate.shift(3*LEFT),run_time=1.7/3, rate_func=rate_functions.ease_in_out_sine) 
        self.play(Rotate(poly1, angle=PI/2, about_point=get_intersect(vertices[2], vertices[6], vertices[3], vertices[1])),run_time=0.5, rate_func=rate_functions.ease_in_out_sine)
        self.play(poly1.animate.shift(3*RIGHT),run_time=0.5, rate_func=rate_functions.ease_in_out_sine)
        self.wait(2)
            
        rect = Rectangle(width=3.0, height=2.11, stroke_color=WHITE, stroke_width=6, fill_opacity = 1, color = '#0B47C2').move_to(octagon.get_center()).set_z_index(8).scale(2)
        rect.joint_type=LineJointType.ROUND 
        
        
        arrow1 = Arrow(DOWN, UP, max_tip_length_to_length_ratio=0.1, buff=0.16).next_to(rect, LEFT+UP, buff=0.5).shift(2.2*DOWN)
        arrow2 = Arrow(UP, DOWN, max_tip_length_to_length_ratio=0.1, buff=0.16).next_to(rect, LEFT+DOWN, buff=0.5).shift(2.2*UP)
        arrows = VGroup(arrow1, arrow2)
        #arrows.shift(0.6*LEFT)
        arrows.set_color(WHITE)
        arrows.set_stroke(width = 4)
        size = MathTex("b").set_color('#FF7E3B').set_stroke(width = 1)
        
        size.next_to(arrow1, DOWN, buff = 0.25)
        
        arrow3 = Arrow(1.25*RIGHT, 1.25*LEFT, max_tip_length_to_length_ratio=0.1, buff=0.06).next_to(rect, DOWN, buff=0.5).shift(1.75*LEFT)
        arrow4 = Arrow(1.25*LEFT, 1.25*RIGHT, max_tip_length_to_length_ratio=0.1, buff=0.06).next_to(rect, DOWN, buff=0.5).shift(1.75*RIGHT)
        arrows_g2 = VGroup(arrow3, arrow4)
        arrows_g2.set_color(WHITE)
        arrows_g2.set_stroke(width = 4).shift(0.6*DOWN)
        size2 = MathTex("l").set_color('#71DF96').set_stroke(width = 1)
        size2.next_to(arrow3, 2.1*RIGHT).shift(0.005*LEFT)
        
        #self.play(GrowArrow(arrows[1], point_color=WHITE), GrowArrow(arrows[0], point_color=WHITE), GrowArrow(arrows_g2[0], point_color=WHITE), GrowArrow(arrows_g2[1], point_color=WHITE), FadeIn(size, size2))
        self.wait()
        octagon_c2 = octagon.copy()
        octagon_c2.set_opacity(0.2)
        self.play(FadeIn(octagon_c2), FadeIn(rect), FadeOut(poly1_copy, poly2_copy, poly3_copy, poly4_copy), FadeOut(poly1,poly2,poly3,poly4,polyInOct ))
        self.play(FadeOut(octagon_c2))
        #self.play(AnimationGroup(Circumscribe(rect,color='#F6F6F6',time_width=2.5),lag_ratio=1.5))
        self.wait(2)
        rect.set_z_index(1)
        self.play(rect.animate.set_opacity(0.2), FadeIn(octagon))
        self.wait(2)
        rectc2=rect.copy()
        rectc2.set_z_index(25).set_opacity(1)
        octagon.set_z_index(20)
        self.play(FadeIn(rectc2), octagon.animate.set_opacity(0.2))
        octagon_c2 = RegularPolygon(n=8, stroke_color='#71DF96', stroke_width=6, fill_opacity = 0, color = '#0B47C2').scale(3)
        octagon_c2.joint_type=LineJointType.ROUND 
        octagon_c2.set_z_index(20)

        self.wait()
        self.play(GrowArrow(arrows[1], point_color=WHITE), GrowArrow(arrows[0], point_color=WHITE), GrowArrow(arrows_g2[0], point_color=WHITE), GrowArrow(arrows_g2[1], point_color=WHITE), FadeIn(size, size2))
        self.wait(2)
        #Show answer
        
        vert = rect.get_vertices()
        rect_len = Line(vert[2], vert[3], stroke_color='#71DF96', stroke_width=6).set_z_index(16)
        rect_bred = Line(vert[1], vert[2], stroke_color='#FF7E3B', stroke_width=6).set_z_index(16)
        
        ans_rect = MathTex("A(", "\phantom{xxx}", ")").next_to(rect, 6 * DOWN).shift(DOWN+LEFT+0.2*RIGHT).shift(0.2*LEFT).shift(0.27*LEFT).shift(0.5*DOWN)
        
        poly_group = VGroup(poly1, poly2, poly3, poly4)
        
        rect_copy = rect.copy()
        equals = MathTex("=").next_to(ans_rect, RIGHT, buff = 0.1).shift(0.2*RIGHT)
        self.play(FadeIn(ans_rect),FadeIn(equals), rect_copy.animate.scale(0.116).next_to(ans_rect, buff = 0.1).shift(1.02*LEFT), self.camera.frame.animate.move_to(2*DOWN), run_time=1.5)
        
        l = MathTex("l", color = '#71DF96').next_to(equals, RIGHT, buff = 0.2).shift(0.315*RIGHT).scale(1.1).scale(1.2).shift(0.1*LEFT)
        mul = MathTex("\\times", color = WHITE).next_to(l, RIGHT, buff = 0.3)
        b = MathTex("b", color = '#FF7E3B').next_to(mul, RIGHT, buff = 0.2).scale(1.1).scale(1.2).shift(0.1*RIGHT)
        
        size2_copy = size2.copy()
        size_copy = size.copy()
        
        self.wait(0.5)
        self.play(size2_copy.animate.scale(1.1).scale(1.2).move_to(l), FadeIn(rect_len), FadeIn(mul))
        self.wait(0.5)
        self.play(size_copy.animate.scale(1.1).scale(1.2).move_to(b), FadeIn(rect_bred))
        
        self.wait(2)
        octagon.set_z_index(10)
        final_ans = MathTex("A(", "\phantom{xxx}", ")").next_to(ans_rect, 3*DOWN).shift(0.5*DOWN)
        #final_ans.shift(LEFT*0.34)
        octagon_copy = octagon.copy()
        rect_len.set_opacity(1).set_z_index(9)
        rect_bred.set_opacity(1).set_z_index(12)
        
        # Create the AnimationGroup and add all the animations
        animations = AnimationGroup(
            
            FadeIn(octagon),
            FadeIn(octagon_c),
            octagon.animate.set_stroke(color=WHITE),
            rect.animate.set_opacity(0.2),
            FadeOut(poly_group),
            run_time=1.5
        )

        # Play the animation group
        self.play(animations)
        self.wait(2)
        equals_copy = equals.copy()
        equals_copy.next_to(final_ans, RIGHT, buff = 0.1).shift(0.2*RIGHT).shift(0.021*LEFT)
        
        self.wait()
        eqn = VGroup(equals, l, mul, b)
        eqn_copy = eqn.copy()
        #self.play(eqn_copy.animate.next_to(final_ans, RIGHT, buff= 0.16))
        
        
        mul_copy = mul.copy()
        d1 = MathTex("d_{1}", color = '#71DF96').next_to(equals_copy, RIGHT, buff = 0.1).shift(0.1*RIGHT).scale(1.1)
        mul_copy.next_to(d1, RIGHT, buff = 0.1).shift(0.13*RIGHT)
        d2 = MathTex("d_{2}", color = '#FF7E3B').next_to(mul_copy, RIGHT, buff = 0.15).shift(0.13*RIGHT).scale(1.1)
        self.wait()
        
        ld.set_color('#71DF96')
        sd.set_color('#FF7E3B')
        rect_len_copy = rect_len.copy()
        rect_len_copy.set_z_index(14)
        self.play(FadeIn(rect_len_copy), FadeOut(rect_len))
        #self.play(ReplacementTransform(eqn_copy[1], d1), eqn_copy[2].animate.shift(RIGHT*0.37), rect_len_copy.animate.move_to(ld), eqn_copy[3].animate.shift(RIGHT*0.37))
        self.play(rect_len_copy.animate.move_to(ld))
        self.play(FadeIn(ld))
        self.wait()
        self.play( rect_bred.animate.move_to(sd).set_color('#FF7E3B'))
        self.play(FadeIn(sd))
        self.wait(2)
        self.play(FadeIn(final_ans),
                 octagon_copy.animate.scale(0.116).next_to(final_ans, buff = 0.1).shift(LEFT*1.02),
                  FadeIn(equals_copy))
        
        self.play(FadeIn(label1, label2))
        label1_copy = label1.copy()
        label2_copy = label2.copy()
        self.play(label1_copy.animate.scale(1.1).move_to(d1), FadeIn(mul_copy))
        self.wait(0.5)
        self.play(label2_copy.animate.scale(1.1).move_to(d2))
        self.wait(4)
        #ReplacementTransform(eqn_copy[1], d1), ReplacementTransform(eqn_copy[3], d2) self.play(FadeIn(mul_copy))