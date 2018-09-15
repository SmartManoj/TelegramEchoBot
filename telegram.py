# -*- coding: utf-8 -*-

from config import *
from cf import *

app = Flask(__name__)

def wish2():
	try:
		global blist,dobz	
		blist=[]
		t=today_dt[5:]
		for k, v in dobl.items():
			v=str(datetime.strptime(v,'%d.%m.%Y').date())[5:]
			dobz[v].append((cse_tid2[k])) 
			if v==t:blist.append(kec_sname(k))
	except Exception as e:
		exception(e)
def wish3(i):
	send_message(b'\xe0\xae\x87\xe0\xae\xa9\xe0\xae\xbf\xe0\xae\xaf \xe0\xae\xaa\xe0\xae\xbf\xe0\xae\xb1\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xa8\xe0\xae\xbe\xe0\xae\xb3\xe0\xaf\x8d \xe0\xae\xa8\xe0\xae\xb2\xe0\xaf\x8d\xe0\xae\xb5\xe0\xae\xbe\xe0\xae\xb4\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x8d\xe0\xae\xa4\xe0\xaf\x81\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xb3\xe0\xaf\x8d...'.decode()+emo('yellow_heart')*3,i)
def wish():
	try:
		global blist,dobz	
		t=today_dt[5:]
		for k, v in doblm.items():
			v=str(datetime.strptime(v,'%d.%m.%Y').date())[5:]
			dobz[v].append(k) 
		for i in (dobz[t]):
			if i:wish3(i)
	except Exception as e:
		exception(e)
				
def nagu():
	i=(today_dy)
	r=requests.get('https://timesofindia.indiatimes.com/tvschannel_schedule.cms?fromdatetime=201805{:02}0000&todatetime=201805{:02}0000&channelname=zee%20tamil'.format(i,i+1),headers=headers)
	if ('Naaga Rani' in r.text):
		send_message('Don\'t Miss Naaga Rani'+emo('red_heart'))
		send_message('Don\'t Miss Naaga Rani'+emo('red_heart'),tidMan)



def get_updates(offset=None):
	try:
		url = URL + 'getUpdates?timeout=200'
		if offset:
			url += '&offset={}'.format(offset)
		js = get_url(url)
		return js.json() if js.ok else None
	except json.decoder.JSONDecodeError:
		send_message('@ NammaLU',tidme)
		print(js.text)
		return None





	


def get_last_update_id(updates):
	update_ids = []
	for update in updates['result']:
		update_ids.append(int(update['update_id']))
	return max(update_ids)





def tvs(c,k,z=0):send_message(tvs2(k,z),c)
	


def exlink(z,c):send_message(link0(z),c)
def exlink27(z,c):send_message(dx(z),c)
def exlink28(z,c):send_message(dx2(z),c)

def exlink26(z,c,k=1):
	'''shortest url xpand and short'''
	try :
		if k:
			data ={'u':z}
			r=requests.get('http://checkshorturl.com/expand.php',params=data,headers=headers,timeout=10)
			z=re.search('&url=(.*?)\'',r.text)[1]
		else:
			h={'public-api-token':'cbc7bb0d8c3149ba91c07c603b2bbd15'}
			d={'urlToShorten':z}
			u='https://api.shorte.st/v1/data/url'
			r=requests.put(u,headers={**h, **headers},timeout=10,data=d)
			z=(r.json()['shortenedUrl'])

			
	except Exception as e:
		exception(e)
		z='Cool Ravi'
	send_message(z,c)


def is_kongu_up():
	import socket 
	try:
		pass
		socket.getaddrinfo('kongu.edu',80)
		r=requests.get('http://kongu.edu')
		return str(r.status_code)
	except Exception as e:
		return 'Nope'


