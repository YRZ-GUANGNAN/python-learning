def quick_sort(items):
    """返回一个从小到大排好序的新列表（这个版本不要求原地）"""

    if len(items) <= 1:
        return items


    pivot = items[0]


    less = []
    greater = []


    for x in items[1:]:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)


    return quick_sort(less) + [pivot] + quick_sort(greater)



if __name__ == "__main__":
    print(quick_sort([5, 3, 8, 1]))
    print(quick_sort([1, 2, 3]))
    print(quick_sort([]))


def binary_search(items, target):

    left = 0
    right = len(items) - 1


    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 7))
    print(binary_search(arr, 4))
    print(binary_search(arr, 9))
    print(binary_search(arr, 1))


def quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = items[0]


    less = [x for x in items[1:] if x < pivot]
    greater = [x for x in items[1:] if x >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)



if __name__ == "__main__":
    print(quick_sort([5, 3, 8, 1]))
    print(quick_sort([1, 2, 3]))
    print(quick_sort([]))