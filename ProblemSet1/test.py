array = [11,10,9,15]
def part_A(cups_of_gold):
	max_gold_so_far = 0
	#your code here
	maxGoldSoFar = 0
	for i in range(0,(len(cups_of_gold)-1)):
		for j in range(i,len(cups_of_gold)):
			gold = cups_of_gold[j] - cups_of_gold[i]
			if gold > maxGoldSoFar:
				maxGoldSoFar = gold
	return maxGoldSoFar


def part_D(A):
    #your code here
	maxGoldSoFar = 0
	M=[A[0]]
	
	for i in range(0,(len(A))):
			if A[i] < M[-1]: #finds min
				M.append(A[i])
			if maxGoldSoFar < A[i]:
				maxGoldSoFar = A[i]
	
	if len(A) == len(M):
		return 0		
	return maxGoldSoFar - M[-1]



def part_C(A):
    #your code here
	maxGoldSoFar = 0
	M=[A[0]]
	jIndex =0
	for i in range(0,(len(A))):
		jIndex=i+1
		if jIndex < len(A):
			gold = A[jIndex] - A[i]
			if gold == A[jIndex] - A[i]:
				if gold > maxGoldSoFar:
					maxGoldSoFar = gold
	return maxGoldSoFar


print(part_A(array))
print(part_D(array))