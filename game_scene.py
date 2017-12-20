from scene import *

class hunter (SpriteNode):
	def __init__ (self, size, max_x, max_y, *args, **kwargs):
		player_image = 'assets/sprites/player_placeholder.PNG'
		player_width = size * 2
		player_height = size * 2
		
		SpriteNode.__init__(self, player_image, *args, **kwargs)
		
		self.size = (player_width, player_height)
		self.position = (max_x / 2, max_y * 0.75)
		
		pass
		
class tile (SpriteNode):
	def __init__ (self, size, x, y, *args, **kwargs):
		tile_image = 'assets/sprites/tile_placeholder.JPG'
		
		tile_size = size
		
		SpriteNode.__init__(self, tile_image, *args, **kwargs)
		self.size = (tile_size, tile_size)
		self.position = (x, y)
		
		pass

class game_scene (Scene):
	def setup (self):
		self.background_color = '#272727'
		
		self.screen_width = self.size.x
		self.screen_height = self.size.y
		
		self.tile_size = 64
		self.tile_list = []
		
		self.player = hunter(self.tile_size, self.screen_width, self.screen_height, parent = self)
		
		self.create_level()
		
		pass
		
	def create_level (self):
		for y in range (0, 4):
			for x in range (0, int (self.screen_width / self.tile_size) + 1):
				self.tile_list.append(tile(self.tile_size, x * self.tile_size, y * self.tile_size, parent = self))
				
		pass

run(game_scene(), show_fps = True, orientation = LANDSCAPE)
