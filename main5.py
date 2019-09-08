#!/usr/bin/env python3

import utils, open_color, arcade #imports for the file

utils.check_version((3,7)) # check version

SCREEN_WIDTH = 800 #screen width
SCREEN_HEIGHT = 600 #screen height
SCREEN_TITLE = "Smiley Face Example" #Title that is written on screen

class Faces(arcade.Window): #Initialized class Faces
    """ Our custom Window Class""" #comment

    def __init__(self): #set init for class faces
        """ Initializer """ #comment
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2 #divides screen width by 2
        self.y = SCREEN_HEIGHT / 2 #divides screen height by 2

        arcade.set_background_color(open_color.white) #Background set to white

    def on_draw(self): #set draw function of class
        """ Draw the face """
        arcade.start_render() #render the face
        face_x,face_y = (self.x,self.y) #set start values for face
        smile_x,smile_y = (face_x + 0,face_y - 10) #the yellow circle location
        eye1_x,eye1_y = (face_x - 30,face_y + 20)  #the left eye location
        eye2_x,eye2_y = (face_x + 30,face_y + 20)  #the right eye location
        catch1_x,catch1_y = (face_x - 25,face_y + 25)  #left eye dot location
        catch2_x,catch2_y = (face_x + 35,face_y + 25)  #right eye dot location

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #draws the yellow cirle
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #draws the black outline
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #draws left eye
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black) #draws right eye
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #draws left eye dot
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) #draws right eye dot
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #draws mouth


    def on_mouse_motion(self, x, y, dx, dy): #set function hand motion
        """ Handle Mouse Motion """
        self.x = x #gets mouse X
        self.y = y #gets mouse y



window = Faces() #sets window equal to faces class
arcade.run() #runs the class