import time

class RepeatDecorator:

    def __init__(self, count: int, start_sleep_time: float,
                    factor: int, border_sleep_time: float):
        self.count = count
        if start_sleep_time > border_sleep_time:
            self.pause = border_sleep_time
        else:
            self.pause = start_sleep_time
        self.factor = factor
        self.border_time = border_sleep_time

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            
            start = time.perf_counter()
            func()
            for i in range(self.count - 1):
                time.sleep(self.pause)
                print("pause:", self.pause, end = " ")
                self._update_sleep_time()
                curr = time.perf_counter()
                print("time passed:", curr - start)
                func()

        return wrapper

    def _update_sleep_time(self):
        if self.pause < self.border_time:
            self.pause *= 2 ** self.factor
        if self.pause > self.border_time:
            self.pause = self.border_time


@RepeatDecorator(5, 1, 1, 10)
def func():
    print("func called")

if __name__ == "__main__":
    func()





# def repeat_decorator(addition: str):

#     def actual_decorator(f):

#         def wrapper():
#             f()
#             print(addition)
    
#     return wrapper

#     return actual_decorator


# @repeat_decorator("Johnny!")
# def func():
#     print("here's", end=' ')

# func()
