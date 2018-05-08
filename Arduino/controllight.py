from flask import Flask
from flask_ask import Ask, statement
import requests
import json
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch

@ask.intent("LightOn")
def on():
    ser.write(b'A')
    return statement("Turn on light.")

@ask.intent("LightOff")
def off():
    ser.write(b'B')
    return statement("Turn off light.")

if __name__ == "__main__":
    app.run(debug=True)