def echo_all(updates):
	global chat
	for update in updates['result']:
		try:
			bv='message'
			if update.get('edited_message'):
				bv='edited_'+bv

			name=update[bv]['chat']['first_name'],update[bv]['chat'].get('last_name','')
			username=update[bv]['chat'].get('username','@')
			chat = update[bv]['chat']['id']
			rtm=update[bv].get('reply_to_message')

			b = update[bv].get('location')
			if b: 
				q=f"{b['latitude']},{b['latitude']}"
				text='<a href=https://maps.google.com/maps?q={0}&ll={0}&z=16>{1}- {2}</a>'.format(
					q,'_'.join(name),chat
					)
				msgid= rtm['message_id']
				delete_message(msgid,tidme)
				send_message(text);continue
			b = update[bv].get('contact')
			if b: 
				send_contact(tidme,contact=b);
				msgid= rtm.get('message_id')
				if msgid:delete_message(msgid,tidme)
				continue

			text = update[bv].get('text','No Text')
			textl=text.lower()
			if chat==tidme :
				if rtm:
					chat = (rtm['text'].split('\n')[0])
					tt=rtm['text'].split('-->')[-1].strip()
					chat = tidme if len(chat)<9 else int(chat)
					msgid= rtm['message_id']
					delete_message(msgid,tidme)
					if text.startswith('ex.'):
						send_message(text[3:],chat)
						text=msgf(text[3:],chat);continue
					if textl!='z':send_message(text,chat)
					continue
			otext='-->'
			if rtm:
				otext+=rtm.get('text')+'\n-->'
			
			msgf(text,chat,otext,name,username)
		except Exception as e:
			exception(e)
			continue

	
def hp_rsp3():
	''''setting tdy bal'''
	while True and not tdy:
		try:
			dto=datetime.utcnow()+timedelta(hours=5,minutes=30)
			hr=dto.hour
			if(5<hr<19):
				_=(hp_rsp2(c=0))
				_=hp_rspx(_)
				if _!='Shortly':
					print('TDY SET')
					break
				sleep(10*60)
			else:sleep(30*60)
		except Exception as e:
			sleep(5*60)
			exception(e)
			continue
	

def hp_rspw(chat,k):send_message(hp_rspw2(*k.split('.')),chat)
def hp_stock2(z,c):send_message(hp_stock(z),c)
def exlink2(z,c):send_message(link2(z),c)




def smt(chat,f,*a,**opt):
	try:
		send_message(f(*a),chat,**opt)
	except Exception as e:
		exception(e)

def hp_rsp(chat=tidpa,fmt='ps',m=None,k=1,msg=''):
	if msg:
		x=w2.send(hp_rspf(hp_rspw2(msg),'l'),m);print('@',x)
	elif k:
		if fmt==5:
			zz=hp_rsp2()
			if zz[0]==today_.strftime('%d-%m-%Y'):return
			zz=hp_rspf(zz,'s')
			z='Today RSP No change\n'
			zz=z+zz
			print('@ done')
		else:zz=hp_rspf(hp_rsp2(),fmt)
		if m:x=w2.send(zz,m);print(x)
		else:send_message(zz,chat)
		
	else:
		lu=(datetime.utcnow()+timedelta(hours=5,minutes=30)).day
		_="SELECT * from bk1 where i='{}'".format(lu)
		cur2.execute(_);
		if cur2.rowcount:return
		while  True:
			try:
				dto=datetime.utcnow()+timedelta(hours=5,minutes=30)
				hr=dto.hour
				if(16<hr<24):
					lu2=hp_rsp2()
					z=lu2[0].split('-')[0]
					if lu2!='Shortly':
						z=z.isdigit() and int(z)
						if z>lu:
							x=w2.send(hp_rspf(lu2,'s'),'5');print(x)
							sleep(3)
							x=w2.send(hp_rspf(lu2,'l'),'2');print(x)
							_='update bk1 set i={}'.format(lu)
							cur2.execute(_);con.commit()
							break
					sleep(10*60)
				else:sleep(60*60)
			except AttributeError as e:
				continue
			except Exception as e:
				exception(e,1)
				sleep(5*60)
				continue


