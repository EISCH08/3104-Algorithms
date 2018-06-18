def SelectionSort(A):
	count =0
	while count!=(len(A)-1):
		key = A[count]
		save = count
		for i in range(count,len(A)):
			if A[i] < key:
				key = A[i]
				save = i
		val = A[count]		
		A[count] = key
		A[save] = val

		count=count+1
	return A
	

array = [1,4,5,2,2,1,6,7 ]

print(SelectionSort(array))			

