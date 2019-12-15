import argparse
import itertools

def prase_args():
    parser=argparse.ArgumentParser(description="A tool to generate wordlist")
    parser.add_argument("--minlen",required=True,dest="min_length",type=int)
    parser.add_argument("--maxlen",required=True,dest="max_length",type=int)
    parser.add_argument("-a",help="Use lower case alphabet",action="store_true")
    parser.add_argument("-A",help="Use upper case aplhabet",action="store_true")
    parser.add_argument("-N",help="Use number",action="store_true")
    parser.add_argument("-s",help="Use symbol",action="store_true")
    parser.add_argument("-leet",help="caution!!!leet mode",action="store_true")
    parser.add_argument("-C",help="contain a word",dest="word",default="")
    parser.add_argument("-O",help="Output file",dest="output_file_path",required=True)
    return parser.parse_args()

if __name__=="__main__":
    args=prase_args()
    words=""
    if args.a:
        words+="abcdefghijklmnopqrstuvwxyz"
    if args.A:
        words+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if args.N:
        words+="0123456789"
    if args.s:
        words+="~!@#$%^&*()_+}{[]\|/.,;:"
    if args.leet:
        leet = {'o':'0','O':'0','i':'1','I': '1','z':'2','Z':'2','e':'3','E':'3','a':'4','A':'4','s':'5','S':'$','t':'7','T':'7','B':'8'}
        for i in leet:
            words=words.replace(i,leet[i])
    file=open(args.output_file_path,"w+")
    if len(args.word)==0:
        for i in range(args.min_length,args.max_length+1):
                for j in list(itertools.product(words, repeat=i)):
                    now_word=""
                    for k in j:
                        now_word+=k
                    file.write(now_word+"\n")
                    file.flush()
    else:
        for l in range(0,args.max_length-len(args.word)+1):
            if l==0:
                for k  in list(itertools.product(words,repeat=args.max_length-len(args.word))):
                    sufix=""
                    for kk in k:
                        sufix+=kk
                    file.write(args.word+sufix+"\n")
                    file.flush()
            else:
                for j in list(itertools.product(words, repeat=l)):
                    for k  in list(itertools.product(words,repeat=args.max_length-l-len(args.word))):
                        prefix=""
                        sufix=""
                        for jj in j:
                            prefix+=jj
                        for kk in k:
                            sufix+=kk
                        file.write(prefix+args.word+sufix+"\n")
                        file.flush()

