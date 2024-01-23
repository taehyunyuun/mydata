x, y, w, h = map(int, input().split())

lst = [x, w - x, y, h - y]

print(min(lst))
