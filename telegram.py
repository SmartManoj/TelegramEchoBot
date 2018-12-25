import requests
import urllib
import os
from flask import Flask,redirect, url_for,request,render_template
from threading import Thread
from datetime import datetime,timedelta
from time import sleep

app = Flask(__name__)

domain='Heroku Domain name'
TOKEN = 'Enter your token'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

print('Started')
@app.route('/')
def main():
    return f'''<html><head><title>Telegram Echobot</title></head><body>Telegram Echobot</body></html>'''
def alink(s,k=None):
    if not k:k=s
    return '<a href="{}">{}</a>'.format(s,k)
def slink(s,k=None,v=1):
    ss=s
    for i,j in (('__','\n'),('--',' '),('-','.'),('_','@'),):
            s=s.replace(j,i)
    if k:ss=k
    s=f'https://t.me/smartmanojbot?start={s}'
    return '<a href="{}">{}</a>'.format(s,ss) if v else s
def tclink(s,d=None):
    if d:return f"+91{s[-10:]} | {slink(f'w.{s}',d)} |"
    return slink(f'w.{s}',f"+91{s[-10:]}")
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
    url=URL + "sendMessage?text={}&chat_id={}&parse_mode=html".format(text, chat_id)
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
            sleep(0.5)
        except Exception as e:
            print(e)        


def echo_all(updates):
    for update in updates["result"]:
        try:
            fname =update["message"]['chat']['first_name']
            chat = update["message"]["chat"]["id"]
            text = update["message"].get("text")
            msg(text,fname,chat)
        except Exception as e:
            print(e)
def msg(text,fname='',chat=admin):
    if text:
        print(chat,text)
    text=text.lower()
    text=text.replace('-','')
    text=text.strip('/')
    if text.startswith('start'):
        v=text.split()
        if len(v)==1:
            text='Welcome {}'.format(fname)
            send_message(text,chat)
            text='/help'
        else:
            msgf(v[1],chat,name=name);return
    elif text.startswith('help'):
        h='''
/help
'''
        text=(h)
    elif text.startswith('hi'):text='Hi buddy'
            #customize here
    if text: print(chat,text)
    send_message(text,chat)

def snt(f,a,b=None):
  try:
    Thread(None,f,None,a,b).start()
  except Exception as e:        
    return str(e)


def restart():
 while True:
  try:
   v=(datetime.utcnow()+timedelta(hours=5,minutes=30))
   if(5*60<v.hour*60+v.minute<21*60+30):
    requests.head(f"http://{domain}.herokuapp.com",timeout=5)
   sleep(25*60)
  except Exception as e:
   sleep(60)
   continue

snt(main,())
snt(restart,())



if __name__ == '__main__':
    app.run()
