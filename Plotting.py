from manim import *

class Learning3(Scene): 
    def construct(self):
        ax = Axes(x_range = (-5,5), y_range = (-5,5))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color = RED)
        area = ax.get_area(curve, x_range = (-2,0))
        self.play(Create(ax, run_time = 5),Create(curve, run_time = 3))
        self.play(FadeIn(area))
        self.wait(2)