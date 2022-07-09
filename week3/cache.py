
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
def string_multiplier(string: str):
    return string + string

if __name__ == "__main__":
    print(multiplier(1))
    print(multiplier(1))
    print(multiplier(2))
    print(multiplier(3))
    print(multiplier(2))

    print(string_multiplier("foo"))
    print(string_multiplier("bar"))
    print(string_multiplier("foo"))
    print(string_multiplier("bar"))

# def state_save():
#     calls: int = 0

#     def c():
#         nonlocal calls
#         calls += 1
#         print("calling for the", calls, "time")

#     return c

# f = state_save()

# for i in range(3):
#     f()