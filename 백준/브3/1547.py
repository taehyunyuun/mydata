M = int(input())

X = []
Y = []

answer = 1

for i in range(M):
    
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
for i in range(M):
    
    if X[i] == answer:
        answer = Y[i]
        
    elif Y[i] == answer:
        answer = X[i]
        
print(answer)
