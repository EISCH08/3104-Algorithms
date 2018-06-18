import matplotlib.pyplot as plt
import math

y=[]
z = []

for n in range(1,50):
	x = n**2 + n/20
	x2 = n**2 + math.log10(n) 
	y.append(x)
	z.append(x2)

i = range(1,50)

plt.plot(i,y,'r--' )
plt.plot(i,z, 'b--')

plt.ylabel('Run time')
plt.xlabel('Number of iterations')
plt.title('Runtime of Each Function Based on Iterations')

plt.show()
