import ctypes
from pathlib import Path


def _load_library() -> ctypes.CDLL:
    repo_root = Path(__file__).resolve().parents[1]
    candidates = [
        repo_root / "build" / "libfibonacci.so",
        repo_root / "libfib.so",
    ]
    for path in candidates:
        if path.exists():
            return ctypes.CDLL(str(path))
    raise FileNotFoundError(
        "Could not find fibonacci shared library. Build first with: cmake -S . -B build && cmake --build build"
    )


lib = _load_library()


# Provide the Python interface
def fibonacci(n):
    lib.fibonacci.argtypes = [ctypes.c_int]
    lib.fibonacci.restype = ctypes.c_int64
    return lib.fibonacci(n)


r = fibonacci(10)
print(r)
