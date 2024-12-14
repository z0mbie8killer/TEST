"""
Author: Cezar Hernandez
Date created: 12/1/2024
Assignment: Module 6 project status report 2
Description: this script uses breezypythongui package to access different things in the tkinter
module. I created a class called My_Frame(EasyFrame), this class builds the window, and
creates the rectangles. I then made a class called My_Rectangle. This class draws any
rectangles you want, but still needs all the arguments in the drawRectangle() in order to work.
I made this class to disable, and enable any rectangles you want. As well as, move them via the x, and y axis.
You can see more in the comments in My_Frame() to see whats going on. I then created 3 other classes called
My_Dialogbox_move_rects(EasyDialog), ,My_Dialogbox_area_setup(EasyDialog) and My_Dialogbox_enable_disable(EasyDialog),
each of these dialogboxes create a new window, and do different things. see the comments on each class to see whats going on


GIT LINK: https://github.com/z0mbie8killer/TEST.git
"""
from tkinter import PhotoImage
from breezypythongui import EasyFrame, EasyDialog,EasyRadiobuttonGroup
#this is my class for drawing rectangles, and enabling/disabling them. I plan to add more later
class My_Rectangle:
    def __init__(self, canvas, x1,y1,x2,y2,out_line,fil): #gets itself, and all the values  for the rectangle
        self.canvas = canvas #see My_Frame() self.rect_1 to see whats being inputted into this
        self.rect_x1 = x1 #the first x value to drawing the rectangle
        self.rect_x2= x2#the second x value to drawing the rectangle
        self.rect_y1 = y1#the first y value to drawing the rectangle
        self.rect_y2 = y2#the second y value to drawing the rectangle
        self.rect_out_line =out_line #the outline of the rectangle
        self.rect_fill = fil#the fill of the rectangle

        self.is_enabled = True #the rectangle can be seen by the user, set to true to see it right after
        #you create the rectangle
        self.rect_id = None #this is so you can draw the rectangle using self.canvas.drawRectangle
        #it's set to none, to let tkinter know that there isn't any rectangle being drawn yet
        self.draw_rect() #draws the rectangle

    #draws the rectangle
    def draw_rect(self):
        if self.rect_id is None: #if there is no rectangle drawn, draw the rectangle
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1 ,self.rect_y1 , self.rect_x2,self.rect_y2, outline=self.rect_out_line,fill=self.rect_fill)

    #enables the rectangle
    def enable_rect(self):
        if self.is_enabled == False: #if you can't see the rectangle, set it to true so you can see it
            self.rect_id = None #get rid of the old rectangle, you no longer need it 
            self.is_enabled = True #the rectangle can be seen by the user
            self.draw_rect()#redraws the rectangle, that was made before

    #disables the rectangle
    def disable_rect(self):
        if self.is_enabled == True: #if the rectangle can be seen, delete it, and create a new 1
            self.canvas.delete(self.rect_id)#deletes old rectangle
            self.rect_id = None#get rid of the old rectangle, you no longer need it 
            self.is_enabled = False#the rectangle is disabled, can't be seen by the user
            #re-draws the rectangle with the same varaibles, but without the fill and outline
            #this makes it so you can't see the rectangle
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1 ,self.rect_y1 , self.rect_x2,self.rect_y2, outline="",fill="")

    #creates a new rectangle, and draws it by adding new_x to both self.rect_x1, and self.rect_x2
    def move_x(self,new_x):
        if self.is_enabled == True:
            self.canvas.delete(self.rect_id)
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1+new_x,self.rect_y1 , self.rect_x2+new_x,self.rect_y2, outline=self.rect_out_line,fill=self.rect_fill)
            
   #creates a new rectangle, and draws it by adding new_y to both self.rect_y1, and self.rect_y2         
    def move_y(self,new_y):
        if self.is_enabled == True:
            self.canvas.delete(self.rect_id)
            
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1 ,self.rect_y1+new_y, self.rect_x2,self.rect_y2+new_y, outline=self.rect_out_line,fill=self.rect_fill)

    
        
