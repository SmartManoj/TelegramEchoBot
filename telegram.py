import requests
import time    
import urllib
from flask import Flask,redirect, url_for,request,render_template

app = Flask(__name__)

TOKEN = "429816072:AAG3p9BNXw4s_CcMMnPcg4TC34QX2QJRIcs"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

@app.route('/')
@app.route('/up/<srvc>')
def main1(srvc='Cool'):
	return f'''<div>You are Rocking Smart - {srvc}</div>'''


@app.route('/open/<z>')
def openz(z='z'):
	f=open(z)
	return f.read()+f'''_'''

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    return  requests.get(url).json()

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url=URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    try:
        r=requests.get(url,timeout=30)
        if r.reason!='OK':print(r.text)
    except Exception as e:
        print(e)
        print(url)

def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)           
            z=updates.get("result")
            if z and len(z) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)
            time.sleep(0.5)
        except Exception as e:
            print(e)        


def echo_all(updates):
    for update in updates["result"]:
        try:
            print(update)
            chat = update["message"]["chat"]["id"]
            a = update["message"].get("text")
            #customize here
            if a: print(chat,a)
            send_message(a,chat)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
