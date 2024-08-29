from manim import *
config.background_color = WHITE
class SineWave(Scene):
    def construct(self):
        
        # Create a title
        title = MathTex(r"\text{This is a Sine Wave ranging from } -2\pi \text{ to } 2\pi").set_color(BLACK)
        
        # Create the value above the range of x
        a= ValueTracker(0)
        
        # Create the x-axis and y-axis
        ax = Axes(x_range=[-8,8,3.15], y_range=[-2,2]).set_color(BLACK)
        
        #Create the sine wave
        curve = ax.plot(lambda x: np.sin(x), color=BLACK)
        
        #Get the area in the range [-2pi to 2pi]
        area = ax.get_area(curve, x_range=[-2*np.pi, 2*np.pi], color = BLUE)
        
        # Animate
        self.play(FadeIn(ax))
        self.wait()
        self.play(Create(curve), run_time = 3)
        self.play(FadeIn(area))
        self.wait()
        self.play(Create(title.next_to(ax, UP)))
        self.add(title.next_to(ax, UP))

        
        # Create the position of the arrow
        position = ValueTracker(0)
        
        # Create the arrow
        pointer = Vector(DOWN).set_color(RED)
        
        # Add updater in the arrow
        pointer.add_updater(
            lambda mob: mob.next_to(
                ax.coords_to_point(position.get_value()), UP
            )
        )
        
        # Create the label for the x-range
        a_number = DecimalNumber(
            a.get_value(),
            color = RED,
            num_decimal_places = 3,
            show_ellipsis = True
        )
        
        # Add updater for the label over the x-range
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(pointer, UP)
        )
        
        # Animate
        
        self.play(FadeIn(pointer, a_number))
        self.wait()
        self.play(position.animate.set_value(-6.26), a.animate.set_value(-2), run_time = 2)
        self.wait()
        self.play(position.animate.set_value(6.26), a.animate.set_value(2), run_time = 4)
        self.wait(2)