version=lambda :'Cool {}'.format(os.getenv('HEROKU_RELEASE_VERSION'))
def hpclbal(bk=0,chat=tidpa):
	s=requests.Session()
	s.headers.update(headers)
	url='https://sales.hpcl.co.in/CreditCheckServiceClient/CreditCheckResponseBP.jsp'
	data={'custcode':'15080010'}
	rt=0
	ft=0

	while True:
		try:
			dto=datetime.utcnow()+timedelta(hours=5,minutes=30)
			hr=dto.hour
			tdt=str(dto.date())
			if(5<hr<22):
				r=s.post(url,data,timeout=300)
				soup=BeautifulSoup(r.content,'lxml')
				rd=soup.find(align='right').next_sibling.next_sibling.text[5:]
				crt=float(soup.find(align='right').text[:-5])
				if crt!=rt and (not tdy or bk):
					t=crt-rt 
					if bk or rt==0 :
						msg='<pre>{}\n{}</pre>'.format(rd,crt)
						if not rt:msg='Today Bal:\n'+msg
						if not rt:snt(hp_rsp,(chat,5,'5'))
					else:msg='<pre>{}\n{}\t||\t{:+.2f}</pre>'.format(rd,crt,t)
					send_message(msg,chat)
				if bk:break	
				rt=crt
		except AttributeError as e:
			continue
		except Exception as e:
			exception(e,0)
			sleep(10*60)
			continue
		sleep(5*60)
				

