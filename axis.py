from manim import *

class Learning2(Scene): 
    def construct(self):
        ax = Axes(x_range = (-5,5), y_range = (-5,5))
        
        self.add(ax)