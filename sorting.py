def bubble_sort(items):
    """把列表从小到大排序（冒泡排序）。原地改，返回排序后的列表。"""
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items



def selection_sort(items):
    """选择排序，原地改，返回列表。"""
    n = len(items)


    for i in range(n - 1):
        min_idx = i


        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j


        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]

    return items





def insertion_sort(items):
    """插入排序，原地改，返回列表。"""
    n = len(items)


    for i in range(1, n):
        current = items[i]
        j = i - 1


        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1


        items[j + 1] = current

    return items


# --- 测试代码 ---
if __name__ == "__main__":
    print(insertion_sort([5, 3, 8, 1]))
    print(insertion_sort([1, 2, 3]))
    print(insertion_sort([]))


if __name__ == "__main__":
    print("冒泡排序：", bubble_sort([5, 3, 8, 1]))
    print("选择排序：", selection_sort([5, 3, 8, 1]))
    print("选择排序：", selection_sort([1, 2, 3]))
    print("选择排序：", selection_sort([]))

