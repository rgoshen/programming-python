lines = int(input())
choice = [input().upper() for _ in range(lines * 2)]
correct = sum(choice[i] == choice[i + lines] for i in range(lines))
print(correct)
