# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from game_scene import *


class main_menu_scene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode('assets/sprites/star_background.png',
        															color = '#636363',
        															position = self.size / 2,              
                                    	parent = self, 
                                    	size = self.size)
        self.slime_text = LabelNode(font = ('Chalkduster', 72),
        															text = 'SLIME',
        															color = 'green',
        															position = (self.size.x / 2, self.size.y * 0.85),
        															parent = self)
        self.hunter_text = LabelNode(font = ('American Typewriter', 72),
        															text = 'HUNTER',
        															color = '#d5fff9',
        															position = (self.size.x / 2, self.size.y * 0.75),
        															parent = self)
        self.start_button = SpriteNode('assets/sprites/start_button.PNG',
        																position = (self.size.x / 2, self.size.y * 0.25),
        																size = (300, 120),
        																parent = self)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if (self.start_button.frame.contains_point(touch.location)):
        	self.present_modal_scene(game_scene())
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
