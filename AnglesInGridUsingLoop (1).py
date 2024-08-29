from manim import *
config.background_color = WHITE
class Grid(Scene):
    def construct(self):
        # Add grids
        rows = 6
        cols = 6
        grid = VGroup(*[
            VGroup(*[Square(side_length=1, fill_opacity=0, stroke_width=5, stroke_opacity = 0.5).move_to((i-rows//2)*RIGHT + (j-cols//2)*UP) for j in range(cols)]) for i in range(rows)
        ]).set_color(GREY).shift(0.6*RIGHT+1.2*UP)

        # Add lines
        line_positions = [
            (0, 5, 0, 1), (1, 4, 0, 1), (2, 3, 0, 1), (3, 2, 0, 1), (4, 1, 0, 1), (5, 0, 0, 1),
            (0, 5, 1, 0), (1, 4, 1, 0), (2, 3, 1, 0), (3, 2, 1, 0), (4, 1, 1, 0), (5, 0, 1, 0),
        ]
        lines = VGroup(*[
            Line(grid[i][j].get_corner(UR), grid[k][l].get_corner(DL), color=BLACK, stroke_width=5) for i, j, k, l in line_positions
        ])

        # Add dots
        dots = VGroup(*[
        Dot(lines[i].get_start(), color=WHITE, fill_opacity=1, stroke_width=4, stroke_color = BLACK) for i in range(len(lines))
            ])

        # Create the sectors
        sector_data = []
        colors = [RED, YELLOW, GREEN, BLUE, PURPLE, PINK]
        angles = [PI/15, PI/12, PI/10, PI/10, PI/12, PI/15]

        for i in range(6):
            sector_data.append((lines[i], lines[i], colors[i], angles[i]))

        sectors = []
        for line1, line2, color, angle in sector_data:
            sector = Sector(
                arc_center=line2.get_start(),
                outer_radius=1.2,
                start_angle=line1.get_angle(),
                angle=angle,
                fill_opacity=1,
                fill_color=color,
            )
            sectors.append(sector)
        sectors = VGroup(*sectors)
        self.add(grid)
        self.add(sectors)
        self.add(lines, dots)
        
        # Make arrays
        colors = [RED, YELLOW, GREEN, BLUE, PURPLE, PINK]
        angles = []
        plus_signs = []
        
        # Using loop, add angle symbols and plus signs as required
        for i in range(len(colors)):
            angle = Tex("$\\angle$", color=colors[i]).scale(1).set_stroke(width=3)
            if i == 0:
                angle.shift(3.2*DOWN+3.75*LEFT)
            else:
                angle.next_to(angles[-1], RIGHT, buff=1)
            angles.append(angle)

            if i < len(colors)-1:
                plus_sign = Tex("+", color=BLACK).scale(0.8).set_stroke(width=3)
                plus_sign.next_to(angle, RIGHT, buff=0.3)
                plus_signs.append(plus_sign)
                
        # Add = ? °
        symbol = Text(" = ? °").scale(0.8).set_color(BLACK).set_stroke(width=1)
        symbol.next_to(angles[-1], RIGHT, buff=0.3)
        
        # Add objects to the scene
        self.add(symbol, *angles, *plus_signs)