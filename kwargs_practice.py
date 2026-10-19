
def add_all(*args):
    return sum(args)

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    print(add_all(1, 2, 3))
    print(add_all(10, 20))


    print("-" * 20)

    show_info(name="小明", age=20, city="湛江")