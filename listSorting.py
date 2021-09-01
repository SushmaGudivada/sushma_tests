def bubbleSort(arr):
    n = len(arr)  
    for i in range(n-1):
        for j in range(0, n-i-1):
              if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0	 
	j = 0	 
	k = l	 
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

arr = input("Enter array of elements: ").split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
alg = input("enter algorithm name:")
print("array elements before sorting: ", arr)
if alg == "bubble":
    bubbleSort(arr)
elif alg == "merge":
    mergeSort(arr, 0, len(arr)-1)
elif alg == "insertion":
    insertionSort(arr)
print("elements after sorting: ",arr)