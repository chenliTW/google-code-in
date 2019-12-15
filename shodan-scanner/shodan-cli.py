import shodan
import requests
import os
import pydoc
import pprint

api_key=''
api = shodan.Shodan(api_key)

def show_options():
    options='''
1.What's my ip
2.Scanning Host
3.Shodan search to scan ip, post, hostname
0.Exit
    '''
    print(options)

if __name__=="__main__":
    while True:
        show_options()
        command=input("SHODAN> ")
        if command=="1":
            res=requests.get("https://ifconfig.me/ip")
            print("\nYour Ip Address :\n\n"+res.text)
        elif command=="2":
            os.system('clear')
            ip_addr=input("Input Host ip address : ")
            result=api.host(ip_addr)
            output="\033[0;32m"+ip_addr+'\033[0m\nHostnames:               '
            for i in result['hostnames']:
                output+=(i+" ")
            output+='''
City:                    {}
Country:                 {}
Organization:            {}
Number of open ports:    {}

Ports:
'''.format(result['city'],result['country_name'],result['org'],len(result['ports']))
            for i in result['data']:
                product=lambda _:str(i['product']) if 'product' in i else " "
                output+=("    \033[1;34m{:<6}\033[0m  {}\n").format(str(i['port']),product(" "))
            pydoc.pager(output)
        elif command=="3":
            os.system('clear')
            search_word=input("Input your have query to searching : ")
            results = api.search(search_word)
            info=''
            for result in results['matches']:
                hostname=lambda _: result['hostnames'][0] if len(result['hostnames'])>0 else " "
                print()
                info+='\033[0;32m{:<16}\033[0m\033[1;33m{:<10}\033[0m\033[1;34m{}\033[0m    \033[1;35m{}\033[0m\n'.format(result['ip_str'],result['port'],result['isp'],hostname(""))
            pydoc.pager(info)
        elif command=="0":
            print("[+]Exiting...")
            exit(0)
        else:
            print("command not found.Exiting")
            exit(0)
