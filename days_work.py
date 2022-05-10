p = int(input())
b = int(input())
d = int(input())

number_of_bottlecaps = p // b if(b != 0) else 0
leftover_paint = p % number_of_bottlecaps if(number_of_bottlecaps != 0) else p
total_profit = number_of_bottlecaps * d + leftover_paint

print(total_profit)
