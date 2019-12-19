import pyshark
import operator
import os
import hexdump

def show_opts():
    question='''

    1-Top 10 Visited Sites
    
    2-User-Agents List
    
    3-Connection details
    
    4-String Grep Mode
    
    5-ALL Ip List
    
    6-Port Used
      
    '''
    print(question)
def topten():
    record=dict()
    for i in cap:
        try:
            host=i['http'].host
            try:
                record[host]+=1
            except:
                record[host]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    output=(" count |                        host\n")
    for i in range(min(len(record),10)):
        output+="{:<7}|  {}\n".format(record[i][1],record[i][0])
    os.system("clear")
    print(output)
    input("press <enter> to continue ...")
def user_agent():
    record=dict()
    for i in cap:
        try:
            user_agent=i['http'].get('User-Agent')
            if user_agent!=None:
                try:
                    record[user_agent]+=1
                except:
                    record[user_agent]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    output=(" count |                 User-Agent\n")
    for i in range(len(record)):
        output+="{:<7}|  {}\n".format(record[i][1],record[i][0])
    os.system("clear")
    print(output)
    input("press <enter> to continue ...")
def conn_details():
    print("\nDo you need all connection details (Y/N)\n")
    opt=input("Y/N ? > ")
    if not (opt=="Y" or opt=="y"):
        return
    print("All protocol Details")
    id_to_name={'6':'TCP','17':'UDP'}
    for i in cap:
        try:
            proto=id_to_name[i['ip'].proto]
            print("Protocol: "+proto+"  -  Source: "+i['ip'].src+" - PORT: "+i[proto].srcport+" ----> Destination: "+i['ip'].dst+" - PORT: "+i[proto].dstport)
        except:
            pass
def search_string():
    string=input("Search String : ")
    for i in cap_raw:
        try:
            id_to_name={'6':'TCP','17':'UDP'}
            proto=id_to_name[i['ip'].proto]
            if bytes(string, 'utf-8') in hexdump.dehex(i[proto].payload_raw[0]):
                for j in hexdump.dehex(i[proto].payload_raw[0]):
                    if chr(j).isprintable():
                        print(chr(j),end='')
                    else:
                        print('.',end='')
                print()
        except:
            pass
    input("press <enter> to continue ...")
def all_ip_list():
    record=dict()
    for i in cap:
        try:
            IPa,IPb=i['ip'].src,i['ip'].dst
            try:
                record[IPa]+=1
            except:
                record[IPa]=1
            try:
                record[IPb]+=1
            except:
                record[IPb]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    output=(" count |     IP\n")
    for i in range(len(record)):
        output+="{:<7}|  {}\n".format(record[i][1],record[i][0])
    os.system("clear")
    print(output)
    input("press <enter> to continue ...")    
def ports_used():
    record=dict()
    for i in cap:
        try:
            id_to_name={'6':'TCP','17':'UDP'}
            proto=id_to_name[i['ip'].proto]
            PORTa,PORTb=i[proto].srcport,i[proto].dstport
            try:
                record[PORTa]+=1
            except:
                record[PORTa]=1
            try:
                record[PORTb]+=1
            except:
                record[PORTb]=1
        except:
            pass
    record=sorted(record.items(), key=operator.itemgetter(1))[::-1]
    output=(" count |  port\n")
    for i in range(len(record)):
        output+="{:<7}|  {}\n".format(record[i][1],record[i][0])
    os.system("clear")
    print(output)
    input("press <enter> to continue ...")  

if __name__=="__main__":
    file_path=input("Location Pcap File > ")
    cap_raw = pyshark.FileCapture(file_path,include_raw=True,use_json=True)
    cap=pyshark.FileCapture(file_path)
    actions=[
        topten,
        user_agent,
        conn_details,
        search_string,
        all_ip_list,
        ports_used
    ]
    while True:
        show_opts()
        operation=int(input("Operation Number > "))
        actions[operation-1]()