class My_Frame(EasyFrame): #the frame or window to hold all my rectangles
    def __init__(self):
        #when drawing shapes, remember it's based of pixels, not the grid system.
        #the first x is the starting point from 0, the second x is the ending point. You +/- to get the shape
        #you want
         #(x1-x2), (y1-y2) = slope the max is 500, if it's greater then 500, divide it by 500, if it's equal, divide it by 2

        #this sets the max, min boundries 
        self.mydraw_window_x = 550
        self.mydraw_window_y =400
        self.x=EasyFrame.__init__(self,title="My Final Project", width= 600, height=500) #sets the window
        self.canva = self.addCanvas(width = self.mydraw_window_x, height = self.mydraw_window_y,row=0,columnspan=4,background="black") #sets the draw area
    
        #these are all the rectangles drawn, they are apart of the My_Rectangle() class
        self.yard_rect = My_Rectangle(self.canva,25,25,self.mydraw_window_x,self.mydraw_window_y-50, "black","green")
        self.house_rect = My_Rectangle(self.canva,325,50,self.mydraw_window_x-50,self.mydraw_window_y-150, "black","brown")
        self.driveway_rect = My_Rectangle(self.canva,250,50,self.mydraw_window_x-225,self.mydraw_window_y-50, "black","blue")
        self.garage_rect = My_Rectangle(self.canva,250,50,self.mydraw_window_x-225,self.mydraw_window_y-250, "black","orange")

        #adds labels for each float field. Each float field is given a name
        self.addLabel(text="Yard area",row=1,column=0)
        self.yard_area_output=self.addFloatField(0,row=1,column=1,width=20,state="disabled")
        self.addLabel(text="House area",row=1,column=2)
        self.house_area_output=self.addFloatField(0,row=1,column=3,width=20,state="disabled")

        self.addLabel(text="Drive-way area",row=2,column=0)
        self.driveway_area_output=self.addFloatField(0,row=2,column=1,width=20,state="disabled")
        self.addLabel(text="Garage area",row=2,column=2)
        self.garage_area_output=self.addFloatField(0,row=2,column=3,width=20,state="disabled")

        #adds buttons to access the different windows, as well as close the program
        self.area_button= self.addButton(text="select area's visability", row=3,column=0,command=self.enable_disable_rects)
        self.create_property_button =self.addButton(text="  set all areas for property", row=3,column=1,command=self.set_property)
        self.create_property_button =self.addButton(text="  move one area on property", row=3,column=2,command=self.move_property)
        self.exit_button= self.addButton(text="exits the program", row=3,column=3,command=self.exit_program)

        #resets to the template i made above(where are the rectangles are called
        self.reset_button=self.addButton(text="reset to template", row=4,column=0,command=self.reset_rects)
        self.create_property_button =self.addButton(text="random pictures", row=4,column=1,command=self.my_pics)

    #resets the rectangles to the template made in the __init__ of My_Frame
    def reset_rects(self):
        self.chk_template = False
        self.yard_rect.disable_rect()
        self.yard_rect.enable_rect()
            
        self.house_rect.disable_rect()
        self.house_rect.enable_rect()

        self.driveway_rect.disable_rect()
        self.driveway_rect.enable_rect()
            
        self.garage_rect.disable_rect()
        self.garage_rect.enable_rect()

    #opens the My_Dialogbox_enable_disable window
    def enable_disable_rects(self): 
       My_Dialogbox_enable_disable(self)

    #closes the program
    def exit_program(self):
        quit()

    #opens My_Dialogbox_move_rects window
    def move_property(self):
        My_Dialogbox_move_rects(self)
        
    #opens the My_Dialogbox_area_setup window
    def set_property(self):
        My_Dialogbox_area_setup(self)
    #opens My_Dialogbox_pics window
    def my_pics(self):
        My_Dialogbox_pics(self)

