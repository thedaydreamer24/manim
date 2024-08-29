from manim import *

import math

#this one works, is useful for the 2nd part
class ShadedArea2(Scene):

    
    def construct(self):
        col_sq=ORANGE;      #color of the square
        side = 5
        sq_vertices = np.array([np.array([0.5*side,0,0]),np.array([0,0.5*side,0]),
        np.array([-0.5*side,0,0]),np.array([0,-0.5*side,0])]) #vertices of rotated square
        sq_center = np.array([0,0,0])                       #center of square
        circ_centers=np.divide(sq_vertices,2)               #centers of circles
        sq = Polygon(*sq_vertices)                          #the square
        sq.set_fill(ORANGE,opacity=0.45)
        line=Line(np.array([0.5*side,0,0]),np.array([0,0.5*side,0]))

        b1 = Brace(line,direction=line.copy().rotate(-PI / 2).get_unit_vector())
        b1text = b1.get_tex(r"1")
        
        d1=Line(*(sq_vertices[i] for i in [0,2]),color=WHITE,stroke_width=DEFAULT_STROKE_WIDTH/2) #first diagonal hozizontal --
        d2=Line(*(sq_vertices[i] for i in [1,3]),color=WHITE,stroke_width=DEFAULT_STROKE_WIDTH/2) #second diagonal vertical ||
        diags=VGroup(d1,d2)
        diags.set_z_index(1)
        
        self.play(DrawBorderThenFill(sq),run_time=2)     #Draw and fill the square
        self.play(FadeIn(b1,b1text))
        self.wait()
        
        #self.play(sq.animate.set_fill(color=col_sq,opacity=0.45))              #color it col_sq) #DONT COLOR NOW
        sq_side=MathTex("1",font_size=DEFAULT_FONT_SIZE*1.5)                                                    #show side length
        sq_side.next_to(np.array([0.25*side,0.25*side,0]),UP+RIGHT)                 #NOT NEEDED RIGHT NOW
        """ self.play(Write(sq_side))
        self.wait()
        self.play(Unwrite(sq_side)) """

        self.play(Create(diags))            #show the diagonals
        self.wait()

        temp_semicircles=VGroup()
        mid_dots=VGroup()

        for ind_v, v in enumerate(sq_vertices):
            curr_circ_center=circ_centers[ind_v]        #current circle's center
            start_angles=[0,PI/2,-PI,3*PI / 2]          #angles for the annuluses to create semi-circles which were tweaked
            curr_rad=math.dist(curr_circ_center,v)      #current circle's radius
            d=Dot(curr_circ_center,radius=1.5*DEFAULT_SMALL_DOT_RADIUS)     #circle center represented as a dot
            d.set_color(DARK_BLUE)
            d.set_z_index(4)
            mid_dots.add(d)
        
        self.play(FadeIn(*mid_dots))
        new_temp_arcs=VGroup()
        
        for ind_v, v in enumerate(sq_vertices):
            curr_circ_center=circ_centers[ind_v]        #current circle's center
            start_angles=[0,PI/2,-PI,3*PI / 2]          #angles for the annuluses to create semi-circles which were tweaked
            curr_rad=math.dist(curr_circ_center,v)      #current circle's radius
            #d=mid_dots(ind_v)
            #mid_dots.add(d)
            factor=side/35;
            """ new_vec=(np.append(np.flip(np.sign(curr_circ_center[0:2])),0))*factor #for the mid point indication

            col_cong_mark=BLACK
            cong_mark1=Line(new_vec,-new_vec,color=col_cong_mark)
            cong_mark1.set_z_index(3)
            cong_mark1.set_opacity(0.75)
            cong_mark1.shift(curr_circ_center/2)
            cong_mark2=Line(new_vec,-new_vec,color=col_cong_mark)
            cong_mark2.set_z_index(3)
            cong_mark2.set_opacity(0.75)
            cong_mark2.shift(curr_circ_center*3/2) """

            """ if (ind_v==0):
                self.add(cong_mark1,cong_mark2)
                self.play(FadeIn(d))         #show the current circle's center
                self.wait() """
            #temp_semicircle=AnnularSector(inner_radius=0, outer_radius=curr_rad, angle=PI,start_angle=start_angles[ind_v],
            #stroke_color=WHITE,stroke_width=5).move_arc_center_to(curr_circ_center) #semi-circle to be created

            temp_semicircle=Arc(radius=curr_rad,angle=PI,arc_center=curr_circ_center)
            new_temp_arc=Arc(radius=curr_rad,angle=PI/2,start_angle=start_angles[ind_v]+PI/2,arc_center=curr_circ_center)
            new_temp_arcs.add(new_temp_arc)
            #self.play(Write(new_temp_arc))
            temp_semicircle.rotate(angle=ind_v*PI/2,about_point=curr_circ_center)
            temp_semicircle.set_opacity(0.5)
            temp_semicircles.add(temp_semicircle)
            col_orig=temp_semicircle.get_fill_color()
            opacity_original=temp_semicircle.get_fill_opacity()
            #temp_circle=Circle(radius=curr_rad).move_to(curr_circ_center)    # add the circle
            """ if (ind_v==0):
                self.play(Write(temp_semicircle))            
                self.play(FadeOut(d,cong_mark1,cong_mark2))                         #remove the semicircle
            self.wait() """
        self.wait(2)
        self.play(FadeOut(b1,b1text))
        self.play(DrawBorderThenFill(temp_semicircles),run_time=5) #this looks so good
        self.wait()
        self.play(FadeOut(mid_dots))
        new_temp_arcs.set_fill(opacity=0)
        new_temp_arcs.set_stroke(opacity=temp_semicircle.get_stroke_opacity())            

        orange_ts=VGroup() #orange triangles
        white_ts=VGroup() #white triangles

        other_endp=np.array([np.array([0.25*side,-0.25*side,0]),np.array([0.25*side,0.25*side,0]),np.array([-0.25*side,0.25*side,0]),np.array([-0.25*side,-0.25*side,0])])
        
        """ lines_temp=VGroup() 
        for i,j in zip(sq_vertices,other_endp):
            lines_temp.add(Line(i,j))
        #self.play(Write(lines_temp)) """

        orange_parts_of_square=VGroup()
        for ind_t, orange_t in enumerate(temp_semicircles):     #for each semi-circle
            triangle_t3=Polygon(sq_center,midpoint(sq_vertices[np.mod(ind_t+1,4)],sq_vertices[np.mod(ind_t,4)]),sq_vertices[np.mod(ind_t+1,4)])
            #triangle_t3.set_fill(RED)
            #self.add(triangle_t3)
            orange_part_here=Intersection(triangle_t3,Difference(sq,Union(*temp_semicircles)))
            orange_part_here.set_fill(col_sq,opacity=0.45)
            orange_part_here.set_stroke(opacity=0)
            orange_parts_of_square.add(orange_part_here)

        for ind_t, temp in enumerate(temp_semicircles):     #for each semi-circle
            #sq.set_stroke(opacity=0)                       #don't touch square
            orange_t = Difference(temp,sq)                  #orange_t is the part of the semi-circle outside the square
            orange_t.set_z_index(3)
            orange_t.set_fill(col_sq,opacity=0.45)          #fill them same as the square
            orange_t.set_stroke(temp_semicircle.get_stroke_color(),temp_semicircle.get_stroke_width(),opacity=0.45)  
            white_sq = Intersection(temp,sq)                #partof the semi-circle that's inside the square
            white_sq.set_stroke(temp_semicircle.get_stroke_color(),temp_semicircle.get_stroke_width(),opacity=0)
            
            
            #self.play(FadeOut(temp),white_sq.animate.set_fill(WHITE,opacity=0.5),FadeIn(orange_t),run_time=2)
            orange_ts.add(orange_t)
            white_ts.add(white_sq)
            #FadeOut the temp circle, FadeIn the Orange part
            #self.wait()
        orange_part_of_square = Difference(sq,Union(*temp_semicircles))
        orange_part_of_square.set_fill(col_sq,opacity=0.45)
        orange_part_of_square.set_stroke(opacity=0)
        self.add(new_temp_arcs)
        self.play(FadeOut(temp_semicircles),white_ts.animate.set_fill(WHITE,opacity=0.5),FadeIn(orange_ts),run_time=2)
        #self.play(FadeOut(temp_semicircles),FadeIn(orange_ts),run_time=2)
        self.wait(5)
        
        triangle_ts=VGroup()
        other_triangle_ts=VGroup()
        triangle_ts2=VGroup()


        """ other_triangle_ts2=VGroup() #new VGroup of white triangles
        for ind_t, orange_t in enumerate(orange_ts):
            other_triangle_t2=Polygon(sq_center,midpoint(sq_vertices[np.mod(ind_t+1,4)],sq_vertices[np.mod(ind_t,4)]),sq_vertices[np.mod(ind_t,4)],color=WHITE)
            other_triangle_t2.set_fill(color=WHITE,opacity=0.45)
            other_triangle_ts2.add(other_triangle_t2) """
        

        sq.set_fill(opacity=0) #remove orange of square
        #self.add(Text("Now"))
        white_ts.set_z_index(2)
        white_ts.set_fill(color=col_orig)
        white_ts.set_opacity(opacity_original)
        white_ts.set_stroke(opacity=0)

        white_ts2 = white_ts.copy()
        white_ts2.set_fill(color=ORANGE)
        white_ts2.set_stroke(opacity=0)
        white_ts2.set_opacity(0.5)
        white_ts2.set_z_index(0)
        self.add(white_ts2)
        self.remove(new_temp_arcs)
        
        self.add(*orange_parts_of_square)       #adddd only certain orange parts (required later)

        self.wait(7)
        other_orange_ts=VGroup()
        other_other_triangle_t2s=VGroup()

        for ind_t, orange_t in enumerate(orange_ts):     #for each semi-circle
        
            

            new_orange_t = orange_ts[0].copy().rotate(PI/2,about_point=circ_centers[0]) #Rotate(orange_ts[0],angle=PI/2,about_point=circ_centers[0])
            #dashed_new_orange_t=DashedVMobject(new_orange_t,num_dashes=12)
            #dashed_new_orange_t.set_stroke(BLACK)
            #dashed_new_orange_t.set_stroke(WHITE,temp_semicircle.get_stroke_width())
            #sq.set_fill()

            if ind_t==0:
                pt = np.array([0.25*side,0.25*side,0]) #midpoint
                line1=Line(pt,ORIGIN,color=DARK_BLUE)
                line2=Line(np.array([0.25*side,0.25*side,0]),np.array([0.5*side,0,0]),color=DARK_BLUE)
                line1.set_z_index(4)
                line2.set_z_index(4)
                #temp_line = Line(pt+2*UP,pt+2*DOWN,color=BLACK)
                #temp_line.set_stroke(opacity=0.75)
                
                #self.play(FadeIn(line1,line2)
                #self.wait()
                new_orange_t.set_fill(color=WHITE,opacity=0.45)
                new_orange_t.set_stroke(opacity=0)
                self.play(Indicate(line1,color=None))
                self.play(Indicate(line2,color=None))
                self.wait()
                self.play(Indicate(new_orange_t,color=None))
                self.remove(new_orange_t)
                self.play(Indicate(orange_t,color=None))
                self.wait()
                self.play(Rotate(orange_t,angle=PI/2),about_point=circ_centers[ind_t])
                
                
                
                
            if ind_t>0:
                self.play(Rotate(orange_t,angle=PI/2),about_point=circ_centers[ind_t])
            #self.play(orange_t.animate.shift(np.array([-side/4,side/4,0])))
            
            triangle_t=Polygon(sq_center,midpoint(sq_vertices[np.mod(ind_t+1,4)],sq_vertices[np.mod(ind_t,4)]),sq_vertices[np.mod(ind_t+1,4)],color=ORANGE)
            
            triangle_t.set_fill(col_sq,opacity=0.45)
            orange_parts_of_square[np.mod(ind_t,4)].set_fill(opacity=0)

            triangle_t.set_stroke(sq.get_stroke_color(),temp_semicircle.get_stroke_width())
            triangle_t.set_z_index(3)

            other_triangle_t=Polygon(sq_center,midpoint(sq_vertices[np.mod(ind_t+1,4)],sq_vertices[np.mod(ind_t,4)]),sq_vertices[np.mod(ind_t,4)],color=WHITE)
            other_triangle_t.set_fill(color=WHITE,opacity=0.45)
            other_triangle_ts.add(other_triangle_t)
            
            #new_part=Polygon(sq_center,midpoint(sq_vertices[np.mod(ind_t,4)],sq_vertices[np.mod(ind_t-1,4)]),sq_vertices[np.mod(ind_t,4)],color=ORANGE)
            

            if(ind_t==0):
                self.remove(white_ts2[ind_t])
                other_triangle_t.set_stroke(opacity=0)
                other_triangle_t2=other_triangle_t.copy()
                other_triangle_t2.set_fill(ORANGE,opacity=0.45)
                other_other_triangle_t2s.add(other_triangle_t2)
                self.add(other_triangle_t2)
                triangle_t.set_stroke(opacity=0)
                self.add(triangle_t)
                self.remove(white_ts[ind_t])
                self.add(other_triangle_t)
                self.remove(new_orange_t)
                self.play(FadeOut(orange_t))
                self.play(FadeOut(line1,line2))
            else:
                triangle_t.set_stroke(opacity=0)
                other_triangle_t.set_stroke(opacity=0)
                other_triangle_t2=other_triangle_t.copy()
                other_triangle_t2.set_fill(ORANGE,opacity=0.45)
                other_other_triangle_t2s.add(other_triangle_t2)
                self.add(other_triangle_t2)
                self.add(triangle_t)

                self.remove(white_ts[ind_t])
                self.add(other_triangle_t)
                self.remove(white_ts2[ind_t])
                self.play(FadeOut(orange_t))
                #self.play(FadeOut(line1,line2))

            triangle_ts.add(triangle_t)             # add this triangle to the group
            
            if(ind_t==0): self.wait(3)

        #triangle_ts.set_fill(opacity=0.45)
        self.wait(3)
        self.play(Indicate(triangle_ts,color=None,scale_factor=1.2))
        self.wait()
        self.play(Indicate(other_triangle_ts,color=None,scale_factor=1.2))
        self.wait()
        
        line=Line(np.array([0.5*side,0,0]),np.array([0,0.5*side,0]))

        b1 = Brace(line,direction=line.copy().rotate(-PI / 2).get_unit_vector())
        b1text = b1.get_tex(r"1")

        areatxt=MathTex(r"\text{Area}=",r"\frac{1}{2}\times 1^2").next_to(np.array([0.25*side,-0.45*side,0]))
        areatxt[0].set_color("#FB9224")
        
        #areatxt.next_to(sq,RIGHT)
        #areatxt2.next_to(sq,RIGHT)
        texts=VGroup()
        #texts.add(sq_side)
        texts.add(areatxt)
        
        self.play(FadeIn(b1,b1text))
        self.wait(2)
        self.play(Write(texts))
        self.wait()
        newtext=MathTex(r"0.5")
        self.play(ReplacementTransform(areatxt[1],newtext.next_to(areatxt[0],RIGHT)),FadeOut(b1,b1text))
        self.wait(10)

        self.play(FadeOut(sq,triangle_ts,other_triangle_ts,d1,d2,texts,newtext,other_other_triangle_t2s))
        self.wait()
        