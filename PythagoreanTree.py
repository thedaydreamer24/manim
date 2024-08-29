from manim import *
import numpy as np

class PythagorasTree(Scene):
    def construct(self):
        ratio = 1.0
        nb_levels = 3

        # Create Pythagoras tree data
        pt_array = self.pythagoras_tree(ratio=ratio, nb_levels=nb_levels)

        # Draw Pythagoras tree
        self.draw_pythagoras_tree(pt_array)

    def draw_pythagoras_tree(self, pt_array):
        squares = VGroup()

        for i in range(pt_array.shape[0]):
            c_x = pt_array[i, 0]
            c_y = pt_array[i, 1]
            theta = pt_array[i, 2] * 180.0 / np.pi
            s_i = pt_array[i, 3]

            square = Square(side_length=s_i, stroke_width=2, fill_opacity=0.7)
            square.move_to([c_x, c_y, 0])
            square.rotate(theta, about_point=[c_x, c_y, 0])

            squares.add(square)

        self.play(Create(squares))
        self.wait()

    def pythagoras_tree(self, ratio: float = 1.0, nb_levels: int = 12):
        # Function definition for Pythagoras tree
        alpha1 = np.pi / 4.0
        alpha2 = np.pi / 4.0
        c_1 = np.cos(alpha1) * ratio
        c_2 = np.cos(alpha2) * ratio
        tr_pat = np.array([[0.0, -ratio], [0.0, 0.0]])

        nb_elements = 2 ** (nb_levels + 1) - 1
        pt_arrray = np.zeros((nb_elements, 4))
        pt_arrray[0, :] = [0.0, 0.0, np.pi / 2.0, ratio]

        def mat_rot(angle_rad: float) -> np.ndarray:
            c_a = np.cos(angle_rad)
            s_a = np.sin(angle_rad)
            return np.array([[c_a, -s_a], [s_a, c_a]])

        for i in range(1, nb_elements, 2):
            j = (i + 1) // 2 - 1
            t_m = pt_arrray[j, 3] * mat_rot(pt_arrray[j, 2]) @ tr_pat
            t_x = t_m[0, :] + pt_arrray[j, 0]
            t_y = t_m[1, :] + pt_arrray[j, 1]
            theta1 = (pt_arrray[j, 2] + alpha1) % (2.0 * np.pi)
            theta2 = (pt_arrray[j, 2] + alpha2) % (2.0 * np.pi)
            pt_arrray[i, 0:4] = [t_x[0], t_y[0], theta1, pt_arrray[j, 3] * c_1]
            pt_arrray[i + 1, 0:4] = [t_x[1], t_y[1], theta2, pt_arrray[j, 3] * c_2]

        return pt_arrray

if __name__ == "__main__":
    # Main entry point for Manim script
    PythagorasTree().render()
