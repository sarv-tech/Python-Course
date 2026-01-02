# Build a Drink Water Reminder App

import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(title = "Please Drink Some Water", message = "You need to Drink Some water")
    time.sleep(60*60)