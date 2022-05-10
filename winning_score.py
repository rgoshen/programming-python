apple_3points = int(input())
apple_2points = int(input())
apple_1point = int(input())

banana_3points = int(input())
banana_2points = int(input())
banana_1point = int(input())

apple_total = apple_3points * 3 + apple_2points * 2 + apple_1point
banana_total = banana_3points * 3 + banana_2points * 2 + banana_1point

if(apple_total > banana_total):
    print("A")
elif(apple_total < banana_total):
    print("B")
else:
    print("T")
