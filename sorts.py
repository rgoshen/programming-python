import time
import random

a_list = [random.randint(0, 20) for _ in range(20)]
# a_list = [122, 1, 2, 3, 6, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b_list = a_list.copy()
c_list = a_list.copy()


def bubble_sort1(list):
    swaps = 0
    list_length = len(list) - 1
    iterations = 0
    for i in range(list_length):
        iterations += 1
        for j in range(list_length):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swaps += 1
    print('swaps:', swaps, 'iterations:', iterations)
    return list


def bubble_sort2(list):
    swaps = 0
    list_length = len(list) - 1
    iterations = 0
    for i in range(list_length):
        iterations += 1
        for j in range(list_length - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swaps += 1
    print('swaps:', swaps, 'iterations:', iterations)
    return list


def bubble_sort3(list):
    swaps = 0
    list_length = len(list) - 1
    iterations = 0
    for i in range(list_length):
        no_swaps = True
        iterations += 1
        for j in range(list_length - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swaps = False
                swaps += 1
            if no_swaps:
                print('swaps:', swaps, 'iterations:', iterations)
                return list
    print('swaps:', swaps, 'iterations:', iterations)
    return list


print('a:', a_list)
print('b:', b_list)
print('c:', c_list)
print('-' * 40)

print('bubble sort1:')
start_bubble1 = time.time()
print(bubble_sort1(a_list))
end_bubble1 = time.time()
print('time:', end_bubble1 - start_bubble1)
print('-' * 40)
print('bubble sort2:')
start_bubble2 = time.time()
print(bubble_sort2(b_list))
end_bubble2 = time.time()
print('time:', end_bubble2 - start_bubble2)
print('-' * 40)
print('bubble sort3:')
start_bubble3 = time.time()
print(bubble_sort3(c_list))
end_bubble3 = time.time()
print('time:', end_bubble3 - start_bubble3)
