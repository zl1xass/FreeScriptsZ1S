import os
import time
from colorama import init, Fore, Back, Style
from termcolor import colored
def init():
    pass

def clear_system():
    os.system("clear")          #Ekranı Temizler

def install_package(install):
    print(f"{install} İndiriliyor...")
    time.sleep(1)
    os.system(f"sudo pacman -S {install}")

def main_menu():
    clear_system
    time.sleep(1)
    print(Fore.RED + "ZLixas Script hayırlı günler diler" + Fore.RESET)
    time.sleep(1)
    while True:
        print(Fore.RED + """Ne istiyorsununuz
                1-Nmap  İndir
                2-Nmap OS arama kullan 
                3-Ping ArchLinux
                4-Çıkış yap               """ + Fore.RESET)
        
        Tercih = input("> Hangisini istiyorsun: ")

        if Tercih == "1":
            print("Nmap indiriliyor")
            time.sleep(1)
            install_package("nmap")
        elif Tercih == "2":
            targetSug = input("Lütfen Target IP'yi yada Domaini yazınız: ")
            os.system(f"sudo nmap -O {targetSug}")
        elif Tercih == "3":
            print("Arch linux pingleniyor...")
            os.system("ping archlinux.org -c 4")
        elif Tercih == "4":
            print("Programdan Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek lütfen tekrar deneyiniz!")

if __name__ == "__main__":
    main_menu()




    