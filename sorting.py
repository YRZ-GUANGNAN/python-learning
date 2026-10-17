def bubble_sort(items):
    """把列表从小到大排序。原地改，返回排序后的列表。"""
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



if __name__ == "__main__":
    print(bubble_sort([5, 3, 8, 1]))
    print(bubble_sort([1, 2, 3]))
    print(bubble_sort([]))