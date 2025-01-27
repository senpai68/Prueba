import os , requests , re , sys , time , webbrowser
from requests import get
from user_agent import generate_user_agent 
from time import time 
from hashlib import md5 
from random import randrange,choice 
from requests import post as pp 
from user_agent import generate_user_agent as gg 
from random import choice as cc
from random import randrange as rr
hits=0
bads_instgram=0
bads_email=0
BLUE = '\033[94m' ; RESET = '\033[0m' ; BOLD = '\033[1m' ; YELLOW = '\033[93m' ; RED = '\033[91m' ; GREEN = '\033[92m' ; CYAN = '\033[96m' ; MAGENTA = '\033[95m' ; P = '\x1b[1;97m' ; H = '\x1b[1;92m' ; K = '\x1b[1;93m' ; R1 = '\033[1;31;40m' ; X1 = '\033[1;33;40m' ; F1= '\033[1;32;40m' ; C1 = "\033[1;97;40m" ; B1 = '\033[1;36;40m' ; K1 = '\033[1;35;40m' ; V1 = '\033[1;36;40m' ; a32 = '\x1b[38;5;180m' ; a14 = '\x1b[38;5;153m'
ID = input('𝑬𝒏𝒕𝒆𝒓 𝑰𝒅:')
token = input('𝑬𝒏𝒕𝒆𝒓 𝑻𝒐𝒌𝒆𝒏')
K3S63 ='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(K3S63)for i in range(rr(6,9)))
    n2=''.join(cc(K3S63)for i in range(rr(3,9)))
    host=''.join(cc(K3S63)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()