mb = int(input())
months = int(input())

total_earned = mb * months
total_used = 0

for i in range(months):
    total_used += int(input())

print(total_earned-total_used + mb)
