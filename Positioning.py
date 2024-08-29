from manim import *

class Learning5(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        
        red_dot = Dot(color = RED)
        blue_dot = Dot(color = BLUE)
        blue_dot.next_to(red_dot, RIGHT+ DOWN )
        self.add(red_dot,blue_dot)
        
        s = Square(color = YELLOW)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)