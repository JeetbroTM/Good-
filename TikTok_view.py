import requests
import re
import shutil
import os
import time
from base64 import b64decode
from urllib.parse import unquote
from bs4 import BeautifulSoup as parser
import glob
import os
import requests
import random
import string
a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
a7 = '\x1b[38;5;13m'
a8 = '\x1b[1;30m'
a9 = '\x1b[1;37m'
a10 = '\x1b[38;5;52m'
a11 = '\x1b[38;5;8m'
a12 = '\x1b[38;5;220m'
a13 = '\x1b[38;5;7m'
a14 = '\x1b[38;5;153m'
a15 = '\x1b[38;5;18m'
a16 = '\x1b[38;5;48m'
a17 = '\x1b[38;5;22m'
a18 = '\x1b[38;5;196m'
a19 = '\x1b[38;5;88m'
a20 = '\x1b[38;5;226m'
a21 = '\x1b[38;5;136m'
a22 = '\x1b[38;5;216m'
a23 = '\x1b[38;5;166m'
from pystyle import Colors, Colorate
from pystyle import Colors, Colorate
from pystyle import Write, Colors
logo = Colorate.Horizontal(Colors.blue_to_red, '\n ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄         \n  ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄       \n ▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄     \n ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██     \n ▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒   \n ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░   \n ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░   \n    ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒      \n          ░  ░           ░  ░   ░        ░  ░    \n                                                ', 1)
ua2 = random.choice([
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.13.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.302 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; ART-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BytedanceWebview/d8a21c6 musical_ly_32.7.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US FalconTag/61374D85-86A1-4AD2-8F26-7B84887D1220',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Snapchat/12.68.0.22 (like Safari/8614.1.25.0.31, panda)',
    'Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.13.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.311 Mobile Safari/537.36'])

def generate_random_string(length):
    letters = string.ascii_lowercase
    return (lambda .0 = None: for _ in .0:
random.choice(letters)None)(range(length)())

domain = generate_random_string(10)
os.system('clear')
print(logo)
TOKEN = input('\x1b[1;32mToken Bott :\x1b[38;5;220m ')
CHAT_ID = input('\x1b[1;32mID Telegramtt :\x1b[38;5;220m ')

class App:
    
    def __init__(self):
        self.baseurl = 'https://zefoy.com'
        self.baseheaders = {
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua2 }

    
    def create_session(self):
        modheaders = self.baseheaders
        modheaders['Sec-Fetch-Dest'] = 'image'
        modheaders['Sec-Fetch-Mode'] = 'no-cors'
        modheaders['Accept'] = 'image/avif,image/webp,*/*'
        print(logo)
        print('\x1b[1;32mCodek Bo Bott Hat la Xwarawa Bnusa')
        self.session = requests.Session()
        req = self.session.get(self.baseurl, headers = self.baseheaders).text
        if requests.exceptions.ConnectionError:
            exit('Keshay internet haya')
        capturl = self.baseurl + re.findall('(\\/\\w+\\.php\\?(.*))cl', req, re.MULTILINE)[0][0].split('"')[0].replace('amp;', '')
        captchapayload = { }
        pars = parser(req, 'html.parser').find('form', {
            'method': 'POST' })
        for z in pars('input'):
            captchapayload[z['name']] = z['value']
            if z['name'] == 'token':
                captchapayload['token'] = ''
            captchapayload['captcha'] = z['name']
            saveimage = self.session.get(capturl, headers = modheaders, cookies = self.session.cookies, stream = True)
            wr = open('/sdcard/image.png', 'wb')
            saveimage.raw.decode_content = True
            shutil.copyfileobj(saveimage.raw, wr)
            wr.close()
            image_files = glob.glob('/sdcard/image.png')
            kid(image_files)
            None(None, None)
            if not None:
                pass
        code = input('\x1b[1;37mCod Bnusa :\x1b[1;32m ')
        if code not in list('Rr'):
            captchapayload[captchapayload['captcha']] = code
            del captchapayload['captcha']
            postcapt = self.session.post(self.baseurl, headers = self.baseheaders, cookies = self.session.cookies, data = captchapayload).text
            self.nexturl = self.baseurl + '/' + parser(postcapt, 'html.parser').find('div', {
                'class': 't-views-menu' }).find('form')['action']
            self.gpayload = {
                parser(postcapt, 'html.parser').find('input', {
                    'type': 'search' })['name']: '' }
            return None
        if requests.exceptions.ConnectionError:
            exit('Keshay internet haya')
        if AttributeError:
            print('\x1b[1;31mCode Halaya')
        print('\x1b[1;32mWenaka La Bott a')

    
    def postone(self):
        modheaders = self.baseheaders
        del modheaders['Upgrade-Insecure-Requests']
        modheaders['X-Requested-With'] = 'XMLHttpRequest'
        modheaders['Sec-Fetch-Dest'] = 'empty'
        modheaders['Sec-Fetch-Site'] = 'same-origin'
        modheaders['Origin'] = 'https://zefoy.com'
        print('')
        nest = self.session
        vturl = input('\x1b[1;37mLink Video Dane :\x1b[1;32m ')
        self.gpayload[list(self.gpayload.keys())[0]] = vturl
        test = nest.post(self.nexturl, headers = modheaders, cookies = nest.cookies, data = self.gpayload).text
        texter = b64decode(unquote(test[::-1])).decode('utf-8').replace('\n', '  ')
        if 'Please enter valid video URL' in texter:
            print('\x1b[1;31mLink halaya')
            if requests.exceptions.ConnectionError:
                print('\x1b[1;31mkeshay internet haya ')
        self.submit(modheaders, vturl)

    
    def submit(self, modheaders, vturl):
        print('  ')
        sender = self.session.post(self.nexturl, headers = modheaders, cookies = self.session.cookies, data = self.gpayload).text
        pars = parser(b64decode(unquote(sender[::-1])).decode('utf-8').replace('\n', '  '), 'html.parser').find('form').find('input')
        payload = {
            pars['name']: pars['value'] }
        submitr = self.session.post(self.nexturl, headers = modheaders, cookies = self.session.cookies, data = payload).text
        texter = b64decode(unquote(submitr[::-1])).decode('utf-8').replace('\n', '  ')
        if 'Successfully' in texter:
            print('\r\x1b[1;32m1000 \x1b[1;37mView Nerdra')
            print('\x1b[1;37mBy : \x1b[1;32m@Abdullha_404')
        print('\r')
        if AttributeError:
            print('\r\x1b[1;31mBAN 1000 VIEW')
        if requests.exceptions.ConnectionError:
            print('\r\x1b[1;31mkeshay internet haya')
        for i in range(1, 301):
            print(f'''\r\x1b[1;37mBusta \x1b[1;32m{300 - i}\x1b[1;37m Chrka''', end = '')
            time.sleep(1)



def kid(image_files):
    for image_file in image_files:
        file = open(image_file, 'rb')
        response = requests.post('http://tinyurl.com/api-create.php', data = {
            'url': f'''http://{domain}.com/{image_file}''' })
        response.raise_for_status()
        tinyurl = response.text.strip()
        response = requests.post(f'''https://api.telegram.org/bot{TOKEN}/sendPhoto''', data = {
            'chat_id': CHAT_ID }, files = {
            'photo': file })
        response.raise_for_status()
        None(None, None)
        if not None:
            pass
        if requests.RequestException:
            e = None
            print('Error')
            e = None
            del e
            e = None
            del e
        return None

if __name__ == '__main__':
    os.system('clear')
    app = App()
    app.create_session()
    app.postone()
    return None

