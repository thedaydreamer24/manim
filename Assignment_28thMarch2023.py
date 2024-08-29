from manim import *

class GridExample(Scene):
    def construct(self):
        # Create a NumberPlane object with a grid
        grid = NumberPlane(
            x_range=(-2.5, 2.5), 
            y_range=(-2.5, 2.5),
            x_length=5,
            y_length=5,
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 2,
            },
            
        )
        
        # Create a 10x10 grid of squares
        squares = VGroup(*[Square(side_length=0.5)
            for i in range(100)])
        squares.arrange_in_grid(10, 10, buff=0)
        
        
        # Color the squares as in the question
        for i in range(0,10):
            for j in range(i+1):
                index = i*10 + j
                squares[index].set_color(RED)
                squares[index].set_fill(opacity=0.8)
                
        squares.set_stroke(color = WHITE, width=4)
                
        self.play(Create(squares))
        # Add the grid and squares to the scene
        self.add(grid, squares)
        
        # Wait for a moment
        self.wait()

class SquareRotation(Scene):
    def construct(self):
        # Create a square
        square = Square(color=RED, fill_opacity=0.5)

        # Rotate the square four times by 90 degrees each time
        for i in range(4):
            self.play(square.animate.rotate(PI/2), run_time = 2)