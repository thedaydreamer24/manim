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

class CircleInSquare(MovingCameraScene):

    
    def construct(self):
        
        #Create square
        square = Square(fill_opacity=0, stroke_width=4, stroke_color=WHITE).scale(2).set_z_index(2)
        square.joint_type=LineJointType.ROUND 
        
        #Zoom out
        X = self.camera.frame.animate.scale(1.3).move_to(square).shift(1.5*DOWN)
        self.play(X)
        
        #Animate square
        self.play(FadeIn(square))
        
        #Create circle
        circle = Circle(fill_opacity=0, stroke_width=4, stroke_color=WHITE).scale(2).set_z_index(2)
        
        #Animate circle
        self.play(FadeIn(circle))
        
        #Create semi-circle
        sc = Arc(radius=2,angle=PI,color=WHITE,stroke_width=4).align_to(square, DOWN).set_z_index(2)
        
        #Animate semi-circle
        self.play(FadeIn(sc))
        self.wait(3)
        
        #Create line
        line = Line(square.get_corner(UL), square.get_corner(DR)).set_z_index(2)
        
        #Animate line
        self.play(Create(line))
        self.wait(2)
        
        #Triangle for getting fill_arc1 at DR
        tri1 = Polygon(square.get_corner(UL), square.get_corner(DR),square.get_corner(UR))
        
        #Create fill_arc1
        fill_arc1 = Intersection(sc,tri1,fill_color='#B038B2',fill_opacity=1,stroke_width=4)
        fill_arc1.joint_type=LineJointType.ROUND 
        
        #Square uppder edge
        lineUpper = Line(square.get_corner(UL), square.get_corner(UR))
        
        #Triangle for getting fill_arc2 at UL
        tri2 = Polygon(lineUpper.get_center(), square.get_center(), square.get_corner(UL))
        
        #Create fill_arc2
        fill_arc2 = Difference(tri2,circle, fill_color='#B038B2',fill_opacity=1,stroke_width=4).set_z_index(10)
        fill_arc2.joint_type=LineJointType.ROUND 
        
        #Square right edge
        lineRight = Line(square.get_corner(UR), square.get_corner(DR))
        
        #Triangle for getting fill_arc3 at DR corner
        tri3 = Polygon(lineRight.get_center(), square.get_center(), square.get_corner(DR))
        
        #Creating fill_arc3
        fill_arc3 = Difference(tri3,circle, fill_color='#B038B2',fill_opacity=1,stroke_width=4)   
        fill_arc3.joint_type=LineJointType.ROUND 
        
        #Creating second semi-circle for getting fill_arc4
        sc2 = Arc(radius=2,angle=PI,color=WHITE,stroke_width=4).align_to(square, DOWN).set_z_index(2).rotate(PI/1.333333333).align_to(square, LEFT)
        sc2.shift(0.3*UP)
        
        #Creating fill_arc4
        fill_arc4 = Difference(sc2, sc, fill_color='#B038B2',fill_opacity=1,stroke_width=4).set_z_index(6)   

        #Title
        questionText = Text("Shaded Fraction?", color = WHITE, font='Athletics', t2c={"Shaded": "#ED6CEF"}).next_to(square, UP, buff=1.5).scale(0.8)
        #square_copy = square.copy()
        #square_copy.set_fill(color = '#B038B2', opacity=1).move_to(questionText, LEFT).scale(0.12).shift(0.56*RIGHT)

        #Fading in everything
        self.play(FadeIn(fill_arc1, fill_arc2, fill_arc3, fill_arc4, questionText))
        self.wait(5)
        self.play(FadeOut(questionText))
        
        #Start solution
        #Create bisector of the square
        sqBisect = DashedLine(square.get_corner(UR), square.get_corner(DL), stroke_width=4, stroke_color=WHITE)
        
        #Animate bisector
        self.play(Create(sqBisect))
        self.wait()
        
        t1 = Polygon(square.get_corner(UR),square.get_corner(DR),square.get_center(),color="#1EB5F0",stroke_width=4).set_z_index(20)
        t2 = Polygon(square.get_corner(DL),square.get_corner(DR),square.get_center(),color="#1EB5F0",stroke_width=4).set_z_index(20)
        t3 = Polygon(square.get_corner(UL),square.get_corner(DL),square.get_center(),color="#1EB5F0",stroke_width=4).set_z_index(20)
        t4 = Polygon(square.get_corner(UL),square.get_corner(UR),square.get_center(),color="#1EB5F0",stroke_width=4).set_z_index(20)
        
        self.add(t1)
        self.wait(0.5)
        self.add(t4)
        self.wait(0.5)
        self.add(t3)
        self.wait(0.5)
        self.add(t2)
        self.wait()
        A = self.camera.frame.animate.scale(0.8).move_to(square)
        A.save_state()
        self.play(FadeOut(t2, t4),
                 square.animate.set_stroke(opacity=0.4),
                 circle.animate.set_stroke(opacity=0.4),
                 sc.animate.set_stroke(opacity=0.4),
                 line.animate.set_stroke(opacity=0.4),
                 sqBisect.animate.set_stroke(opacity=0.4),
                 fill_arc1.animate.set_opacity(0.4),
                 fill_arc2.animate.set_opacity(0.4),
                 fill_arc3.animate.set_opacity(0.4),
                 fill_arc4.animate.set_opacity(0.4),
                 A)
        self.play(Indicate(t1, color = None))
        self.play(Indicate(t3, color = None))
        t1.set_z_index(4)
        t2.set_z_index(4)
        t3.set_z_index(4)
        t4.set_z_index(4)
        self.wait()
        fill_arc4_pos = fill_arc4.copy().rotate(axis=[0,2,0],about_point=square.get_center(),angle=PI)
        fill_arc4_pos.set_opacity(1).set_fill(color = '#3DD771').set_z_index(6)
        self.play(fill_arc4.animate.set_opacity(1).set_fill(color = '#3DD771'))
        self.wait(0.5)
        self.play(FadeIn(fill_arc4_pos), fill_arc4.animate.set_opacity(1).set_fill(color = '#B038B2'))
        self.wait(0.5)
        self.play(FadeOut(fill_arc4_pos))
        #3D rotation for fill_arc4
        
        self.play(Rotate(fill_arc4,axis=[0,2,0],about_point=square.get_center(),angle=PI), run_time=2)
        #self.play(fill_arc4.animate.set_fill(color = '#B038B2'))
        self.wait()
        
        #Triangle for fill_arc5 (for updater)
        tri4 = Polygon(lineRight.get_center(), square.get_center(), square.get_corner(UR))
        
        #UR part where fill_arc2 will go
        fill_arc5 = Difference(tri4,circle, fill_color='#3DD771',fill_opacity=1,stroke_width=4).set_z_index(10)
        fill_arc5.joint_type=LineJointType.ROUND 
        
        self.play(FadeIn(t4), 
                  fill_arc4.animate.set_opacity(0.4),
                  FadeOut(t3))
        self.play(Indicate(t1, color = None))
        self.play(Indicate(t4, color = None))
        self.wait()
        
        
        
        self.play(fill_arc2.animate.set_opacity(1).set_fill(color = '#3DD771'))
        self.wait(0.5)
        self.play(FadeIn(fill_arc5), fill_arc2.animate.set_opacity(1).set_fill(color = '#B038B2'))
        self.wait(0.5)
        self.play(FadeOut(fill_arc5))
        
           
        t = ValueTracker(0)
        
        # Calculate the distance vector from initial position to the final position beside s6_copy
        distance_vector = fill_arc5.get_center() - fill_arc2.get_center()

        # Updater function for fill_arc2
        def update_fill_arc2(mob, dt):
            angle = 4*PI/2 - PI / 2 * t.get_value()
            mob.become(
                Difference(tri2, circle, 
                           fill_color='#B038B2',
                           fill_opacity=1,
                           stroke_width=4).set_z_index(4).rotate(angle).shift(distance_vector * t.get_value())
            )

        fill_arc2.add_updater(update_fill_arc2)

        # Play the animation
        self.play(t.animate.set_value(1), run_time=2)
        
        # Remove the updater after animation
        fill_arc2.clear_updaters()
        self.play(fill_arc2.animate.set_fill(color = '#B038B2'))

        self.wait(2)
        
        #Create final triangle
        finalTri = Polygon(square.get_corner(UR), 
                           square.get_center(), 
                           square.get_corner(DR), 
                           fill_color='#B038B2',
                           fill_opacity=1,
                           stroke_width=4, 
                           stroke_color = WHITE).set_z_index(12)
        
        sqBisectNormal = Line(square.get_corner(UR), square.get_corner(DL), stroke_width=4, stroke_color=WHITE)
        
        self.play(FadeOut(t1, t4),
                 square.animate.set_stroke(opacity=1),
                 circle.animate.set_stroke(opacity=1),
                 sc.animate.set_stroke(opacity=1),
                 line.animate.set_stroke(opacity=1),
                 sqBisect.animate.set_stroke(opacity=1),
                 fill_arc1.animate.set_opacity(1),
                 fill_arc2.animate.set_opacity(1),
                 fill_arc3.animate.set_opacity(1),
                 fill_arc4.animate.set_opacity(1),
                 self.camera.frame.animate.scale(1.25).move_to(square).shift(1.5*DOWN))
        self.wait(2)
        
        #Animate final triangle
        #self.play(FadeIn(finalTri))
        self.play(FadeIn(sqBisectNormal,finalTri), FadeOut(circle,sc, fill_arc4, fill_arc1, fill_arc3, fill_arc2, sqBisect))
        
        #Indicate final triangle
        self.play(Indicate(finalTri, color = None))
        self.wait()
        
        fraction = MathTex(r" \frac{1}{} ").next_to(square, DOWN, buff= 1.5).scale(1)
        fractionB = MathTex(r" \frac{1}{4} ").next_to(square, DOWN, buff= 1.5).scale(1)
        eqn = VGroup(fraction, fractionB)
        box = SurroundingRectangle(eqn, color="#B038B2", buff=MED_LARGE_BUFF)
        
        t1.set_z_index(14).set_stroke(color = WHITE)
        t2.set_z_index(14).set_fill(color = "#0A47C2", opacity = 1).set_stroke(color = WHITE)
        t3.set_z_index(14).set_fill(color = '#0A47C2', opacity = 1).set_stroke(color = WHITE)
        t4.set_z_index(14).set_fill(color = '#0A47C2', opacity = 1).set_stroke(color = WHITE)
        
        tx1 = MathTex("1").move_to(t1.get_center()).scale(1).set_z_index(18)
        tx2 = MathTex("2").move_to(t2.get_center()).scale(1).set_z_index(18)
        tx3 = MathTex("3").move_to(t3.get_center()).scale(1).set_z_index(18)
        tx4 = MathTex("4").move_to(t4.get_center()).scale(1).set_z_index(18)
        
        self.add(t1, tx1, fraction)
        self.wait(0.5)
        self.add(t2, tx2)
        self.wait(0.5)
        self.add(t3, tx3)
        self.wait(0.5)
        self.add(t4, tx4, fractionB)
        self.play(Create(box))
        self.wait(2)

        #Follow up
        fill_arc5.set_fill(color = "#3DD771")
        fill_arc2_c = Difference(tri2,circle, fill_color='#3DD771',fill_opacity=1,stroke_width=4).set_z_index(4)
        fill_arc2_c.joint_type=LineJointType.ROUND 
        
        fill_arc4_c = Difference(sc2, sc, fill_color='#3DD771',fill_opacity=1,stroke_width=4)   
        fill_arc4_c.joint_type=LineJointType.ROUND 
        
        fill_arc6 = Intersection(t2, circle, fill_color='#3DD771',fill_opacity=1,stroke_width=4)   
        fill_arc6.joint_type=LineJointType.ROUND 
        
        lineLeft = Line(square.get_corner(UL), square.get_corner(DL))
        tri5 = Polygon(square.get_center(), square.get_corner(DL), lineLeft.get_center())
        
        fill_arc7 = Difference(tri5,circle, fill_color='#3DD771',fill_opacity=1,stroke_width=4)
        fill_arc7.joint_type=LineJointType.ROUND 
        
        fill_arc1.set_fill(color = "#3DD771")
        fill_arc2_c.set_fill(color = "#3DD771")
        fill_arc3.set_fill(color = "#3DD771")
        fill_arc4_c.set_fill(color = "#3DD771")
        fill_arc5.set_fill(color = "#3DD771")
        fill_arc6.set_fill(color = "#3DD771")
        fill_arc7.set_fill(color = "#3DD771")
        
        self.play(FadeOut(t1, t2, t3, t4, tx1, tx2, tx3, tx4, box, fraction, fractionB, finalTri), 
                  FadeIn(circle, line, sc, fill_arc1, fill_arc2_c, fill_arc3, fill_arc4_c, fill_arc5, fill_arc6, fill_arc7))
        self.wait(3)
        square_copy2 = square.copy()
        square_copy2.set_z_index(20)
        questionTextf = Text("Shaded Fraction?", color = WHITE, font='Athletics', t2c={"Shaded": "#3DD771"}).next_to(square, UP, buff=1.5).scale(0.8)
        
        self.play(FadeIn(questionTextf))
        self.wait(2)