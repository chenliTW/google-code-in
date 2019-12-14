import requests

def check_by_status_code_200(url,username,suffix):
    return requests.get(url+username+suffix).status_code==200

if __name__=="__main__":
    username=input("username :")
    site={
        'Github':{'url':'https://github.com/','check':check_by_status_code_200},
        'Instergram ':{'url':'https://www.instagram.com/','check':check_by_status_code_200},
        'Twitter':{'url':'https://twitter.com/','check':check_by_status_code_200},
        'Pinterest':{'url':'https://www.pinterest.it/','check':check_by_status_code_200},
        'Vk':{'url':'https://vk.com/','check':check_by_status_code_200}
    }
    found=False
    for i in site:
        if site[i]['check'](site[i]['url'],username,""):
            found=True
            print("\033[0;32m"+"[+]User Present in "+i+"\033[0m")
    if not found:
        print("\033[0;31m[-]User not found in our site list\033[0m")