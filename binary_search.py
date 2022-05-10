sorted_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'lemon', 'mango',
                 'nectarine', 'orange', 'papaya', 'peach', 'pear', 'plum', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while last >= first:
        mid = (first + last) // 2
        if list[mid] == target:
            return True
        elif list[mid] > target:
            last = mid - 1
        else:
            first = mid + 1

    return False


print(binary_search(sorted_fruits, 'banana'))
print(binary_search(sorted_fruits, 'kiwi'))
