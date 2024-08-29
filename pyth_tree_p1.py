import argparse
from math import atan2, ceil, pi, sqrt
from typing import List

from manim import *

config.media_width = "100%"
config.verbosity = "WARNING"
config.frame_size = (1080,1920)
config.frame_width = 7.5
config.background_color=BLACK

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, patches

def rgba_to_hex(rgba_tuple):
    """
    Convert RGBA tuple to hex code.

    Parameters:
    - rgba_tuple: Tuple representing RGBA values (e.g., (0.5, 0.0, 1.0, 1.0))

    Returns:
    - Hex code as a string
    """
    r, g, b, a = rgba_tuple
    hex_code = "#{:02X}{:02X}{:02X}{:02X}".format(
        int(r * 255), int(g * 255), int(b * 255), int(a * 255)
    )
    return hex_code


def pythagoras_tree(ratio: float = 1.0, nb_levels: int = 12):
    """
    Compute Pythagoras_tree
    The Pythagoras Tree is a plane fractal constructed from squares.
    It is named after Pythagoras because each triple of touching squares
    encloses a right triangle, in a configuration traditionally used to
    depict the Pythagorean theorem.
    http://en.wikipedia.org/wiki/Pythagoras_tree

          All these arguments are optional: the function can run with
          argument.
    Output :
          - Matrix M: Pythagoras tree is stored in a matrix M.
            This matrix has 5 columns.
            Each row corresponds to the coordinate of each square of the tree
            The two first columns give the bottom-left position of each
            square. The third column corresponds to the orientation angle of
            each square. The fourth column gives the size of each square. The
            fifth column specifies the level of recursion of each square.
            The first row corresponds to the root of the tree. It is always
            the same
            M[0,:] = [0 -1 0 1 1];
            The leaf located at row i will give 2 leaves located at 2*i and
            2*i+1.
    """
    # pylint: disable=too-many-locals
    # Check inputs
    if ratio <= 0:
        raise Exception("Length of ratio has to be greater than zero")
    if int(nb_levels) != float(nb_levels):
        raise Exception("The number of level has to be integer")

    # Compute constants
    c_d = sqrt(1.0 + ratio ** 2)
    # Normalized length 1
    c_1 = 1.0 / c_d
    # Normalized length 2
    c_2 = ratio / c_d
    # Translation pattern
    tr_pat = np.array(
        [[0.0, 1.0 / (1.0 + ratio ** 2)], [1.0, 1.0 + ratio / (1.0 + ratio ** 2)]]
    )
    # Defines the first rotation angle
    alpha1 = atan2(ratio, 1.0)
    # Defines the second rotation angle
    alpha2 = alpha1 - pi / 2.0
    # Number of elements (square)
    nb_elements = 2 ** (nb_levels + 1) - 1
    # Matrice containing the tree
    pt_arrray = np.zeros((nb_elements, 5))
    # Initialization of the tree
    pt_arrray[0, :] = [0.0, -1.0, 0.0, 1.0, 1.0]

    # Compute the level of each square contained in the resulting matrix
    offset = 0
    for i in range(nb_levels + 1):
        tmp = 2 ** i
        pt_arrray[offset : offset + tmp, 4] = i
        offset += tmp

    def mat_rot(angle_rad: float) -> np.ndarray:
        c_a = np.cos(angle_rad)
        s_a = np.sin(angle_rad)
        return np.array([[c_a, -s_a], [s_a, c_a]])

    # Compute the position and size of each square wrt its parent
    for i in range(1, nb_elements, 2):
        j = (i + 1) // 2 - 1
        t_m = pt_arrray[j, 3] * mat_rot(pt_arrray[j, 2]) @ tr_pat
        t_x = t_m[0, :] + pt_arrray[j, 0]
        t_y = t_m[1, :] + pt_arrray[j, 1]
        theta1 = (pt_arrray[j, 2] + alpha1) % (2.0 * pi)
        theta2 = (pt_arrray[j, 2] + alpha2) % (2.0 * pi)
        pt_arrray[i, 0:4] = [t_x[0], t_y[0], theta1, pt_arrray[j, 3] * c_1]
        pt_arrray[i + 1, 0:4] = [t_x[1], t_y[1], theta2, pt_arrray[j, 3] * c_2]
    return pt_arrray

print(pythagoras_tree(1).shape)

