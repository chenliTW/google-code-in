import requests

image_save_path="./image.iso"

image_url="https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso"

def download_image():
    res=requests.get(image_url,stream=True)
    content_length=response.headers.get('content-length')
    file=open(image_save_path, 'wb')
    total_length = int(r.headers.get('content-length'))
    for part in progress.bar(r.iter_content(chunk_size=1024), expected_size=(content_length/1024) + 1): 
        if part:
            file.write(part)
            file.flush()


if __name__=="__main__":