from manim import *
config.media_width = "100%"
config.verbosity = "WARNING"
config.frame_size = (1080,1920)
config.frame_width = 7.5
config.background_color=BLACK

class TwoSquares(MovingCameraScene):
    def construct(self):
        
        
        
        #Create squares
        square1 = Square(fill_opacity=0, stroke_width=5, stroke_color=WHITE).scale(2).set_z_index(2).shift(LEFT)
        square2 = Square(fill_opacity=0, stroke_width=5, stroke_color=WHITE).scale(1).set_z_index(2).shift(LEFT)
        squareGroup = VGroup(square1, square2)
        

        #Position square2
        square2.next_to(square1, RIGHT, buff=0).shift(DOWN)
        
        #JoinType
        square1.joint_type=LineJointType.ROUND 
        square2.joint_type=LineJointType.ROUND 
        
        #Add dots
        dot1 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square1.get_corner(UL)).set_z_index(4)
        dot2 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square1.get_corner(UR)).set_z_index(4)
        dot3 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square1.get_corner(DL)).set_z_index(4)
        dot4 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square1.get_corner(DR)).set_z_index(4)
        dot5 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square2.get_corner(UL)).set_z_index(4)
        dot6 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square2.get_corner(UR)).set_z_index(4)
        dot7 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square2.get_corner(DR)).set_z_index(4)
        
        
        
        #Create lines to form the question
        line1 = Line(square1.get_corner(UR), square2.get_corner(UR), color=WHITE, stroke_width=5).set_z_index(2)
        line2 = Line(square1.get_corner(UL), square2.get_corner(UL), color=WHITE, stroke_width=5).set_z_index(2)
        line3 = Line(square2.get_corner(UL), square1.get_corner(DL), color=WHITE, stroke_width=5).set_z_index(2)
        line4 = Line(square2.get_corner(UR), square1.get_corner(DL), color=WHITE, stroke_width=5).set_z_index(2)
        
        #Make a polygon using the lines
        polygon = Polygon(
            square1.get_corner(UR), square2.get_corner(UR), square1.get_corner(DL),
            square2.get_corner(UL), square1.get_corner(UL),
            fill_color="#3DD771", fill_opacity=1, color=WHITE
        )
        
        
        #JoinType
        polygon.joint_type=LineJointType.ROUND 

        X = self.camera.frame.animate.scale(1.67).move_to(polygon).shift(2*DOWN)
        self.play(X)
        
        #Show the size of square1
        
        arrow1 = Arrow(DOWN, UP, max_tip_length_to_length_ratio=0.1).next_to(square1, LEFT+UP, buff=0.5).shift(2*DOWN)
        arrow2 = Arrow(UP, DOWN, max_tip_length_to_length_ratio=0.1).next_to(square1, LEFT+DOWN, buff=0.5).shift(2*UP)
        arrows = VGroup(arrow1, arrow2)
        arrows.set_color(WHITE)
        arrows.set_stroke(width = 4)
        #arrows.set_x(0)
        
        size = MathTex("12").set_color("#3DD771").set_stroke(width = 1).scale(1)
        size.next_to(arrow1, DOWN, buff = 0.35)
        #size.scale(0.8)
        
        #Add everything
        #self.add(square1, square2, line1, line2, line3, line4, polygon)
    
        
        #self.play(GrowFromEdge(square1, DR, point_color=WHITE),
        #          GrowFromEdge(square2, DL, point_color=WHITE)
        #          )
        self.play(Create(square1), Create(square2))
        self.play(GrowArrow(arrows[1], point_color=WHITE), 
                  GrowArrow(arrows[0], point_color=WHITE), 
                  FadeIn(size),)
        self.play(FadeIn(dot1, dot2, dot3, dot4, dot5, dot6, dot7))
        
        self.play(Create(line1))
        self.play(Create(line4))
        self.play(Create(line2))
        self.play(Create(line3))
        questionText = Text("Area of the shaded portion?", color = WHITE, font='Athletics', t2c={"shaded": "#3DD771"}).next_to(polygon, UP, buff=1.5).scale(0.9)

        self.play(FadeIn(polygon))
        self.wait()
        
        #shift_amount = LEFT * 2 
        #camera_frame = self.camera.frame
        question = polygon.copy()
        question.set_stroke(width = 2)
        equal_to_what = MathTex("A(", "\phantom{xxx}", ")\ =\ ? ").scale(1.25).set_color(WHITE).set_stroke(width = 1).next_to(polygon, DOWN, buff=1.5)
        #Y = self.camera.frame.animate.move_to(RIGHT)
        self.play(self.camera.frame.animate.shift(DOWN), question.animate.next_to(equal_to_what, RIGHT).scale(0.15).shift(5.33*LEFT), FadeIn(equal_to_what), FadeIn(questionText))

        self.wait(5)
        
        #Dashed Lines for solving
        dashed_1 = DashedLine(config.left_side, config.right_side, stroke_width=4)
        dashed_1.move_to(square2, DOWN).set_length(8)
       
        
        self.play(FadeOut(question), FadeOut(equal_to_what, questionText))
        self.wait()
        
        # Show parallel lines
        l1 = Line(square2.get_corner(UL), square2.get_corner(UR), color=PURE_RED, stroke_width=7).set_z_index(2)
        #l2 = Line(square1.get_corner(DL), square2.get_corner(DR), color=PURE_RED, stroke_width=4).set_z_index(2)
        l3 = Line(square1.get_corner(UL), square1.get_corner(UR), color=PURE_RED, stroke_width=8.6).set_z_index(2)
        l4 = Line(dot3.get_center(), dot7.get_center(), color=PURE_RED, stroke_width=7).set_z_index(2)
        l5 = Line(dot3.get_center(), dashed_1.get_end(), color=PURE_RED, stroke_width=7).set_z_index(2)
        self.play(FadeIn(l1, l4))
        l4_half = Line(dot4.get_center(), dot7.get_center(), color=PURE_RED, stroke_width=7).set_z_index(2)
        arrow_1 = Arrow(start=l1.get_start(), end=l1.get_center(), color=WHITE,stroke_width=0.5,max_tip_length_to_length_ratio=1).set_z_index(10).shift(0.5*RIGHT)
        arrow_2 = Arrow(start=l4_half.get_start(), end=l4_half.get_center(), color=WHITE,stroke_width=0.5,max_tip_length_to_length_ratio=1).set_z_index(10).shift(0.5*RIGHT)
        self.play(Indicate(l1, color = None, scale_factor = 1.4), Indicate(l4, color = None))
        self.play(FadeOut(l1, l4), FadeIn(arrow_1, arrow_2))
        self.wait()
        #Indicate tri1
        
        tri1 = Polygon(dot3.get_center(), dot5.get_center(), dot6.get_center(), color = "#0A47C2", fill_opacity=1, stroke_width = 5)
        self.play(FadeIn(tri1))
        self.wait(0.5)
        
        #self.play(Indicate(tri1, color = "#9E2F00", scale_factor=1), run_time=1.5)
        
        
        # First move
        
        polygon_4sides = Polygon(
            square1.get_corner(UR), square2.get_corner(UR), square2.get_corner(UL),
            square1.get_corner(UL),
            fill_color="#3DD771", fill_opacity=1, color=WHITE, stroke_width = 5
        )
        
        
        
        dot8 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square2.get_corner(DR)).set_z_index(4)
        dot8.shift(2*RIGHT)
        #self.play(FadeIn(dot8))
        
        A = Dot(line1.get_end(),radius=0.01,color=BLACK)
        B = Dot(line3.get_end(),radius=0.01,color=BLACK)
        C = Dot(line1.get_end(),radius=0.01,color=BLACK)        
       
        triangle1 =Polygon(A.get_center(),B.get_center(),C.get_center(),color=WHITE, fill_color="#0A47C2", fill_opacity=1, stroke_width=5)
        
        
        #self.add(triangle1)
        triangle1.joint_type=LineJointType.ROUND
        self.play(FadeIn(triangle1, polygon_4sides))
        self.wait()
        
        #line_a1 = Line(square2.get_corner(UL), square1.get_corner(DL), color=BLACK)  # Modify this line
        #line_a2 = Line(square2.get_corner(UR), square1.get_corner(DL), color=BLACK)  # Modify this line
        
        dot3_copy = dot3.copy()
        dot3_copy.set_color(PURE_RED).set_stroke(width = 4, color  =WHITE)
        self.play(FadeIn(dot3_copy))
        self.play(Indicate(dot3_copy, scale_factor=2, color = None))
        self.play(FadeIn(l4))
        self.wait(0.5)
        self.play(FadeIn(dashed_1), self.camera.frame.animate.shift(RIGHT))
        triangle1.add_updater(lambda x:x.become(Polygon(dot3_copy.get_center(),line3.get_start(),line4.get_start(),color=WHITE, fill_color="#0A47C2", fill_opacity=1, stroke_width=5)))
        self.wait(2)
        
        self.play( FadeOut(polygon, tri1), FadeOut(line3), FadeOut(line4) )
        self.wait(2)
        self.play(FadeOut(l4), FadeIn(l5))
        self.wait(2)
        
        triangle1_pos = Polygon(dot5.get_center(),dot6.get_center(),dot8.get_center(),color=WHITE, fill_color="#3DD771", fill_opacity=0.25, stroke_width=5).set_z_index(0)
        
        self.play(AnimationGroup(AnimationGroup(dot3_copy.animate.move_to(dot8.get_center())), AnimationGroup(FadeIn(triangle1_pos)), lag_ratio=0), run_time=2)
            
        #Indicate tri2
        tri2 = Polygon(dot1.get_center(), dot2.get_center(), dot8.get_center(), color = "#3DD771", fill_opacity=1, stroke_width=5, stroke_color = WHITE)
        tri2.joint_type=LineJointType.ROUND 
        #self.play(Indicate(tri2), run_time=1.5, color = None)
        triangle1.set_z_index(0)
        self.play(FadeIn(tri2), FadeOut(triangle1_pos), run_time=0.5)
        self.play(Indicate(tri2, color = None, scale_factor=1.2), FadeOut(triangle1))
        #self.play(Indicate(tri2, color = None, scale_factor=1.2))
        self.wait()
        
        
        #Second move
        
        X = Dot(line1.get_start(),radius=0.01,color=BLACK)
        Y = Dot(line2.get_start(),radius=0.01,color=BLACK)
        Z = Dot(dot8.get_center(),radius=0.01,color=BLACK)        
        
        triangle2 =Polygon(X.get_center(),Y.get_center(),Z.get_center(),color=WHITE, fill_color="#0A47C2", fill_opacity=1, stroke_width=5)
        triangle2.joint_type=LineJointType.ROUND
        
        self.play(FadeOut(polygon_4sides), FadeOut(arrow_1, arrow_2), dot3_copy.animate.set_fill(color  ="#0A47C2" ))
        self.wait(2)
        
        #self.play(Indicate(tri2, color = "#9E2F00", scale_factor=1), run_time=1.5)
        
        self.play(FadeIn(l3))
        l5_half = Line(dot3.get_center(), dot4.get_center(), color=PURE_RED, stroke_width=7).set_z_index(2)
        arrow_3 = Arrow(start=l3.get_start(), end=l3.get_center(), color=WHITE,stroke_width=0.5,max_tip_length_to_length_ratio=0.5).set_z_index(10).shift(0.5*RIGHT)
        arrow_4 = Arrow(start=l5_half.get_start(), end=l5_half.get_center(), color=WHITE,stroke_width=0.5,max_tip_length_to_length_ratio=0.5).set_z_index(10).shift(0.5*RIGHT)
        self.play(Indicate(l3, color = None, scale_factor = 1.4), Indicate(l5, color = None))
        self.play(FadeOut(l3, l5), FadeIn(arrow_3, arrow_4))
        self.wait()

        self.play(FadeIn(triangle2))
        tri2.set_z_index(0)
        self.play(FadeOut(tri2))
        
        dot8_copy = dot8.copy()
        dot8_copy.set_color(PURE_RED).set_stroke(width = 4, color  =WHITE)
        self.play(FadeIn(dot8_copy))
        self.play(Indicate(dot8_copy, scale_factor=2, color = None), FadeOut(dot3_copy))
        self.play(FadeIn(l5))
        self.wait()
        linef1 = Line(square1.get_corner(UR), dot8_copy.get_center(), color=WHITE, stroke_width=5)
        linef2 = Line(square1.get_corner(UL), dot8_copy.get_center(), color=WHITE, stroke_width=5)
        
        triangle2.add_updater(lambda x:x.become(Polygon(dot8_copy.get_center(),linef1.get_start(),linef2.get_start(),color=WHITE, fill_color="#0A47C2", fill_opacity=1, stroke_width=5)))
        
        self.play(FadeOut(line1), FadeOut(line2))

        triangle2_pos = Polygon(dot1.get_center(),dot2.get_center(),dot4.get_center(),color=WHITE, fill_color="#3DD771", fill_opacity=0.25, stroke_width=5).set_z_index(0)
        
        self.play(AnimationGroup(AnimationGroup(dot8_copy.animate.move_to(dot4.get_center())), AnimationGroup(FadeIn(triangle2_pos)), lag_ratio=0), run_time=2)
        
        #self.play(dot8_copy.animate.move_to(dot4.get_center()),run_time=2)
        triangle2.suspend_updating()


        tri3 = Polygon(dot1.get_center(), dot2.get_center(), dot4.get_center(), color = "#3DD771", fill_opacity=1, stroke_width=5, stroke_color = WHITE)

        self.play(FadeIn(tri3), FadeOut(triangle2_pos), run_time = 0.5)
        triangle2.set_z_index(0)
        self.play(FadeOut(triangle2))
        
        self.play(FadeOut(dot8_copy, l5, dashed_1 ), self.camera.frame.animate.move_to(polygon).shift(3*DOWN))
        self.wait(0.7)
        self.wait(2)
        
        # Show answer
        #line = Tex("Area of the shaded portion =")
        #eqn = MathTex(r" \frac{1}{2} ").next_to(line, buff = 0.5)
        #star = Tex("*").next_to(eqn, buff = 0.5)
        #ans = Tex("Area of the bigger square ").next_to(star, buff = 0.5)
        #eqn1 = VGroup(line,eqn,star,ans)
        #eqn1.next_to(dot4, DOWN, buff = 0.5).scale(0.7)
        #self.play(FadeIn(eqn1))
        #self.wait()
        
        #num = Tex("(12 * 12)").scale(0.7).next_to(star, buff = 0.5)
        #self.play(ReplacementTransform(ans,num))
        #self.wait()
        
        #equal_to = Tex("=").next_to(num, buff = 0)
        #final_ans = Tex("72 sq. units").next_to(equal_to, buff = 0.5)
        #equal_to_final_ans = VGroup(equal_to, final_ans).scale(0.7)
        #self.play(FadeIn(equal_to_final_ans))
        #self.wait(2)
        
        
        self.play(FadeOut(arrow_3, arrow_4))
        A = MathTex("A(", "\phantom{xxx}", ")").next_to(square1, 6* DOWN).shift(0.7*LEFT).scale(1.1).shift(0.5*RIGHT)
        tri3_copy = Polygon(dot1.get_center(), dot2.get_center(), dot4.get_center(), color = "#3DD771", fill_opacity=1, stroke_width=2, stroke_color = WHITE)

        self.play(FadeIn(A), tri3_copy.animate.scale(0.143).move_to(A).shift(0.19*RIGHT))
        equal_to = MathTex("=").next_to(A, buff = 0.2).scale(1.1)
        self.play(FadeIn(equal_to))

        C = MathTex("A(", "\phantom{xxxx}", ")").next_to(equal_to, buff = 0.2).scale(1.1)
        question.move_to(C).shift(0.205*RIGHT).scale(0.935)

        self.play(FadeIn(C, question))

        grp = VGroup(C, question)
        grp_copy = grp.copy()
        
        grp_tri3 = VGroup(A, tri3_copy)
        grp_tri3_copy = grp_tri3.copy()
        grp_tri3_copy.move_to(grp_copy).shift(0.1*LEFT)
        grp_copy.move_to(grp_tri3).shift(0.2*LEFT)

        play_kw = {"run_time": 1}
        self.play(
            ReplacementTransform(
                grp, grp_copy,
                path_arc=90 * DEGREES,
            ), 
            ReplacementTransform(
                grp_tri3, grp_tri3_copy,
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        grp_tri3_copy2 = grp_tri3_copy.copy()

        self.play(grp_tri3_copy2.animate.move_to(grp_copy).shift(2*DOWN))
        equal_to_copy = equal_to.copy()
        equal_to_copy.move_to(equal_to).shift(2*DOWN)
        self.play(FadeIn(equal_to_copy))

        eqn = MathTex(r" \frac{1}{2} ").next_to(equal_to_copy, buff = 0.3).scale(1.1)
        self.play(FadeIn(eqn))
        star = MathTex("\\times").next_to(eqn, buff = 0.2).scale(1.1)
        self.play(FadeIn(star))
        B = MathTex("A(", "\phantom{xxx}", ")").next_to(star, buff = 0.2).scale(1.1)
        square1_copy = square1.copy()
        self.play(FadeIn(B), square1_copy.animate.scale(0.143).move_to(B).shift(0.22*RIGHT).set_fill(color = "#3DD771", opacity = 1))
        self.wait(2)
        size_copy = size.copy()
        #size_copy.set_color(WHITE)
        #self.play(size_copy.animate.next_to(star, buff = 0.2).scale(1.25), FadeOut(B, square1_copy))
        twlvSq = MathTex("12^2").next_to(star, buff = 0.2).shift(0.1*UP).scale(0.99)
        self.play(FadeTransform(size_copy, twlvSq), FadeOut(B, square1_copy))
        self.wait(2)
        
        eqnGrp = VGroup(eqn, star, twlvSq)
        
        sevTwo = MathTex("72").next_to(equal_to_copy, buff = 0.3).scale(1.1)
        
        self.play(TransformMatchingTex(eqnGrp, sevTwo))
        self.wait(2)

        self.play(sevTwo.animate.next_to(equal_to, buff=0.3), FadeOut(grp_tri3_copy2, equal_to_copy,grp_tri3_copy))
        
        finalAns = VGroup(grp_copy, equal_to, sevTwo)
        
        box = SurroundingRectangle(finalAns, color="#3DD771", buff=MED_LARGE_BUFF)
        
        self.play(Create(box))
        
        self.wait(4)

        self.play(FadeOut(finalAns, tri3, size, box, grp_copy))

        followUp_size = MathTex("10").set_color("#3DD771").set_stroke(width = 1).scale(1)
        followUp_size.move_to(size.get_center())
        square3 = Square(fill_opacity=0, stroke_width=5, stroke_color=WHITE).scale(0.5).set_z_index(2).shift(LEFT)
        square3.next_to(square2, LEFT, buff=0).shift(0.5*DOWN)
        square3.joint_type=LineJointType.ROUND 

        dot9 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square3.get_corner(UL)).set_z_index(4)
        dot10 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square3.get_corner(UR)).set_z_index(4)
        dot11 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square3.get_corner(DL)).set_z_index(4)
        dot12 = Circle(radius=0.09, fill_color="#0A47C2", fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(square3.get_corner(DR)).set_z_index(4)

        polygon_followUp = Polygon(
            square1.get_corner(UR), square2.get_corner(UR), square3.get_corner(UR),
            square2.get_corner(DR), square3.get_corner(UL), square2.get_corner(UL), square1.get_corner(UL),
            fill_color="#3DD771", fill_opacity=1, color=WHITE, stroke_width = 5
        )

        self.play(FadeIn(polygon_followUp, followUp_size, square3, dot9, dot10, dot11, dot12), self.camera.frame.animate.move_to(polygon_followUp).shift(2*DOWN))
        self.wait(2)
        polygon_followUpCopy = polygon_followUp.copy()
        polygon_followUpCopy.set_stroke(width=2)
        self.play(FadeIn(equal_to_what,questionText), polygon_followUpCopy.animate.next_to(equal_to_what, RIGHT).scale(0.14).shift(5.33*LEFT), self.camera.frame.animate.shift(DOWN))
        self.wait(3)
        