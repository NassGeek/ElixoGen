import random
import time
import colorama
import os
from os import system
from colorama import Back, Fore, Style

system("title " + "ELIXO GEN BY eldoxx#5549")

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nitrocode = ''

with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"Merci d'utiliser Elixo Gen !\n")

            nitroFile.close()

colorama.init(autoreset=True)

print(Fore.WHITE + '███████╗██╗     ██╗██╗  ██╗ ██████╗      ██████╗ ███████╗███╗   ██╗    ██╗   ██╗██████╗ ')
print(Fore.WHITE + '██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║    ██║   ██║╚════██╗')
print(Fore.RED + '█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║    ██║   ██║ █████╔╝')
print(Fore.RED + '██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║    ╚██╗ ██╔╝ ╚═══██╗')
print(Fore.BLUE + '███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║     ╚████╔╝ ██████╔╝')
print(Fore.BLUE + '╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝      ╚═══╝  ╚═════╝ ')
print(Fore.RED + '                                                       by eldoxx#5549\n                                                    WE SUPPORT RUSSIANS HACKERS...')
time.sleep(1.5)
print(Fore.LIGHTGREEN_EX + 'Lancement...')
print(Fore.LIGHTGREEN_EX + 'Launching...')
print('')
print(Fore.LIGHTGREEN_EX + 'TikTok : @nassgeek.exe')
print(Fore.LIGHTBLACK_EX + 'Settings : (changable soon...)')
print(Fore.BLUE + '    Language : fr')
print(Fore.BLUE + "    double-check : " + Fore.GREEN + 'on')
print('')
print('double-check by elixo team softwares (C)')
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
    for i in range(5):
        nitrocode = ''
        
        time.sleep(0.2)

        for i in range(24):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"

        print(Fore.BLUE + "Status : " + Fore.RED + "[INVALIDE] " + Fore.RED + f"               https://discord.gift/{nitrocode}")

        with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close()

    system('cls')

    print(Fore.BLUE + "Status : " + Fore.GREEN + "[VALIDE]   " + Fore.GREEN + f"               https://discord.gift/{nitrocode}")

    with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"[ VALIDE ! ] https://discord.gift/{nitrocode}\n")

            nitroFile.close()
    
    print(Fore.GREEN + 'Reprend dans 5 secondes !')
    time.sleep(5)
    system("cls")