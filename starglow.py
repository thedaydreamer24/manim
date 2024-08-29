from manim import *
import math
config.media_width = "100%"
config.verbosity = "WARNING"
config.frame_size = (1080,1920)
config.frame_width = 7.5

def create_glow(x, rad=0.4, col=TEAL):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius=rad*(1.0025**(idx**2))/400, stroke_opacity=0, fill_color=col,
        fill_opacity=0.2-idx/300).move_to(x)
        glow_group.add(new_circle)
    return glow_group

class Pattern(MovingCameraScene):
    def construct(self):
        
        # Define the points
        A = [-4, -2, 0]
        B = [0, 6, 0]
        C = [2, -2, 0]
        D = [-4.0064689342404, 3.1982113378685, 0]
        E = [3.1911927437642, 3.1982113378685, 0]
        F=  [-0.2748217374162,1.983215224197,0]

        # Create the segments
        f = Line(A, B, color=TEAL, stroke_width=5)
        g = Line(B, C, color=TEAL, stroke_width=5)
        h = Line(C, D, color=TEAL, stroke_width=5)
        i = Line(D, E, color=TEAL, stroke_width=5)
        j = Line(E, A, color=TEAL, stroke_width=5)

        # Create the star polygon
        star_points = [A, B, C, D, E]
        s = Polygon(*star_points, color=TEAL, stroke_width=5).set_z_index(2)
        s.joint_type=LineJointType.ROUND 
        
        self.play(self.camera.frame.animate.scale(1.3).move_to(s))
        
        line = []

        for k in range(5):
            l = Line(s.point_from_proportion(k/5), s.point_from_proportion((k+1)/5), stroke_width=5).set_color(TEAL)
            line.append(l)

        dot = Dot(s.point_from_proportion(0)).set_color(TEAL)
        b = TracedPath(dot.get_center, dissipating_time=0.0001, stroke_opacity=[0, 1]).set_color(TEAL)

        self.add(dot, b)
        def glows():
            return VGroup(*[create_glow(x) for x in [dot]])
        glow_all = always_redraw(lambda: glows())
        self.add(glow_all)
        self.play(LaggedStart(MoveAlongPath(dot, s), FadeIn(f), FadeIn(g), FadeIn(h), FadeIn(i), FadeIn(j), lag_ratio=0.1, run_time=2))
        #self.play(LaggedStart(MoveAlongPath(dot, s), FadeOut(line[0]), FadeOut(line[1]), FadeOut(line[2]), FadeOut(line[3]), FadeOut(line[4]), lag_ratio=0.1))
        self.play(FadeOut(dot, glow_all))
        self.wait()