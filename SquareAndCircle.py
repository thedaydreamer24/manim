from manim import *
class Learning1(Scene): 
    def construct(self):
        red_circle = Circle(color = RED, fill_opacity = 0.5)
        blue_square = Square(color = BLUE, fill_opacity = 0.8)
        blue_square.next_to(red_circle, LEFT)
        self.add(red_circle, blue_square)