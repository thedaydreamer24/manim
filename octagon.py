from manim import *

config.background_color=WHITE
scale_factor= 3     
vertices = [np.array([scale_factor*np.cos(angle), scale_factor*np.sin(angle), 0]) for angle in np.linspace(0, 2*np.pi, 9)]
octagon = Polygon(*vertices,color=BLACK)
        

class OctArea(Scene):
    def construct(self):  
        
        octagon.rotate(angle=PI/8).shift(0.5*UP).joint_type=LineJointType.ROUND

        self.play(Create(octagon),run_time=3)
        #self.play(Rotate(,angle=PI/8))

        line1 = Line(octagon.get_vertices()[2], octagon.get_vertices()[5],color=BLACK)
        line2 = Line(octagon.get_vertices()[0], octagon.get_vertices()[4],color=BLACK)
        self.play(Create(line1),run_time=0.5)
        self.play(Create(line2),run_time=0.5)
    
        intersect_point = self.find_intersection(line1,line2)
        dot=Dot(intersect_point,color=BLACK,radius=0.01)
        line3 = Line(dot, octagon.get_vertices()[7],color=BLACK)
        self.wait(1)
        self.play(Create(line3))
        self.wait(1)
        polygon_vertices = [
            line3.get_start(),
            line3.get_end(),
            self.find_intersection(line1,line3),
            line1.get_end(),
            octagon.get_vertices()[5],
            octagon.get_vertices()[6],
            octagon.get_vertices()[7]
        ]
        polygon = Polygon(*polygon_vertices,stroke_width=0,color=BLACK)
        polygon.set_z_index=2
        polygon.joint_type=LineJointType.ROUND
        polygon.set_fill(color='#B03882',opacity=0.5)
        self.play(FadeIn(polygon))
    
        question = Text("What fraction of the octagon is shaded in pink?",
                        t2c = {"[:41]":'#2B2B2B','[42:46]':'#B03882','[46:47]':'#2B2B2B'},font_size=30)
        question.next_to(octagon,1.8*DOWN)
        self.add(question)
        self.wait(5)
        self.play(Uncreate(question),run_time=0.1)
        self.wait(3)
        
            #DashedLine( octagon.get_vertices()[0],octagon.get_vertices()[4],color=BLACK,stroke_width=2),
        diag1 =  DashedLine( octagon.get_vertices()[1],octagon.get_vertices()[5],color=BLACK,stroke_width=2)
        diag2 =  DashedLine( octagon.get_vertices()[2],octagon.get_vertices()[6],color=BLACK,stroke_width=2)
        diag3= DashedLine( octagon.get_vertices()[3],octagon.get_vertices()[7],color=BLACK,stroke_width=2)
        diagonals = VGroup(diag1,diag2,diag3)
          #Line(center,octagon.get_vertices()[5],color=BLACK) 
        

        
        
        diag=AnimationGroup(FadeIn(diag1),FadeIn(diag2),FadeIn(diag3),lag_ratio=1,run_time=0.8)
        self.play(diag)
        self.wait(2)


        A = Dot(intersect_point,radius=0.01,color=BLACK)
        B = Dot(line3.get_end(),radius=0.01,color=BLACK)
        C = Dot(line1.get_end(),radius=0.01,color=BLACK)        
        center=octagon.get_center()
        
        triangle1 =Polygon(A.get_center(),B.get_center(),C.get_center(),color=PURE_RED)
        self.add(A,B,C)
        triangle1.joint_type=LineJointType.ROUND
        self.play(Create(triangle1))
        pline2 = Line(octagon.get_vertices()[5],octagon.get_vertices()[7],color=PURE_RED)  
        self.wait(3)


        
        arrow_1 = Arrow(start=line2.get_end(), end=line2.get_center(), color=BLACK,stroke_width=0.5,max_tip_length_to_length_ratio=0.08)
        arrow_2 = Arrow(start=pline2.get_start(), end=pline2.get_center(), color=BLACK,stroke_width=0.5,max_tip_length_to_length_ratio=0.12)

        self.play(Indicate(line2),Indicate(pline2),color=None,run_time=2)
        self.add(arrow_1,arrow_2)
        
        self.wait()

    
        NewDot = Dot(intersect_point,radius=0.1,color=PURE_RED)
        self.add(NewDot)
        triangle1.add_updater(lambda x:x.become(Polygon(NewDot.get_center(),line3.get_end(),line1.get_end(),color=PURE_RED)))
        self.play(NewDot.animate.move_to(octagon.get_vertices()[4]),run_time=2)
        self.wait(0.3)
        self.play(NewDot.animate.move_to(octagon.get_vertices()[0]),run_time=3)
        self.wait(0.7)

        self.play(NewDot.animate.move_to(octagon.get_center()),run_time=4)
        self.wait(4)
        final_polygon = Polygon(center,
                                octagon.get_vertices()[5],
                                octagon.get_vertices()[6],
                                octagon.get_vertices()[7],color=None,stroke_width=0)
        newline = DashedLine(octagon.get_vertices()[0], octagon.get_vertices()[4],color=BLACK,stroke_width=2)
        
        full_polygon = VGroup(final_polygon,octagon,diagonals)
        groups = AnimationGroup(AnimationGroup(FadeOut(NewDot)),
                                AnimationGroup(FadeIn(final_polygon),FadeOut(polygon),
                                                final_polygon.animate.set_fill(color=PINK,opacity=0.5).set_z_index(0)),
                                AnimationGroup(FadeOut(pline2),
                                            FadeOut(line3),FadeOut(line1),FadeOut(arrow_1),
                                            FadeOut(arrow_2),FadeOut(line2),
                                            FadeIn(newline)),
                                            lag_ratio=.5,run_time=6,rate_function=linear)
        
        self.play(groups)
        self.play(FadeOut(triangle1))
        self.wait(0.7)
       
      
        eq = MathTex(r"\Rightarrow ",color=BLUE)
        eq.next_to(octagon)
        self.play(Write(eq))
        s1 = MathTex(r" \frac{2}{}",color=BLUE)
        s1.next_to(eq)
        
        
        self.play(Indicate(final_polygon),scale_factor=1,color=PINK,run_time=2)
        self.add(s1)
        self.wait(1)
        full_polygon = VGroup(final_polygon,octagon,diagonals)
        full_polygon.save_state()
       
        for sector in range(0,8):
            if sector==5 or sector==6:
                sectors = Polygon(octagon.get_vertices()[sector],octagon.get_vertices()[sector+1],center,color="#9E2F00")
                sectors.joint_type=LineJointType.ROUND
                self.play(Indicate(sectors),scale_factor=1,color="#9E2F00",run_time=0.3)
            
            #sectors.set_fill(color=ORANGE,opacity=0.5)
            
            else:
                sectors = Polygon(octagon.get_vertices()[sector],octagon.get_vertices()[sector+1],center,color="#9E2F00")
                sectors.joint_type=LineJointType.ROUND
                self.play(Indicate(sectors),sectors.animate.set_fill(color="#FF7E3B",opacity=0.5),scale_factor=1,color="#9E2F00",run_time=0.3)
            #self.play(FadeOut(sectors),run_time=0.5)
            #self.remove(sectors)
        s2 = MathTex(r" \frac{2}{8} ",color=BLUE)
        self.add(s1.become(s2).next_to(eq))
        
        #self.add(s1)
        self.wait(1)
        full_polygon.restore()
        new = MathTex(r" =\frac{1}{4}",color=BLUE)
        new.next_to(eq,3*RIGHT)
        self.add(new)
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