def msgf(text='SAM',chat=tidme,otext='',name='@',username='@',r=1):
	def rns(func,maxsplit=-1):
		z=text2.split('.',maxsplit)
		if len(z)==1:z.append(str(chat))
		z[1]=rn(z[1])
		if z[1]==fgs:func=str
		snt(smt,(chat,func,*z[1:]));
	try:
		fname=name[0]
		name2='_'.join(name) 
		if r:
			print('@',chat,fname,'@',username)
			uprint('@',text)
		text3=text
		text2=text.lower()
		for i,j in (('__','\n'),('--',' '),('-','.'),('_','@'),):
			text2=text2.replace(i,j)
		text2=text2.replace('. ','.')
		if text2 ==('start'):text='Already Started';
		if text2.startswith('reg'):
			if text2[3]=='q':srn='14CSL260'
			else :srn=rn(int(text2[3:])^783)
			cse_tid2[srn]=chat
			cse_tid[chat]=srn
			text=slink(text2,'Save for 2mrw')
			
		if text2.startswith('/start'):
			v=text2.split()
			if len(v) ==1:
				text='Welcome {}'.format(fname)
				send_message(str(chat)+'\nN:'+name2+f" @{username}",tidme)
			else:
				msgf(text2[7:],chat,name=name)

		elif re.match(r'^/?help$',text2):text=f"""
		{pre(help1)}
	- Help yourself by helping others
		"""
		elif text2=='help.kec':text=pre(help2)
		elif text2=='help.cseb':text=pre(help3)
		elif text2=='help.cse':text=pre(help4)
		elif text2.startswith('/'):text='Command to be created'
		elif text2.startswith('ss.') and chat==tidme:
			n=text2.split('#')
			n2=int(n[1]) if len(n)!=1 and n[1].isdigit() else 1
			z=n[0].split('.')
			if len(z[1])==9:s=z[1]
			else:s=cse_tid2.get(rn(z[1]))
			if s==None:text='TID Not found'
			else:
				for i in range(n2):send_message('.'.join(z[2:]),s);
		elif text2.startswith('znu.') and chat==tidme:
			z=text2.split('.')
			if len(z[1])==9:s=z[1]
			else:s=cse_tid2.get(rn(z[1]))
			if s==None:text='TID Not found'
			else:msgf('.'.join(z[2:]),s);
		elif any(i in text2 for i in emos_h):text=emo_hm*3
		elif emo_tup in text2:text=emo_tup*2
		elif 'bye' in text2:text='Cheers'
		elif 'hello' ==text2:text+=' Buddy'
		elif 'fgs' ==text2:text=fgs
		elif 'id' ==text2:text=str(chat)
		elif 'iku' ==text2:snt(smt,(chat,is_kongu_up))
		elif any(i in text2.split() for i in ['luv','love']):text=emo_he
		elif 'no text' ==text2:text='Send Me <b>Text</b> Baby'
		elif 'tr' ==text2 :
			if chat==tidme:snt(smt,(chat,tr));
			else:
				text=' Due to request from Anti Piracy Cell,Tamil Film Producers Council, the command is removed '
		elif 'ty' ==text2:snt(smt,(chat,tr));
		elif 'rmrl' == text2:send_message('Location',chat,rlc=1)
		elif 'rmrc' == text2:send_message('Contact',chat,rlc=2)
		elif 'super' in text2:text='Cool'
		elif 'vv' ==text2:text=version()
		
		elif text2=='wish':text='\n'.join(blist) or 'Cool'
		elif text2=='wish3':wish3(chat)
		elif 'wherey' in text2:text=wherey or 'Ruby'
		elif 'wow' ==text2:text='Cool'
		

		elif text2.startswith('rs.'):text=text[3:]
		elif text2.startswith('wa'):
			if text2[3:] in helpl:text='wa.pno\nWhatsapp API'
			else: text=api_wa(*text[3:].split('.',1))
		elif text2.startswith('tg.'):send_contact(chat,*text[3:].split('.',2));return
		elif text2.startswith('dt.'):text=datec(text2[3:])
		elif text2.startswith('multi.'):
			for i in text2[6:].strip().splitlines():
				i=i.strip()
				if i:msgf(i,chat)
		elif text2.startswith('c4.'):text='Itz cg NOW'
		elif text2.startswith('emo.'):text=emo2(text2[4:])
		elif text2.startswith('s.'):
			if text2[2:] in helpl:text='Link to command'
			else:text=slink(*text[2:].split('##'))
		elif text2.startswith('s2.'):
			if text2[3:] in helpl:text='Direct Link to command'
			else:text=slink(text[3:],v=0)
		elif text2.startswith('exf.'):snt(globals()[z[1]],tuple(text2.split('.')[2:]))
		elif text2.startswith('b.'):text=f"https://bit.ly/{text[2:]}"
		elif text2.startswith('b2.'):text=f"https://bit.ly/my3{text[3:]}"
		elif text2.startswith('st3'):text=f"https://bit.ly/sm3st3"
		elif text2.startswith('g.'):snt(smt,(chat,egen,text[2:],1))
		elif text2.startswith('anz.') and chat==tidme:snt(anz,(text[4:],))
		elif text2.startswith('anz2.') and chat==tidme:snt(anz,(text[5:],tid2.inv))
		elif text2.startswith('anz3.') and chat==tidme:
			msgf('anz.'+text[5:],r=0)
			msgf('anz2.'+text[5:],r=0)
		elif text2.startswith('cc.'):snt(smt,(chat,cc,text2[3:]))
		elif text2.startswith('cc2.'):snt(smt,(chat,cc2,text2[4:]))
		elif text2.startswith('f.'):snt(smt,(chat,fac,text2[2:]))
		elif text2.startswith('w.'):
			snt(smt,(chat,tc,*text2[2:].split('.',1)),{'opt':'dwbp'})
		elif text2.startswith('el.'):#multi af ls
			if text2[3:] in helpl:text= 'Extraxt Link from adfly (ex6) and linkshrink (ex7)'
			else:snt(exlink2,(text[4:],chat))
		elif text2.startswith('tts'):
			snt(smt,(chat,tts,text[4:]))
		elif text2.startswith('el5.'):#st
			snt(exlink26,(text[4:],chat))
		elif text2.startswith('el6.'):#af
			snt(exlink27,(text[4:],chat))
		elif text2.startswith('el7.'):#ls
			if text2[4:] in helpl:text= 'Extraxt Link from shortest'
			else:snt(exlink28,(text[4:],chat))
		elif text2.startswith('sh.'):#st create
			if text2[3:] in helpl:text= 'Short url by shortest'
			else:snt(exlink26,(text[3:],chat,0))

		elif text2.startswith('af'):
			# text=kongu_not
			rns(af)
		elif text2.startswith('atd'):
			rns(atd)
		elif text2.startswith('bk'):rns(bkid)
		elif text2.startswith('bm2'):rns(bm2,1)
		elif text2.startswith('bm'):rns(bm,1)
		elif text2.startswith('cf2'):rns(feesf2)
		elif text2.startswith('cf'):rns(feesf)
		elif text2.startswith('cg2'):text='Itz cx NOW'
		elif text2.startswith('cv'):
			rns(cgf2)
		elif text2.startswith('cx'):
			rns(cgf)

		elif text2.startswith('cg3'):
			msgf('cg2',chat);msgf('cg!@6',chat)
		elif text2.startswith('dp'):
			if text2[3:] and text2[3:] in helpl:text='''Dp Counter
			http://smartmanoj.blogspot.com/2018/06/get-telegram-dp-count.html
			'''
			else:snt(smt,(chat,count_dp,text2[3:] or chat))
		elif text2.startswith('est'):
			text='Developer Need'
			# rns(ests)
		elif text2.startswith('ese'):snt(smt,(chat,ese,text2[4:],),{'opt':'dwbp'})
		elif text2.startswith('bg.'):snt(smt,(chat,kec_bgf,text2[3:],))
		elif text2.startswith('syl.'):
			text2=f"ese.{text2[4:]} syl"
			msgf(text2,chat,r=0)
		elif text2.startswith('evs'):rns(evs)
		elif text2.startswith('im'):
			# text=kongu_not
			rns(im)
		elif text2.startswith('rn2'):rns(kec_rn2)
		elif text2.startswith('rn4'):rns(kec_rn4)
		elif text2.startswith('rn3'):rns(kec_sname)
		elif text2.startswith('rn'):rns(kec_rn,1)
		elif text2.startswith('time'):
			dto=datetime.utcnow()+timedelta(hours=5,minutes=30)
			text=dto.strftime('%I:%M:%S %p')
		elif text2.startswith('ar'):rns(kec_ar,1)
		elif text2.startswith('zbus'):send_message(text[1:],tidpa);text='Success'
		elif text2.startswith('cg'):
		
			# text=kongu_not;return
			text2=text2.replace('!','')
			z=text2.split('.',2)
			z.insert(1,z[0][3:] if z[0][3:] else None)
			if not z[2:]:z.append(str(chat))
			z[2]=rn(z[2])
			if not z[3:]:z.append(dobl.get(z[2],''))
			snt(smt,(chat,cg,*z[1:]));
		elif text2.startswith('cal'):
			snt(smt,(chat,calf,text2));
		elif text2.startswith('tt'):
			text=ttf(text2.split('.'))
			

			
		elif text2.startswith('uid'):rns(uid)
		elif text2 in ['kid']:text='<a href="https://drive.google.com/open?id=1OmbVxQYS9SKBTG8mCd-h4_gXMK_giNbw">KID</a>'
		elif text2 =='sam':text='@SmartManoj'
		elif text2 =='hh':msgf('b.househusband',chat)
		elif text2 =='kidh':text='''
		- kid
		1 username
		2 pwd
		3 netid pwd
		4 step
		5 android
		6 vpn
		'''
		elif text2 =='kid1':text='cc10'
		elif text2 =='kid2':text='C0mputercentre'
		elif text2 =='kid6':text='https://t.me/SmartManojChannel/10'
		elif text2 =='kid5':text='http://bit.ly/my3krex'
		elif text2 =='kid4':text='http://bit.ly/kecfi'
		elif text2 =='kid3':text=kid3();send_message('@kec_l_py',chat)
		elif text2 =='smc':text='@SmartManojChannel'
		elif text2.startswith('kid'):text='Just Kidding'
		elif text2.startswith('skid'):
			if text2[5:]=='skid.rn':text='rn missing'
			try:
				t=random.choice(string.ascii_letters)
				text=t+str((487+int(text2[:-3])*47)%10000)
				send_message(text2[5:],tidme)
			except Exception as e:
				text=text2[5:]+'invalid rn'

			
		elif re.match(r'^(hey|ha?i+)$',text2.split()[0]):text='Hi '+fname
		elif re.match(r'^(baby|sara)$',text2):text='Hi Baby'
		elif re.match(r'(good|gud) (morning|mrn?g)',text2):text='Have a sweet day...'
		elif re.match(r'(good|gud) (aftrn|afternoon)',text2):text='Have a pleasant day...'
		elif re.match(r'(good|gud) (evng|evening)',text2):text='Have a fabulous day...'
		elif re.match(r'(good|gud) (night|ni8)',text2):text='Have a cute sleep...'
		elif re.match(r'ha ?ha',text2):text=emo('smiling_face')*3
		elif re.match(r'how a?re? (yo)?u',text2):text='I am fine.. '
		elif re.match(r'who a?re? (yo)?u',text2):text='I am Sara.. '
		elif re.match(r'where a?re? (yo)?u',text2):
			h=alink("https://www.google.com/maps/place/11%C2%B016'24.6%22N+77%C2%B036'28.6%22E/@11.2735014,77.6073672,200m/data=!3m2!1e3!4b1!4m6!3m5!1s0x0:0x0!7e2!8m2!3d11.2734996!4d77.607946",'Here')
			text=f"I am Sara.. I was once found at {h}..Find me if u can.. "
		elif re.match(r'^(h*m+|o?k+)$',text2):
			for i in range(5):send_message(text,chat)
		elif re.match(r'^oi+$',text2):text='Oii Baby'
		elif re.match(r'thank (yo)?u|thanks|tq',text2):text='Anytime.. '
		elif re.match(r'what(\'s)?( is )?y?o?ur name',text2):text='I am Sara..'	
		elif re.match(r'(what|wt) (a?re? (yo)?u )?do?i?ng|nothing',text2):text='https://play.google.com/store/apps/details?id=com.gorro.nothing&hl=en_US'
		elif re.match(r'^\d{2}[A-z]{3}\d{3}$',text2.strip()):
			text2=f"rn.{text2}"
			msgf(text2,chat,r=0)
		elif chat in [tidme,tidpa,tidna,tidma,590230821,578901888,569829168]:
			if text2.startswith('bal'):
				snt(hpclbal,(1,chat));
			elif text2==('rsp'):snt(hp_rsp,(chat,))
			elif text2==('rspl'):snt(hp_rsp,(chat,'l'))
			elif text2==('rspm'):snt(hp_rsp,(chat,'s','5'))
			elif text2.startswith('rsplm'):snt(hp_rsp,(chat,'l','2'),{'msg':text2[6:]})
			elif text2.startswith('rspw'):snt(hp_rspw,(chat,text2[5:]))
			elif text2.startswith('hps'):snt(hp_stock2,(text2[4:],chat))
			elif text2.startswith('tv1'):snt(tvs,(chat,text2[4:],1))
			elif chat==tidme:
				if text2.startswith('exec.'):exec(text[5:]);	
				elif text2.startswith('z.'):
					z=text.split('.')
					for _ in (' ','+91','-'):z[1]=z[1].replace(_,'')
					text='';a='.'.join(z[2:])
					for aa in range(0,len(a),160):text+=w2.send(a[aa:aa+160],z[1])
					text=str(text)
				elif text2.startswith('zz.'):text=(w2.get_limit())
			else:send_message('\n'.join([str(chat),name2+cse_tid.get(chat,''),otext,text]),tidme,1);
			

		

		elif chat!=tidme:
			z=' @'+username
			send_message('\n'.join([str(chat),name2+' `'+cse_tid.get(chat,'')+z,otext,text]),tidme,chat!=tidMan);

		if text==text3:return
		send_message(text, chat)	
	except Exception as e:
		exception(e)
		print(e)




