from flask import Flask, request, jsonify
from hadara import Whatsappbot
import json
import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = Whatsappbot(request.json)
        return bot.Welcome_prompt()

    # if request.method == 'GET':
    #     bot = Whatsappbot(request.json)
    #     return bot.Welcome_prompt
    #     payload = request.data
    #     wa.receive_message(payload)

if(__name__) == '__main__':
    app.run()