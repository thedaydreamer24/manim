from manim import *
config.media_width = "100%"
config.verbosity = "WARNING"
config.frame_size = (1080,1920)
config.frame_width = 7.5
config.background_color=BLACK

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
        
        A = self.camera.frame.scale(1.3).move_to(grid)
        self.add(A)
        
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
        
        txt = Text("What's the sum of these angles?", font = "Athletics", weight=BOLD ).next_to(grid, 1.5 * UP).scale(0.7)
        text_group = VGroup(angle_red,plus1,angle_yellow,  plus2,angle_green, plus3,angle_blue,  plus4,angle_purple,  plus5, angle_pink, equal_to, symbol  )
        text_group.arrange(buff = 0.3).next_to(grid, 2.5 * DOWN)
        
        
        self.add(grid,
                 dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,
                 line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,
                 sector1, sector2, sector3, sector4, sector5, sector6,
                 text_group, txt)
        