class My_Dialogbox_move_rects(EasyDialog):
    #calls the EasyDialog class, and sets the parent to My_Frame
    def __init__(self, parent):
        EasyDialog.__init__(self,parent)

    #the body of the dialogbox, this lets you put in all the widgets, the widgets are listed below
    def body(self,master):
        self.house_checkbut = self.addCheckbutton(master,text="house",row=0,column=0)
        self.garage_checkbut = self.addCheckbutton(master,text="garage",row=0,column=1)
        self.driveway_checkbut = self.addCheckbutton(master,text="drive-way",row=0,column=2)
        self.myscalex = self.addScale(master,row=1, column=0, from_=-225, to=225, command =self.move_vert)
        self.myscaley = self.addScale(master,row=1, column=1, from_=-25, to=100, command =self.move_hori)

    #moves the rectangles vertically, each if is checking which boxes are checked, and which aren't
    def move_vert(self,value):
        #this is checking every checkbox to make sure it moves everything correctly
        if self.house_checkbut.isChecked()and self.garage_checkbut.isChecked()== False and self.driveway_checkbut.isChecked()== False:
            self.parent.house_rect.move_x(int(value))
            self.myscalex["from_"]=-300
            self.myscalex["to"]=50
            
        elif self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked()== False and self.house_checkbut.isChecked()== False:
            self.parent.garage_rect.move_x(int(value))
            self.myscalex["from_"]=-225
            self.myscalex["to"]=225
            
        elif self.driveway_checkbut.isChecked() and self.garage_checkbut.isChecked()== False and self.house_checkbut.isChecked()== False:
            self.myscalex["from_"]=-225
            self.myscalex["to"]=225
            self.parent.driveway_rect.move_x(int(value))

        elif self.house_checkbut.isChecked() and self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscalex["from_"]=-225
            self.myscalex["to"]=50
            self.parent.house_rect.move_x(int(value))
            self.parent.driveway_rect.move_x(int(value))
            self.parent.garage_rect.move_x(int(value))

        elif self.house_checkbut.isChecked() and self.garage_checkbut.isChecked():
            self.parent.house_rect.move_x(int(value))
            self.parent.garage_rect.move_x(int(value))
            self.myscalex["from_"]=-225
            self.myscalex["to"]=50

        elif self.house_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscalex["from_"]=-225
            self.myscalex["to"]=50
            self.parent.house_rect.move_x(int(value))
            self.parent.driveway_rect.move_x(int(value))
            
        elif self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscalex["from_"]=-225
            self.myscalex["to"]=225
            self.parent.driveway_rect.move_x(int(value))
            self.parent.garage_rect.move_x(int(value))
            
    def move_hori(self,value):
         #this is checking every checkbox to make sure it moves everything correctly
        if self.house_checkbut.isChecked()and self.garage_checkbut.isChecked()== False and self.driveway_checkbut.isChecked()== False:
            self.parent.house_rect.move_y(int(value))
            self.myscaley["from_"]=-25
            self.myscaley["to"]=100
            
        elif self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked()== False and self.house_checkbut.isChecked()== False:
            self.parent.garage_rect.move_y(int(value))
            self.myscaley["from_"]=-25
            self.myscaley["to"]=200
            
        elif self.driveway_checkbut.isChecked() and self.garage_checkbut.isChecked()== False and self.house_checkbut.isChecked()== False:
            self.myscaley["from_"]=-25
            self.myscaley["to"]=0
            self.parent.driveway_rect.move_y(int(value))

        elif self.house_checkbut.isChecked() and self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscaley["from_"]=-25
            self.myscaley["to"]=0
            self.parent.house_rect.move_y(int(value))
            self.parent.driveway_rect.move_y(int(value))
            self.parent.garage_rect.move_y(int(value))

        elif self.house_checkbut.isChecked() and self.garage_checkbut.isChecked():
            self.parent.house_rect.move_y(int(value))
            self.parent.garage_rect.move_y(int(value))
            self.myscaley["from_"]=-25
            self.myscaley["to"]=100

        elif self.house_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscaley["from_"]=-25
            self.myscaley["to"]=0
            self.parent.house_rect.move_y(int(value))
            self.parent.driveway_rect.move_y(int(value))
            
        elif self.garage_checkbut.isChecked() and self.driveway_checkbut.isChecked():
            self.myscaley["from_"]=-25
            self.myscaley["to"]=100
            self.parent.driveway_rect.move_y(int(value))
            self.parent.garage_rect.move_y(int(value))
            

