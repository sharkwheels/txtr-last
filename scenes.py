import time

def action(f):

	f._is_action = True
	return f


class Scene(object):

	def __init__(self, game):
		self.game = game

	def send_sms(self, body):
		self.game.send_sms(body)

	def send_mms(self, body, media_url):
		self.game.send_mms(body, media_url)

	def enter_scene(self, scene):
		self.game.enter_scene(scene)

	def enter(self):
		pass

	def default(self):
		pass
		
	@action
	def restart(self):
		self.enter_scene(SceneOne)		
	@action
	def info(self):
		self.send_sms("Available actions are in ALL CAPS, ie: \"OFFICE\". QUIT will unsubscribe you. If there is a delay, sorry, sometimes the network sucks. Just be cool and hang for a bit.")
	

### this is the intro scene ####################################

class Intro(Scene):

	def enter(self):
		self.send_sms("txtr skeleton. Text BEGIN to get the ball rolling.")
	
	@action
	def begin(self):
		self.enter_scene(SceneOne)

	def default(self):
		self.enter_scene(Intro)



### Scene Examples ####################################################

class SceneOne(Scene):
	
	def enter(self):
		self.send_sms("This is Scene One, go to scene TWO or head to the ENDING.")
	
	## if message body is... ##
	@action
	def two(self):
		self.enter_scene(SceneTwo)

	@action
	def ending(self):
		self.game.state['end_location'] = 'end_1'  # sets the ending location
		self.enter_scene(End)
	
	def default(self):
		self.enter_scene(SceneOne)


class SceneTwo(Scene):
	def enter(self):
		self.send_sms("This is Scene Two, go to scene ONE or head to the ENDING.")

	@action
	def one(self):
		self.enter_scene(SceneOne)

	@action
	def ending(self):
		self.game.state['end_location'] = 'end_2'
		self.enter_scene(End)

	def default(self):
		self.enter_scene(SceneTwo)


class End(Scene):

	def enter(self):
		if self.game.state['end_location'] == "end_1":
			self.send_sms("First Ending.")
			self.send_mms(":3", media_url=["http://work.nadinelessio.com/twiliothings/cats_07/cat_recycle.jpg"])
			self.enter_scene(Reload)

		elif self.game.state['end_location'] == "end_2":
			self.send_sms("Second Ending")
			self.send_mms(":3", media_url=["http://work.nadinelessio.com/twiliothings/cats_07/cat_bed.jpg"])
			self.enter_scene(Reload)

		else:
			pass



class Reload(Scene):

	def enter(self):
		#### Delay for a bit ########
		time.sleep(8)
		self.game.state['end_location'] = "finished"
		self.send_sms("Thanks for Playing! It might take a while for your ending image to show up (slow networks). If you'd like to play again, text AGAIN. Or you can QUIT to unsubscribe to this app.")
		
	
	## if the player texts 'again' in this state, restart the game. Bypass the Intro, they don't need it. 
	@action
	def again(self):
		self.enter_scene(SceneOne)

	def default(self):
		self.enter_scene(Intro)

