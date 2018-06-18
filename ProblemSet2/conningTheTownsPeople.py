

import numpy as np  #you may need to install this package
from timeit import default_timer as timer
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
	
	if len(A) == len(M): #all are in reverse order
		return 0		
	return maxGoldSoFar - M[-1]

times = []
print('Part D results:')
for seed in range(10):  #running the loop for 10 iterations, using seed for the random generator
    np.random.seed(seed)  # sets the seed for the random generator
    cups_of_gold = np.random.randint(low=1,high=1001, size=1000)#cups_of_gold is list with 1000 elements, where the elements are positive integers in range(1, 1000)

    start_A = timer()   #start the timer for part A
    result_A = part_A(cups_of_gold) #run part A algorithm
    total_time_A = timer() - start_A    #calculate total time for part A

    start_D = timer()   #start the timer for part D
    result_D = part_D(cups_of_gold) #run part D algorithm
    print(result_D)
    total_time_D = timer() - start_D    #calculate total time for part D

    times.append([total_time_A, total_time_D])  #add the times to the list

    if result_A != result_D:    #checks if the algorithms are calculating the same result
        print('One of your algorithms has a mistake.')
        quit()

times = np.array(times) #makes the list print nicely
print()
print('[Part A Times, Part D Times]')
print(times)








def linearSearch(A,v):
	for i in range(0,len(A)):
		if A[i]==v:
			return i
	return "NIL"	




