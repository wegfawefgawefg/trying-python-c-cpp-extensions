import ctypes
from pathlib import Path


def _load_library() -> ctypes.CDLL:
    repo_root = Path(__file__).resolve().parents[1]
    library_path = repo_root / "build" / "libvec.so"
    if not library_path.exists():
        raise FileNotFoundError(
            "Could not find vector shared library. Build first with: cmake -S . -B build && cmake --build build"
        )
    return ctypes.CDLL(str(library_path))


lib = _load_library()
lib.vector_create.argtypes = [ctypes.c_int]
lib.vector_create.restype = ctypes.c_void_p
lib.vector_destroy.argtypes = [ctypes.c_void_p]
lib.vector_destroy.restype = None
lib.vector_set.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float]
lib.vector_set.restype = None
lib.vector_get.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.vector_get.restype = ctypes.c_float
lib.vector_add.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.vector_add.restype = ctypes.c_void_p
lib.vector_sub.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.vector_sub.restype = ctypes.c_void_p
lib.vector_sum.argtypes = [ctypes.c_void_p]
lib.vector_sum.restype = ctypes.c_float
lib.vector_fill.argtypes = [ctypes.c_void_p, ctypes.c_float]
lib.vector_fill.restype = None
lib.vector_get_size.argtypes = [ctypes.c_void_p]
lib.vector_get_size.restype = ctypes.c_int


class Vector:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be >= 0")

        ptr = lib.vector_create(size)
        if not ptr:
            raise MemoryError("vector_create failed")
        self.vector = ctypes.c_void_p(ptr)

    @classmethod
    def _from_ptr(cls, ptr):
        # Wrap an existing C allocation without creating and leaking a temp Vector(0).
        instance = cls.__new__(cls)
        instance.vector = ctypes.c_void_p(ptr)
        return instance

    def __del__(self):
        # Destructors should be best-effort only; never raise during GC.
        try:
            if hasattr(self, "vector") and self.vector and self.vector.value:
                lib.vector_destroy(self.vector)
                self.vector = ctypes.c_void_p(None)
        except Exception:
            pass

    def _ensure_live(self):
        if not self.vector or not self.vector.value:
            raise ReferenceError("vector handle is not valid")

    def set(self, index, value):
        self._ensure_live()
        if index < 0 or index >= self.get_size():
            raise IndexError("index out of range")
        lib.vector_set(self.vector, index, value)

    def get(self, index):
        self._ensure_live()
        if index < 0 or index >= self.get_size():
            raise IndexError("index out of range")
        return lib.vector_get(self.vector, index)

    def add(self, other):
        self._ensure_live()
        if not isinstance(other, Vector):
            raise TypeError("other must be a Vector")
        other._ensure_live()
        if self.get_size() != other.get_size():
            raise ValueError("vectors must have the same size")

        ptr = lib.vector_add(self.vector, other.vector)
        if not ptr:
            raise RuntimeError("vector_add failed")
        return Vector._from_ptr(ptr)

    def sub(self, other):
        self._ensure_live()
        if not isinstance(other, Vector):
            raise TypeError("other must be a Vector")
        other._ensure_live()
        if self.get_size() != other.get_size():
            raise ValueError("vectors must have the same size")

        ptr = lib.vector_sub(self.vector, other.vector)
        if not ptr:
            raise RuntimeError("vector_sub failed")
        return Vector._from_ptr(ptr)

    def sum(self):
        self._ensure_live()
        return lib.vector_sum(self.vector)

    def fill(self, value):
        self._ensure_live()
        lib.vector_fill(self.vector, value)

    def get_size(self):
        self._ensure_live()
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
