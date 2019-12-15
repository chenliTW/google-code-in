import zipfile
import argparse

def prase_args():
    parser = argparse.ArgumentParser(description="A tool for brute forcing encrypted zip file")
    parser.add_argument('--wordlist','-w', type=str, required=True, help='wordlist path')
    parser.add_argument('--zipfile','-z', type=str, required=True, help='zipfile path')
    return parser.parse_args()

if __name__=="__main__":
    args=prase_args()
    try:
        wordlist=open(args.wordlist,'r')
    except:
        print("Error while opening wordlist")
        exit(0)
    try:
        zip_file=zipfile.ZipFile(args.zipfile)
    except:
        print("Error while opening zipfile")
        exit(0)
    cracked=False
    for word in wordlist.read().split('\n'):
        try:
            zip_file.extractall(pwd=bytes(word,'utf-8'))
            print("\033[0;32m[+]Successfully crack the zip file, password is :"+word+"\033[0m")
            print("The zip file is automated extracted by this script!!!")
            cracked=True
            break
        except:
            pass
    if not cracked:
        print("\033[0;31m[-]Sorry,can't crack this zip file with the wordlist\033[0m")