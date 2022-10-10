# 백준 10989

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 첫 제출 시 공간복잡도로 인해 메모리 초과 발생
# input이 0부터 10000사이의 숫자 10,000,000개 이하.
# -> for 문으로 list에 append하면 메모리 재할당이 이루어져 메모리 효율이 떨어진다.
# -> length가 10000인 list를 만든 후 해당 index 숫자에 +1씩 해준 뒤 출력하는 방식으로 진행
total = int(input())
ls = [0 for i in range(10001)]
for i in range(total):
    n = int(input())
    ls[n]+=1
for i in range(10001):
    if ls[i]!=0:
        for j in range(ls[i]):
            print(i, end='\n')