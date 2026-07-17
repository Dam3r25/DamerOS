from colorama import Fore
import psutil
import math
import os
import platform
import winsound
import time
import tkinter as tk

root = tk.Tk()
root.withdraw()

x = root.winfo_screenheight()
y = root.winfo_screenwidth()

hdd = psutil.disk_usage('/')

base = os.path.dirname(os.path.abspath(__file__))

audio = os.path.join(base, "song.wav")

audio2 = os.path.join(base, "valve.wav")

memoria = math.floor(hdd.total / 1073741824)

Ram2 = psutil.virtual_memory()

save = os.path.join(base, "savefile.txt")

RamUsado = math.floor(Ram2.used / 1073741824)

RamTotal = math.floor(Ram2.total / 1073741824)

cuadrados = "████"

importar3 = []

winsound.PlaySound(audio, winsound.SND_ASYNC | winsound.SND_FILENAME)

commando = ""

listaa = []

listab = []

with open(save, "r") as importar:
    importar2 = importar.readlines()

    for i in range(len(importar2)):
        importar3 += importar2[i].strip().split("|")

    for i in range(len(importar3)):
        if i % 2 == 0:
                listab.append(importar3[i])
        else:
            listaa.append(importar3[i])

ruta = "Home"
print(platform.processor())
print("Loading...")

ramtemp = math.floor(psutil.virtual_memory().total / 1073741824)

cpuname = platform.processor()

print(platform.processor())

def hl3():
    clear()
    clear()
    print("loading.")
    time.sleep(0.5)
    clear()
    print("loading..")
    time.sleep(0.5)
    clear()
    print("loading...")
    time.sleep(0.5)
    clear()
    print("loading.")
    time.sleep(0.5)
    clear()
    print("loading..")
    time.sleep(0.5)
    clear()
    print("Welcome to Half life 3 beta!")
    print("Detecting if device is authorized by Valve")
    time.sleep(0.5)
    print("Detecting steam")
    time.sleep(2)
    print("Detecting steam | success")
    time.sleep(2)
    print("Detecting device hardware")
    time.sleep(1)
    print("Detecting device hardware | ERROR")
    time.sleep(1)
    print(Fore.RED + "NON VALVE DEVICE DETECTED. CLOSING GAME.")

os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cd1():
    global cd
    cd = input(Fore.GREEN + "DamerOS@localhost" + Fore.WHITE + ":" + Fore.BLUE + ruta + Fore.WHITE + "$  ").lower()

