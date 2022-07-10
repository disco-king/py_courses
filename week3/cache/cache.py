
def cache_decorator(f):
    cache = {}

    def wrapper(*args, **kwargs):
        nonlocal cache

        hash_val = hash(str(*args) + str(**kwargs))

        signal = "cache"

        if hash_val not in cache:
            #returning from cache
            cache[hash_val] = f(*args, **kwargs)
            signal = "call"

        #returning from call
        print("returning from", signal)
        return cache[hash_val]

    return wrapper


@cache_decorator
def multiplier(number: int):
    return number * 2

@cache_decorator
def adder(item):
    return item + item


if __name__ == "__main__":

    print(multiplier(1))
    print(multiplier(1))
    print(multiplier(2))
    print(multiplier(3))
    print(multiplier(2))

    print(adder("foo"))
    print(adder("bar"))
    print(adder("foo"))
    print(adder("bar"))

    print(adder([1, 2, 3]))
    print(adder([4, 5, 6]))
    print(adder([1, 2, 3]))
    print(adder([4, 5, 6]))

