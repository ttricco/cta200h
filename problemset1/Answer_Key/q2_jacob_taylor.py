import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Recursive Factorial Function
def factorial(n):
        if n < 1:
                return 1
        else:
                return n*factorial(n-1)

""" A """
#Function that gets the Binomial coefficient for a given n,k
def get_binomial_coeeficiant(n,k):
        return factorial(n)/(factorial(k)*factorial(n-k))

""" B """
#Prints the first 20 coefficients

for i in range(20):
    Values = ""
    for j in range(i+1):
        Values += str(get_binomial_coeeficiant(i,j)) + " "
    print("Line #%d: %s"%(i+1,Values))

""" C """
#Set Parameters
p = 0.6
k = 4
n = 6

#Function to calculate the probability of getting k heads in n rolls wth bias p
def calculate_probabaility(n,k,p):
        return 100*round(get_binomial_coeeficiant(n,k)*(p**k)*((1-p))**(n-k),4)

prob = calculate_probabaility(n,k,p)
print("Probability is: " + str(prob) + "%!")

""" d """

#Function to run the experiment simulation N times
def Run_Experiment_N_Times(N):
        
        successful = 0.0
        #Run experiment N times and keep track of how many succeed
        for j in range(int(N)):
            heads = 0
            tails = 0
            #run experiment
            for i in range(n):
                #randomly select in between 1 and 100
                rand = random.randint(1,100)
                #if if less than p% count as heads
                if(rand <= 100*p):
                    heads += 1
                #otherwise tails
                else:
                    tails += 1
            #Check if experiment was successful
            if (heads >= k):
                successful += 1
        #return the percentage than were successful
        return round((successful/N),4)*100

#Run the experiment N times for N in [1,1000]
x = np.arange(1,1000,5)
vfunc = np.vectorize(Run_Experiment_N_Times)
y = vfunc(x)

#Compare to theoretical probability in a graph
y2 = np.zeros_like(x)
for i in range(k,n+1):
        y2 = y2 + calculate_probabaility(n,i,p)
#plot
plt.plot(x,y,label='Experimental')
plt.plot(x,y2,label='Theoretical')
plt.legend()
plt.show()

raw_input("Press Enter to continue...")
        

