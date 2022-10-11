# 삽입 정렬 - 단순히 배열 i부터 끝까지 i+1과 비교하며 swap
# 시간복잡도는 O(n^2)

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