N = int(input())
nums = []

for i in range(N) : 
    nums.append(int(input()))

# Insert Sort
for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        i -= 1
nums.reverse() #작은 수부터 출력
for i in range(len(nums)):        
	print(nums.pop())