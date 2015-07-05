#### TXTR ############################################

Txtr is a small SMS text adventure engine written in Python 2.7+. It uses an online application called Twilio to handle the SMS side of things. 
It was originally built at the end of 2013 to run the game Cat Quest. It was later built out into an online application to run the game Sext Adventure. 
This is the barebones local running non oline webby database version. <br />

This is here AS IS. There is no guarantee its gonna work. But its pretty stable, so it should be mostly ok. 

### DOWNLOADS ###############################################

You will need a Twilio Account: https://www.twilio.com/ <br />
Download and Install ngrok:  https://ngrok.com/ <br />

### Modules ###############################################

Flask: pip install flask <br />
Twilio for Python: pip install twilio <br />

### SETUP AND RUNNING ###############################################

Note you should probably run this out of a virtual environemnt with Virtualenv. 

1) Make your own keys.cfg file that will include your twilio account info / auth tokens save it to the root directory.<br />

<blockquote>
TWIL_SID = 'XXXXXXXXXXXXXX' <br />
TWIL_TOKEN = 'XXXXXXXXXXXXXX' <br />
TWILIO_NUMBER = 'XXXXXXXXXXXXXX' <br />
</blockquote>

2) Follow the ngrok documentation to open a tunnel to the internets. (or any other tunnel of your choice)<br />
3) On the twilio end, set your SMS/MMS settings for your number to the ngrok subdomain. eg: http://ba50b210.ngrok.io/sms <br />
4) Start up the app with python app.py<br />

Things should be texting at this point.<br />

### Contributors ####################################

Nadine Lessio - Initial concpet / programming (@_nadine)  <br />
Jonathan Doda - Decorator Concept / Database / Further programming (@jondoda) <br />
Angus Flecther - Debugging, Troubleshooting, Ops (@angusiguess) <br />

### Usage ####################################

You are free to use this for NON COMMERCIAL purposes. <br />
But I would appreciate it if you could link back to here with a mention if you do use it. <br />
Also it would be awesome to see what you make with it! :)<br />