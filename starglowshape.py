from manim import*
import math
def create_glow(x, rad=0.4, col=PINK):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius=rad*(1.002**(idx**2))/400, stroke_opacity=0, fill_color=col,
        fill_opacity=0.2-idx/300).move_to(x)
        glow_group.add(new_circle)
    return glow_group

class Pattern(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(0.8))
        n = 5
        s = RegularPolygram(5, stroke_width=3).scale(2).set_color(PINK)
        line = []

        for k in range(5):
            l = Line(s.point_from_proportion(k/5), s.point_from_proportion((k+1)/5), stroke_width=1).set_color(PINK)
            line.append(l)

        dot = Dot(s.point_from_proportion(0)).set_color(PINK)
        b = TracedPath(dot.get_center, dissipating_time=0.2, stroke_opacity=[0, 1]).set_color(PINK)

        self.add(dot, b)
        def glows():
            return VGroup(*[create_glow(x) for x in [dot]])
        glow_all = always_redraw(lambda: glows())
        self.add(glow_all)
        self.play(LaggedStart(MoveAlongPath(dot, line[0]), Create(line[0]), lag_ratio=1))
        self.play(LaggedStart(MoveAlongPath(dot, line[1]), Create(line[1]), lag_ratio=1))
        self.play(LaggedStart(MoveAlongPath(dot, line[2]), Create(line[2]), lag_ratio=1))
        self.play(LaggedStart(MoveAlongPath(dot, line[3]), Create(line[3]), lag_ratio=1))
        self.play(LaggedStart(MoveAlongPath(dot, line[4]), Create(line[4]), lag_ratio=1))
        #self.play(LaggedStart(MoveAlongPath(dot, s), FadeOut(line[0]), FadeOut(line[1]), FadeOut(line[2]), FadeOut(line[3]), FadeOut(line[4]), lag_ratio=0.1))
        
        self.wait(2)
        