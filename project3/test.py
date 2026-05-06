# def fight(p1, c1, p2, c2):
#     if c1 == c2:
#         return min(p1, p2)
#     wins = {(2,1), (3,2), (1,3)}
#     if (c1, c2) in wins:
#         return p1
#     return p2

# def tournament(cards, i, j):
#     if i == j:
#         return i 
#     mid = (i + j) // 2
#     left  = tournament(cards, i, mid)
#     right = tournament(cards, mid + 1, j)
#     return fight(left, cards[left-1], right, cards[right-1])


# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#     print(f"#{test_case}", tournament(cards, 1, N))

N1 = int(input())
k = 1
if N1 <=0:
    print("INPUT ERROR!")
for i in range(1,N1+1):
    if N1 % 2 == 0 or N1>50:
        print("INPUT ERROR!")
    else:
        lst = list(range(k,k+i))
        if i % 2 == 0:
            lst = lst[::-1]
    print(*lst)
    k += i
