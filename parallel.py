from manim import *

class ParallelLines(Scene):
    def construct(self):
        # Create the parallel lines
        line1 = Line(start=LEFT*3, end=RIGHT*3)
        line2 = Line(start=LEFT*3+UP*1.5, end=RIGHT*3+UP*1.5)

        # Calculate the midpoint between the lines
        midpoint = (line1.get_center() + line2.get_center()) / 2

        # Add the parallel symbol using TexMobject
        symbol = Tex("\parallel").move_to(midpoint)

        # Add everything to the scene
        self.add(line1, line2, symbol)

# Render the scene
ParallelLines().render()
