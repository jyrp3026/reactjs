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

# N1 = int(input())
# k = 1
# if N1 <=0:
#     print("INPUT ERROR!")
# for i in range(1,N1+1):
#     if N1 % 2 == 0 or N1>50:
#         print("INPUT ERROR!")
#     else:
#         lst = list(range(k,k+i))
#         if i % 2 == 0:
#             lst = lst[::-1]
#     print(*lst)
#     k += i

# def solution(array, height):
#     return sum(1 for h in array if h > height)

# array = list(map(int,input().split()))
# hei = int(input())
# array.append(hei)

# print(solution(array,hei))

# def solution(my_str,n):
#     answer = []
#     for i in range(0, len(my_str), n):
#         answer.append(my_str[i:i+n])
#     return answer


# solution1 = "abc1Addfggg4556b"
# solution2 = "abcdef123"

# print(solution(solution1,6))

# def solution(numbers):
#     answer = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#     for i, answer in enumerate(answer):
#         numbers = numbers.replace(answer, str(i))
#     return int(numbers)

# solution1 = "onetwothreefourfivesixseveneightnine"
# print(solution(solution1))

# def solution(dots):
#     answer = dots
#     if(answer[1][1] - answer[0][1]) / (answer[3][0] - answer[2][0]) == (answer[3][1] - answer[2][1]) / (answer[1][0] - answer[0][0]):
#         return 1
#     elif(answer[2][1] - answer[0][1]) / (answer[3][0] - answer[1][0]) == (answer[3][1] - answer[1][1]) / (answer[2][0] - answer[0][0]):
#         return 1
#     elif(answer[3][1] - answer[0][1]) / (answer[2][0] - answer[1][0]) == (answer[2][1] - answer[1][1]) / (answer[3][0] - answer[0][0]):
#         return 1
#     else:
#         return 0    

# solution1 = [[1, 4], [9, 2], [3, 8], [11, 6]]
# solution2 = [[3, 5], [4, 1], [2, 4], [5, 10]]

# print(solution(solution1))

def solution(age):
    answer = list(str(age))
    result = ""
    for i in range(len(answer)):
        result += chr(ord('a') + int(answer[i]))
    return result
    

solution1 = 24

print(solution(solution1))