@app.route('/')
@app.route('/up/<srvc>')
def main1(srvc='Cool'):
	return f""'<div>You are Rocking Smart - {srvc}</div>'''

def uptime():
	if today_.hour>=9:return
	pause.until(today1+timedelta(hours=9))
	url = 'https://api.uptimerobot.com/v2/editMonitor'
	payload = 'api_key=u452671-7958ec6f5779ecca4c2735e7&format=json&id=779042947'
	headers = {
		'cache-control': 'no-cache',
		'content-type': 'application/x-www-form-urlencoded'
		}
	response = requests.request('POST', url, data=payload, headers=headers)
	print('@',response.text)

def restart():
	while True:
		try:
			v=(datetime.utcnow()+timedelta(hours=5,minutes=30))
			if(5*60<v.hour*60+v.minute<21*60+30):
				requests.head('http://smartmanojbot.herokuapp.com/up/pys',timeout=25)
			sleep(25*60)
		except Exception as e:
			exception(e)
			sleep(60)
			continue


def main():
	last_update_id = None
	while True:
		try:
			updates = get_updates(last_update_id)			
			if updates:
				z=updates.get('result')
				if z and len(z) > 0:
					last_update_id = get_last_update_id(updates) + 1
					echo_all(updates)
			sleep(0.5)
		except Exception as e:
			exception(e)


