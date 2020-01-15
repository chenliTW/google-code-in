
def ans(x):
    if x==0:
        return 1
    if x==1:
        return 2
    if x%2==0:
        return ans(x//2)**2
    else:
        return ans(x//2)*ans(x-(x//2))


def main():
    n=input('n = ')
    print(ans(int(n)))

if __name__=="__main__":
    main()