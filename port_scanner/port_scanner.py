import socket


if __name__=="__main__":
    ip=input("Enter the ip you want to scan :")
    print("-"*50+"\nScaning "+ip+"\n"+"-"*50)
    port=[i for i in range(1,1025)]
    count=0
    for i in port:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        recv=sock.connect_ex((ip,i))
        if recv==0:
            count+=1
            print("\033[0;32m"+"Port "+str(i)+" is open"+"\033[0m")
    print("Finished scaning "+ip+" , "+str(count)+" opening port(s).")