def pythagor_tree_plot(
    pt_array: np.ndarray, colormap_name: str = "summer", output_filename: str = "lm.png"
):
    """Plot a Pythagoras tree for a PNG format"""
    colormap = cm.get_cmap(colormap_name)
    fig, axis = plt.subplots()
    for i in range(pt_array.shape[0]):
        c_x = pt_array[i, 0]
        c_y = pt_array[i, 1]
        theta = pt_array[i, 2] * 180.0 / pi
        s_i = pt_array[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (pt_array[-1, 4] + 1)),
        )
        axis.add_patch(rect)
    plt.xlim([-4, 4])
    plt.ylim([-1.5, 3.5])
    # plt.gca().relim()
    plt.gca().set_aspect("equal", adjustable="box")
    plt.axis("off")
    fig.savefig(output_filename, bbox_inches="tight", dpi=300)

PT_ARR = pythagoras_tree(1)
c_x = PT_ARR[1, 0]
c_y = PT_ARR[1, 1]
theta = PT_ARR[1, 2] 
s_i = PT_ARR[1, 3]
colormap = cm.get_cmap("summer")

class test(MovingCameraScene):
    def construct(self):
        Q = [0.5,0.5,0]
        A = self.camera.frame.move_to(Q).save_state()
        self.add(A)
        poly = Polygon(ORIGIN,RIGHT,UP/2+RIGHT/2, 
                       stroke_width = 2, 
                       stroke_color = WHITE).set_z_index(8)
        poly.joint_type=LineJointType.ROUND 
        self.play(self.camera.frame.animate.move_to(poly).scale(0.5))
        self.play(Create(poly), 
                  run_time=1.5)
        
        # self.wait()
        l = Line(RIGHT,UP/2+RIGHT/2)
        ninety = Square(side_length=0.16, 
                        stroke_width = 0,
                        fill_color = "#C22300",
                        fill_opacity=1)
        ninety.next_to(l.get_end(), LEFT, buff=0).rotate(PI/4)
        ninety.rotate(PI/2, about_point=UP/2+RIGHT/2).shift(0.03*DOWN).set_z_index(6)
        self.play(GrowFromPoint(ninety,UP/2+RIGHT/2))
        tri1 = VGroup(poly, ninety)
        tri1_copy = tri1.copy()
        self.wait(2)

        # a = MathTex("a").next_to(poly, LEFT, buff=0.1).scale(0.5).shift(0.1*UP+0.3*RIGHT).scale(0.8)
        # b = MathTex("b").next_to(poly, RIGHT, buff=0.1).scale(0.5).shift(0.1*UP+0.3*LEFT).scale(0.8)
        # c = MathTex("c").next_to(poly, DOWN, buff=0.1).scale(0.5).shift(0.05*UP).scale(0.8)

        # self.play(FadeIn(a, b, c))
        # self.wait(2)

        # a_sq = MathTex("a^2").scale(0.5)
        # plus = MathTex("+").next_to(a_sq, RIGHT, buff=0.1).scale(0.5)
        # b_sq = MathTex("b^2").next_to(plus, RIGHT, buff=0.1).scale(0.5)
        # equals = MathTex("=").next_to(b_sq, RIGHT, buff=0.1).scale(0.5)
        # c_sq = MathTex("c^2").next_to(equals, RIGHT, buff=0.1).scale(0.5)

        # ac = a.copy()
        # bc = b.copy()
        # cc = c.copy()

        # eqn = VGroup(a_sq, b_sq, c_sq, plus, equals).next_to(poly, 1.4*DOWN).scale(0.8)

        # # self.play(FadeIn(plus, equals),
        # #           ReplacementTransform(ac, a_sq),
        # #           ReplacementTransform(bc, b_sq),
        # #           ReplacementTransform(cc, c_sq),)

        # txt = Text("Pythagorean Tree", 
        #            font='Athletics', 
        #            weight = BOLD).next_to(poly, 2 * UP).scale(0.3)
        # self.play(FadeIn(txt))
        # self.wait()

        # self.play(ReplacementTransform(ac, a_sq))
        # self.wait(0.25)
        # self.play(FadeIn(plus))
        # self.wait(0.25)
        # self.play(ReplacementTransform(bc, b_sq))
        # self.wait(0.25)
        # self.play(FadeIn(equals))
        # self.play(ReplacementTransform(cc, c_sq))
        # self.wait(5)

        k=2**8-1
        i = 0  # Index of the square to add
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        self.play(GrowFromEdge(s, UP))
        self.wait()  

        # Add the second square
        i = 1
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        B1 = [0.25, 0.25, 0]
        self.play(GrowFromPoint(s, B1))
        self.wait()  

        # Add the third square
        i = 2
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        C1 = [0.75, 0.25, 0]
        self.play(GrowFromPoint(s, C1))
        self.wait(3)  

        O = [-0.5, 0.5, 0]
        P = [0,1,0]
        S = [-0.5,1,0]
        Q = [0.5,0.5,0]
        R = [0,0,0]

        s2 = Polygon(O,P,Q,R)
        self.play(self.camera.frame.animate.move_to(s2).scale(0.7))

        tri2 = Polygon(O,P,S, 
                       stroke_width = 2, 
                       stroke_color = WHITE).set_z_index(8)
        tri2.joint_type=LineJointType.ROUND 
        tri2center = [-0.375, 0.875, 0]
        self.play(tri1_copy.animate.move_to(tri2center).scale(0.7).rotate(PI/4))

        self.wait()  

        #Create fourth sq
        i = 3
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        B1 = [-0.5, 0.75, 0]
        self.play(GrowFromPoint(s, B1))
        self.wait(3)  

        # Add the fifth square
        i = 4
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        C1 = [-0.25, 1, 0]
        self.play(GrowFromPoint(s, C1))
        self.wait(3)  

        # self.play(Restore(A))
        # self.wait(2)

        B = [1, 0, 0]
        X = [1,1,0]
        Y = [1.5, 0.5, 0]
        Z = [1.5, 1, 0]
        sq3 = Polygon(Q, B, Y, X)

        self.play(self.camera.frame.animate.move_to(sq3))

        
        tri3 = Polygon(X,Y,Z, 
                       stroke_width = 2, 
                       stroke_color = WHITE).set_z_index(8)
        tri3.joint_type=LineJointType.ROUND 

        tri1_copy2 = tri1.copy()
        tri3center = [1.375, 0.875, 0]
        self.play(tri1_copy2.animate.move_to(tri3center).scale(0.7).rotate(-PI/4))

        self.wait()  

        #Create sixth sq
        i = 5
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        D1 = [1.25, 1, 0]
        self.play(GrowFromPoint(s, D1))
        self.wait(3)  

        # Add the seventh square
        i = 6
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2] * 180 / np.pi
        s_i = PT_ARR[i, 3]
        rect = patches.Rectangle(
            [c_x, c_y],
            s_i,
            s_i,
            angle=theta,
            ec="none",
            color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
        )
        pts = rect.get_corners()
        color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
            width=0).set_z_index(4)
        E1 = [1.5, 0.75, 0]
        self.play(GrowFromPoint(s, E1))
        self.wait(2)
        self.play(FadeOut(tri1, tri1_copy, tri1_copy2), Restore(A))

        # Continue this pattern for other squares
        for i in range(7, k):
            c_x = PT_ARR[i, 0]
            c_y = PT_ARR[i, 1]
            theta = PT_ARR[i, 2] * 180 / np.pi
            s_i = PT_ARR[i, 3]
            rect = patches.Rectangle(
                [c_x, c_y],
                s_i,
                s_i,
                angle=theta,
                ec="none",
                color=colormap(1.0 - i / (PT_ARR[-1, 4] + 1)),
            )
            pts = rect.get_corners()
            color2 = colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
            s = Polygon(*[np.append(p, 0) for p in pts]).set_fill(rgba_to_hex(color2), opacity=color2[-1]).set_stroke(
                width=0)
            self.play(AnimationGroup(FadeIn(s), lag_ratio = 0.8), run_time=2)
            self.wait(0.25)  # Adjust the delay as needed

        self.wait(2)

        txt = Text("Pythagorean Tree", 
                   font='Athletics', 
                   weight = BOLD).scale(0.7)
        txt.next_to(Q, 14*UP)
        # self.play(FadeIn(txt))
        self.wait(3)
        self.play(FadeIn(txt))
        self.wait(3)
        poly.set_stroke(width = 3)

        #Add symbols for equality of the sides of the pentagon
        M = [0.25, 0.25, 0]
        U = [0.75, 0.25, 0]
        parallel_symbol_p1 = Arrow(max_tip_length_to_length_ratio=0, color = "#0A47C2", stroke_width=2)
        parallel_symbol_p2 = Arrow(max_tip_length_to_length_ratio=0, color = "#0A47C2", stroke_width=2).next_to(parallel_symbol_p1, DOWN, buff = 0.7)
        parallel_symbol1 = VGroup(parallel_symbol_p1, parallel_symbol_p2).move_to(M).rotate(PI/4+PI/2).scale(0.075).set_z_index(10)       
        parallel_symbol2 = parallel_symbol1.copy().move_to(U).rotate(PI/2)
        ps = VGroup(parallel_symbol1, parallel_symbol2)

        self.play(FadeIn(poly, ninety, ps), 
                  self.camera.frame.animate.move_to(poly).scale(0.5),
                  poly.animate.set_color("#0A47C2"))
        self.play(Indicate(poly, color = "#0A47C2", scale_factor= 1.3), 
                  Indicate(ps, color = None), run_time = 2)
        self.wait()
        self.play(Restore(A), poly.animate.set_color(WHITE), FadeOut(ps))
        self.wait(3)
            
