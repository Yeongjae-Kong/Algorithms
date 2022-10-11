# 퀵 정렬 - 배열 가운데 원소(피벗)를 기준으로 아래는 작은 값, 위는 큰값
# 해당 과정 분할된 리스트가 1(혹은 0)일 때까지 재귀적으로 반복
# 시간복잡도 O(nlogn), worst=O(n^2)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)