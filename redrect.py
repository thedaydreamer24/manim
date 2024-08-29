from manim import *
import math
config.frame_size = (1080,1920)
config.frame_width = 7.5
class RectArea(MovingCameraScene):
    def construct(self):
        b = 2 * math.pow(3,1/4)
        c = 2 * math.pow(3,3/4)
        redv =[
            np.array([0, 0, 0]),
            np.array([c,  0, 0]),
            np.array([c, b, 0]),
            np.array([0,b, 0])
        ]   
       
        rectangle = Polygon(*redv,stroke_color=PURE_RED,stroke_width=5.5).set_z_index(2)
        self.camera.frame.scale(0.9)
        rectangle.shift(1.7*DOWN+2.25*LEFT)
        self.play(Create(rectangle),run_time=1.5)
        self.wait()

        diagonal = Line(rectangle.get_vertices()[0],rectangle.get_vertices()[2],color=WHITE,stroke_opacity=1).set_z_index(1)

        self.play(Create(diagonal))
        rectangle.save_state()
        self.wait(1)
        a= 2/(math.pow(3,1/4))
        yelv = [
            np.array([0, 0, 0]),
            np.array([a, 0, 0]),
            np.array([a, b, 0]),
            np.array([0, b, 0])
        ]
        
        rect2 = Polygon(*yelv,color=BLACK)
        rect2.align_to(rectangle,LEFT).shift(1.7*DOWN)
        rect2.set_fill(color="#FFCF56",opacity=1)
        self.play(FadeIn(rect2))
        

        rect3 = rect2.copy()
        rect3.set_fill(color=PURPLE,opacity=1).stroke_color=PURPLE
        rect3.rotate(PI/6+PI/2)    
        rect3.align_to(diagonal.get_start())
        rect3.shift(1.8045*UR+0.48*DOWN+0.47*RIGHT)
        self.play(FadeIn(rect3))
        self.wait(1)
       
        area_num = Tex("4",color=BLACK,font_size=40).set_z_index(10)
        area_num.move_to(rect3.get_center()).shift(0.3*DOWN+0.1*LEFT)
        area_num2 = area_num.copy().move_to(rect2.get_center())
        self.play(FadeIn(area_num),FadeIn(area_num2),run_time=1)
        self.wait(1)
        
        #with register_font("C:/Users/manasa.a/manim_projects/learning/fonts/Athletic.ttf"):
        ques = Text("Area of the red rectangle?", t2c = {"[:12]":'#FCF4E4','[12:16]':PURE_RED,'[17:27]':'#FCF4E4'},font_size=30,font="Athletic.ttf")
        ques.next_to(rectangle,8*UP)
        

        self.play(AnimationGroup(FadeIn(ques),Circumscribe(rectangle,color='#F6F6F6',time_width=2.5),lag_ratio=1.5))
        self.wait(4)
        
        r1 = rectangle.get_vertices()
        r2 = rect2.get_vertices()
        r3 = rect3.get_vertices()
        r3p1 = Polygon(r3[0],r3[2],r3[3],fill_color=BLACK,fill_opacity=1)
        r3p2 = Polygon(r3[0],r3[1],r3[2],fill_color=BLACK,stroke_width=4,color=BLACK,stroke_opacity=1,fill_opacity=1)
        newline = Line(r2[1],r2[2],color=None,stroke_width=0).set_z_index(0)
        intersect_point= self.find_intersection(diagonal,newline)
        new_polygon = Polygon(r2[0],r2[1],intersect_point,stroke_color="#F6F6F6",fill_color="#FFCF56",fill_opacity=1,stroke_opacity=1).set_z_index(5)
        new_polygon.joint_type=LineJointType.ROUND
       # self.play(Indicate(new_polygon))
        pol_copy= new_polygon.copy()
        pol_copy.set_fill(color=BLACK,opacity=4).set_z_index(4)
        r2p1 = Polygon(r2[0],intersect_point,r2[2],r2[3],fill_color=BLACK,stroke_width=0,fill_opacity=1)

       # pol2 = Polygon(rect3.get_vertices()[2],intersect_point,rect3.get_vertices()[3],fill_color="#FFCF56",fill_opacity=1,stroke_color="#F6F6F6")
        pol2 = Polygon(r3[2],intersect_point,r3[3],stroke_color="#F6F6F6",stroke_opacity=1).set_z_index(8)
        pol2.joint_type=LineJointType.ROUND
        pol3 = Polygon(rect3.get_vertices()[0],rectangle.get_vertices()[3],rectangle.get_vertices()[0],color="#F6F6F6",stroke_width=5.5).set_z_index(20)

        line2 = Line(r3p1.get_vertices()[0],r3p1.get_vertices()[1],color="#F6F6F6",stroke_width=5.6).set_z_index(7)
       # self.play(Rotate(new_polygon,axis=[2,-1.15,0],about_point=new_polygon.get_corner(UR),angle=PI),run_time=2)
        self.camera.frame.save_state()
        #self.play(self.camera.frame.animate.scale(0.7).move_to(intersect_point),FadeOut(ques))
        self.wait(2)
        g1 = AnimationGroup(AnimationGroup(self.camera.frame.animate.scale(0.6).move_to(intersect_point),FadeOut(ques),run_time=2),AnimationGroup(rectangle.animate.set_stroke(opacity=0.3,color=PURE_RED),diagonal.animate.set_stroke(opacity=0.3,color=WHITE),
                                           rect2.animate.set_fill(opacity=0.3,color="#FFCF56"),
                                         run_time=1,lag_ratio=0),
                             AnimationGroup(FadeIn(new_polygon),FadeIn(pol2),rect3.animate.set_stroke(opacity=0.1,color=PURPLE).set_fill(color=PURPLE,opacity=0.3),run_time=1.5,lag_ratio=0),lag_ratio=0)
        new_polygon.set_stroke(width=3)
        self.wait(2)


        #explanation
        sline = Line(r2[0],r1[2],color=WHITE,stroke_width=0).set_z_index(10)
        sline2 = Line(intersect_point,r2[1],color=BLACK,stroke_width=6).set_z_index(9)
        
        nline1 = Line(intersect_point,r2[2])
        nline2 = Line(intersect_point,r3[3])
        nline3 = Line(r2[0],intersect_point)
        nline4 = Line(r3[3],r3[2])
        nline5 = Line(r2[0],r2[1])
        ang1 = Angle(nline2,nline1,radius=0.2).set_z_index(20)
        ang2 = Angle(nline3,sline2,radius=0.2,quadrant=(-1,1)).set_z_index(20)
        rang1 = RightAngle(nline2,nline4,length=0.2,quadrant=(-1,1)).set_z_index(20)
        rang2 = RightAngle(sline2,nline5,length=0.2,quadrant=(-1,-1)).set_z_index(20)


        eq_symbol1 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE,stroke_width=3)
        eq_symbol2 = Arrow(max_tip_length_to_length_ratio=0, color = WHITE,stroke_width=3).next_to(eq_symbol1, DOWN, buff = 0.7)
        parallel_symbol1 = VGroup(eq_symbol1, eq_symbol2).scale(0.1)
        symbol1 = parallel_symbol1.copy().rotate(PI/2).move_to(nline5.get_center()).set_z_index(20)
        symbol2= parallel_symbol1.copy().rotate(PI/6).move_to(nline4.get_center()).set_z_index(20)

        scopy=symbol1.copy()
        rang_copy=rang2.copy()
        ang_copy= ang2.copy()




        trigp = VGroup(scopy,rang_copy,new_polygon,ang_copy)
       # trigp = VGroup(symbol1,rang2,new_polygon,ang2)



        group = AnimationGroup(       
        AnimationGroup(FadeIn(pol_copy),Rotate(trigp,axis=[2,-1.15,0],about_point=new_polygon.get_corner(UR),angle=PI),run_time=4,lag_ratio=0.5),
        lag_ratio=1,run_time=4)
        self.play(g1)
        self.wait(1.5)
        self.play(AnimationGroup(AnimationGroup(GrowFromPoint(ang1,intersect_point),GrowFromPoint(ang2,intersect_point),GrowFromPoint(rang1,r3[3]),GrowFromPoint(rang2,r2[1])),AnimationGroup(FadeIn(symbol1,symbol2)),lag_ratio=1,run_time=2))

       # self.play(new_polygon.animate.set_fill(color="#FFCF56",opacity=1))
        self.play(group)
        self.wait(0.5)
       # self.play(self.camera.frame.animate.restore(),FadeIn(ques))
        r2p1.set_stroke(color="#FFCF56")
        r3p1.set_stroke(color="#FFCF56",width=0)
    
        area_num2.set_z_index(10)
        fpol = Polygon(r3[2],r3[3],r1[0],r1[3],color="#FFCF56",fill_opacity=1,fill_color="#FFCF56")
        r2p1.set_fill(color="#FFCF56",opacity=1)
        r3p1.set_fill(color=PURPLE,opacity=1)
       
      
        self.wait(2.2)
        
        pol2.set_z_index(2)
        gr2 = AnimationGroup(AnimationGroup(rectangle.animate.set_stroke(color=PURE_RED,opacity=1),diagonal.animate.set_stroke(color=WHITE,opacity=1),                            
                            FadeOut(pol2),FadeIn(sline2),lag_ratio=0),
                AnimationGroup(FadeIn(fpol),rect3.animate.set_fill(color=PURPLE,opacity=1),run_time=2,lag_ratio=0),
                AnimationGroup(FadeOut(ang1,ang2,rang1,rang2,symbol1,symbol2,scopy,rang_copy,ang_copy),run_time=1,lag_ratio=0),
                AnimationGroup(self.camera.frame.animate.restore(),FadeIn(ques),Indicate(area_num2,color=None,scale_factor=1),Indicate(area_num,color=None,scale_factor=1),lag_ratio=0,run_time=1.5),
                        
                run_time=2,lag_ratio=0)
        new_polygon.set_z_index(0)
        sline.set_z_index(3)
        rectangle.set_z_index(15)
        diagonal.set_z_index(14)
        gr3 = AnimationGroup(rectangle.animate.set_stroke(opacity=1,color=PURE_RED),diagonal.animate.set_stroke(color=WHITE,opacity=1),
                             Indicate(rectangle,scale_factor=1,color=None),Indicate(diagonal,color=None,scale_factor=1),lag_ratio=0)
        self.play(gr2)
        self.play(gr3)
        self.wait(1.5)
        line2.set_z_index(50)
        #rectangle.set_z_index(3)
       
        self.play(Indicate(line2,color="#F6F6F6",scale_factor=1.15),run_time=2)
        self.wait(1.5)
        area2 = area_num.copy()

        n1 = Tex("2",color=BLACK, font_size = 40).next_to(area_num,2*UP+0.5*RIGHT)
        #n2 = n1.copy().move_to(r3p1.get_center())
        n2 = n1.copy().next_to(area_num,0.001*LEFT+0.016*DOWN)

        self.play(FadeTransform(area_num,n1),FadeTransform(area2,n2))

        self.wait(2)
       
        n2.set_z_index(35)
        r3p1.joint_type=LineJointType.ROUND



        #self.add(r3p1) #new rect
        self.play(FadeIn(r3p2),FadeOut(line2)) #don't fade out rect3, add a outer black polygon
        pol3.joint_type= LineJointType.ROUND
        diagonal.set_z_index(5)
        self.play(Indicate(pol3,color=None,scale_factor=1.1))
        pol3.set_z_index(45)

        n3 = MathTex("4","+","2",color=BLACK,font_size = 40).next_to(pol3.get_center(),0.000001*UR+0.5*LEFT+1.2*UP).set_z_index(10)
        n4 = Text(" ").next_to(n1)
        self.play(TransformMatchingTex(Group(area_num2,n2),n3))
        

        new = Tex("6",color=BLACK,font_size=40).shift(n3.get_center()).set_z_index(30)
        self.play(FadeTransform(n3,new))
        
        pol4 = Polygon(rect3.get_vertices()[0],rectangle.get_vertices()[0],rectangle.get_vertices()[1],color="#F6F6F6",stroke_width=5.5).set_z_index(25)
        pol4.joint_type= LineJointType.ROUND
        self.play(Indicate(pol4,color=None,scale_factor=1.1))
      
        n6 = MathTex("6",color=WHITE, font_size = 40).next_to(pol4.get_center(),DOWN+1.8*RIGHT)
        eq1 = MathTex("6","+","6",color=WHITE,font_size=40,stroke_opacity=1).next_to(rectangle.get_center()).set_z_index(65)
        eq1.shift(0.8*LEFT)
        self.play(FadeIn(n6))
        self.wait(2)
        #self.play(rectangle.animate.set_stroke(color=PURE_RED,width=5),rectangle.animate.set_z_index(30))
        new.set_z_index(20)
        #self.remove(rect2,rect3,pol2,new_polygon,pol3,pol4,diagonal,sline,r3p1,pol_copy,r2p1,fpol).run_time=2
        
       
        rect3.set_z_index(0)
        #r3p1.set_fill(color=None,opacity=0.5).set_z_index(0)
        copyrect = rectangle.copy()
        copyrect.set_fill(color=BLACK,opacity=1).set_z_index(60)
        copy2 = copyrect.copy()
        copy2.set_fill(color='#FF7E3B',opacity=0.5).set_z_index(61)
        new.set_z_index(62)
        n6.set_z_index(62)
    
        g3 = AnimationGroup(AnimationGroup(FadeIn(copyrect,copy2)),AnimationGroup(TransformMatchingTex(Group(new,n6),eq1)),lag_ratio=0,run_time=1.5)
        self.play(g3)


        self.wait(1)        
        n7 = MathTex("12",color=WHITE,font_size=40).move_to(rectangle.get_center()).set_z_index(65)  
        self.play(FadeTransform(eq1,n7))

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
