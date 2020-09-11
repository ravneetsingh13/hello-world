#wap to shift all the 0's to the left and 1's to the right
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
n=len(arr)
left = 0
right = n-1
while(left<right):
	while(arr[left]==0):
		left+=1
	while (arr[right]==1):
		right-=1
	if(left<right):
		arr[left] = 0
		arr[right] = 1
		left+=1
		right-=1
print(arr)