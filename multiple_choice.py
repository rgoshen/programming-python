lines = int(input())
choice = []
correct = 0

for i in range(lines * 2):
    choice.append(input().upper())

for i in range(lines):
    if choice[i] == choice[i + lines]:
        correct += 1

print(correct)
