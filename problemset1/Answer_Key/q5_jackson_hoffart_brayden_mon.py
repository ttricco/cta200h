import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-1.0)

def F(x,d):
    return (f(x+d)-f(x))/d

d = np.logspace(-14, -4, num=50)

plt.plot(d,F(1,d),'o')
plt.xscale('log')
plt.ylim([0.999,1.0005])
plt.xlabel('$\delta$')
plt.ylabel('f\'(1)')
plt.savefig('p5.pdf')
plt.show()

print('\n')
print('Things start to get funky below 10e-11.')
print('\n')