def cmd():
    global cow
    global ruta
    global memoria
    if commando == "neofetch":
        print("                          ")
        print(f"            @@@@@           {cpuname}")
        print(f"       @@@@     @@@@        {ramtemp} GB RAM")
        print(f"   @@@@            @@@      {memoria} GB TOTAL DISK SPACE")
        print("     @@@            @@@   ")
        print("      @@@            @@     OS: DamerOS")
        print("       @@            @@@    Shell: Python")
        print(f"        @@           @@     Resolution: {y} x {x} ")
        print("         @@         @@@     Kernel: 6.13.5-arch1-1")
        print(f"         @@@       @@       Memory: {RamUsado} / {RamTotal}")
        print("          @@@   @@@       ")
        print(f"           @@@@            {Fore.BLACK + cuadrados}{Fore.RED + cuadrados}{Fore.GREEN + cuadrados}{Fore.LIGHTRED_EX + cuadrados}{Fore.BLUE + cuadrados}{Fore.MAGENTA + cuadrados}{Fore.CYAN + cuadrados}{Fore.WHITE + cuadrados}")
        print(f"          @                {Fore.BLACK + cuadrados}{Fore.RED + cuadrados}{Fore.GREEN + cuadrados}{Fore.LIGHTRED_EX + cuadrados}{Fore.BLUE + cuadrados}{Fore.MAGENTA + cuadrados}{Fore.CYAN + cuadrados}{Fore.WHITE + cuadrados}")
        print("                          ")
        return 

    elif commando == "cd":
        while True:
            ruta = ("home")
            cd1()

            if cd.startswith("touch "):
                commandosp = cd.split()
                archivo = commandosp[1]
                print(archivo)
                os.system('cls' if os.name == 'nt' else 'clear')
                contenido = input("")
                listaa.append(contenido)
                os.system('cls' if os.name == 'nt' else 'clear')
                listab.append(archivo)
                with open(save, "a") as archivo1:
                        archivo1.write(archivo + "|" + contenido + "\n")
            
            elif cd == "dir":
                print(listab)

            elif cd.startswith("rm "):
                commandorm = cd.split(" ")
                rmarchivo = commandorm[1]
                with open(save, "r") as archivo:
                    lineas = archivo.readlines()
                with open(save, "w") as archivo:
                    for linea in lineas:
                        if rmarchivo not in linea:
                            archivo.write(linea)

            elif cd.startswith("cat "):
                try:
                    cmdsp = cd.split()
                    cmd1 = cmdsp[1]
                    cmd2 = (listaa.index(cmd1))
                    print(listab[cmd2])
                except ValueError:
                    print("This file doesn't exist.")

            elif cd == "exit":
                return
            
            elif cd == "cd":
                print(Fore.RED + "Invalid command")
            
            else:
                print(Fore.RED + "Invalid command")
        
    elif commando == "hl3":
            winsound.PlaySound(audio2, winsound.SND_FILENAME | winsound.SND_ASYNC)
            os.system('cls' if os.name == 'nt' else 'clear')
            hl3()

    elif commando == "cowsay":
        cow = input ("message : ")
        cow2 = len(cow) * "-"
        print(" ", cow2)
        print("<", cow, ">")
        print(" ", cow2)
        print(" \   ^__^ ")
        print("  \  (oo)\_______")
        print('     (__)\       )\/\ ')
        print("         ||----w |")
        print("         ||     ||")

    if commando == "help":
        print("Neofetch - View your components")
        print("CD - View your folders")
        print("     Touch (Name of file) for creating files")
        print("     Cat (Name of file) for reading files")
        print("Cowsay - Muuu")
        print("Whoami - Get username")
        print("rev (text) - Reverse text")
        print("clear - Deletes previus commands.")
        return
    
    elif commando == "whoami":
        print("DamerOS")

    elif commando.startswith("rev"):
        rev1 = commando.replace("rev", "")
        rev2 = rev1[::-1]
        print(rev2)

    elif commando == "clear":
        clear()

    elif commando == "sudo rm -rf / --no-preserve-root":
        print("\033[91m[!] !!! DELETING SYSTEM FILES !!!\033[0m")
        time.sleep(1.5)

        # --- BLOQUE 1 ---
        print("Removing /bin/bash... OK")
        print("Removing /bin/cat... OK")
        print("Removing /bin/chmod... OK")
        print("Removing /bin/chown... OK")
        print("Removing /bin/cp... OK")
        print("Removing /bin/date... OK")
        print("Removing /bin/echo... OK")
        print("Removing /bin/grep... OK")
        print("Removing /bin/ln... OK")
        print("Removing /bin/ls... OK")
        print("Removing /bin/mkdir... OK")
        print("Removing /bin/mv... OK")
        print("Removing /bin/ps... OK")
        print("Removing /bin/pwd... OK")
        print("Removing /bin/rm... OK")
        time.sleep(0.1) # Pausa dramática de carga de disco

        # --- BLOQUE 2 ---
        print("Removing /boot/vmlinuz-linux... OK")
        print("Removing /boot/initramfs-linux.img... OK")
        print("Removing /boot/grub/grub.cfg... OK")
        print("Removing /dev/null... OK")
        print("Removing /dev/random... OK")
        print("Removing /dev/urandom... OK")
        print("Removing /dev/sda1... OK")
        print("Removing /dev/stdout... OK")
        print("Removing /etc/fstab... OK")
        print("Removing /etc/passwd... OK")
        print("Removing /etc/shadow... OK")
        print("Removing /etc/group... OK")
        print("Removing /etc/hosts... OK")
        print("Removing /etc/resolv.conf... OK")
        print("Removing /etc/sudoers... OK")
        time.sleep(0.1)

        # --- BLOQUE 3 ---
        print("Removing /etc/network/interfaces... OK")
        print("Removing /etc/ssh/sshd_config... OK")
        print("Removing /etc/apt/sources.list... OK")
        print("Removing /etc/profile... OK")
        print("Removing /home/damer/.bashrc... OK")
        print("Removing /home/damer/.config/damerOS... OK")
        print("Removing /home/damer/Desktop/juegos... OK")
        print("Removing /home/damer/Documents/secretos.txt... OK")
        print("Removing /home/damer/Downloads/todo_legal.mp4... OK")
        print("Removing /home/damer/Music/Untitled.wav... OK")
        print("Removing /home/damer/Pictures/avatar.png... OK")
        print("Removing /home/damer/.ssh/id_rsa... OK")
        print("Removing /home/damer/.cache/google-chrome... OK")
        print("Removing /lib/libc.so.6... OK")
        print("Removing /lib/libm.so.6... OK")
        time.sleep(0.1)

        # --- BLOQUE 4 ---
        print("Removing /lib/libpthread.so.0... OK")
        print("Removing /lib/modules/kernel/drivers... OK")
        print("Removing /lib64/ld-linux-x86-64.so.2... OK")
        print("Removing /media/usb_drive/backup_final... OK")
        print("Removing /mnt/external_hdd... OK")
        print("Removing /opt/discord/Discord... OK")
        print("Removing /opt/spotify/spotify... OK")
        print("Removing /proc/cpuinfo... OK")
        print("Removing /proc/meminfo... OK")
        print("Removing /proc/sys/kernel/panic... OK")
        print("Removing /root/.bash_history... OK")
        print("Removing /root/.ssh/authorized_keys... OK")
        print("Removing /run/systemd/notify... OK")
        print("Removing /sbin/fdisk... OK")
        print("Removing /sbin/init... OK")
        time.sleep(0.1)

        # --- BLOQUE 5 ---
        print("Removing /sbin/iptables... OK")
        print("Removing /sbin/reboot... OK")
        print("Removing /sbin/shutdown... OK")
        print("Removing /srv/www/index.html... OK")
        print("Removing /sys/block/sda/size... OK")
        print("Removing /sys/class/power_supply/BAT0... OK")
        print("Removing /sys/kernel/security... OK")
        print("Removing /tmp/.X11-unix... OK")
        print("Removing /usr/bin/python3... OK")
        print("Removing /usr/bin/gcc... OK")
        print("Removing /usr/bin/git... OK")
        print("Removing /usr/bin/nano... OK")
        print("Removing /usr/bin/vim... OK")
        print("Removing /usr/bin/curl... OK")
        print("Removing /usr/bin/wget... OK")
        time.sleep(0.1)

        # --- BLOQUE 6 ---
        print("Removing /usr/bin/sudo... OK")
        print("Removing /usr/lib/python3.10/os.py... OK")
        print("Removing /usr/lib/python3.10/sys.py... OK")
        print("Removing /usr/share/fonts... OK")
        print("Removing /usr/share/icons... OK")
        print("Removing /usr/share/doc... OK")
        print("Removing /usr/local/bin/node... OK")
        print("Removing /var/log/auth.log... OK")
        print("Removing /var/log/syslog... OK")
        print("Removing /var/log/nginx/access.log... OK")
        print("Removing /var/mail/damer... OK")
        print("Removing /var/spool/cron/crontabs... OK")
        print("Removing /var/www/html/site... OK")
        print("Removing /var/lib/mysql/mysql.db... OK")
        print("Removing /var/lib/dpkg/status... OK")
        print("Removing /var/cache/apt/archives... OK")
        print("Removing /usr/games/sl... OK")
        print("Removing /usr/games/cowsay... OK")
        print("Removing /home/damer/.local/share/Steam... OK")
        print("Removing /etc/init.d/rc... OK")
        print("Removing /lib/firmware/intel... OK")
        print("Removing /boot/EFI/BOOT/BOOTX64.EFI... OK")
        print("Removing /sys/firmware/efi/efivars... OK")
        print("Removing /dev/loop0... OK")
        time.sleep(0.5) # Un frenazo antes del final

        print("DamerOS was deleted.")

        time.sleep(1.0)
        print("\n\033[91m[!] KERNEL PANIC: NO ROOT FILE SYSTEM FOUND.")
        
        time.sleep(3.0)
        exit()
        
    else:
        print(Fore.RED + "Invalid command")

while True:
    commando = input(Fore.GREEN + "DamerOS@localhost" + Fore.WHITE + ":" + Fore.BLUE + "~" + Fore.WHITE + "$  ").lower()
    cmd()