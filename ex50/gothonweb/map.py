class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go (self, direction):
		return self.paths.get(direction, None)
	def add_paths(self, paths):
		self.paths.update(paths)
central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you
""")

the_bridge = Room("The Bridge",
"""
The container clicks open
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb
""")

the_end_winner = Room("The End",
"""
You jump into pod 2
""")

the_end_loser = Room("The End",
"""
You jump into a random pod
""")