import matplotlib.pyplot as plt
import math

patrons = 0

Arnold = []
Barry = []

for d in range(1,20): #array for Arnolds guess
	patrons = d/2
	Arnold.append(patrons)

patrons =
for i in range(1,20): #array of Barrys guess
	patrons = math.log10(i)
	Barry.append(patrons)

ResultsX = [5,10,15,20]
ResultsY = [4,10,4,8]

x = range(1,20)

plt.plot(x,Arnold,'r--')
plt.plot(x,Barry,'b--')
plt.plot(ResultsX,ResultsY,'g--')

plt.ylabel('Number of Patrons')
plt.xlabel('Number of Drinks')
plt.title('Number of Patrons Corresponding to the Number of Drinks Consumed')

plt.show()