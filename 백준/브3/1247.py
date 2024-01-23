# input 사용 시 시간초과
from sys import stdin

for i in range(3):

    N = int(stdin.readline())
    lst = []

    for j in range(N):
        lst.append(int(stdin.readline()))
        
    S = sum(lst)
    
    if S > 0:
        print('+')
    
    elif S == 0:
        print(0)
        
    else:
        print('-')
