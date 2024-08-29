from manim import *

config.media_width = "100%"
config.verbosity = "WARNING"
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

class starv4(MovingCameraScene):
    def construct(self):
        # Define the points
        A = [-4, -2, 0]
        B = [0, 6, 0]
        C = [2, -2, 0]
        D = [-4.0064689342404, 3.1982113378685, 0]
        E = [3.1911927437642, 3.1982113378685, 0]
        F=  [-0.2748217374162,1.983215224197,0]

        # Create the segments
        f = Line(A, B, color=TEAL, stroke_width=5)
        g = Line(B, C, color=TEAL, stroke_width=5)
        h = Line(C, D, color=TEAL, stroke_width=5)
        i = Line(D, E, color=TEAL, stroke_width=5)
        j = Line(E, A, color=TEAL, stroke_width=5)

        # Create the star polygon
        star_points = [A, B, C, D, E]
        star = Polygon(*star_points, color=TEAL, stroke_width=5).set_z_index(2)
        star.joint_type=LineJointType.ROUND 
        
        X = self.camera.frame.animate.move_to(star).scale(1.3)
        X.save_state()
        self.play(X)
        
        # Create the star by adding the segments to the scene
        self.play(Create(f))
        self.play(Create(g))
        self.play(Create(h))
        self.play(Create(i))
        self.play(Create(j))
        
        txt = Text("Sum of these angles?", font='Athletics', weight = BOLD).next_to(star, 3.6 * UP).scale(1.1)

        self.play(FadeIn(star),FadeOut(f,g,h,i,j))
        self.wait(2)
        
        #Create sectors
        s1 = Sector(arc_center=g.get_start(), outer_radius=0.8, start_angle=f.get_angle(), angle=PI/4.43349, fill_opacity=1, fill_color=RED_B).rotate(angle=PI, about_point=g.get_start())
        s2 = Sector(arc_center=i.get_start(), outer_radius=0.8, start_angle=h.get_angle(), angle=PI/4.4, fill_opacity=1, fill_color=BLUE_C).rotate(angle=PI, about_point=i.get_start())
        s3 = Sector(arc_center=j.get_end(), outer_radius=0.8, start_angle=j.get_angle(), angle=PI/6.5288, fill_opacity=1, fill_color=GREEN_B).rotate(angle=PI, about_point=j.get_end())
        s4 = Sector(arc_center=g.get_end(), outer_radius=0.8, start_angle=g.get_angle(), angle=PI/5.129, fill_opacity=1, fill_color=LIGHT_PINK).rotate(angle=PI, about_point=g.get_end())
        s5 = Sector(arc_center=i.get_end(), outer_radius=0.8, start_angle=i.get_angle(), angle=PI/5.0195, fill_opacity=1, fill_color=PURPLE_B).rotate(angle=PI, about_point=i.get_end())
        
        # Create angle symbols
        a1 = MathTex(r"\angle", color=RED_B).scale(1).set_stroke(width=3)
        a2 = MathTex(r"\angle", color=BLUE_C).scale(1).set_stroke(width=3)
        a3 = MathTex(r"\angle", color=GREEN_B).scale(1).set_stroke(width=3)
        a4 = MathTex(r"\angle", color=LIGHT_PINK).scale(1).set_stroke(width=3)
        a5 = MathTex(r"\angle", color=PURPLE_B).scale(1).set_stroke(width=3)

        # Position angle symbols
        a2.next_to(a1, RIGHT, buff=1)
        a3.next_to(a2, RIGHT, buff=1)
        a4.next_to(a3, RIGHT, buff=1)
        a5.next_to(a4, RIGHT, buff=1)

        # Create plus signs
        plus1 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus2 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus3 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus4 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)

        # Position plus signs
        plus1.next_to(a1, RIGHT, buff=0.3)
        plus2.next_to(a2, RIGHT, buff=0.3)
        plus3.next_to(a3, RIGHT, buff=0.3)
        plus4.next_to(a4, RIGHT, buff=0.3)
        
        #Add =?°
        equal_to = MathTex(" = ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        ques_sym = Text(" ? ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        equal_to.next_to(a5, RIGHT, buff=0.3)
        ques_sym.next_to(equal_to, RIGHT, buff=0.3)
        text_group2 = VGroup(a1,plus1,a2,  plus2,a3, plus3,a4,  plus4,a5, equal_to,ques_sym  )
        text_group2.arrange(buff = 0.3).next_to(star, 3.6 * DOWN).scale(1.1)
        #text_group2.shift(0.61*LEFT)
        
        secgr = VGroup(s1,s2,s3,s4,s5)
        self.play(Create(secgr), FadeIn(txt, text_group2), run_time = 1.6)
        
        self.wait(2)
        
        G = [6, 2, 0]
        H = [7.3345847774472, 0, 0]
        I = [10, 0, 0]
        J = [6, 0 , 0]
        K = [4.2113460923646,2.0616634037924,0]
        
        tri_proof = Polygon(G,H,I, color = '#0A47C2', stroke_width=5).set_z_index(14)
        tri_proof.joint_type=LineJointType.ROUND 
        line_proof = DashedLine(H, J).set_z_index(2)

        self.wait(2)
        x = MathTex("1").scale(3).move_to(F)
        y = MathTex("2").scale(3).move_to(F)
        z = MathTex("3").scale(3).move_to(F)
        #self.play(LaggedStart(AnimationGroup(AnimationGroup(star.animate.set_stroke(opacity=0), txt.animate.set_opacity(0), secgr.animate.set_opacity(0)), AnimationGroup(FadeIn(x)), lag_ratio=0.5)))
        #self.play(FadeTransform(x,y))
        #self.play(FadeTransform(y,z))
        #self.wait(2)
        #self.play(LaggedStart(AnimationGroup(AnimationGroup(FadeOut(z)), AnimationGroup(star.animate.set_stroke(opacity=1), txt.animate.set_opacity(1), secgr.animate.set_opacity(1)), lag_ratio=0.9)))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(secgr, star, txt, text_group2), self.camera.frame.animate.move_to(tri_proof).scale(0.7), FadeIn(tri_proof, line_proof), run_time = 1.5))
        self.wait(2)
        a = Line(G, I)
        b = Line(I, H)
        c = Line(H, G)
        d = Line(H, J)
        e = Line(H, K)
        
        s6 = Sector(arc_center=a.get_end(), outer_radius=0.8, start_angle=a.get_angle(), angle=PI/7.30549129, fill_opacity=1, fill_color='#ED6CEF').rotate(angle=PI, about_point=a.get_end())
        s7 = Sector(arc_center=c.get_end(), outer_radius=0.8, start_angle=c.get_angle(), angle=PI/6.3047948, fill_opacity=1, fill_color=ORANGE).rotate(angle=PI, about_point=c.get_end())
        s7.set_z_index(2)
        self.wait(2)
        self.play(FadeIn(s6, s7))
        
        s8 = Sector(arc_center=d.get_start(), outer_radius=0.8, start_angle=c.get_angle(), angle=PI/3.24, fill_opacity=1, fill_color=TEAL)
        #self.play(FadeIn(s8))
        
        self.wait(2)
        
        s6_copy = s6.copy()
        s7_copy = s7.copy()
        s7_copy.set_z_index(6)
        # Shift s6_copy and s7_copy to their initial positions
        #self.play()
        
        s7_copy_pos = Sector(arc_center=e.get_start(), outer_radius=0.8, start_angle=c.get_angle(), angle=PI/5, fill_opacity=1, fill_color=ORANGE).shift(0.02*DR+0.01*LEFT)
        
        t = ValueTracker(0)
        self.add(s7_copy)

        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector = s7_copy_pos.get_center() - s7_copy.get_center()

        self.add(s7_copy)

        s7_copy.add_updater(lambda x: x.become(
            Sector(
                arc_center=c.get_end(),
                outer_radius=0.8,
                start_angle=c.get_angle(),
                angle=PI / 6.3047948,
                fill_opacity=1,
                fill_color=ORANGE
            ).rotate(angle=PI, about_point=c.get_end()).rotate(2*PI / 2 * t.get_value()).shift(distance_vector * t.get_value())
        ))

        self.play(t.animate.set_value(1), s6_copy.animate.align_to(line_proof, RIGHT).rotate(PI/178), run_time=2)
        s7_copy.suspend_updating()
        self.wait(2)
        
        s8_copy = s8.copy()
        s8_copy.set_color(TEAL).set_z_index(8)
        
        ang1 = MathTex(r"\angle", color='#ED6CEF').scale(1).set_stroke(width=3)
        pl1  = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        ang2 = MathTex(r"\angle", color=ORANGE).scale(1).set_stroke(width=3)
        eq   = MathTex(" = ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        ang3 = MathTex(r"\angle", color=TEAL).scale(1).set_stroke(width=3)
        
        text_group1 = VGroup(ang3, eq, ang1, pl1, ang2)
        text_group1.arrange(buff = 0.3).next_to(tri_proof, 6 * DOWN).scale(1.1)
        
        self.play(FadeIn(s8_copy, text_group1))
        
        txt2 = Text("Exterior Angle Theorem", font='Athletics', weight = BOLD).next_to(tri_proof, 5 * UP).scale(0.65)
        
        self.wait(2)
        
        self.play(FadeIn(txt2))
        
        self.wait(2)
        
        self.play(AnimationGroup(FadeOut(tri_proof, s6,s7,s8_copy,s6_copy,s7_copy,line_proof,txt2,text_group1), self.camera.frame.animate.move_to(star).scale(1.42857143), FadeIn(secgr, star, txt, text_group2), run_time=1.5))
        
        
        L = (get_intersect(A, B, D, E))
        line1 = DashedLine(L,B, color = TEAL, stroke_width=5).set_z_index(4)
        tri1 = Polygon(L,A,E, color = PURE_RED, stroke_width=5).set_z_index(10)
        self.play(FadeIn(tri1, line1), star.animate.set_stroke(opacity=0.2), s1.animate.set_opacity(0.2), s2.animate.set_opacity(0.2), s4.animate.set_opacity(0.2))
        self.wait(2)
        
        s3_copy = s3.copy()
        s3_copy_pos = Sector(arc_center=line1.get_start(), outer_radius=0.8, start_angle=line1.get_angle(), angle=PI/6.5288, fill_opacity=1, fill_color=GREEN_B).rotate(angle=-PI/6.5288, about_point=line1.get_start())
        #self.play(FadeIn(s3_copy_pos))
        
        lineLE = Line(L,E)
        s5_copy_pos = s5.copy()
        s5_copy_pos.rotate(PI).move_to(lineLE, LEFT).shift(0.24*UP+0.01*LEFT).shift(0.009*RIGHT+0.004*DOWN)
        s5_copy = s5.copy()
        u = ValueTracker(0)
        self.add(s5_copy)

        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector2 = s5_copy_pos.get_center() - s5_copy.get_center()

        self.add(s5_copy)

        s5_copy.add_updater(lambda x: x.become(
            Sector(arc_center=i.get_end(), outer_radius=0.8, start_angle=i.get_angle(), angle=PI/5.0195, fill_opacity=1, fill_color=PURPLE_B).rotate(angle=PI, about_point=i.get_end()).rotate(2*PI / 2 * u.get_value()).shift(distance_vector2 * u.get_value())
        ))

        
        s3_c2 = s3.copy()
        s3_c2.set_stroke(width = 5, color = WHITE).set_fill(opacity = 0).set_z_index(20)
        s3_c2.joint_type=LineJointType.ROUND 
        
        s5_c2 = s5.copy()
        s5_c2.set_stroke(width = 5, color = WHITE).set_fill(opacity = 0).set_z_index(20)
        s5_c2.joint_type=LineJointType.ROUND 
        #self.play(LaggedStart(AnimationGroup(AnimationGroup(Indicate(s5_c2), Indicate(s3_c2)), AnimationGroup(FadeOut(s5_c2, s3_c2)), lag_ratio = 1, run_time = 1)))
        
        self.play(FadeIn(s3_c2, s5_c2))
        self.play(Indicate(s3_c2, color = WHITE), Indicate(s5_c2, color = WHITE))
        self.play(FadeOut(s3_c2, s5_c2), run_time = 0.5)
        
        self.play(u.animate.set_value(1), s3_copy.animate.move_to(s3_copy_pos.get_center()), run_time=2)
        s5_copy.suspend_updating()
        self.wait(2)
        
        #s9 = Sector(arc_center=line1.get_start(), outer_radius=0.8, start_angle=line1.get_angle(), angle=-PI/2.83755254, fill_opacity=1, fill_color=YELLOW)
        
        #self.play(FadeIn(s9),FadeOut(s3_copy,s5_copy))
        #self.wait(2)
        
        M = (get_intersect(B, C, D, E))
        line2 = DashedLine(M,B, color = TEAL, stroke_width=5).set_z_index(4)
        tri2 = Polygon(D,M,C, color = PURE_RED, stroke_width=5).set_z_index(10)
        
        self.play(FadeOut(tri1,line1), FadeIn(line2, tri2), s2.animate.set_opacity(1), s4.animate.set_opacity(1), s3.animate.set_opacity(0.2), s5.animate.set_opacity(0.2))
        self.wait(2)
        
        s4_copy = s4.copy()
        
        l = Line(D,M)
        s2_copy = s2.copy()
        s2_copy_pos = s2.copy()
        s2_copy_pos.align_to(l, UR).rotate(PI).shift(0.51*UP)
        #s2_copy_pos.shift(0.0865*LEFT+0.008*UP)
        
        v = ValueTracker(0)
        self.add(s2_copy)

        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector3 = s2_copy_pos.get_center() - s2_copy.get_center()

        self.add(s2_copy)

        s2_copy.add_updater(lambda x: x.become(
            Sector(arc_center=i.get_start(), outer_radius=0.8, start_angle=h.get_angle(), angle=PI/4.4, fill_opacity=1, fill_color=BLUE_C).rotate(angle=PI, about_point=i.get_start()).rotate(2*PI / 2 * v.get_value()).shift(distance_vector3 * v.get_value())
        ))

        s4_c2 = s4.copy()
        s4_c2.set_stroke(width = 5, color = WHITE).set_fill(opacity = 0).set_z_index(20)
        s4_c2.joint_type=LineJointType.ROUND 
        
        s2_c2 = s2.copy()
        s2_c2.set_stroke(width = 5, color = WHITE).set_fill(opacity = 0).set_z_index(20)
        s2_c2.joint_type=LineJointType.ROUND 
        
        self.play(FadeIn(s2_c2, s4_c2))
        self.play(Indicate(s2_c2, color = WHITE), Indicate(s4_c2, color = WHITE))
        self.play(FadeOut(s4_c2, s2_c2), run_time = 0.5)
        
        self.play(v.animate.set_value(1), s4_copy.animate.align_to(line2, DL).shift(0.093*RIGHT+0.015*DOWN), run_time=2)
        s2_copy.suspend_updating()
        self.wait(2)
        
        #s10 = Sector(arc_center=i.get_start(), outer_radius=0.8, start_angle=h.get_angle(), angle=PI/2.36955106, fill_opacity=1, fill_color='#0A47C2').rotate(angle=PI, about_point=i.get_start()).align_to(line2, DL).rotate(PI).shift(0.1*LEFT)
        #s10.rotate(-PI/5.129).shift(0.24*DOWN+0.1*RIGHT)
        #self.play(FadeIn(s10), FadeOut(s2_copy,s4_copy))
        
        self.wait(2)
        tri3 = Polygon(B,L,M, color = PURE_RED, stroke_width=5).set_z_index(15)
        self.play(FadeOut(tri2, line2), FadeIn(tri3), s2.animate.set_opacity(0.2), s4.animate.set_opacity(0.2), s1.animate.set_opacity(1))
        self.wait(2)
        tri3_copy = Polygon(B,L,M, color = TEAL, stroke_width=5).set_z_index(16)
        tri3_copy.joint_type=LineJointType.ROUND 
        #self.play(ShowPassingFlash(tri3_copy, time_width=2, run_time=2))
        self.wait()
        self.play(self.camera.frame.animate.move_to(tri3).scale(0.5), FadeOut(txt, text_group2))
        self.wait(2)

        s5_copy2 = Sector(arc_center=i.get_end(), outer_radius=0.8, start_angle=i.get_angle(), angle=PI/5.0195, fill_opacity=1, fill_color=PURPLE_B).rotate(angle=PI, about_point=i.get_end()).rotate(PI).move_to(lineLE, LEFT).shift(0.24*UP+0.01*LEFT).shift(0.009*RIGHT+0.004*DOWN)
        s2_copy2 = Sector(arc_center=i.get_start(), outer_radius=0.8, start_angle=h.get_angle(), angle=PI/4.4, fill_opacity=1, fill_color=BLUE_C).rotate(angle=PI, about_point=i.get_start()).align_to(l, UR).rotate(PI).shift(0.51*UP)
        
        
        self.play(Indicate(s2_copy, scale_factor=1, run_time=1.5),Indicate(s3_copy, scale_factor=1, run_time=1.5),Indicate(s4_copy, scale_factor=1, run_time=1.5),Indicate(s5_copy, scale_factor=1, run_time=1.5), Indicate(s1, scale_factor=1, run_time=1.5))
        degree_tex = MathTex("180^\circ").move_to(tri3.get_center()).scale(0.6).shift(0.2*RIGHT+0.3*DOWN)
        self.wait()
        self.play(Write(degree_tex))
        self.wait()
        
        self.play(self.camera.frame.animate.move_to(star).scale(2), FadeIn(txt, text_group2))
        
        self.wait()
        sectors = VGroup(s2,s3,s4,s5)
        
        fstar = Polygon(*star_points, color=TEAL, stroke_width=5).set_z_index(2)
        fstar.joint_type=LineJointType.ROUND 
        
        #Animate all the sectors back to their original positions
        #----------------------------------------------------------
        
        
        p = ValueTracker(0)
        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector4 = s5.get_center() - s5_copy2.get_center()
        
        s5_copy2.add_updater(lambda x: x.become(
            Sector(arc_center=i.get_end(), outer_radius=0.8, start_angle=i.get_angle(), angle=PI/5.0195, fill_opacity=1, fill_color=PURPLE_B).rotate(angle=PI, about_point=i.get_end()).rotate(PI).move_to(lineLE, LEFT).shift(0.24*UP+0.01*LEFT).shift(0.009*RIGHT+0.004*DOWN).rotate(2*PI / 2 * p.get_value()).shift(distance_vector4 * p.get_value())
        ))
        
        #self.play(, run_time=2)
        
        q = ValueTracker(0)
        
        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector5 = s2.get_center() - s2_copy2.get_center()

        s2_copy2.add_updater(lambda x: x.become(
            Sector(arc_center=i.get_start(), outer_radius=0.8, start_angle=h.get_angle(), angle=PI/4.4, fill_opacity=1, fill_color=BLUE_C).rotate(angle=PI, about_point=i.get_start()).align_to(l, UR).rotate(PI).shift(0.51*UP).rotate(2*PI / 2 * q.get_value()).shift(distance_vector5 * q.get_value())
        ))
        
        self.play(ReplacementTransform(s2_copy, s2_copy2), ReplacementTransform(s5_copy, s5_copy2))
        
        self.play(FadeIn(fstar), FadeOut(star), s1.animate.set_opacity(1), q.animate.set_value(1), s4_copy.animate.move_to(s4.get_center()), p.animate.set_value(1), s3_copy.animate.move_to(s3.get_center()), run_time=2)
        
        text_group2_woq = VGroup(a1,plus1,a2,  plus2,a3, plus3,a4,  plus4,a5, equal_to)
        
        degree_tex_copy = degree_tex.copy()
        self.play(degree_tex_copy.animate.scale(1.6).next_to(equal_to, buff=0.3).shift(0.2*LEFT),text_group2_woq.animate.shift(0.2*LEFT), FadeOut(ques_sym), run_time = 1.5)
        self.wait(3)

        O=(-14.2614736893265,6.7337036543719,0)
        P=(-13.1094987926487,-3.9632061004942,0)
        Q=(-18.2769290434609,5.8450373055061,0)
        R=(-10.6080675884338,-0.8364170952256,0)
        S=(-20,2,0)
        T=(-11.266338957964,3.2119518273852,0 )
        N=N=(-18.0465340641253,-2.7783176353398,0)

        follow_up = [N,O,P,Q,R,S,T]
        star_follow_up = Polygon(*follow_up, color=TEAL, stroke_width=5).set_z_index(2)
        star.joint_type=LineJointType.ROUND 

        self.play(self.camera.frame.animate.move_to(star_follow_up).scale(1.2))
        self.wait(2)
        
        NO = Line(N,O)
        OP = Line(O,P)
        PQ = Line(P,Q)
        QR = Line(Q,R)
        RS = Line(R,S)
        ST = Line(S,T)
        TN = Line(T,N)

        fs1 = Sector(arc_center=NO.get_start(), outer_radius=0.96, start_angle=NO.get_angle(), angle=-PI/6.70621645, fill_opacity=1, fill_color=PINK)
        fs2 = Sector(arc_center=OP.get_start(), outer_radius=0.96, start_angle=OP.get_angle(), angle=-PI/6.46426108, fill_opacity=1, fill_color=BLUE_C)
        fs3 = Sector(arc_center=PQ.get_start(), outer_radius=0.96, start_angle=PQ.get_angle(), angle=-PI/8.31958983, fill_opacity=1, fill_color=YELLOW)
        fs4 = Sector(arc_center=QR.get_start(), outer_radius=0.96, start_angle=QR.get_angle(), angle=-PI/8.50908655, fill_opacity=1, fill_color=RED_B)
        fs5 = Sector(arc_center=RS.get_start(), outer_radius=0.96, start_angle=RS.get_angle(), angle=-PI/7.41985976, fill_opacity=1, fill_color=PURPLE)
        fs6 = Sector(arc_center=ST.get_start(), outer_radius=0.96, start_angle=ST.get_angle(), angle=-PI/7.28598128, fill_opacity=1, fill_color=ORANGE)
        fs7 = Sector(arc_center=TN.get_start(), outer_radius=0.96, start_angle=TN.get_angle(), angle=-PI/5.36351538 , fill_opacity=1, fill_color=GREEN_B)

        # Create angle symbols
        f1 = MathTex(r"\angle", color=RED_B).scale(1).set_stroke(width=3)
        f2 = MathTex(r"\angle", color=BLUE_C).scale(1).set_stroke(width=3)
        f3 = MathTex(r"\angle", color=GREEN_B).scale(1).set_stroke(width=3)
        f4 = MathTex(r"\angle", color=PURPLE).scale(1).set_stroke(width=3)
        f5 = MathTex(r"\angle", color=YELLOW).scale(1).set_stroke(width=3)
        f6 = MathTex(r"\angle", color=PINK).scale(1).set_stroke(width=3)
        f7 = MathTex(r"\angle", color=ORANGE).scale(1).set_stroke(width=3)

        # Position angle symbols
        f2.next_to(f1, RIGHT, buff=1)
        f3.next_to(f2, RIGHT, buff=1)
        f4.next_to(f3, RIGHT, buff=1)
        f5.next_to(f4, RIGHT, buff=1)
        f6.next_to(f5, RIGHT, buff=1)
        f7.next_to(f6, RIGHT, buff=1)

        # Create plus signs
        p1 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        p2 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        p3 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        p4 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        p5 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        p6 = MathTex("+", color=WHITE).scale(0.8).set_stroke(width = 3)

        # Position plus signs
        p1.next_to(f1, RIGHT, buff=0.3)
        p2.next_to(f2, RIGHT, buff=0.3)
        p3.next_to(f3, RIGHT, buff=0.3)
        p4.next_to(f4, RIGHT, buff=0.3)
        p5.next_to(f5, RIGHT, buff=0.3)
        p6.next_to(f6, RIGHT, buff=0.3)
        
        
        #Add =?°
        eq_to = MathTex(" = ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        sym = Text(" ? ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        eq_to.next_to(f7, RIGHT, buff=0.3)
        sym.next_to(eq_to, RIGHT, buff=0.3)

        follow_up_eq = VGroup(f1,p1,f2,  p2,f3, p3, f4, p4, f5, p5, f6, p6, f7 , eq_to,sym  )
        follow_up_eq.arrange(buff = 0.3).next_to(star_follow_up, 4.32 * DOWN).scale(1.2)

        self.play(FadeIn(star_follow_up))
        self.wait(2)
        txt_copy = txt.copy()
        txt_copy.next_to(star_follow_up, 4.32 * UP).scale(1.2)
        self.play(FadeIn(txt_copy, follow_up_eq, fs1, fs2, fs3, fs4, fs5, fs6, fs7))
        self.wait(3)

