%%manim -pqh GridAlternate
from manim import *
config.background_color = BLACK
class GridAlternate(MovingCameraScene):
    def construct(self):
        
        rows = 6
        cols = 6
        grid = VGroup(*[
            VGroup(*[Square(side_length=1, fill_opacity=0, stroke_width=5, stroke_opacity = 1).move_to((i-rows//2)*RIGHT + (j-cols//2)*UP) for j in range(cols)]) for i in range(rows)
        ]).set_color(GRAY_C).shift(0.6*RIGHT)
        grid.to_edge(ORIGIN)
        square = Square(side_length=6, fill_opacity=0, stroke_width=5, stroke_opacity = 1).set_color(GRAY_C).set_z_index(3)
        square.move_to(grid.get_center())
        
        A = self.camera.frame.animate.scale(1.2).move_to(grid).save_state()
        self.play(A)
        
        # Add lines
        line1 = Line(grid[0][5].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line2 = Line(grid[0][5].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        line3 = Line(grid[1][4].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line4 = Line(grid[1][4].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        line5 = Line(grid[2][3].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line6 = Line(grid[2][3].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        line7 = Line(grid[3][2].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line8 = Line(grid[3][2].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        line9 = Line(grid[4][1].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line10 = Line(grid[4][1].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        line11 = Line(grid[5][0].get_corner(UR), grid[0][0].get_corner(UL), color=WHITE, stroke_width=5).set_z_index(3)
        line12 = Line(grid[5][0].get_corner(UR), grid[1][0].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        
        
        #Add sectors
        sector1 = Sector(arc_center=line2.get_start(), outer_radius=1.2, start_angle=line1.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=RED).set_z_index(2)
        sector2 = Sector(arc_center=line4.get_start(), outer_radius=1.2, start_angle=line3.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=YELLOW).set_z_index(2)
        sector3 = Sector(arc_center=line6.get_start(), outer_radius=1.2, start_angle=line5.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=GREEN)
        sector4 = Sector(arc_center=line8.get_start(), outer_radius=1.2, start_angle=line7.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=BLUE)
        sector5 = Sector(arc_center=line10.get_start(), outer_radius=1.2, start_angle=line9.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=PURPLE)
        sector6 = Sector(arc_center=line12.get_start(), outer_radius=1.2, start_angle=line11.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=PINK)
        
        #Add dots
        dot1 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line1.get_start()).set_z_index(4)
        dot2 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line1.get_end()).set_z_index(4)
        dot3 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line3.get_start()).set_z_index(4)
        dot4 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line4.get_end()).set_z_index(11)
        dot5 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line5.get_start()).set_z_index(4)
        dot6 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line7.get_start()).set_z_index(4)
        dot7 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line9.get_start()).set_z_index(4)
        dot8 = Circle(radius=0.12, fill_color='#71DF96', fill_opacity=1, stroke_width=0, stroke_color=WHITE).move_to(line11.get_start()).set_z_index(4)
        
        # Create angle symbols
        angle_red = Tex("$\\angle$", color=RED).scale(1).set_stroke(width = 3)
        angle_yellow = Tex("$\\angle$", color=YELLOW).scale(1).set_stroke(width = 3)
        angle_green = Tex("$\\angle$", color=GREEN).scale(1).set_stroke(width = 3)
        angle_blue = Tex("$\\angle$", color=BLUE).scale(1).set_stroke(width = 3)
        angle_purple = Tex("$\\angle$", color=PURPLE).scale(1).set_stroke(width = 3)
        angle_pink = Tex("$\\angle$", color=PINK).scale(1).set_stroke(width = 3)

        # Position angle symbols
        #angle_red.shift(3.2*DOWN+3.75*LEFT)
        angle_yellow.next_to(angle_red, RIGHT, buff=1)
        angle_green.next_to(angle_yellow, RIGHT, buff=1)
        angle_blue.next_to(angle_green, RIGHT, buff=1)
        angle_purple.next_to(angle_blue, RIGHT, buff=1)
        angle_pink.next_to(angle_purple, RIGHT, buff=1)

        # Create plus signs
        plus1 = Tex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus2 = Tex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus3 = Tex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus4 = Tex("+", color=WHITE).scale(0.8).set_stroke(width = 3)
        plus5 = Tex("+", color=WHITE).scale(0.8).set_stroke(width = 3)

        # Position plus signs
        plus1.next_to(angle_red, RIGHT, buff=0.3)
        plus2.next_to(angle_yellow, RIGHT, buff=0.3)
        plus3.next_to(angle_green, RIGHT, buff=0.3)
        plus4.next_to(angle_blue, RIGHT, buff=0.3)
        plus5.next_to(angle_purple, RIGHT, buff=0.3)
        
        #Add =?°
        equal_to = Text(" = ").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        equal_to.next_to(angle_pink, RIGHT, buff=0.3)
        symbol = Text("?").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        symbol.next_to(equal_to, RIGHT, buff=0.3)

        # Add objects to the scene
        #self.play(FadeIn(title))
        #self.wait(2)
        #self.play(FadeOut(title))
        self.wait()
        self.play(FadeIn(grid), FadeIn(square))
        self.wait(2)
        #self.add(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)
        
        self.play(FadeIn(dot1, dot3, dot5, dot6, dot7, dot8))
        self.wait(2)
        self.play(FadeIn(dot2, dot4))
        self.wait(3)
        self.play(Create(line1), Create(line3), Create(line5), Create(line7), Create(line9), Create(line11), run_time = 3)
        self.play(Create(line2), Create(line4), Create(line6), Create(line8), Create(line10), Create(line12), run_time = 3)
        #self.play(Create(line3))
        #self.play(Create(line4))
        #self.play(Create(line5))
        #self.play(Create(line6))
        #self.play(Create(line7))
        #self.play(Create(line8))
        #self.play(Create(line9))
        #self.play(Create(line10))
        #self.play(Create(line11))
        #self.play(Create(line12))
        self.wait(2)
        #self.add(sector1, sector2, sector3, sector4, sector5, sector6)
        txt = Text("What's the sum of these angles?").next_to(grid, 1.5 * UP).scale(0.7)
        text_group = VGroup(angle_red,plus1,angle_yellow,  plus2,angle_green, plus3,angle_blue,  plus4,angle_purple,  plus5, angle_pink, equal_to, symbol  )
        text_group.arrange(buff = 0.3).next_to(grid, 2.5 * DOWN)
        sec_gr = VGroup(sector1, sector2, sector3, sector4, sector5, sector6)
        self.play(Create(sec_gr), run_time=2)
        self.wait(2)
        self.play(FadeIn(text_group), FadeIn(txt), run_time = 1.5)
        self.wait(5)
        
        # Add sectors for the solution
        #sector_compare = Sector(arc_center=line2.get_end(), outer_radius=1.2, start_angle=line1.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=RED).rotate(PI).shift(1.2*UP+0.22*RIGHT)
        
        #Add arrows
        #arrow1 = Arrow(grid[0][0].get_corner(UL), grid[0][5].get_corner(UR), stroke_width=5).set_color(WHITE).set_length(1)
        #arrow1.set_length(line1.get_length())
        #arrow1.next_to(line1.get_start(), direction=line1.get_unit_vector(), buff=0)
        #arrow1.shift(0.1 * line1.get_length() * 0.5* line1.get_unit_vector() )
        
        #arrow2 = Arrow(grid[1][0].get_corner(DL), grid[1][4].get_corner(UR), stroke_width=5).set_color(WHITE).set_length(1)
        #arrow2.set_length(line4.get_length())
        #arrow2.next_to(line4.get_start(), direction=line4.get_unit_vector(), buff=0)
        #arrow2.shift(0.1 * line4.get_length() * 0.5* line4.get_unit_vector() )
        
        #Analysing first angle (red one)
        self.play(FadeOut(line3, line5, line6, line7, line8, line9, line10, line11, line12, dot5, dot6, dot7, dot8, sector2, sector3, sector4, sector5, sector6, text_group, txt), self.camera.frame.animate.scale(0.8).move_to(0.5*DOWN))

        self.wait(2)
        #self.play(Indicate(line1), Indicate(line4), color = ORANGE)
        #self.wait()
        #self.play(Indicate(line2), color = ORANGE)
        #self.wait()
        
        #Animating for red angle and shifting
        
        line4_copy = Line(grid[1][0].get_corner(DL), grid[1][4].get_corner(UR),  color=WHITE, stroke_width=5).set_z_index(3)
        line2_copy = line2.copy()
        line1_copy = Line(grid[0][0].get_corner(UL), grid[0][5].get_corner(UR),  color=WHITE, stroke_width=5).set_z_index(3)
        
        
        #for line in [line1_copy, line2_copy, line4_copy]:
         #   self.play(ShowPassingFlash(line.set_color(BLUE), time_width=0.5), run_time=1, rate_func=linear)
        self.wait(2)
            
        #self.play(FadeIn(arrow1), FadeIn(arrow2))
        self.wait()
        
        
        #animatedline
        line_a = Line(grid[0][5].get_corner(UR), grid[1][1].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        
        #Add rectangle
        #rectangle = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.5)

        rect1 = Rectangle(width = 1, height = 5 ,fill_opacity=0, stroke_width=5, color=YELLOW_C, stroke_opacity = 1).move_to(grid, UL).set_z_index(5)
        rect2 = Rectangle(width = 1, height = 5 ,fill_opacity=0, stroke_width=5, color=YELLOW_C, stroke_opacity = 1).move_to(grid[1][4], UL).set_z_index(5)
        
        line1_copy = line1.copy().set_z_index(3)
        #line2_copy = line2.copy()
        sector1_copy = sector1.copy().set_z_index(2)
        dot1_copy = dot1.copy().set_z_index(4)
        dot2_copy = dot2.copy().set_z_index(4)
        #dot4_copy = dot4.copy()
        grid_copy1 = grid[0][5].copy()
        grid_copy2 = grid[0][4].copy()
        grid_copy3 = grid[0][3].copy()
        grid_copy4 = grid[0][2].copy()
        grid_copy5 = grid[0][1].copy()
        #grid_copy6 = grid[0][0].copy()
        
        #self.play(Indicate(rect1), scale_factor = 1, run_time = 2, color = YELLOW_C)
        self.play(FadeIn(rect1))
        self.wait()
        self.play(FadeOut(rect1), FadeIn(rect2))
        self.wait()
        self.play(FadeOut(rect2))
        #self.remove(rect1)
        #self.play(Indicate(rect2), scale_factor = 1, run_time = 2, color = YELLOW_C)
        #self.remove(rect2)
        rotate_and_coincide = VGroup(line1_copy, line_a, sector1_copy, dot1_copy, dot2_copy, grid_copy1, grid_copy2, grid_copy3, grid_copy4, grid_copy5)
        
        #self.play(rotate_and_coincide.animate.shift(3*LEFT))
        #self.play(rotate_and_coincide.animate.shift(2*LEFT))
        self.play(Rotate(rotate_and_coincide, -PI, run_time = 2))
        self.play(rotate_and_coincide.animate.shift(RIGHT+DOWN))
        self.play(Indicate(sector1), Indicate(sector1_copy), scale_factor = 1, run_time = 2)
        self.wait(2)
        
        
        
        
        #Animating for yellow angle and shifting
        self.play(FadeIn(line3, line6, sector2, dot5))
        self.wait(2)
        
        grid_copy6 = grid[1][4].copy()
        grid_copy7 = grid[1][3].copy()
        grid_copy8 = grid[1][2].copy()
        grid_copy9 = grid[1][1].copy()
        grid_copy10 = grid[1][0].copy()
        line_b = Line(grid[1][4].get_corner(UR), grid[1][3].get_corner(DL), color=WHITE, stroke_width=5).set_z_index(3)
        #line4_copy = Line(grid[1][0].get_corner(DL), grid[1][4].get_corner(UR),  color=WHITE, stroke_width=5).set_z_index(3)
        sector2_copy = sector2.copy().set_z_index(2)
        dot4_copy = dot4.copy()
        dot3_copy = dot3.copy()
        #rect3 = Rectangle(width = 1, height = 5 ,fill_opacity=0, stroke_width=5, color=YELLOW_C, stroke_opacity = 1).move_to(grid[1][4], UL).set_z_index(5)
        self.play(FadeIn(rect2))
        self.play(FadeOut(rect2))
        rotate_and_coincide2 = VGroup(line4_copy, line_b, sector2_copy, dot3_copy, dot4_copy, grid_copy10, grid_copy6, grid_copy7, grid_copy8, grid_copy9)
        self.play(Rotate(rotate_and_coincide2, -PI, run_time = 2))
        self.play(Indicate(sector2), Indicate(sector2_copy), scale_factor = 1, run_time = 2)
        self.wait(2)
        
        
        
        
        self.play(self.camera.frame.animate.scale(1.25).move_to(grid), FadeIn(txt, line5, line7, line8, line9, line10, line11, line12, dot6, dot7, dot8, sector3, sector4, sector5, sector6))
        #self.play(FadeOut(arrow1), FadeOut(arrow2))
        self.wait(4)
        #self.play(FadeIn(sector7.set_z_index(8)))
        sector7 = Sector(arc_center=line2.get_end(), outer_radius=1.2, start_angle=line1.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=RED)
        sector8 = Sector(arc_center=line4.get_end(), outer_radius=1.2, start_angle=line3.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=YELLOW)
        sector9 = Sector(arc_center=line6.get_end(), outer_radius=1.2, start_angle=line5.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=GREEN)
        sector10 = Sector(arc_center=line8.get_end(), outer_radius=1.2, start_angle=line7.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=BLUE)
        sector11 = Sector(arc_center=line10.get_end(), outer_radius=1.2, start_angle=line9.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=PURPLE)
        sector12 = Sector(arc_center=line12.get_end(), outer_radius=1.2, start_angle=line11.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=PINK)
        self.add(sector7, sector8, sector9, sector10, sector11, sector12)
        
        sectors_group = VGroup(sector7, sector8, sector9, sector10, sector11, sector12)

        # Rotate the sectors by 180 degrees
        sectors_group.rotate(PI).shift(1.18*UP+1.2*RIGHT)

        # Add the group to the scene
        self.play(Create(sectors_group, run_time =4))
        self.wait(2)
        
        # Copy the sectors group
        sectors_copy = sectors_group.copy()
        
        #answer
        self.play(Indicate(sectors_group), color = None)
        self.wait()
        self.play(sectors_copy.animate.next_to(angle_pink, RIGHT, buff=0.6).scale(0.5), FadeIn(text_group), FadeOut(symbol))
        self.wait(2)
        
        #Add right-angle
        line_ra1 = Line( LEFT, RIGHT, color = PURE_BLUE, buff = 0, stroke_width = 2.5).move_to(sectors_copy, DOWN).scale(0.3)
        line_ra2 = Line( DOWN, UP, color = PURE_BLUE , buff = 0, stroke_width = 2.5).move_to(sectors_copy, LEFT).scale(0.3)
        line_ra = VGroup(line_ra1, line_ra2)
        line_ra.joint_type=LineJointType.ROUND 
        right_angle = RightAngle(line_ra1, line_ra2, length=0.25, color=PURE_BLUE, stroke_width = 2.5).align_to(sectors_copy, LEFT)
        ra = VGroup(line_ra1,line_ra2, right_angle)
        
        ra_copy = ra.copy().set_stroke(width = 6)
        ra_copy.move_to(sectors_group).scale(2).set_z_index(6)
        
        self.wait(2)
        answer = Text(" 90°").scale(0.8).set_color(WHITE).set_stroke(width = 1).next_to(angle_pink, RIGHT, buff=0.8)
        #answer.next_to(angle_pink, RIGHT, buff=1.8)
        #self.play(FadeIn(answer))
        mini_sg = VGroup(sectors_copy)
        self.play(FadeOut(mini_sg), FadeIn(answer), FadeIn(ra_copy))
        self.wait(3)

        
        angle_red_copy = angle_red.copy()
        plus1_copy = plus1.copy()
        angle_green_copy = angle_green.copy()
        plus2_copy = plus2.copy()
        angle_purple_copy = angle_purple.copy()
        equal_to_copy = equal_to.copy()
        symbol_l = Text("?").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        symbol_l.next_to(equal_to, RIGHT, buff=0.3)
        self.play(FadeOut(ra_copy,sectors_group,sector1_copy,sector2_copy), ReplacementTransform(answer, symbol_l))
        self.wait(2)
        
        symbol_end = Text("?").scale(0.8).set_color(WHITE).set_stroke(width = 1)
        symbol_end.next_to(equal_to_copy, RIGHT, buff=0.3)
        text_group = VGroup(angle_red,plus1,angle_yellow,  plus2,angle_green, plus3,angle_blue,  plus4,angle_purple,  plus5, angle_pink, equal_to, symbol,symbol_l  )
        follow_up_ques = VGroup(angle_red_copy, plus1_copy, angle_green_copy, plus2_copy, angle_purple_copy, equal_to_copy , symbol_end)
        follow_up_ques.arrange(buff = 0.3).next_to(grid, 2.5 * DOWN)
        
        self.play(ReplacementTransform(text_group, follow_up_ques),FadeOut(dot2_copy, line1_copy, dot4_copy, line3, line4, line7, line8, line11, line12, sector2, sector4, sector6, dot3, dot6, dot8), FadeOut(line4_copy), FadeOut(dot3_copy))
        #self.play(ReplacementTransform(text_group, follow_up_ques), FadeOut(sector1_copy, dot2_copy, line1_copy, dot4_copy, sector2_copy, ra_copy, answer, sectors_group, sector2, sector4, sector6), FadeOut(line4_copy), FadeOut(dot3_copy))
        self.wait(3)
        #text_group