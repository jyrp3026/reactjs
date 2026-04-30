
# import math
# N = int(input())

# lst = []
# for i in range(1, int(math.isqrt(N)) + 1):
#     if N % i == 0:
#         lst.append(i)
#         if i != N // i:         
#             lst.append(N // i)

# for i in range(len(lst) - 1):
#     for j in range(len(lst)-1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# for k in lst:
#     print(f"{k}(은)는 {N}의 약수입니다.")

# for i in range(5):
#     print('+' * i + '#' + '+' * (5 - 1 - i))


# def solution(numer1, denom1, numer2, denom2):
#     N1 = numer1
#     D1 = denom1
#     N2 = numer2
#     D2 = denom2
#     answer = [N1,D1,N2,D2]
#     return answer

def solution(numer1, denom1, numer2, denom2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)
    answer = [numer // g, denom // g]
    return answer