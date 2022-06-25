# 하한의 시간 복잡도를 낮춘 정렬
arr = [6, 3, 5, 2, 7, 4, 1, 8]

n = len(arr)
loop_flag = true
for i in range(n-1, 0, -1): # n-1번
	for j in range(i):  # n-2번
		if arr[j] > arr[j+1]:
		    arr[j], arr[j+1] = arr[j+1], arr[j]
            loop_flag = false
   
print(arr)