'''
N = int(input())
for i in range(N):
    name,age = input().split()
    print(name,age)
    pp=Pp(name,age)

S=""
class Pp():
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = int(Age)

    def print(self):
        print(f"Name:{self.Name}, Age:{self.Age}")
                
lst = []                
N = int(input())
for i in range(N):
    name,age = input().split()
    pp=Pp(name,age)
    lst.append(pp)

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i].Age < lst[j].Age:
            lst[i], lst[j] = lst[j], lst[i]

for p in lst:
    print(f"Name:{p.Name}, Age:{p.Age}")


class ex():
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def print(self):
        for i in range(N):
            if lit[i][1] > M:
                print(lit[i][0])

lit = []
N,M = map(int,input().split())
for i in range(N):
    A, B = map(str,input().split())
    lit.append((A,int(B)))

#print(lit[0][0])
ex1= ex(3,2)
ex1.print()
'''
'''
A = " "
num = int(input())
for i in range(num): 
    for j in range(i):
        print(A,end="")
    for k in range(num-i,0,-1):
        print("*",end="")
    print()



while True:
    N = int(input())
    if N==1:
        print("one")
    elif N==2:
        print("two")
    elif N==3:
        print("three")
    else:
        break

m = {1: 'one', 2: 'two', 3: 'three'}
while True:
    n = int(input())
    if n in m:
        print(m[n])
    else:
        break
'''
'''
N1 = int(input())
N2 = int(input())

if N1 >=3 and N2 >=3:
    print("High")
elif N1< 3 and N2 <3:
    print("Low")
else:
    print("Mid")
    '''
'''
N1,N2 =map(int,input().split())

if N1 >12:
    print(f"{N1-12:02d} : {N2} PM")
elif N1 ==12:
    print(f"{N1:02d} : {N2} PM")
else:
    print(f"{N1:02d} : {N2} AM")
    '''

'''
lst = []
N = int(input())

for i in range(N):
    N1,N2,N3 = map(int,input().split())
    lst.append([N1,N2,N3])

for i in range(1,N):
    lst[i][0] = lst[i][0] + min(lst[i-1][1], lst[i-1][2])
    lst[i][1] = lst[i][1] + min(lst[i-1][0], lst[i-1][2])
    lst[i][2] = lst[i][2] + min(lst[i-1][0], lst[i-1][1])
print(min(lst[N-1]))
'''
# N1,N2 = map(float, input().split())

# if N1 >= 4.0 and N2 >= 4.0:
#     print("A grade")
# elif N1 >= 3.0 and N2 >= 3.0:
#     print("B grade")
# else:
#     print("F grade")

# N = int(input())

# for i in range(N,0,-3):
#     print(i)

# N1,N2 = map(int, input().split())
# k = 1
# for i in range(N1):
#     for j in range(N2):
#         print(k,end=" ")
#         k+=1
#     print()


'''
for i in range(N):
    V = str(input())
    
    for j in range(len(V)-1):
        if
print(V)

'''

# N = int(input())
# for i in range(N):
#     s = input()
#     count = 0
    
#     for j in s:
#         if j == '(':
#             count += 1
#         else:
#             count -= 1
        
#         if count < 0:
#             break
    
#     if count == 0:
#         print("YES")
#     else:
#         print("NO")

# N1,N2 = map(int, input().split())
# k = 1
# for i in range(N1):
#     row = list(range(k, k + N2))
#     if i % 2 == 1:
#         row = row[::-1]
#     print(*row)
#     k += N2

'''lst = []

for i in range(10):
    N1 = int(input())
    lst.append(N1 % 42)
    
print(len(set(lst)))'''



'''class Ex:
    def __init__(self,A,B):
        self.A = A
        self.B = B
    def __add__(self,other):
        return Ex(self.A + other.A, self.B + other.B)
    def __sub__(self,other):
        return Ex(self.A - other.A, self.B - other.B)
    def __str__(self):
        return f"{self.A:.1f}, {self.B:.1f}"

N1, N2 = map(float, input().split())
ex1 = Ex(N1, N2)

N1, N2 = map(float, input().split())
ex2 = Ex(N1, N2)

add = ex1 + ex2
sub = ex1 - ex2

print(f"add = ({add})")
print(f"sub = ({sub})")
print(f"center = ({(ex1.A+ex2.A)/2:.1f}, {(ex1.B+ex2.B)/2:.1f})")
'''

# str1 = str(input())
# str2 =''.join(reversed(str1))
# if str1 == str2:
#     print(str1,"\n입력하신 단어는 회문(Palindrome)입니다.")

# lst = []
# for i in range(5):
#     N = int(input())
#     lst.append(N)
# print(lst)

# del lst[3:]
# print(lst)


# N = int(input())
# arr = list(map(int, input().split()))

# for i in range(N - 1):
#     for j in range(N-i-1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     print(arr)

N, M = map(int, input().split())
box = [0] * N
for l in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        box[x] = k
print(*box)