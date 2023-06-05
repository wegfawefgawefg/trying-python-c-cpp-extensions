import time
import random
import numpy as np
from mininumpy import Vector


def test(size):
    x = [1.0 for _ in range(size)]
    y = [2.0 for _ in range(size)]

    # Adding the lists using Python
    start = time.time()
    result_list = [a + b for a, b in zip(x, y)]
    end = time.time()
    python_time = end - start
    print(f"Time taken by Python: {python_time} seconds")

    # Adding the lists using our Vector class
    x = Vector(size)
    y = Vector(size)
    x.fill(1)
    y.fill(2)

    start = time.time()
    result_vector = x.add(y)
    end = time.time()
    vector_time = end - start
    print(f"Time taken by Vector: {vector_time} seconds")

    # now lets do numpy
    x = np.ones(size)
    y = np.ones(size) * 2

    start = time.time()
    result_numpy = x + y
    end = time.time()
    numpy_time = end - start
    print(f"Time taken by NumPy: {numpy_time} seconds")

    # how much faster is the vector implementation?
    faster_or_slower = "faster" if python_time > vector_time else "slower"
    print(f"Vector is {python_time / vector_time} times {faster_or_slower}")

    # how much faster is the vector implementation?
    faster_or_slower = "faster" if python_time > numpy_time else "slower"
    print(f"NumPy is {python_time / numpy_time} times {faster_or_slower}")

    # vector vs numpy
    faster_or_slower = "faster" if vector_time > numpy_time else "slower"
    print(f"NumPy is {vector_time / numpy_time} times {faster_or_slower} than Vector")


for size in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]:
    print(f"For a vector of size = {size}")
    test(size)
    print()
