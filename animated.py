from manim import *
import math
config.frame_size = (1080,1920)
config.frame_width = 7.5
class Semicircles(MovingCameraScene):
    def construct(self):

      l1 = Line(ORIGIN,color=WHITE,stroke_width=4).set_length(4).set_angle(PI/2).set_z_index(10)
      l1.shift(1.5*DOWN)
      dot = Dot(l1.get_start(),radius=0)
      l2 = Line(dot,color=WHITE,stroke_width=4).set_length(4).set_angle(PI).set_z_index(10)
      self.camera.frame.scale(1).move_to(ORIGIN).shift(0.3*RIGHT)
    
      l2.move_to(dot,2*LEFT).set_z_index(20)
      #dot2 = Dot(l1.get_center()).shift(2*RIGHT)
      radius=2
      sc1 = Arc(radius=radius,angle=PI,color=WHITE,stroke_width=4).shift(1.5*DOWN+0.5*RIGHT).set_z_index(10)
      sc2 = sc1.copy().set_z_index(10)
      sc2.rotate(angle=-PI/2,about_point=l2.get_end()).shift(4*UP)
    
      #self.play(FadeIn(l1),FadeIn(l2),FadeIn(sc1),FadeIn(sc2))
      #self.wait(2)

      da1 = DoubleArrow(l1.get_start(),l1.get_end(), buff=0, tip_length=0.2,max_tip_length_to_length_ratio=0.07, color=WHITE,stroke_width=3).set_z_index(13)
      da1.shift(0.4*LEFT)

      label1 = MathTex("4",color=WHITE,font_size=42).set_z_index(20)
      label1.next_to(da1.get_center()).shift(0.55*LEFT)

      d2 = DoubleArrow(l2.get_start(),l2.get_end(), buff=0, tip_length=0.2,max_tip_length_to_length_ratio=0.07, color=WHITE,stroke_width=3).set_z_index(13)
      d2.shift(0.4*DOWN)
      label2 = label1.copy().move_to(d2.get_center()).shift(0.25*DOWN)
      self.play(AnimationGroup(FadeIn(l1,sc2),FadeIn(l2,sc1),FadeIn(label1,da1,label2,d2),lag_ratio=0.5))
      self.wait(2)
      #fill yellow shaded area
      intersect_point= self.find_intersection(sc1,sc2)
      d1 = Dot(l1.get_center(),radius=0).shift(2*RIGHT).set_z_index(20) 
    
      fill_arc1 = Intersection(sc1,sc2,fill_color='#3DD771',fill_opacity=1,stroke_width=0.3,stroke_opacity=0.2).set_z_index(0)       
      self.wait(1)
      
      #question
      with register_font("C:/Users/manasa.a/manim_projects/learning/fonts/Athletics-Bold.ttf"):
          ques = Text("Area of the shaded region?",t2c = {"[:12]":'#FCF4E4','[12:18]':'#3DD771','[18:26]':'#FCF4E4'},opacity=1,
                      font="Athletics",font_size=32).move_to(l2.get_center()).shift(5*UP+0.2*LEFT)  
      #self.play(FadeIn(ques))
      self.play(AnimationGroup(FadeIn(fill_arc1),FadeIn(ques),lag_ratio=0.5))
      

      self.wait(3)
      self.play(FadeOut(ques))
      self.wait(2)

      #solution
      l3 = Line(d1,intersect_point,color=WHITE,stroke_width=3).set_z_index(20)
      l4 = Line(d1, l2.get_start(),color=WHITE,stroke_width=3).set_z_index(20)
      

     # self.wait(1.3)
      rad = Line(d1, l2.get_center(),color=WHITE,stroke_width=3,stroke_opacity=1).set_z_index(40)
      rlabel = MathTex("2",color=WHITE,font_size=32).set_z_index(40)
      rlabel.next_to(rad.get_center()).shift(0.01*RIGHT)
      #self.play(AnimationGroup(FadeIn(rad),FadeIn(rlabel),lag_ratio=0.5))
      orig = Dot(ORIGIN,color=WHITE)
      #self.add(orig)
      half1=ArcBetweenPoints(start= ORIGIN+0.5*UR,end=ORIGIN+1.5*DL,angle=-PI/2,stroke_color='#3DD771',stroke_width=4).set_z_index(14)
      h2 = ArcBetweenPoints(start= ORIGIN+0.5*UR,end=ORIGIN+1.5*DL,angle=-PI/2,stroke_color=BLACK,stroke_width=5).set_z_index(12)
      #self.play(FadeIn(half1))
      gr1 = VGroup(half1,l3)
      gr1.set_fill(color='#3DD771',opacity=1)
      
      half2 = ArcBetweenPoints(start=ORIGIN+0.5*UR,end=ORIGIN+1.5*DL,angle=PI/2,stroke_width=4,stroke_color='#3DD771').set_z_index(14)
      half3 = ArcBetweenPoints(start=ORIGIN+0.5*UL,end=ORIGIN+1.5*DR,angle=-PI/2,stroke_width=3,stroke_color=WHITE).shift(RIGHT).set_z_index(14)

      gr2 = VGroup(half2,l3)
      gr2.set_fill(color='#3DD771',opacity=1)
      rep_half = VGroup(half3,l4)
      

      
      #self.play(FadeIn(half1,half2))
      #self.add(half1,half2)
      #self.remove(fill_arc1)
      #self.add(h2,l3.copy())
      #self.play(Indicate(gr1,color=None,scale_factor=1),Indicate(gr2,color=None,scale_factor=1))
      #self.play(FadeIn(gr1,gr2))
      tri = Polygon(l2.get_start(),d1.get_center(),l2.get_end(),stroke_color=WHITE).set_z_index(30)
      tri.joint_type=LineJointType.ROUND
      self.play(AnimationGroup(FadeIn(d1,l3,l4),FadeOut(da1,label1),self.camera.frame.animate.scale(0.7).move_to(tri.get_center()),FadeOut(label2,d2),
                                l1.animate.set_stroke(opacity=0.3),l2.animate.set_stroke(color=WHITE),
                                fill_arc1.animate.set_fill(opacity=0.3),sc1.animate.set_stroke(opacity=0.2),sc2.animate.set_stroke(opacity=0.2),lag_ratio=0))
      self.wait(1.5)
      half3.set_stroke(opacity=0.3)
      #self.add(half3)
      
      self.play(AnimationGroup(AnimationGroup(FadeIn(half1),FadeIn(tri),FadeIn(half2),FadeIn(half3),lag_ratio=0),AnimationGroup(FadeOut(fill_arc1)),lag_ratio=0))
      self.wait(1)
      #self.add(tri)
      self.play(Indicate(gr1,color='#DA5107',scale_factor=1),run_time=1.2)
      self.add(h2,l3.copy())
      rep_half.save_state()
      #self.play(AnimationGroup(half3.animate.set_stroke(opacity=1,color='#DA5107'),Indicate(l4,color='#DA5107',opacity=0.5,scale_factor=1),lag_ratio=0))
      rep_half.set_fill(color=BLACK,opacity=1)
      self.play(Indicate(rep_half,color='#DA5107',scale_factor=1))
      rep_half.restore()
      
      #self.remove(half3)
      self.play(Rotate(gr1,angle=PI/2,about_point=d1.get_center()),lag_ratio=0)

      # self.play(gr1.animate.rotate(angle=PI/2,about_point=d1))
      
      #tri.set_fill(color=BLACK)
      
      
      self.remove(half3)
      self.play(AnimationGroup(AnimationGroup(half1.animate.set_z_index(30),half2.animate.set_z_index(30),half1.animate.set_stroke(opacity=1,color=WHITE),
                                half2.animate.set_stroke(opacity=1,color=WHITE),FadeOut(d1),l2.animate.set_stroke(color=WHITE)),AnimationGroup(tri.animate.set_fill(color='#52C8F5',opacity=0.7),FadeOut(l1,sc2)),lag_ratio=0.8))
      #self.play(Indicate(tri,color=None,scale_factor=1))
      #self.play(FadeOut(l1,sc2))
      self.wait(3)
      ans_semi = MathTex("A(", "\phantom{xxx}", ")",font_size=35).next_to(l2, 1.1* DOWN,buff=0.2).shift(LEFT+0.8*RIGHT).shift(0.27*RIGHT+0.1*LEFT).shift(0.5*DOWN)
      minus = MathTex("-",font_size=35).next_to(ans_semi, RIGHT, buff = 0.1)
      ans_tri = MathTex("A(", "\phantom{xxx}", ")",font_size=35).next_to(minus,0.3*RIGHT,buff=0.3)
      equals = MathTex("=",font_size=32).next_to(ans_semi,0.27* LEFT, buff = 0.3)
      ans_fill = MathTex("A(", "\phantom{xxx}", ")",font_size=35).next_to(equals,0.27*LEFT,buff=0.4)




          
      
      #self.play(FadeOut(l1,sc2))
      self.wait(3)      
      sc1_copy = sc1.copy()
      sc1_copy.set_stroke(opacity=1,width=1.5).set_z_index(40)
      
      l2_copy=l2.copy()
      l2_copy.set_stroke(width=1.5)

      half1_copy1=half1.copy()
      half2_copy1=half2.copy()
      half1_copy2 = half1.copy()
      half2_copy2 = half2.copy()
      half1_copy3 = half1.copy().set_stroke(color='#3DD771',width=1.5)
      half2_copy3 = half2.copy().set_stroke(color='#3DD771',width=1.5)
      half1_copy1.set_stroke(color='#3DD771',width=1.5)
      half2_copy1.set_stroke(color='#3DD771',width=1.5)
      half1_copy2.set_stroke(color='#3DD771',width=1.5)
      half2_copy2.set_stroke(color='#3DD771',width=1.5)
      tri_copy = tri.copy()
      tri_copy.set_stroke(width=1.5)
      
      sem_gr = VGroup(sc1_copy,l2_copy,tri_copy,half1_copy3,half2_copy3)
      gr3 = VGroup(sc1_copy,l2_copy)
      gr4 = VGroup(half1_copy2,half2_copy2)
      self.play(FadeIn(ans_fill),FadeIn(equals),self.camera.frame.animate.move_to(l2.get_center()).shift(0.5*DOWN),gr4.animate.scale(0.15).next_to(ans_fill,buff=0.1).shift(0.815*LEFT), run_time=1.5)
      self.play(FadeIn(ans_semi), sem_gr.animate.scale(0.15).next_to(ans_semi, buff = 0.1).shift(0.815*LEFT), run_time=1.5)
      tri_copy2 = tri_copy.copy()
      self.play(FadeIn(minus),FadeIn(ans_tri),tri_copy2.animate.next_to(ans_tri,buff=0.1).shift(0.815*LEFT), run_time=1.5)
      #self.play(Rotate(half1_copy,angle=-PI/2,about_point=half2_copy.get_start()))
      self.wait(2)

      
      
      
      
      new_group = VGroup(sem_gr.copy(),ans_semi.copy())
      new_group2 = VGroup(tri_copy2.copy(),ans_tri.copy())
      new_group3 = VGroup(ans_fill,gr4)

    
      #self.play()
      self.play(new_group.animate.move_to(new_group3).shift(1*DOWN),new_group2.animate.move_to(new_group3).shift(2*DOWN))
     # self.play(new_group.animate.shift(1.3*LEFT+1*DOWN),new_group2.animate.shift(2.8*LEFT+2*DOWN))
      eq_copy = MathTex("=",font_size=32).next_to(equals,3.9*DOWN) 
      eq_copy2 = MathTex("=",font_size=32).next_to(equals,7.85*DOWN)
     # eq_copy =MathTex("=",font_size=35).next_to(new_group,buff=0.2)
      self.play(FadeIn(eq_copy))


      semi_form = MathTex(r'\frac {\pi \times r^2}{2}',color=WHITE,font_size=32).next_to(eq_copy,buff=0.2)
      tri_form = MathTex(r'(\frac{1}{2} \times {b} \times {h})',color=WHITE,font_size=32).next_to(eq_copy2,buff=0.2)
      
      #self.play(FadeIn(semi_form))
      
      #self.play(AnimationGroup(FadeTransform(new_group2,tri_form),minus.animate.shift(0.3*LEFT),equals.animate.shift(0.25*RIGHT),ans_fill.animate.shift(0.3*RIGHT),gr4.animate.shift(0.3*RIGHT),l2.animate.set_stroke(color=WHITE,opacity=1),tri.animate.set_z_index(12),FadeIn(rad,rlabel),lag_ratio=0))
      #self.wait(2)

      semi_area1 = MathTex(r'\frac {\pi \times 2^2}{2}',color=WHITE,font_size=32).next_to(eq_copy,buff=0.2)
    
     # semi_area2 = MathTex(r'\frac {\pi \times 4 }{2}',color=WHITE,font_size=32).next_to(eq_copy,buff=0.2)
      
      semi_area3 = MathTex(r'=','2' ,'\pi',color=WHITE,font_size=32).next_to(semi_area1,buff=0.2)

     
      tri_area1 = MathTex(r'\frac{1}{2}',color=WHITE,font_size=32).next_to(eq_copy2,buff=0.2)
      tri_area3 = MathTex('\\times',color=WHITE,font_size=32).next_to(tri_area1,buff=0.15)
      tri_area4 = MathTex('b',color=WHITE,font_size=32).next_to(tri_area3,buff=0.15)
      tri_area5 = MathTex('\\times',color=WHITE,font_size=32).next_to(tri_area4,buff=0.15)
      tri_area6 = MathTex('h',color=WHITE,font_size=32).next_to(tri_area5,buff=0.15)
      tri_form = VGroup(tri_area1,tri_area3,tri_area4,tri_area5,tri_area6)
      l2_copy2 = l2.copy()
      l2.set_z_index(0)
      l2_copy2.set_stroke(color=WHITE,width=3).set_z_index(50)
      #self.wait(1)
      d2.shift(0.25*UP)
      label2.font_size=32
      label2.shift(0.3*UP)
      d2.set_color(WHITE)
      label2.set_color(WHITE)
      
      

     # self.play(FadeIn(tri_form),FadeIn(l2_copy2,rad,rlabel),label2.animate.set_color(WHITE),d2.animate.set_color(WHITE))
      tri_area7 = MathTex('2',color=WHITE,font_size=32).next_to(tri_area5,buff=0.15)
      tri_area8 = MathTex('4',color=WHITE,font_size=32).next_to(tri_area3,buff=0.15)
      tri_area2 = MathTex('=','4',color=WHITE,font_size=32).next_to(tri_area7,buff=0.2)
      #semi_area3.next_to(minus,3.7*DOWN)
      
     

      self.play(FadeIn(semi_form),FadeIn(rad,rlabel),FadeIn(label2),FadeIn(d2))
      self.play(TransformMatchingTex(semi_form,semi_area1))
      self.wait(0.5)
     
      self.play(FadeIn(semi_area3))
      self.wait(1.5)
      self.play(FadeIn(eq_copy2))
      self.play(FadeIn(tri_form),run_time=1)
      self.wait(1)
      self.play(FadeTransform(tri_area6,tri_area7),FadeTransform(tri_area4,tri_area8))      
      






      self.play(FadeIn(tri_area2))
      self.play(FadeOut(label2,d2,rad,rlabel))
     
      eq2 = equals.copy().next_to(l2.get_center(),3*DOWN)
      ans_fill2 = new_group3.copy()
      ans_fill2.next_to(eq2,buff=0.2).shift(1.7*LEFT)
      #eq2.next_to(ans_fill2,buff=0.2)
     # gr4_copy=gr4.copy().shift(0.815*LEFT)
     # gr4_copy.next_to(ans_fill2,buff=0.2)
      
      #self.play(FadeIn(ans_fill2),FadeIn(eq2),FadeIn(gr4_copy), run_time=1.5)

      f_ans = MathTex(r'2', '\pi', '-', '4',font_size=32,color=WHITE).move_to(minus).shift(0.1*RIGHT)
      self.play(AnimationGroup(equals.animate.shift(0.8*RIGHT),new_group3.animate.shift(0.7*RIGHT),TransformMatchingTex(Group(tri_area2,semi_area3),f_ans),FadeOut(semi_area1,sem_gr,eq_copy,eq_copy2,tri_area7,minus,ans_tri,tri_copy2,new_group,new_group2,tri_area8,tri_area3,tri_area5,tri_area1,new_group2,ans_semi,eq_copy,sc1_copy,l2_copy),lag_ratio=0))
      #self.play(AnimationGroup(AnimationGroup(TransformMatchingTex(Group(tri_area2,semi_area3),f_ans),FadeOut(semi_area2,sem_gr,eq_copy,eq_copy2,tri_area7,tri_area8,tri_area3,tri_area5,tri_area1,new_group2,ans_semi,eq_copy,sc1_copy,l2_copy),lag_ratio=0),lag_ratio=0))
      all_group=VGroup(new_group3,equals,f_ans)
      rect = SurroundingRectangle(all_group,color=YELLOW,buff=0.2)
      self.play(Create(rect))
      self.wait(4)



  

    def find_intersection(self, line1, line2):
        p1, p2 = line1.get_start_and_end()
        p3, p4 = line2.get_start_and_end()

        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        x3, y3 = p3[0], p3[1]
        x4, y4 = p4[0], p4[1]

        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if det == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det
        intersection_x = x1 + t * (x2 - x1)
        intersection_y = y1 + t * (y2 - y1)

        return np.array([intersection_x, intersection_y, 0])

