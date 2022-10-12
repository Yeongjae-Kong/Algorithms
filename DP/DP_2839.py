# 백준 2839

# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 정확하게 N킬로그램 배달해야 할 때, 배달하는 봉지의 최소 개수를 출력한다. 
# 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# DP의 핵심 개념은 memoization을 통해 반복 계산 최소화

n=int(input())
arr = [5001]*(n+5) #memoization
arr[3] = 1 
arr[5] = 1

for i in range(6, n+1):
    arr[i] = min(arr[i-3], arr[i-5]) + 1

if arr[n]<5001:
    print(arr[n]) 
else:
    print(-1)