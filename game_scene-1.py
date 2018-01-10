# Created by: Michael Taylor
# Created on: December 2017
# Created for: ICS3U

from scene import *

class hunter (SpriteNode):
	#class of hunter/player
	def __init__ (self, size, max_x, max_y, *args, **kwargs):
		#hunter constructor
		player_image = 'assets/sprites/player_placeholder.PNG'
		player_width = size * 2
		player_height = size * 2
		
		SpriteNode.__init__ (self, player_image, *args, **kwargs)
		
		self.size = (player_width, player_height)
		self.position = (max_x / 2, max_y * 0.75)
		
		self.x_velocity = 0
		self.x_acceleration = 10
		self.terminal_velocity = player_width
		
		
		pass
		
	def move_left (self):
		if (self.x_velocity < self.terminal_velocity):
			self.x_velocity = self.x_velocity + self.x_
		pass
		
class tile (SpriteNode):
	#tile class 
	def __init__ (self, size, x, y, *args, **kwargs):
		#tile constructor
		tile_image = 'assets/sprites/tile_placeholder.JPG'
		
		tile_size = size
		
		SpriteNode.__init__ (self, tile_image, *args, **kwargs)
		self.size = (tile_size, tile_size)
		self.position = (x, y)
		
		pass

class game_scene (Scene):
	#main game class/scene 
	def setup (self):
		background_color = '#150077'
		self.background = SpriteNode (color = background_color,
																	position = self.size / 2,
																	size = self.size,
																	parent = self)
		
		self.SCREEN_WIDTH = self.size.x
		self.SCREEN_HEIGHT = self.size.y
		self.UI_HEIGHT = 192
		self.BUTTON_SIZE = (156, 156)
		self.left_button_down = False
		self.right_button_down = False
		
		self.tile_size = 64
		self.tile_list = []
		
		self.player = hunter(self.tile_size, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, parent = self)
		
		self.create_level()
		self.setup_ui()
		
		pass
		
	def setup_ui (self):
		ui_background = SpriteNode (color = '#ffffff',
															  position = (self.SCREEN_WIDTH / 2, self.UI_HEIGHT / 2),
															  size = (self.SCREEN_WIDTH, self.UI_HEIGHT),
															  parent = self)
		
		self.left_button = SpriteNode ('assets/sprites/left_button.PNG',
																		position = (self.BUTTON_SIZE[0], self.UI_HEIGHT / 2),
																		size = self.BUTTON_SIZE,
																		parent = self)
																		
		self.right_button = SpriteNode ('assets/sprites/right_button.PNG',
																		position = (self.BUTTON_SIZE[0] * 2, self.UI_HEIGHT / 2),
																		size = self.BUTTON_SIZE,
																		parent = self)
																		
		pass
		
	
	def create_level (self):
		for y in range (0, 4):
			for x in range (0, int(self.SCREEN_WIDTH / self.tile_size) + 1):
				self.tile_list.append(tile(self.tile_size, x * self.tile_size, self.UI_HEIGHT + (y * self.tile_size), parent = self))
				
		pass
		
	def update (self):
		#game loop
		
		if (self.left_button_down):
			self.player.move_left()
		
		pass
		
	def touch_began (self, touch):
		if (self.left_button.frame.contains_point(touch.location)):
			self.left_button_down = True
			
		if (self.right_button.frame.contains_point(touch.location)):
			self.right_button_down = True
			
		'''if (self.jump_button.frame.contains_point(touch.location)):
			self.player_jump()'''
						
		pass
		
	def touch_moved (self, touch):
		if (self.left_button.frame.contains_point(touch.location)):
			self.left_button_down = True
		else:
			self.left_button_down = False
			
		if (self.right_button.frame.contains_point(touch.location)):
			self.right_button_down = True
		else:
			self.right_button_down = False
			
		pass
		
		
	def touch_ended(self, touch):
		if(self.left_button.frame.contains_point(touch.location)):
			self.left_button_down = False
		
		if(self.right_button.frame.contains_point(touch.location)):
			self.right_button_down = False
			
		pass
