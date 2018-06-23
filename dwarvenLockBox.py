

def DwarvenLockBoxEfficient(A):
	n = len(A)
	B = [[0 for x in range(n)] for y in range(n)]
	for i in range(0,len(A)):
		for j in range(0,len(A)):
			z = j +1
			h = i 
			if i >= j:
				B[i][j] = 0
			else:
				B[i][j] = ((z * (z+1)) / 2) - ((h * (h+1)) / 2)
	return B


A = [1,2,3,4]

print(DwarvenLockBoxEfficient(A))