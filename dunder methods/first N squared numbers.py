import sys
import time


# List-based function
def square_list(n):
    result = []

    for i in range(n):
        result.append(i * i)

    return result


# Generator function
def square_generator(n):
    for i in range(n):
        yield i * i


for n in [1000, 100000]:

    print("\nN =", n)

    # List memory and time
    start = time.perf_counter()
    l = square_list(n)
    end = time.perf_counter()

    list_time = end - start
    list_memory = sys.getsizeof(l)

    # Generator memory and time
    start = time.perf_counter()
    g = square_generator(n)
    end = time.perf_counter()

    generator_time = end - start
    generator_memory = sys.getsizeof(g)

    print("List memory     :", list_memory, "bytes")
    print("Generator memory:", generator_memory, "bytes")

    print("List time       :", list_time)
    print("Generator time  :", generator_time)