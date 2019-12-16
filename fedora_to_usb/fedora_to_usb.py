import requests
from clint.textui import progress
import os
import hashlib

image_save_path="./image.iso"

image_url="https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso"

check_sum_url="https://getfedora.org/static/checksums/Fedora-Workstation-31-1.9-x86_64-CHECKSUM"

def download_image():
    res=requests.get(image_url,stream=True)
    content_length=int(res.headers.get('content-length'))
    file=open(image_save_path, 'wb')
    for part in progress.bar(res.iter_content(chunk_size=1024),label="downloading image",expected_size=(content_length/1024) + 1): 
        if part:
            file.write(part)
            file.flush()

def check_sum():
    sha256=hashlib.sha256()
    sha256.update(open(image_save_path,"rb").read())
    res=requests.get(check_sum_url)
    correct_hash=res.text.split("SHA256 (Fedora-Workstation-Live-x86_64-31-1.9.iso) = ")[1][:64]
    return str(sha256.hexdigest())==correct_hash

if __name__=="__main__":
    #download_image()
    if not check_sum():
        print("check sum failed!!!\nExiting ...")
        os.remove(image_save_path)
        exit(0)
    else:
        print("[+]checksum passed")