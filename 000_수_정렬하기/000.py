'''
## 소스1
N = int(input())
M = []
for i in range(N):
    M.append((int(input())))

M = sorted(M)
for i in range(len(M)):
    print(M[i])
'''

'''
## 소스 2
N = int(input())
M = set()
for i in range(N):
    M.add(int(input()))
M = list(M)
M.sort()
for i in range(len(M)):
    print(M[i]) 
'''

## 버블정렬로 정렬하기
N = int(input())

M = []

for i in range(N):
    M.append(int(input()))

for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

for n in M:
    print(n)
