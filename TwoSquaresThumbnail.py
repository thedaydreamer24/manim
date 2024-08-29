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

        X = self.camera.frame.scale(1.67).move_to(polygon).shift(2*DOWN).shift(DOWN)
        self.add(X)
        
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
        

        questionText = Text("Area of the shaded portion?", color = WHITE, font='Athletics', t2c={"shaded": "#3DD771"}).next_to(polygon, UP, buff=1.5).scale(0.9)
        
        #shift_amount = LEFT * 2 
        #camera_frame = self.camera.frame
        question = polygon.copy()
        
        equal_to_what = MathTex("A(", "\phantom{xxx}", ")\ =\ ? ").scale(1.25).set_color(WHITE).set_stroke(width = 1).next_to(polygon, DOWN, buff=1.5)
        question.set_stroke(width = 2).next_to(equal_to_what, RIGHT).scale(0.15).shift(5.33*LEFT), FadeIn(equal_to_what)

        self.add(square1, square2, arrows, size, dot1, dot2, dot3, dot4, dot5, dot6, dot7,
                 line1,line2, line3, line4, polygon, questionText,
                 equal_to_what, question,)