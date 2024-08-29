from manim import *

class Learning4(Scene):
    def construct(self):
        green_square = Square(color = GREEN, fill_opacity = 0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color = PINK, fill_opacity = 0.8)
        self.play(Transform(green_square,blue_circle))
        self.wait()
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))