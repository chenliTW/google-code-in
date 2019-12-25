import matplotlib.pyplot as plt
import sys

plt.figure()
plt.xlabel('term')
plt.xlim((1,22))
plt.ylabel('value')
plt.ylim((0,18000))

y_value=list()
x_value=list()

now=int(1)

for i in sys.stdin:
    x_value.append(now)
    now+=1
    y_value.append(int(i))

plt.plot(x_value,y_value)

plt.show()