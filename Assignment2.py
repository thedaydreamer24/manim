from manim import *

config.background_color = BLACK

class TriangleScaling(Scene):
    def construct(self):

        #Create a title
        
        title = Tex("Let's Scale a Triangle")
        
        #Create the triangle
        triangle = Triangle().set_stroke(PURPLE).set_color(PURPLE).set_opacity(0.5)
        triangle.save_state()
        
        #Create the scale value
        scale_factor = ValueTracker(1)
        scale_value = Integer(scale_factor.get_value())
        scale_value.add_updater(
            lambda mob: mob.next_to(triangle,RIGHT, buff = 2)
            )
        
        #Add everything to the canvas and animate
        
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))
        self.wait()
        self.play(FadeIn(triangle, scale_value))
        triangle.generate_target()
        triangle.target.scale(0)
        self.add(triangle)
        self.wait()
        self.play(MoveToTarget(triangle), scale_value.animate.set_value(0), run_time = 3)
        self.play(Restore(triangle), scale_value.animate.set_value(1), run_time = 3)
        self.wait()
        self.play(triangle.animate.scale(3), scale_value.animate.set_value(3), run_time = 4)
        self.wait()
        self.play(Restore(triangle),scale_value.animate.set_value(1), run_time = 3)
        self.wait()