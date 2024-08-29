from manim import *
import math
config.background_color = BLACK
def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1[0:2],a2[0:2],b1[0:2],b2[0:2]])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return np.array([x/z, y/z,0])

class PolygonAngleDark(Scene):
    def construct(self):
        
        
        pentagon = RegularPolygon(n=5, stroke_color=WHITE, stroke_width=6, fill_opacity = 0.2, color = TEAL).scale(3)
        pentagon_edges = VGroup(*[Line(pentagon.get_vertices()[i], pentagon.get_vertices()[(i+1)%5], color=WHITE, stroke_width=6) for i in range(5)]).set_z_index(4)
        pentagon.joint_type=LineJointType.ROUND 
        pentagon_edges.joint_type=LineJointType.ROUND 
        
        # Select two pairs of vertices
        vertices = pentagon.get_vertices()
        pair1 = [vertices[0], vertices[2]]
        pair2 = [vertices[1], vertices[4]]
        
        
        
        # Create lines joining the selected vertices
        line1 = Line(pair1[0], pair1[1], color=WHITE, stroke_width=6).set_z_index(2)
        line2 = Line(pair2[0], pair2[1], color=WHITE, stroke_width=6).set_z_index(2)
        line1.joint_type=LineJointType.ROUND 
        line2.joint_type=LineJointType.ROUND 
        
        intersection = get_intersect(pair1[0], pair1[1], pair2[0], pair2[1] )
        
        #Add dots
        dot1 = Circle(radius=0.08, fill_color=BLACK, fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(line1.get_start()).set_z_index(5)
        dot2 = Circle(radius=0.08, fill_color=BLACK, fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(line1.get_end()).set_z_index(5)
        dot3 = Circle(radius=0.08, fill_color=BLACK, fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(line2.get_start()).set_z_index(5)
        dot4 = Circle(radius=0.08, fill_color=BLACK, fill_opacity=1, stroke_width=4, stroke_color=WHITE).move_to(line2.get_end()).set_z_index(5)
        
        
        #Add symbols for equality of the sides of the pentagon
        parallel_symbol_p1 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE)
        parallel_symbol_p2 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE).next_to(parallel_symbol_p1, DOWN, buff = 0.7)
        parallel_symbol1 = VGroup(parallel_symbol_p1, parallel_symbol_p2).move_to(pentagon_edges[0].get_center()).rotate(math.atan(3/4)+PI/2).scale(0.2)       
        parallel_symbol2 = parallel_symbol1.copy().move_to(pentagon_edges[1].get_center()).rotate(-PI/1.67)
        parallel_symbol3 = parallel_symbol1.copy().move_to(pentagon_edges[2].get_center()).rotate(-2*PI/1.67)
        parallel_symbol4 = parallel_symbol1.copy().move_to(pentagon_edges[3].get_center()).rotate(2*PI/1.67)
        parallel_symbol5 = parallel_symbol1.copy().move_to(pentagon_edges[4].get_center()).rotate(PI/1.67)
        
        #Add arrows
        arrow1 = Arrow(max_stroke_width_to_length_ratio=0, color = WHITE).move_to(pentagon_edges[2].get_center()).shift(0.5*LEFT)
        arrow2 = Arrow(max_stroke_width_to_length_ratio=0, color = WHITE).move_to(line2.get_center()).shift(0.5*LEFT)
        arrow3 = Arrow(max_stroke_width_to_length_ratio=0, color = WHITE).move_to(pentagon_edges[3].get_center()).rotate(PI/2.5).shift(0.5*DOWN+0.165*LEFT)
        arrow4 = Arrow(max_stroke_width_to_length_ratio=0, color = WHITE).move_to(line1.get_center()).rotate(PI/2.5).shift(0.5*DOWN+0.165*LEFT)
        
        # Create a parallelogram
        parallelogram = Polygon(pair1[1], intersection, pair2[1], pentagon.get_vertices()[3], color=WHITE, stroke_width=6, fill_opacity = 0)
        
        #Intersecting lines
        intersecting_line1 = line1.copy()
        intersecting_line2 = line2.copy()
        
        # Add sector
        sector = Sector(arc_center=line2.get_start(), outer_radius=0.7, start_angle=line1.get_angle(), angle = PI/1.67, fill_opacity=1, fill_color=PURPLE_B, stroke_width = 2, stroke_color = WHITE)
        sector.rotate(PI)
        sector.move_to(intersection)
        sector.shift(0.24*LEFT+0.33*UP)
        
        # Start solving
        
        #pentagon sector
        pentagon_sector = sector.copy()
        pentagon_sector.align_to(pentagon, DR)
        pentagon_sector.align_to(vertices[3], RIGHT).shift(0.2*RIGHT)
        
        
        #create pentagon degree text
        # Add text of 108 degrees beside pentagon_sector
        pentagon_degree = MathTex("108^\\circ", color = WHITE).next_to(pentagon_sector, RIGHT, buff=SMALL_BUFF).scale(0.7).shift(0.1*LEFT)
        
        
        # Opposite angle
        opposite_angle = sector.copy()
        opposite_angle.move_to(intersection)
        opposite_angle.shift(0.24*RIGHT+0.33*DOWN)
        opposite_angle.rotate(PI)
        
        
        #add everything
        #self.play(FadeIn(number_plane))
        self.play(GrowFromCenter(pentagon, run_time=2))
        self.wait()
        self.play(FadeIn(dot1, dot2))
        self.wait()
        self.play(FadeIn(dot3, dot4))
        self.wait()
        self.play(Create(line1))
        self.play(Create(line2))
        self.wait()
        question = MathTex("?").scale(0.6).set_color(WHITE).set_stroke(width = 1).move_to(sector.get_center()).set_z_index(6)
        self.play(FadeIn(sector, run_time = 2), FadeIn(question, run_time = 2))
        self.wait(3)       
        self.play(FadeOut(sector), FadeOut(question))
        self.wait()
        
        self.play(Indicate(pentagon_edges, scale_factor = 1, color = YELLOW, run_time = 2))
        self.wait()
        
        #add equal symbols to the scene       
        self.play(FadeIn(parallel_symbol1, parallel_symbol2, parallel_symbol3, parallel_symbol4, parallel_symbol5))
        self.wait(2)
        
        self.play(FadeOut(parallel_symbol1, parallel_symbol2, parallel_symbol3, parallel_symbol4, parallel_symbol5))
        self.wait(2)
        
        self.play(Indicate(line2), Indicate(pentagon_edges[2]), scale_factor = 1, color = PURE_RED, run_time=1.5)
        self.play(FadeIn(arrow1), FadeIn(arrow2))
        self.wait()
        self.play(Indicate(line1), Indicate(pentagon_edges[3]), scale_factor = 1, color = PURE_RED, run_time=1.5)
        self.play(FadeIn(arrow3), FadeIn(arrow4))
        self.wait()
        self.play(FadeOut(arrow1, arrow2, arrow3, arrow4), FadeIn(parallelogram))
        self.wait(2)
        
        self.play(Indicate(parallelogram), run_time = 3)
        
        self.play(FadeIn(pentagon_sector), FadeIn(pentagon_degree))
        self.wait()
        
        self.play(Indicate(parallelogram), run_time = 2, color = YELLOW, scale_factor = 1, fill_color =YELLOW)
        
        pentagon_sector_copy = pentagon_sector.copy()
        
        self.play(pentagon_sector_copy.animate.rotate(PI).move_to(opposite_angle.get_center()))    
        self.wait()
        
        self.play(ShowPassingFlash(intersecting_line1.set_color(RED), time_width=0.5), ShowPassingFlash(intersecting_line2.set_color(RED), time_width=0.5), run_time=2, rate_func=linear)
        self.wait()
        self.play(opposite_angle.animate.rotate(PI).move_to(sector.get_center()))    
        self.wait()
        
        sector_copy = sector.copy()
        self.play(Indicate(sector), color = None)
        self.wait()
        self.play(sector_copy.animate.next_to(pentagon, RIGHT, buff=0.6).scale(1), FadeOut(pentagon_degree))
        
        answer = MathTex(" = 108^\\circ").scale(0.8).set_color(WHITE).set_stroke(width = 1).next_to(sector_copy, RIGHT)
        answer.next_to(sector_copy, RIGHT, buff=0.3)
        
        self.play(FadeIn(answer))
        self.wait()