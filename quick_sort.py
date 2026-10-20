def quick_sort(items):
    """返回一个从小到大排好序的新列表（不要求原地）。"""
    if len(items) <= 1:
        return items

    pivot = items[0]
    less = [x for x in items[1:] if x < pivot]
    greater = [x for x in items[1:] if x >= pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def binary_search(items, target):
    """在已排好序的列表里查找 target，返回下标；找不到返回 -1。"""
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
    print("快速排序：")
    print(quick_sort([5, 3, 8, 1]))
    print(quick_sort([1, 2, 3]))
    print(quick_sort([]))

    print("\n二分查找：")
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 7))
    print(binary_search(arr, 4))
    print(binary_search(arr, 9))
    print(binary_search(arr, 1))
