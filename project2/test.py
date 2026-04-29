import math
N = int(input())

lst = []
for i in range(1, int(math.isqrt(N)) + 1):
    if N % i == 0:
        lst.append(i)
        if i != N // i:         
            lst.append(N // i)

for i in range(len(lst) - 1):
    for j in range(len(lst)-1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
for k in lst:
    print(f"{k}(은)는 {N}의 약수입니다.")