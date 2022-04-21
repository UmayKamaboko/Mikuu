# A File That Keeps the Bot Online -----

#Imports

from flask import Flask
from threading import Thread
#Copy of Flask class
app = Flask('')

#Triggers when the bot is Online
@app.route('/')
def main():
    return "Bot Online Shod"

#Running the app
def run():
    app.run(host="0.0.0.0", port=8080)

#Function that can be used in main.py
def keep_alive():
    server = Thread(target=run)
    server.start()