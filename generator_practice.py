
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def even_numbers(limit):
    for x in range(0, limit + 1):
        if x % 2 == 0:
            yield x



if __name__ == "__main__":
    for x in count_up(3):
        print(x)

    print("---")

    for x in even_numbers(10):
        print(x)