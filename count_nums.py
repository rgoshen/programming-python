import time
import sys

num = input('Enter in the number to count to: ')

n = int(num)

print('recursion limit:', sys.getrecursionlimit())


def count_iterative(n):
    for i in range(1, n):
        # print(i)
        pass


def count_recursive(n):
    if n == 0:
        return
    # print(n)
    count_recursive(n - 1)


start_iterative = time.time()
count_iterative(n)
end_iterative = time.time()
print('iterative time:', end_iterative - start_iterative)

start_recursive = time.time()
count_recursive(n)
end_recursive = time.time()
print('recursive time:', end_recursive - start_recursive)
