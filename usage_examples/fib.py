import ctypes

# Load the shared library
lib = ctypes.CDLL("./build/libfibonacci.so")


# Provide the Python interface
def fibonacci(n):
    lib.fibonacci.argtypes = [ctypes.c_int]
    lib.fibonacci.restype = ctypes.c_int64
    return lib.fibonacci(n)


r = fibonacci(10)
print(r)
