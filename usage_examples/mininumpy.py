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

    def fill(self, value):
        lib.vector_fill.argtypes = [ctypes.c_void_p, ctypes.c_float]
        lib.vector_fill(self.vector, value)

    def get_size(self):
        lib.vector_get_size.argtypes = [ctypes.c_void_p]
        lib.vector_get_size.restype = ctypes.c_int
        return lib.vector_get_size(self.vector)

    def __repr__(self):
        size = self.get_size()
        elements = [self.get(i) for i in range(size)]
        return "Vector(" + ", ".join(map(str, elements)) + ")"


if __name__ == "__main__":
    # convert these to tests with assert
    size = 3
    a = Vector(size)
    b = Vector(size)
    a.fill(1)
    b.fill(2)

    assert a.get_size() == size
    assert b.get_size() == size
    assert a.get(0) == 1
    assert b.get(0) == 2

    c = a.add(b)
    assert c.get(0) == 3
    print(f"a + b: {c}")

    c = a.sub(b)
    assert c.get(0) == -1
    print(f"a - b: {c}")

    assert a.sum() == 3
    print(f"Sum: {a.sum()}")
