month = int(input())
day = int(input())

if month >= 2 and month <= 2 and day < 18 or month < 2:
    print('Before')
elif month <= 2 and day > 18 or month > 2:
    print('After')
else:
    print('Special')
