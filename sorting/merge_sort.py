# 분할 정복 패러다임에 기반, 전부 절반으로 나눈다. 
# 최대한 분할한 뒤(logn) bottom-up방식으로 대소비교해가면(n) 시간복잡도는 O(nlogn)

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr

n=int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums = merge_sort(nums)

for i in nums:
    print(i)