s = input()
id = list(map(int, input().split()))
print(s[id[0]:id[1] + 1], s[id[2]:id[3] + 1])
