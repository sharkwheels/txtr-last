### Modules ################################

import sys, re
from flask import Flask, request
from twilio.rest import TwilioRestClient
import twilio.twiml
import game

### App Config ########################################################################

app = Flask(__name__)

### Key / Passwords File ###

app.config.from_pyfile('keys.cfg')

### Twilio Stuff ###

account_sid = app.config['TWIL_SID']
auth_token = app.config['TWIL_TOKEN']
twilio_client = TwilioRestClient(account_sid, auth_token)

### save path ####################################################################

save_dir = sys.path[0] 

### App Views ####################################################################

@app.route("/", methods=['GET','POST'])

def index():
	app_title = "txtr engine"

	return render_template('index.html', app_title=app_title)


@app.route("/sms", methods=['GET', 'POST'])
def accept_response():
    from_number = request.values.get('From') # get the from number

    raw = request.values.get('Body') # get the body of the text message 
    body = re.sub(r'[^\w\s]','',raw) # strip all the punctuation out of the message.

    g = game.Game(twilio_client, from_number, "+1647XXXXXXX", save_dir)
    g.take_action(body) # pass the body to the take action function
    g.save() # save this in a file

    resp = twilio.twiml.Response()
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
