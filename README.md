# securehome
An IoT-based home security system

Home Security Systems uses a Magnetic Reed Switch, ESP8266 Wi-Fi module, and Bolt application.
A notification message is sent to the desired application each time the door is opened or closed.
The ESP8266 Wifi Module programming is done in such a way that it sends only one notification message
when the door is opened or the door is closed, which became possible by using a flag in the programming.
Even if this application is running in the background still you will be able to receive the notifications.
This project can be used to monitor the lockers, cupboards, and garage doors,
and it can also be used in advanced-level projects like tracking the car bonnet, doors, etc. 
This project can be used anywhere where you need the magnetic Reed Switch. Hence the system
is named “Secure Home”.

In this project, I used Bolt Cloud and other third-party services to send the alert
messages by capturing the door movement through connecting magnetic reed switch door
sensor to the bolt wifi module. The door sensor is fixed onto the door frame and the
magnet is fixed onto the door, the sensor gets active when the door movement takes
place and the alert message is sent to the user by using third party services.
At first, the movement data is captured through the bolt wifi module to the cloud,
from the cloud it is taken and sent to third-party services called Twilio, Mailgun, and
Telegram bot to send the alert messages to the registered user. This project uses a simple
mechanism and uses less price to build and set up.
