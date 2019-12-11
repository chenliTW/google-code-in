import hashlib

def do_hash(method,word):
    if method=="1":
        md5=hashlib.md5()
        md5.update(word.encode())
        return md5.hexdigest()
    elif method=="2":
        sha1=hashlib.sha1()
        sha1.update(word.encode())
        return sha1.hexdigest()
    elif method=="3":
        sha224=hashlib.sha224()
        sha224.update(word.encode())
        return sha224.hexdigest()
    elif method=="4":
        sha256=hashlib.sha256()
        sha256.update(word.encode())
        return sha256.hexdigest()
    elif method=="5":
        sha384=hashlib.sha3_384()
        sha384.update(word.encode())
        return sha384.hexdigest()
    elif method=="6":
        sha512=hashlib.sha512()
        sha512.update(word.encode())
        return sha512.hexdigest()
    
def burte_hash(hash_target,wordlist):
    table={32:1,40:2,56:3,64:4,96:5,128:6}
    method=table[len(hash_target)]
    wordlist=wordlist.split('\n')
    for word in wordlist: 
        if str(do_hash(str(method),word))==hash_target:
            print("\033[92m"+"[+]found --> "+hash_target+" = "+word+"\033[0m")
            return
    print("\033[91m"+"[-]sorry no word match hash"+"\033[0m")
    return

if __name__=="__main__":
    while True:
        decision=str(input("To Hash press 1 and to Crack Hash press 2 :"))
        if decision=="1":
            question="What kind of HASHING\n1.md5\n2.sha1\n3.sha224\n4.sha256\n5.sha384\n6.sha512\nEnter the number:"
            hash_decision=str(input(question))
            plain_string=str(input("Enter the thing to be Hashed:"))
            print(plain_string+" = "+do_hash(hash_decision,plain_string))
        elif decision=="2":
            hashed_string=str(input("Enter the Hash :"))
            word_list_path=str(input("Enter name of password list :"))
            try:            
                word_list=open("./"+word_list_path,"r")
            except FileNotFoundError:
                print("\033[91m"+"[-]wordlist file not found!!!"+"\033[0m")
                continue
            burte_hash(hashed_string,word_list.read())
        else:
            print("unsupported command")