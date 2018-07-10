import math
import random
import string
import matplotlib.pyplot as plt
file = open("Census.txt","r")

def CensusArray():
	file = open("Census.txt","r")
	names=[]
	for i in range(0,88799):
		x = file.readline()
		y = x[0:15]
		y = y.replace(" ", "")
		names.append(y) 
	return names	


def HashFunction(word, n):
	sum =0
	for i in word:
		sum+=string.ascii_uppercase.index(i)
	return sum%n
def NewHashFunction(word, n):
	sum =0
	for i in word:
		sum+=string.ascii_uppercase.index(i)
		sum*=7
	return sum%n


def CensusHash(A,n):
	count = math.floor(len(A)/2)
	namesRandom = [None] * count 
	longestStringPerN = [0] *n
	for i in range(0,count):
		x = random.randint(0,88798)
		namesRandom[i] = A[x]
	hashTable=[None] * n
	countArray = [0] * n
	for i in namesRandom:
		index = HashFunction(i,n)
		keyValue = [i,index]
		if hashTable[index] ==None: #unit doesnt already exists
			hashTable[index] = list([keyValue])
			countArray[index] = 1
		else: #collision
			hashTable[index].append(keyValue)
			countArray[index]+=1
		longestStringPerN.append(max(countArray))

	return hashTable, countArray, longestStringPerN
	
def FindLongestBin(A):
	count = 0
	for i in range(0,len(A)):
		if A[i] > count:
			count = A[i]
			index = i
	return count, i


names = CensusArray()

hashedNames, hashedCount, longestString =CensusHash(names,200)

longestList, indexInArray = FindLongestBin(hashedCount)

#creates the histogram
n, bins, patches = plt.hist(hashedCount, 200, facecolor='blue', alpha=0.5)
plt.xlabel('Number of Strings in a Bin')
plt.ylabel('Number of Bins containing X Value of Strings')
plt.title('Histogram of our Hash Function')
plt.show()

#creates the lg graph
xlg= list(range(0,44599))
lg = []
for i in range(0,44599):
	val = 2*math.log(i+1,2)
	lg.append(val)
print(lg)
#creates the uniform hash graph
uniformHash = []
value = 1
for i in range(0,44599):
	if i%200 == 0:
		value+=1
	uniformHash.append(value)


x = list(range(0,len(hashedCount)))


plt.plot(x,hashedCount)
plt.xlabel('Bins of HashTable')
plt.ylabel('Number of Entries in Bin')
plt.title('Hash Table Representation of Half US Last Names')
plt.show()


xLongest = list(range(44599))

plt.plot(xlg,uniformHash)
plt.xlabel('Total Number of Strings Hashed')
plt.ylabel('Length of the Longest List')
plt.title('The Length of the Longest List After Each Hash for a Unifrom Hash')
plt.show()

plt.plot(xLongest,longestString)
plt.xlabel('Total Number of Strings Hashed')
plt.ylabel('Length of the Longest List')
plt.title('The Length of the Longest List After Each Hash')
plt.show()
