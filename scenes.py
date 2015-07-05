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

## To create a new scene, follow this template, make a new Scene / class. 
## Any def w/ a decorator becomes an action word.
## default will reload the scene if people don't choose one of the action words. 
## you can have as many action words as you want in each scene. 

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
		self.game.state['end_location'] = 'end_2' # sets the ending location
		self.enter_scene(End)

	def default(self):
		self.enter_scene(SceneTwo)


## ENDING ##########################################################################################
## just add an elif statement for each ending you have.
## this gets bone ugly long if you have a lot, so keep that in mind. 


class End(Scene):

	def enter(self):
		if self.game.state['end_location'] == "end_1":
			self.send_sms("First Ending.")
			self.send_mms(":3", media_url=["http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg"])
			self.enter_scene(Reload)

		elif self.game.state['end_location'] == "end_2":
			self.send_sms("Second Ending")
			self.send_mms(":3", media_url=["http://placekitten.com.s3.amazonaws.com/homepage-samples/200/287.jpg"])
			self.enter_scene(Reload)

		else:
			pass


## RELOAD ##########################################################################################
## Just a way to have a thanks message and an option for restart. 

class Reload(Scene):

	def enter(self):
		#### Delay for a bit ########
		time.sleep(5)
		self.game.state['end_location'] = "finished"
		self.send_sms("Thanks for Playing! It might take a while for your ending image to show up (slow networks). If you'd like to play again, text AGAIN. Or you can QUIT to unsubscribe to this app.")
		
	
	## if the player texts 'again' in this state, restart the game. Bypass the Intro, they don't need it. 
	@action
	def again(self):
		self.enter_scene(SceneOne)

	def default(self):
		self.enter_scene(Intro)

