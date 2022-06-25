arr = [6, 3, 5, 2, 7, 4, 1, 8]

n = len(arr)

for i in range(0, n-1): # n-1번 반복
    min_idx = i
    for j in range(i+1, n): # n-1, n-2, … , 2, 1 번 = (n-1)(n)/2번
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
print(arr)