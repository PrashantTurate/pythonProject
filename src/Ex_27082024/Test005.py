import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(f"start time : {start_time}")
        func()
        end_time = time.time()
        print(f"end_time is : {end_time}")
        print(f"Time taken by function {end_time - start_time}")
    return wrapper()

@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function is 2 sec")
    time.sleep(2) # wait for 2 seconds


@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function is 5 sec")
    time.sleep(5)