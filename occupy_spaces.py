N = int(input())
yesterday = input()
today = input()
count = 0

for i in range(N):
    if yesterday[i].upper() == 'C' and yesterday[i] == today[i]:
        count += 1
print(count)
