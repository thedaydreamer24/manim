from manim import *
import math
import datetime
config.frame_size = (1080,1920)
config.frame_width = 7.5

class grids2(MovingCameraScene):
    def construct(self):
      rows = 5
      cols = 5
      grid = VGroup(*[
          VGroup(*[Square(side_length=1, fill_opacity=0.3, stroke_width=3 ,stroke_opacity = 1).move_to((i-rows//2)*RIGHT + (j-cols//2)*UP) for j in range(cols)]) for i in range(rows)
      ]).set_color('#52C8F5').shift(0.6*RIGHT+0.5*DOWN)
      grid.to_edge(ORIGIN)
      self.camera.frame.scale(1).move_to(grid)
      #s2 = Square(side_length=1,stroke_color='#52C8F5',stroke_width=3,stroke_opacity=1,fill_color='#52C8F5',fill_opacity=0.3).set_z_index(10)
      #s2.align_to(grid[0][1]).shift(1.5*UP+0.4*LEFT)
      
      #s3 = s2.copy().shift(4*DOWN).set_z_index(12)
      #self.remove(grid[2][0],grid[3][0],grid[4][0],grid[2][4],grid[3][4],grid[4][4])
      self.play(FadeIn(grid),FadeOut(grid[2][0],grid[3][0],grid[4][0],grid[2][4],grid[3][4],grid[4][4]))
      #d = Dot(grid[1][0].get_corner(UR))
      d2 = DoubleArrow(grid[0][4].get_corner(UL),grid[1][0].get_corner(UR), buff=0, tip_length=0.2,max_tip_length_to_length_ratio=0.07, color=WHITE,stroke_width=3).set_z_index(13)


      label = MathTex("8",color=WHITE,font_size=42).set_z_index(20)
      label.next_to(d2.get_center()).shift(0.2*UP+0.65*LEFT)
      #with register_font("C:/Users/manasa.a/manim_projects/learning/fonts/Athletics-Regular.ttf"):
      ques = Text("Area of the blue region?",t2c = {"[:12]":'#FCF4E4','[12:17]':'#52C8F5','[17:25]':'#FCF4E4'},font="Athletics-Regular",font_size=32).next_to(grid,7*UP)
      self.play(AnimationGroup(FadeIn(d2),FadeIn(label),FadeIn(ques),lag_ratio=0.5))
      self.wait(4)

class grids3(MovingCameraScene):
    def construct(self):
      rows = 5
      cols = 3
      grid = VGroup(*[
          VGroup(*[Square(side_length=1, fill_opacity=0.3, stroke_width=3 ,stroke_opacity = 1).move_to((i-rows//2)*RIGHT + (j-cols//2)*UP) for j in range(cols)]) for i in range(rows)
      ]).set_color('#52C8F5').shift(0.6*RIGHT+0.5*DOWN)
      grid.to_edge(ORIGIN)
      self.camera.frame.scale(1).move_to(grid)
      s2 = Square(side_length=1,stroke_color='#52C8F5',stroke_width=3,stroke_opacity=1,fill_color='#52C8F5',fill_opacity=0.3).set_z_index(10)
      s2.align_to(grid[0][1]).shift(1.5*UP+0.4*LEFT)
      
      s3 = s2.copy().shift(4*DOWN).set_z_index(12)
      self.play(FadeIn(grid,s2,s3))

      self.wait(2)
      line1 = Line(s2.get_vertices()[1],s3.get_vertices()[0],color=RED).set_z_index(0)
      line1.get_length()
      
      d2 = DoubleArrow(s2.get_vertices()[1],s3.get_vertices()[0], buff=0, tip_length=0.2,max_tip_length_to_length_ratio=0.07, color=WHITE,stroke_width=3).set_z_index(13)

      label = MathTex("3",color=WHITE,font_size=42).set_z_index(20)
      label.next_to(d2.get_center()).shift(0.2*UP+0.55*LEFT)
      self.play(AnimationGroup(FadeIn(d2),FadeIn(label),lag_ratio=0.5))
      self.wait(1.5)
      #with register_font("C:/Users/manasa.a/manim_projects/learning/fonts/Athletics-Bold.ttf"):
      ques = Text("Area of the blue region?",t2c = {"[:12]":'#FCF4E4','[12:17]':'#52C8F5','[17:25]':'#FCF4E4'},font="Athletics",font_size=32).next_to(grid,7*UP)
      self.play(FadeIn(ques))
      new_square = Square(side_length=4.1231056256177, color=WHITE, stroke_width=4,stroke_opacity=1).set_z_index(40)
      new_square.rotate(-0.4220208696*PI).align_to(s2.get_vertices()[1],s3.get_vertices()[0])
      new_square.shift(4*DR+RIGHT)
      nv = new_square.get_vertices()
      self.wait(4)
      self.play(FadeOut(ques))
      self.wait(2)
      self.play(FadeIn(new_square), d2.animate.shift(0.2*LEFT),label.animate.shift(0.4*LEFT))
      s1 = VGroup(grid[0][0],grid[0][1],grid[0][2])
      self.wait(4)
      

      gl1 = Line(nv[2],color='#52C8F5',stroke_width=3 ).set_length(4.2492243493112).set_angle(PI).move_to(nv[2]).shift(2.1*RIGHT).set_z_index(0)
      gl2 = Line(s2.get_vertices()[3],color='#52C8F5',stroke_width=3 ).set_length(3.5002748403973).set_angle(PI).move_to(s2.get_vertices()[3]).shift(1.77*RIGHT)
      gl3 = Line(grid[4][1].get_corner(UR),color='#52C8F5',stroke_width=3 ).set_length(0.7511225823996).set_angle(PI).move_to(grid[4][1].get_corner(UR)).shift(0.35*RIGHT)
      gl4 = Line(grid[4][1].get_corner(DR),color='#52C8F5',stroke_width=3 ).set_length(1).set_angle(PI).move_to(grid[4][1].get_corner(DR)).shift(0.5*RIGHT)
      gl5 = Line(s2.get_vertices()[0],color='#52C8F5',stroke_width=3 ).set_length(0.25).set_angle(PI/2).move_to(s2.get_vertices()[0]).shift(0.1*UP)
      gl6 = Line(grid[2][0].get_corner(UR),color='#52C8F5',stroke_width=3 ).set_length(1.5).set_angle(PI/2).move_to(grid[2][0].get_corner(UR)).shift(2.75*UP)
      gl7 = Line(grid[3][0].get_corner(UR),color='#52C8F5',stroke_width=3 ).set_length(1.75).set_angle(PI/2).move_to(grid[3][2].get_corner(UR)).shift(0.89*UP)
      gl8 = Line(grid[4][0].get_corner(UR),color='#52C8F5',stroke_width=3 ).set_length(2).set_angle(PI/2).move_to(grid[4][0].get_corner(UR)).shift(3*UP)
      self.play(AnimationGroup(FadeIn(gl1),FadeIn(gl2),FadeIn(gl3),FadeIn(gl4),FadeIn(gl5),FadeIn(gl6),FadeIn(gl7),FadeIn(gl8),lag_ratio=0,run_time=1.8))
      self.wait(2)

      d2.set_z_index(15)
      pol1 = Polygon(s2.get_vertices()[1],s3.get_vertices()[0],s3.get_vertices()[1],fill_color='#52C8F5',fill_opacity=0.3,stroke_color='#52C8F5',stroke_width=3)
      pol1.joint_type=LineJointType.ROUND


      l1 = Line(grid[0][0].get_corner(UR),color='#52C8F5',stroke_width=3).set_length(0.25).set_angle(PI).move_to(grid[0][0].get_corner(UR)).shift(2*UP+0.12*RIGHT)
      l2 = Line(grid[0][1].get_corner(UR),color='#52C8F5',stroke_width=3).set_length(0.5).set_angle(PI).move_to(grid[0][1].get_corner(UR)).shift(0.24*RIGHT)
      l3 = Line(grid[0][2].get_corner(UR),color='#52C8F5',stroke_width=3).set_length(0.75).set_angle(PI).move_to(grid[0][2].get_corner(UR)).shift(2*DOWN+0.37*RIGHT)

     

      #3grids shifting
      s1.set_z_index(1)
      self.play(Indicate(s1,color='#3DD771',scale_factor=1,run_time=1))

      #dt = 1/30
      frame_rate = self.camera.frame_rate
      self.dt=1/frame_rate
      s1.add_updater(lambda mob,dt : mob.rotate((PI/2)*0.284*dt))
      #s1.add_updater(lambda mob,dt : mob.rotate((PI/2)*dt))
      def shifter(mob,dt):
        mob.shift((0.57*UP+0.859*RIGHT)*dt)
        #mob.shift((2*UP+3*RIGHT)*dt)
      self.play(self.camera.frame.animate.move_to(new_square.get_center()), s1.animate.add_updater(shifter),run_time=1.5)
   
      self.wait(2)
      s1.suspend_updating()
      gr = VGroup(pol1,l1,l2,l3)
      #self.play(Indicate(gr,color='#3DD771',scale_factor=1,run_time=1))
      #self.wait(1)
      pol2 = pol1.copy()
      pol2.set_fill(color=BLACK,opacity=1).set_z_index(10)
      pol2.set_stroke(width=4,color=BLACK,opacity=1)
      pol2.joint_type=LineJointType.ROUND
      self.wait(2)
      pol2.set_z_index(1)
      s2.set_z_index(0)
      gr.set_z_index(20)
      
      self.add(pol2)
      self.play(Indicate(gr,color='#3DD771',scale_factor=1,run_time=1.5))
      self.play(AnimationGroup(Rotate(gr,about_point=s2.get_vertices()[1],angle=PI/2,rate_func=rate_functions.ease_in_sine),run_time=1.5,lag_ratio=0))
      self.wait(4)
      self.play(Indicate(s3,color='#3DD771',scale_factor=1,run_time=2))
      self.wait(2)
      self.play(s3.animate.shift(4*RIGHT+1*UP))
      self.wait(5)
      s3.set_z_index(2)
      
      pol3 = Polygon(s3.get_vertices()[0],s3.get_vertices()[3],new_square.get_vertices()[3],fill_color='#52C8F5',fill_opacity=0.3,stroke_color='#52C8F5')
      pol3.joint_type=LineJointType.ROUND
      l4 = Line(grid[2][1].get_corner(DR),color='#52C8F5',stroke_width=3).set_length(0.25).set_angle(PI/2).move_to(grid[2][1]).shift(1.3488*DOWN+0.5*RIGHT)
      l5 = Line(grid[3][1].get_corner(DR),color='#52C8F5',stroke_width=3).set_length(0.5).set_angle(PI/2).move_to(grid[3][1]).shift(1.25*DOWN+0.5*RIGHT)
      l6 = Line(grid[4][1].get_corner(DR),color='#52C8F5',stroke_width=3).set_length(0.75).set_angle(PI/2).move_to(grid[4][1].get_corner(DR)).shift(0.6*DOWN)

      pol4 = pol3.copy()
      pol4.set_fill(color=BLACK,opacity=1).set_z_index(10)
      pol4.set_stroke(width=4,color=BLACK,opacity=1)

      gr2 = VGroup(pol3,l4,l5,l6)
      self.wait(1)
      #self.play(Indicate(gr2,color='#3DD771',scale_factor=1))
      
      pol4.set_z_index(0)
      s3.set_z_index(0)
      self.add(pol4)
      self.play(Indicate(gr2,color='#3DD771',scale_factor=1,run_time=1.5))
      self.play(AnimationGroup(Rotate(gr2,about_point=s3.get_vertices()[0],angle=-PI/2,rate_func=rate_functions.ease_in_sine),run_time=1.5,lag_ratio=0))

      #self.wait(8)
      self.wait(2)
      pol4.set_z_index(4)
      new_group = VGroup(grid,new_square,s2,s3,gr,gr2,gl1,gl2,gl3,gl4,gl5,gl6,gl7,gl8)
     
      fsq = new_square.copy()
      grid.set_z_index(0)
      pol1.set_z_index(0)
      pol3.set_z_index(0)
      s2.set_z_index(0)
      s3.set_z_index(0)
      fsq.set_z_index(40)

      fsq.set_fill(color='#52C8F5',opacity=0.3)
    
      self.play(FadeOut(new_group),FadeIn(fsq))
      
      self.play(AnimationGroup(AnimationGroup(Rotate(fsq,angle=-0.2449786631)),AnimationGroup(d2.animate.rotate(angle=-0.2449786631).shift(0.5*UP+0.1*LEFT),label.animate.shift(0.5*UP),self.camera.frame.animate.move_to(fsq.get_center())),lag_ratio=0))
     # self.play(d2.animate.align_to(fsq))
      
      sol = MathTex("(side)^2",color=WHITE,font_size=42).move_to(fsq.get_center())
      self.play(FadeIn(sol))
      ans = MathTex("(3)^2",color=WHITE,font_size=42).move_to(fsq.get_center())
      f_ans = MathTex("9",color=WHITE,font_size=42).move_to(fsq.get_center())
      self.play(FadeTransform(sol,ans))
      self.wait(2)
      self.play(FadeTransform(ans,f_ans))
      #self.play(FadeIn(f_ans),ans.animate.shift(0.3*LEFT))
      self.wait(2)

