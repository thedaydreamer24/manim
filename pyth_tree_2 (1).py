import argparse
from math import atan2, ceil, pi, sqrt
from typing import List

from manim import *

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

print(pythagoras_tree(ratio=0.2).shape)

def pythagor_tree_plot(
    pt_array: np.ndarray, colormap_name: str = "bone", output_filename: str = "lm.png"
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

PT_ARR = pythagoras_tree(10)
c_x = PT_ARR[1, 0]
c_y = PT_ARR[1, 1]
theta = PT_ARR[1, 2] 
s_i = PT_ARR[1, 3]
colormap = cm.get_cmap("summer")

class test(MovingCameraScene):
    def construct(self):
        """ k=2**4
        self.wait()
        for i in range(k):
            c_x = PT_ARR[i, 0]
            c_y = PT_ARR[i, 1]
            theta = PT_ARR[i, 2]
            s_i = PT_ARR[i, 3]
            print(i,c_x,c_y,theta,s_i)
            self.add(Square().scale(s_i).move_to([c_x+s_i/2,c_y+s_i/2,0]).rotate(theta,about_point=[c_x,c_y,0]))
            self.add(Dot([c_x,c_y,0]))
            self.wait() """
        k=2**7-1
        for i in range(k):
            c_x = PT_ARR[i, 0]
            c_y = PT_ARR[i, 1]
            theta = PT_ARR[i, 2]*180/PI
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
            color2=colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
            print(color2[0:4])
            print(color2[-1])
            s = Polygon(*[np.append(p,0) for p in pts]).set_fill(rgba_to_hex(color2),opacity=color2[-1]).set_stroke(width=0)
            self.add(s)
            self.wait(0.25)


def give_poly(r):
    k=2**8-1
    PT_ARR = pythagoras_tree(r)
    poly = VGroup()
    for i in range(k):
        c_x = PT_ARR[i, 0]
        c_y = PT_ARR[i, 1]
        theta = PT_ARR[i, 2]*180/PI
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
        color2=colormap(1.0 - i / (PT_ARR[-1, 4] + 1))
        #print(color2[0:4])
        #print(color2[-1])
        s = Polygon(*[np.append(p,0) for p in pts]).set_fill(rgba_to_hex(color2),opacity=color2[-1]).set_stroke(width=0)
        poly.add(s)
    return poly

class test2(MovingCameraScene):
    def construct(self):
        
        r=ValueTracker(1)
        
        new_tree = always_redraw(
            lambda: give_poly(r.get_value())
        )

        right_triangle = always_redraw(
            lambda:
            Polygon(new_tree[1].get_vertices()[1],new_tree[0].get_vertices()[2],new_tree[0].get_vertices()[3])
        )
        #self.add(give_poly(r.get_value()))
        self.add(new_tree,right_triangle)
        self.wait()
        self.play(r.animate.set_value(0.5),run_time=2.5)
        self.wait()
        self.play(r.animate.set_value(1/0.5),run_time=5)
        self.wait()
        self.play(r.animate.set_value(1),run_time=2.5)
        self.wait()

class test3(MovingCameraScene):
    def construct(self):
        
        new_tree = give_poly(1)
        #self.add(give_poly(r.get_value()))
        self.add(new_tree[0])
        self.wait()
        for k in range(6):
            #self.add(new_tree[k])
            #self.wait(0.5)
            self.play(*[ReplacementTransform(new_tree[i].copy(),new_tree[j]) for i in range(2**k-1,2**k+2**(k)-1) for j in range(2*i+1,2*i+3)])
        #self.play(*[ReplacementTransform(new_tree[0].copy(),new_tree[i]) for i in range(1,2+1)])
        #self.play(*[ReplacementTransform(new_tree[1].copy(),new_tree[i]) for i in range(3,4+1)],*[ReplacementTransform(new_tree[2].copy(),new_tree[i]) for i in range(5,6+1)])
        
        self.wait()
        
class test4(MovingCameraScene):
    def construct(self):
        
        new_tree = give_poly(1)
        #self.add(give_poly(r.get_value()))
        self.add(new_tree[0:3])
        self.wait()
        print(new_tree[0].get_vertices()[0])
        self.add(Dot(new_tree[1].get_vertices()[1]))
        self.add(Dot(new_tree[0].get_vertices()[2]),Dot(new_tree[0].get_vertices()[3]))
        #self.add(*[Dot(d new_tree[0].get_vertices(0))])
        #self.add(p)
        self.wait()
        