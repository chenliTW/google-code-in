import time
import random
import numpy
import matplotlib.pyplot as plt
from numba import jit

def gen_random(n):
    a=list()
    for i in range(n):
        now_a=list()
        for j in range(n):
            now_a.append(random.randint(-2147483648,2147483647))
        a.append(now_a)
    return a

def use_hardcode(a,b):
    n=len(a)
    result=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                result[i][j]+=(a[i][r]*b[r][j])

@jit
def use_hardcodewithnumba(a,b):
    n=len(a)
    result=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                result[i][j]+=(a[i][r]*b[r][j])

def use_numpy(a,b):
    a.dot(b)
    

def main():
    plt.figure()
    plt.xlabel('n')
    plt.ylabel('time(s)')
    hardcode_time=list()
    hardcodewithnumba_time=list()
    numpy_time=list()
    x_label=[(x+1) for x in range(200)]
    for i in x_label:
        a,b=gen_random(i),gen_random(i)
        start_time = time.time()
        use_hardcode(a,b)
        hardcode_time.append(time.time()-start_time)
        start_time = time.time()
        use_hardcodewithnumba(numpy.array(a),numpy.array(b))
        hardcodewithnumba_time.append(time.time()-start_time)
        start_time = time.time()
        use_numpy(numpy.array(a),numpy.array(b))
        numpy_time.append(time.time()-start_time)
        print(str(hardcode_time[-1])+" vs "+str(hardcodewithnumba_time[-1])+" vs "+str(numpy_time[-1]))
    plt.plot(x_label,hardcode_time,color='red')
    plt.plot(x_label,hardcodewithnumba_time,color='orange')
    plt.plot(x_label,numpy_time,color='blue')
    plt.show()
if __name__=="__main__":
    main()