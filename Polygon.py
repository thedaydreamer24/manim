from manim import *

class PolygonScene(Scene):
    def construct(self):
        # Create a regular polygon with 10 sides
        n = 10
        polygon = RegularPolygon(n, start_angle=PI/2)
        self.play(Create(polygon))

        # Draw two parallel lines using vertices of the polygon
        vertices = polygon.get_vertices()
        line1 = Line(vertices[2], vertices[-2], color=RED)
        self.play(Create(line1))
        self.wait()
        line2 = Line(vertices[3], vertices[-3], color=RED)
        self.play(Create(line2))
        self.wait()

        #Fill the area
        self.play(DrawBorderThenFill(Rectangle(width=1.86, height=2/3, stroke_width = 0, fill_opacity=0.3, fill_color=PINK)))

        #Draw the dotted lines by joining opposite sides of the polygon
        dotted_lines = []
        for i in range(n//2):
            dotted_line = DashedLine(vertices[i], vertices[i+n//2], dash_length=0.1)
            dotted_lines.append(dotted_line)
            self.play(Create(dotted_line))

        self.wait() 