class My_Dialogbox_area_setup(EasyDialog):
    #calls the EasyDialog class, and sets the parent to My_Frame
    def __init__(self, parent):
        EasyDialog.__init__(self,parent)

    #the body of the dialogbox, this lets you put in all the widgets, the widgets are listed below
    def body(self,master):
        self.addLabel(master, text="enter the property/yard length",row=0,column=0)
        self.property_inputL=self.addFloatField(master,0,row=0,column=1,width=20)
        self.addLabel(master, text="enter the property/yard width",row=0,column=2)
        self.property_inputW=self.addFloatField(master,0,row=0,column=3,width=20)

        self.addLabel(master, text="enter the house length",row=1,column=0)
        self.house_inputL=self.addFloatField(master,0,row=1,column=1,width=20)
        self.addLabel(master, text="enter the house width",row=1,column=2)
        self.house_inputW=self.addFloatField(master,0,row=1,column=3,width=20)

        self.addLabel(master, text="enter the driveway length",row=2,column=0)
        self.driveway_inputL=self.addFloatField(master,0,row=2,column=1,width=20)
        self.addLabel(master, text="enter the driveway width",row=2,column=2)
        self.driveway_inputW=self.addFloatField(master,0,row=2,column=3,width=20)
        
        self.addLabel(master, text="enter the garage length",row=3,column=0)
        self.garage_inputL=self.addFloatField(master,0,row=3,column=1,width=20)
        self.addLabel(master, text="enter the garage width",row=3,column=2)
        self.garage_inputW=self.addFloatField(master,0,row=3,column=3,width=20)

    #this is checking all invaild inputs, if it's invaild print out a messagebox to show what error you got
    def chk_inputs(self,P):
        try:
        # Try converting the input to a float
            float(P)
            return True  # Valid number
        except ValueError:
            return False  # Invalid input
        
    def apply(self):
        #if any of these are true when you close the window, it'll send you a error message
        if self.chk_inputs(self.property_inputL.get()) == False or self.chk_inputs(self.house_inputL.get()) == False or self.chk_inputs(self.driveway_inputL.get()) == False or self.chk_inputs(self.garage_inputL.get()) == False:
             self.messageBox(title="ERROR", message="one of the inputs is not a number, check inputs")
        elif  self.chk_inputs(self.property_inputW.get()) == False or self.chk_inputs(self.house_inputW.get()) == False or self.chk_inputs(self.driveway_inputW.get()) == False or self.chk_inputs(self.garage_inputW.get()) == False:
            self.messageBox(title="ERROR", message="one of the inputs is not a number, check inputs")
        elif self.property_inputL.getNumber() <0 or self.house_inputL.getNumber() <0 or self.driveway_inputL.getNumber() < 0 or self.garage_inputL.getNumber()< 0:
            self.messageBox(title="ERROR", message="one of the inputs is a negative number, please check inputs.")
        elif self.property_inputW.getNumber()< 0 or self.house_inputW.getNumber()< 0 or self.driveway_inputW.getNumber() < 0 or self.garage_inputW.getNumber() < 0:
            self.messageBox(title="ERROR", message="one of the inputs is a negative number, please check inputs.")
        elif self.property_inputL.getNumber() > 1000 or self.house_inputL.getNumber() > 1000 or self.driveway_inputL.getNumber() > 1000 or self.garage_inputL.getNumber() > 1000:
            self.messageBox(title="ERROR", message="one of the inputs is over 1,000, you cannot have a input over 1,000, please check inputs.")
        elif self.property_inputW.getNumber()  > 1000 or self.house_inputW.getNumber()  > 1000 or self.driveway_inputW.getNumber()  > 1000 or self.garage_inputW.getNumber() > 1000:
            self.messageBox(title="ERROR", message="one of the inputs is over 1,000, you cannot have a input over 1,000, please check inputs.")
        elif self.property_inputL.getNumber() < self.house_inputL.getNumber() or self.property_inputL.getNumber() < self.driveway_inputL.getNumber() or self.property_inputL.getNumber() < self.garage_inputL.getNumber():
            self.messageBox(title="ERROR", message="one of the inputs is greater then the properpty area, this cannot be")
        elif self.property_inputW.getNumber() < self.house_inputW.getNumber() or self.property_inputW.getNumber() < self.driveway_inputW.getNumber() or self.property_inputW.getNumber() < self.garage_inputW.getNumber():
            self.messageBox(title="ERROR", message="one of the inputs is greater then the properpty area, this cannot be")
        else:
            #assumed all inputs are correct
            self.parent.yard_area_output.setNumber(float(self.property_inputL.get())*float(self.property_inputW.get()))
            self.parent.house_area_output.setNumber(float(self.house_inputL.get())*float(self.house_inputW.get()))
            self.parent.driveway_area_output.setNumber(float(self.driveway_inputL.get())*float(self.driveway_inputW.get()))
            self.parent.garage_area_output.setNumber(float(self.garage_inputL.get())*float(self.garage_inputW.get()))

