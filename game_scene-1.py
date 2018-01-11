# Created by: Michael Taylor
# Created on: December 2017
# Created for: ICS3U

from scene import *

class hunter (SpriteNode):
	#class of hunter/player
	def __init__ (self, size, max_x, max_y, *args, **kwargs):
		#hunter constructor
		player_image = 'assets/sprites/player.PNG'
		self.player_width = size
		self.player_height = size * 2
		
		SpriteNode.__init__ (self, player_image, *args, **kwargs)
		
		self.size = (self.player_width, self.player_height)
		self.position = (max_x / 2, max_y)
		
		self.bottom_collision = False
		
		self.x_velocity = 0
		self.X_ACCELERATION = 5
		
		self.y_velocity = 0
		self.Y_ACCELERATION = 5
		
		self.GRAVITY = 1
		self.TERMINAL_X_VELOCITY = 40
		self.TERMINAL_Y_VELOCITY = 120
		
		self.bottom_collision = False
		
		pass
		
	def move_left (self):
		if (self.x_velocity > -self.TERMINAL_X_VELOCITY):
			self.x_velocity = self.x_velocity - self.X_ACCELERATION
		pass
		
	def move_right (self):
		if (self.x_velocity < self.TERMINAL_X_VELOCITY):
			self.x_velocity = self.x_velocity + self.X_ACCELERATION
		pass
		
	def update_position (self):
		if (self.x_velocity > 0):
			self.x_velocity = self.x_velocity - self.X_ACCELERATION / 2
		elif (self.x_velocity < 0):
			self.x_velocity = self.x_velocity + self.X_ACCELERATION / 2
			
		if (self.bottom_collision == False and self.y_velocity > -self.TERMINAL_Y_VELOCITY):
			self.y_velocity = self.y_velocity - self.GRAVITY
		elif (self.bottom_collision == True):
			self.y_velocity = 0
		
		update_position = Action.move_by (self.x_velocity, self.y_velocity)
		self.run_action(update_position)
		pass
		
		
class tile (SpriteNode):
	#tile class 
	def __init__ (self, size, x, y, *args, **kwargs):
		#tile constructor
		tile_image = 'assets/sprites/tile.PNG'
		
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
		
		GRAVITY = 1
		
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
		
	def collision_check (self):
		self.player.bottom_collision = False
		
		for tile in self.tile_list:
			if (self.player.position.y <= tile.position.y + (tile.size.y / 2) + (self.player.player_height / 2)):
				self.player.bottom_collision = True
		pass
		
	def update (self):
		#game loop
		
		if (self.left_button_down):
			self.player.move_left()
			
		if (self.right_button_down):
			self.player.move_right()
			
		self.collision_check()
		self.player.update_position()
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