def anz(r,j=cse_tid):
	for i in j:
		print(i)
		if i in [410390700]:continue
		if i:
			if r[0]=='.':snt(send_message,(r[1:],i))
			else:snt(msgf,(r,i))
def imc():
	bk2=2
	while True:
		try:
			if 1:
				r2=requests.get('http://coe.kongu.edu/caout.php?regno=15csr094',proxies=proxies,timeout=60,headers=headers)
				if r2.reason =='OK' and '14CSC61' in r2.text and '14MAT51' not in r2.text  and 'Invalid' not in r2.text and bk2:
					bk2=0
					msgf('im')
					anz('im')
			if not bk2:break
			sleep(5*60)
		except Exception as e:
			exception(e,0)
			print(e)
			sleep(60)


def o6():
	if tdy:return
	pause.until(datetime.combine(today_,dttime.min)+timedelta(hours=6))
	snt(wish,()) 
	snt(nagu,()) 
	if 0:
		if today_.weekday():msgf('tv1')
		else:msgf('rs.Weekend Chill Baby Chill')
	
tdy=None
if wherey:
	snt(wish2,()) 
	snt(hp_rsp,(),{'k':0}) 
	snt(hpclbal,()) 	
	snt(main,())  
	snt(restart,()) 
	# snt(imc,()) 
	snt(uptime,()) 

	s=today_.strftime('%Y-%m-%d')
	a="SELECT * FROM hp where mdate='{}' order by id".format(s)
	cur.execute(a)
	tdy=bool(cur.rowcount)


	if tdy and (5<today_.hour<22):sleep(20);send_message(version())
	snt(hp_rsp3,())
	snt(o6,())

if __name__ == '__main__':
	# emo1s2()
			
	msgf('''rn4''')
	# msgf('bm.k.san')
	# msgf('rmrc')
	# send_contact(tidme,'z9','')
	# msgf('wa.+917708758665.23')
	sleep(60)

	# app.runrun(debug=1)
	pass

