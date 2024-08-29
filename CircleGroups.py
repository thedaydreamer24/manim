from manim import *

class ArcShapeIris(Scene):
    def construct(self):
        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_B]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        self.play(Create(circles_group), run_time = 5)