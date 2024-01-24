N = int(input())
CT = []

CT.extend(list(map(int, input().split())))

ys = CT.copy()
ms = CT.copy()

for i in range(len(CT)):
    
    ys[i] = ((ys[i] // 30) * 10) + 10
    ms[i] = ((ms[i] // 60) * 15) + 15

if sum(ys) < sum(ms):
    print("Y", int(sum(ys)))
    
elif sum(ms) < sum(ys):
    print("M", int(sum(ms)))
    
else:
    print("Y M", int(sum(ys)))
