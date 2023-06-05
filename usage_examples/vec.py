import ctypes

# Load the shared library
lib = ctypes.CDLL("./build/libvec.so")


class Vector:
    def __init__(self, size):
        lib.vector_create.argtypes = [ctypes.c_int]
        lib.vector_create.restype = ctypes.c_void_p
        self.vector = ctypes.c_void_p(lib.vector_create(size))

    def __del__(self):
        lib.vector_destroy.argtypes = [ctypes.c_void_p]
        lib.vector_destroy(self.vector)

    def set(self, index, value):
        lib.vector_set.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
        lib.vector_set(self.vector, index, value)

    def get(self, index):
        lib.vector_get.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.vector_get.restype = ctypes.c_float
        return lib.vector_get(self.vector, index)

    def add(self, other):
        lib.vector_add.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.vector_add.restype = ctypes.c_void_p
        result = Vector(0)
        result.vector = ctypes.c_void_p(lib.vector_add(self.vector, other.vector))
        return result

    def sub(self, other):
        lib.vector_sub.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.vector_sub.restype = ctypes.c_void_p
        result = Vector(0)
        result.vector = ctypes.c_void_p(lib.vector_sub(self.vector, other.vector))
        return result

    def sum(self):
        lib.vector_sum.argtypes = [ctypes.c_void_p]
        lib.vector_sum.restype = ctypes.c_float
        return lib.vector_sum(self.vector)


def print_vector(v, size):
    for i in range(size):
        print(v.get(i))


def fill_vector(v, size, value=0):
    for i in range(size):
        v.set(i, value)


size = 3
a = Vector(size)
b = Vector(size)
fill_vector(a, size, 1)
fill_vector(b, size, 2)

c = a.add(b)
print("a + b:")
print_vector(c, size)

c = a.sub(b)
print("a - b:")
print_vector(c, size)

print(f"Sum: {a.sum()}")
