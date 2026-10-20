def log(func):
    def wrapper(*args, **kwargs):

        print(f"调用 {func.__name__}，参数 {args}")


        result = func(*args, **kwargs)

        print(f"{func.__name__} 返回 {result}")

        # 4. 把结果交出去
        return result

    return wrapper



@log
def add(a, b):
    return a + b


print(add(3, 4))
