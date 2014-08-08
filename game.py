import json
import os
import inspect
import scenes


class Game():

    def __init__(self, twilio, to_number, from_number, save_dir):
        self.twilio = twilio
        self.from_number = from_number
        self.to_number = to_number
        self.save_path = os.path.join(save_dir, '%s.save' % (self.to_number,))
        
        if os.path.exists(self.save_path):
            self.state = json.load(open(self.save_path, 'rb'))
        else:
            self.state = {}
            self.enter_scene(scenes.Intro)     

    def send_sms(self, body):
        self.twilio.messages.create(body=body, to=self.to_number, from_=self.from_number)

    def send_mms(self, body, media_url):
        self.twilio.messages.create(body=body, media_url=media_url, to=self.to_number, from_=self.from_number)

    def enter_scene(self, scene_class):
        
        print(self.state)

        self.state['scene'] = scene_class.__name__
        scene = scene_class(self)
        scene.enter()
        
    def save(self):
        json.dump(self.state, open(self.save_path, 'wb'))


    def take_action(self, body):      
        scene_class = getattr(scenes, self.state['scene']) 
        scene = scene_class(self)

        action_names = [name for name, _ in inspect.getmembers(scene_class, lambda m: hasattr(m, '_is_action') and m._is_action == True)]
        # trace to log to make sure its getting them
        print(action_names)
        #raise Exception(action_names)
        
        #find the first word that matches any word in the list and make it the action.
        for word in body.lower().split():
            if word in action_names:
                action = getattr(scene, word)
                action()
                return

        
        scene.default()