from flask import Flask, request
from message import *
import json


app = Flask(__name__)



@app.route("/", methods=['GET','POST'])
def main():
    

    receiver_name = json.loads(request.form['senderobj'])
    messagebot = json.loads(request.form['messageobj'])
    user_message = messagebot['text'].lower()

    if user_message == "/start":
        return f"hey {receiver_name['display']} 🙏 welcome to shreyasmohite bot 😄"

    if user_message in greetings:
        return f"hello {receiver_name['display']} 🤪"

    if user_message in goodmorning_message:
        return f"hello good morning ☕ "
    
    if user_message in casual_message:
        return f"I am pretty good thankyou 😁"
    
    if user_message in helps:
        return f"how can I help you 😃?"

    if user_message == "/help":
        return f"sorry i can't help you right now"

    if user_message == "/about":
        return f'''
        Experienced Web Developer adept in all stages of advanced web development. Knowledgeable in user interface, testing, and debugging processes. Bringing forth expertise in design, installation, testing and maintenance of web systems. Equipped with a diverse and promising skill-set. Proficient in an assortment of technologies, including python, nodejs and go and able to work with there frameworks. Able to effectively self-manage during independent projects, as well as collaborate in a team setting.
        '''

    if user_message == "/resume":
        return f"resume https://bit.ly/3LG484y"

    if user_message == "/contact's":
        return f''' My Contact's
        Github https://bit.ly/3S2FVaf \n
        LinkedIn https://bit.ly/3VvGVa3 \n
        Portfolio Link \n
        Codechef https://bit.ly/3EFRqkS \n
        HackerRank https://bit.ly/3CYJGJA \n
        '''

    if user_message == "/blogs":
        return f''' My Blog's \n
        Medium https://bit.ly/3g5EDOw \n
        dev_to https://bit.ly/3rWDprK
        '''

    if user_message in offensive_words:
        return f"🙏 please don't use such words"
    return ""

    

@app.route("/ping", methods=['GET'])
def pong():
    return "pong"


if __name__ == "__main__":
    app.run(debug=True)
