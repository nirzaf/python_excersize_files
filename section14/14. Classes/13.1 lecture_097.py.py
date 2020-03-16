class Ereader():
	"""A class to repesent an ereader."""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize the attributes to describe an ereader."""
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery = battery
		self.screen_type = screen_type
		self.library_count = 0

	def get_ereader_name(self):
		"""Return a formatted descriptive name for our ereader."""
		long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
		return long_name.title()

	def read_library_count(self):
		"""Show the amount of ebooks in our kindle library."""
		print("You have " + str(self.library_count) + " books in your kindle library.")

	def update_library_count(self, ebook_count):
		"""Set the library count."""
		self.library_count = ebook_count

	def increment_library_count(self, purchased_ebooks):
		"""Add our new ebooks to our library count."""
		self.library_count += purchased_ebooks

class Screen():
	"""Create a class to model the screen of a kindle fire."""

	def __init__(self, screen_resolution = '1280 * 800'):
		"""Initialize the screens attributes."""
		self.screen_resolution = screen_resolution

	def describe_screen(self):
		"""Print out some marketing copy about the Kindle fire."""
		print("\nFire HD 8 features a widescreen " + self.screen_resolution + " HD screen.")

class KindleFire(Ereader):
	"""Represents aspects of an ereader specific to a Kindle Fire."""
	
	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize attributes of the parent class.
			Then initialize attributes specific to a Kindle Fire."""
		

		super().__init__(make, model, backlight, battery, screen_type)
		self.firescreen = Screen()
	

my_kindle_fire = KindleFire('amazon', 'kindle fire', 'backlight', '12 hours battery life', 'color screen')
print(my_kindle_fire.get_ereader_name())	

my_kindle_fire.firescreen.describe_screen()

