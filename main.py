import random
import time
import colorama
import os
from os import system
from colorama import Back, Fore, Style

system("title " + "KORO GEN BY NassGeek#5549")

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nitrocode = ''

with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"Merci d'utiliser Koro Gen ! Rejoint le discord ! : [NON DISPONIBLE]\n")

            nitroFile.close()

colorama.init(autoreset=True)

print(Fore.LIGHTBLACK_EX + '                                 ██ ▄█▀ ▒█████   ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ ')
time.sleep(0.5)
print('                                 ██▄█▒ ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ')
time.sleep(0.5)
print(Fore.LIGHTBLACK_EX + '                                ▓███▄░ ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒')
time.sleep(0.5)
print('                                ▓██ █▄ ▒██   ██░▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒')
time.sleep(0.5)
print(Fore.LIGHTBLACK_EX + '                                ▒██▒ █▄░ ████▓▒░░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░')
time.sleep(0.5)
print('                                ▒ ▒▒ ▓▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ')
time.sleep(0.5)
print(Fore.LIGHTBLACK_EX + '                                ░ ░▒ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░')
time.sleep(0.5)
print('                                ░ ░░ ░ ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ ')
time.sleep(0.5)
print(Fore.LIGHTBLACK_EX + '                                ░  ░       ░ ░     ░         ░ ░           ░    ░  ░         ░ ')
time.sleep(0.5)
print(Fore.RED + '                                                       by NassGeek#5549')
time.sleep(1.5)
print('Lancement...')
print('')
print('')
print('                                                                                TikTok : @nassgeek.exe')
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
print('                         Pour voir tout tes codes générés, ouvre NITRO EZ.txt')

time.sleep(3.0)

while True:
    nitrocode = ''

    for i in range(24):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}"

    print(Fore.BLUE + "Status : " + Fore.GREEN + "[GENERER] " + Fore.RED + f"               https://discord.gift/{nitrocode}")

    with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close()