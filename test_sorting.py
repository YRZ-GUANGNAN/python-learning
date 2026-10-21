from sorting import bubble_sort, selection_sort, insertion_sort
from quick_sort import quick_sort


def test_bubble_sort():
    assert bubble_sort([5, 3, 8, 1]) == [1, 3, 5, 8]


def test_selection_sort():
    assert selection_sort([5, 3, 8, 1]) == [1, 3, 5, 8]


def test_insertion_sort():
    assert insertion_sort([5, 3, 8, 1]) == [1, 3, 5, 8]


def test_quick_sort():
    assert quick_sort([5, 3, 8, 1]) == [1, 3, 5, 8]

# ============ 边界测试 ============

def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single():
    assert bubble_sort([5]) == [5]


def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_selection_sort_empty():
    assert selection_sort([]) == []


def test_selection_sort_single():
    assert selection_sort([5]) == [5]


def test_insertion_sort_empty():
    assert insertion_sort([]) == []


def test_insertion_sort_single():
    assert insertion_sort([5]) == [5]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single():
    assert quick_sort([5]) == [5]


def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]


def test_quick_sort_duplicates():
    assert quick_sort([3, 1, 3, 2]) == [1, 2, 3, 3]