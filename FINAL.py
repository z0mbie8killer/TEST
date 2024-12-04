"""
Author: Cezar Hernandez
Date created: 12/1/2024
Assignment: Module 6 project status report 2
Description: this script uses breezypythongui package to access different things in the tkinter
module. I created a class called My_Frame(EasyFrame), this class builds the window, and
creates the rectangles. I then made a class called My_Rectangle. This class draws any
rectangles you want, but still needs all the arguments in the drawRectangle() in order to work.
I made this class to disable, and enable any rectangles you want. You can see more in the
comments in My_Frame() to see whats going on.
"""

from breezypythongui import EasyFrame
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

    def draw_rect(self):
        if self.rect_id is None: #if there is no rectangle drawn, draw the rectangle
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1 ,self.rect_y1 , self.rect_x2,self.rect_y2, outline=self.rect_out_line,fill=self.rect_fill)

    def disable_rect(self):
        if self.is_enabled == True: #if the rectangle can be seen, delete it, and create a new 1
            self.canvas.delete(self.rect_id)#deletes old rectangle
            self.rect_id = None#get rid of the old rectangle, you no longer need it 
            self.is_enabled = False#the rectangle is disabled, can't be seen by the user
            #re-draws the rectangle with the same varaibles, but without the fill and outline
            #this makes it so you can't see the rectangle
            self.rect_id =  self.canvas.drawRectangle(self.rect_x1 ,self.rect_y1 , self.rect_x2,self.rect_y2, outline="",fill="")

    def enable_rect(self):
        if self.is_enabled == False: #if you can't see the rectangle, set it to true so you can see it
            self.rect_id = None #get rid of the old rectangle, you no longer need it 
            self.is_enabled = True #the rectangle can be seen by the user
            self.draw_rect()#redraws the rectangle, that was made before
        
class My_Frame(EasyFrame): #the frame or window to hold all my rectangles
    
    def __init__(self):
        #when drawing shapes, remember it's based of pixels, not the grid system.
         #(x1-x2), (y1-y2) = slope
        EasyFrame.__init__(self,title="My Final Project", width=200, height=300) #sets the window
        self.canva = self.addCanvas(width = 200, height = 100,row=1,column=1) #sets the draw area

        #these are all the different rectangles i drew using the class My_Rectangle, each has
        #different values
        self.rect_1 = My_Rectangle(self.canva,25,25,175,175, "black","green")
        self.rect_2 = My_Rectangle(self.canva,50,50,150,150,"black","brown")
        self.rect_3 = My_Rectangle(self.canva,75,75,125,125, "black","orange")
        self.rect_4 = My_Rectangle(self.canva, 175//2,175//2,225//2,225//2, "black","blue")

        #2 buttons to show that you can enable and disable the rectangles using the class functions
        self.enable_button= self.addButton(text="enable all rectangle", row=2,column=1,command=self.enable_all)
        self.disable_button=self.addButton(text="disable all rectangles:", row=3,column=1,command=self.disable_all)

    def enable_all(self): #enable all rectangles, so they can be seen
       self.rect_1.enable_rect()
       self.rect_2.enable_rect()
       self.rect_3.enable_rect()
       self.rect_4.enable_rect()

    def disable_all(self): #disable all rectangles, so they can't be seen
        self.rect_1.disable_rect()
        self.rect_2.disable_rect()
        self.rect_3.disable_rect()
        self.rect_4.disable_rect()
        
My_Frame() #runs everything above this, basically starts the program
