import requests
from clint.textui import progress
import os
import hashlib

image_save_path="./image.iso"

image_base_url="https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/"

check_sum_url="https://spins.fedoraproject.org/static/checksums/Fedora-Spins-31-1.9-x86_64-CHECKSUM"

def download_image(url):
    res=requests.get(url,stream=True)
    content_length=int(res.headers.get('content-length'))
    file=open(image_save_path, 'wb')
    for part in progress.bar(res.iter_content(chunk_size=1024),label="downloading image",expected_size=(content_length/1024) + 1): 
        if part:
            file.write(part)
            file.flush()

def check_sum(version):
    sha256=hashlib.sha256()
    sha256.update(open(image_save_path,"rb").read())
    res=requests.get(check_sum_url)
    correct_hash=res.text.split(version+") = ")[1][:64]
    return str(sha256.hexdigest())==correct_hash

def detect_and_chose_usb():
    res=os.popen("ls /dev/ | grep sd").read()
    print(res)
    res=res.split("\n")[:-1]
    devices=list()
    for i in res:
        if not any(char.isdigit() for char in i):
            devices.append(i)
    os.system("clear")
    if len(res)==0:
        print("no usb found,check before you run this program.\n[-]Exiting...")
        exit()
    for i in range(len(devices)):
        print(str(i+1)+". "+devices[i])
    device=devices[int(input("chose what device you want to burn into : "))-1]
    return device

def burn_to_usb(device):
    os.system("sudo dd if="+image_save_path+" of=/dev/"+device+" bs=1M")


if __name__=="__main__":
    spin_opt=[
        {"name":"Cinnamon","image_url":"Fedora-Cinnamon-Live-x86_64-31-1.9.iso"},
        {"name":"KDE","image_url":"Fedora-KDE-Live-x86_64-31-1.9.iso"},
        {"name":"LXDE","image_url":"Fedora-LXDE-Live-x86_64-31-1.9.iso"},
        {"name":"LXQt","image_url":"Fedora-LXQt-Live-x86_64-31-1.9.iso"},
        {"name":"MATE_Compiz","image_url":"Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso"},
        {"name":"SoaS","image_url":"Fedora-SoaS-Live-x86_64-31-1.9.iso"},
        {"name":"Xfce","image_url":"Fedora-Xfce-Live-x86_64-31-1.9.iso"}
    ]
    os.system("clear")
    for i in range(len(spin_opt)):
       print(str(i+1)+". "+spin_opt[i]["name"])
    user_opt=int(input("Chose the spin you want to download : "))-1
    download_image(image_base_url+spin_opt[user_opt]["image_url"])
    if not check_sum(spin_opt[user_opt]["image_url"]):
        print("check sum failed!!!\nExiting ...")
        os.remove(image_save_path)
        exit(0)
    else:
        print("[+]checksum passed")
    device=detect_and_chose_usb()
    check_user=input("Are you sure to burn Fedora "+spin_opt[user_opt]["name"]+" into "+device+" ?[Y/N]")
    if check_user=="Y" or check_user=="y":
        os.system("sudo umount -f /dev/"+device+"*")
        method=input("Does your target system supports UEFI ?[Y/N]")
        if method=="Y" or method=="y":
            os.system("clear")
            print("format "+device+" into fat32")
            os.system("sudo mkdosfs -F 32 -I /dev/"+device)
            print("copy image to usb..")
            os.system("sudo mount /dev/"+device+"  /media/$USER/fedora")
            os.system("sleep 1")
            #target=os.popen("lsblk -o MOUNTPOINT -nr /dev/"+device).read()
            target="/media/$USER/fedora/"
            print("cp "+image_save_path+" "+target)
            os.system("sudo cp "+image_save_path+" "+target)
            os.system("sync")
            os.system("sudo umount -f /dev/"+device+"*")
            print("done")
        elif method=="N" or method=="n":
            os.system("clear")
            print("burning please wait some (lot) moment...")
            burn_to_usb(device)
            print("done")
        else:
            print("user Abort\n[-]Exiting ...")
            exit(0)
    else:
        print("user Abort\n[-]Exiting ...")
        exit(0)
