from manim import *
config.background_color = WHITE
class Grid(Scene):
    def construct(self):
        rows = 6
        cols = 6
        title = Tex("Here is a 6x6 grid").set_color(BLACK)
        grid = VGroup(*[
            VGroup(*[Square(side_length=1, fill_opacity=0, stroke_width=5, stroke_opacity = 0.5).move_to((i-rows//2)*RIGHT + (j-cols//2)*UP) for j in range(cols)]) for i in range(rows)
        ]).set_color(GREY).shift(0.6*RIGHT+1.2*UP)
        
        # Add lines
        line1 = Line(grid[0][5].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line2 = Line(grid[0][5].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        line3 = Line(grid[1][4].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line4 = Line(grid[1][4].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        line5 = Line(grid[2][3].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line6 = Line(grid[2][3].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        line7 = Line(grid[3][2].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line8 = Line(grid[3][2].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        line9 = Line(grid[4][1].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line10 = Line(grid[4][1].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        line11 = Line(grid[5][0].get_corner(UR), grid[0][0].get_corner(UL), color=BLACK, stroke_width=5).set_z_index(2)
        line12 = Line(grid[5][0].get_corner(UR), grid[1][0].get_corner(DL), color=BLACK, stroke_width=5).set_z_index(2)
        
        
        #Add sectors
        sector1 = Sector(arc_center=line2.get_start(), outer_radius=1.2, start_angle=line1.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=RED)
        sector2 = Sector(arc_center=line4.get_start(), outer_radius=1.2, start_angle=line3.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=YELLOW)
        sector3 = Sector(arc_center=line6.get_start(), outer_radius=1.2, start_angle=line5.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=GREEN)
        sector4 = Sector(arc_center=line8.get_start(), outer_radius=1.2, start_angle=line7.get_angle(), angle=PI/9.5, fill_opacity=1, fill_color=BLUE)
        sector5 = Sector(arc_center=line10.get_start(), outer_radius=1.2, start_angle=line9.get_angle(), angle=PI/11.5, fill_opacity=1, fill_color=PURPLE)
        sector6 = Sector(arc_center=line12.get_start(), outer_radius=1.2, start_angle=line11.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=PINK)
        
        #Add dots
        dot1 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line1.get_start()).set_z_index(4)
        dot2 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line1.get_end()).set_z_index(4)
        dot3 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line3.get_start()).set_z_index(4)
        dot4 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line4.get_end()).set_z_index(4)
        dot5 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line5.get_start()).set_z_index(4)
        dot6 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line7.get_start()).set_z_index(4)
        dot7 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line9.get_start()).set_z_index(4)
        dot8 = Circle(radius=0.08, fill_color=WHITE, fill_opacity=1, stroke_width=4, stroke_color=BLACK).move_to(line11.get_start()).set_z_index(4)
        
        # Create angle symbols
        angle_red = Tex("$\\angle$", color=RED).scale(1).set_stroke(width = 3)
        angle_yellow = Tex("$\\angle$", color=YELLOW).scale(1).set_stroke(width = 3)
        angle_green = Tex("$\\angle$", color=GREEN).scale(1).set_stroke(width = 3)
        angle_blue = Tex("$\\angle$", color=BLUE).scale(1).set_stroke(width = 3)
        angle_purple = Tex("$\\angle$", color=PURPLE).scale(1).set_stroke(width = 3)
        angle_pink = Tex("$\\angle$", color=PINK).scale(1).set_stroke(width = 3)

        # Position angle symbols
        angle_red.shift(3.2*DOWN+3.75*LEFT)
        angle_yellow.next_to(angle_red, RIGHT, buff=1)
        angle_green.next_to(angle_yellow, RIGHT, buff=1)
        angle_blue.next_to(angle_green, RIGHT, buff=1)
        angle_purple.next_to(angle_blue, RIGHT, buff=1)
        angle_pink.next_to(angle_purple, RIGHT, buff=1)

        # Create plus signs
        plus1 = Tex("+", color=BLACK).scale(0.8).set_stroke(width = 3)
        plus2 = Tex("+", color=BLACK).scale(0.8).set_stroke(width = 3)
        plus3 = Tex("+", color=BLACK).scale(0.8).set_stroke(width = 3)
        plus4 = Tex("+", color=BLACK).scale(0.8).set_stroke(width = 3)
        plus5 = Tex("+", color=BLACK).scale(0.8).set_stroke(width = 3)

        # Position plus signs
        plus1.next_to(angle_red, RIGHT, buff=0.3)
        plus2.next_to(angle_yellow, RIGHT, buff=0.3)
        plus3.next_to(angle_green, RIGHT, buff=0.3)
        plus4.next_to(angle_blue, RIGHT, buff=0.3)
        plus5.next_to(angle_purple, RIGHT, buff=0.3)
        
        #Add =?°
        symbol = Text(" = ? °").scale(0.8).set_color(BLACK).set_stroke(width = 1)
        symbol.next_to(angle_pink, RIGHT, buff=0.3)

        # Add objects to the scene
        #self.play(FadeIn(title))
        #self.wait(2)
        #self.play(FadeOut(title))
        self.wait()
        self.play(FadeIn(grid))
        self.wait(2)
        #self.add(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)
        self.play(FadeIn(dot2, dot4))
        self.wait(2)
        self.play(FadeIn(dot1, dot3, dot5, dot6, dot7, dot8))
        self.wait(3)
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Create(line4))
        self.play(Create(line5))
        self.play(Create(line6))
        self.play(Create(line7))
        self.play(Create(line8))
        self.play(Create(line9))
        self.play(Create(line10))
        self.play(Create(line11))
        self.play(Create(line12))
        self.wait(2)
        #self.add(sector1, sector2, sector3, sector4, sector5, sector6)
        self.play(FadeIn(sector1, sector2, sector3, sector4, sector5, sector6))
        self.wait(3)
        text_group = VGroup(symbol, angle_red, angle_yellow, angle_green, angle_blue, angle_purple, angle_pink, plus1, plus2, plus3, plus4, plus5)
        self.wait(2)
        self.play(FadeIn(text_group))
        self.wait(5)
        
        # Add sectors for the solution
        sector_compare = Sector(arc_center=line2.get_end(), outer_radius=1.2, start_angle=line1.get_angle(), angle=PI/15.5, fill_opacity=1, fill_color=RED).rotate(PI).shift(1.2*UP+0.22*RIGHT)
        #Analysing first angle (red one)
        self.play(FadeOut(line3, line5, line6, line7, line8, line9, line10, line11, line12, dot5, dot6, dot7, dot8, sector2, sector3, sector4, sector5, sector6))
        self.wait(3)
        self.play(Indicate(line1), Indicate(line4), color = ORANGE)
        self.wait()
        self.play(Indicate(line2), color = ORANGE)
        self.wait()
        self.play(FadeIn(sector_compare))
        self.wait(5)
        self.play(FadeIn(line3, line5, line6, line7, line8, line9, line10, line11, line12, dot5, dot6, dot7, dot8, sector2, sector3, sector4, sector5, sector6))
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
        self.play(Create(sectors_group, run_time =4),FadeOut(sector_compare))
        self.wait(2)
        
        # Copy the sectors group
        sectors_copy = sectors_group.copy()
        
        #answer
        equal_to = Text(" = ").scale(0.8).set_color(BLACK).set_stroke(width = 1)
        equal_to.next_to(angle_pink, RIGHT, buff=0.3)
        self.play(Indicate(sectors_group), run_length = 4, color = None)
        self.wait()
        self.play(sectors_copy.animate.next_to(angle_pink, RIGHT, buff=0.6).scale(0.5), FadeOut(symbol), FadeIn(equal_to) )
        self.wait(5)
        answer = Text(" = 90°").scale(0.8).set_color(BLACK).set_stroke(width = 1)
        answer.next_to(angle_pink, RIGHT, buff=1.8)
        self.play(FadeIn(answer))
        self.wait(3)