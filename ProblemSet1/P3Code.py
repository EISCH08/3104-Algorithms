
def Function(n):
	A = [1,-1,2] #initializing the base cases

	for i in range(3,n):
		val = (A[i-1]*A[i-2])+A[i-3]
		A.append(val)
	return A


def Recursion(n):
	if n == 1:
		return 1
	if n == 2:
		return -1
	if n == 3:
		return 2

	else:
		return (Recursion(n-1)* Recursion(n-2)+Recursion(n-3))
		





print(Function(10))
print(Recursion(10))