class My_Dialogbox_enable_disable(EasyDialog):
    #calls the EasyDialog class, and sets the parent to My_Frame
    def __init__(self, parent):
        EasyDialog.__init__(self,parent)

    #the body of the dialogbox, this lets you put in all the widgets, the widgets are listed below
    def body(self,master):
        self.addLabel(master, text="pick area's to enable and disable",row=0,column=0,columnspan=3)
        self.house_enable =self.addCheckbutton(master,text="disable/enable house     ",column=2,row=1, command= self.set_area_visable)
        self.yard_enable=self.addCheckbutton(master,text="disable/enable yard       ",column=1,row=2, command= self.set_area_visable)
        self.driveway_enable =self.addCheckbutton(master,text="disable/enable drive-way",column=2,row=2, command= self.set_area_visable)
        self.garage_enable =self.addCheckbutton(master,text="disable/enable yard",column=1,row=1, command= self.set_area_visable)

    #sets rectangles to being visable not invisable when clicking the check mark
    #remember you have to press it twice because of the way canvas is set up
    def set_area_visable(self):
        if self.house_enable.isChecked():
            self.parent.house_rect.disable_rect()
        if self.yard_enable.isChecked():
            self.parent.yard_rect.disable_rect()
        if self.driveway_enable.isChecked():
            self.parent.driveway_rect.disable_rect()
        if self.garage_enable.isChecked():
            self.parent.garage_rect.disable_rect()
            
        if self.house_enable.isChecked() == False:
            self.parent.house_rect.enable_rect()
        if self.yard_enable.isChecked() == False:
            self.parent.yard_rect.enable_rect()
        if self.garage_enable.isChecked() == False:
            self.parent.garage_rect.enable_rect()
        if self.driveway_enable.isChecked() == False:
            self.parent.driveway_rect.enable_rect()

#this is for displaying pictures, i used some houses i found online as an example of what i was going for
class My_Dialogbox_pics(EasyDialog):
    #calls the EasyDialog class, and sets the parent to My_Frame
    def __init__(self, parent):
        EasyDialog.__init__(self,parent)
    #the body of the dialogbox, this lets you put in all the widgets, the widgets are listed below
    def body(self,master):
        self.my_image1 = PhotoImage(file="deco_1.png")
        picture_label1 = self.addLabel(master,text="", row=0, column=0)
        picture_label1["image"]=self.my_image1

        self.my_image2 = PhotoImage(file="deco_2.png")
        picture_label2 = self.addLabel(master,text="", row=0, column=1)
        picture_label2["image"]=self.my_image2
            
def main():
    #runs everything above this, basically starts the program
    My_Frame().mainloop()

if __name__ == "__main__":
    main()
