# trying-python-c-cpp-extensions

Small experiments for calling C code from Python using `ctypes`.

This repo includes:
- Fibonacci in C, called from Python (`usage_examples/fib.py`)
- A tiny C vector library wrapped in Python (`usage_examples/mininumpy.py`)
- A basic speed comparison against Python lists and NumPy (`usage_examples/vec_speedtest.py`)

## Prerequisites

- CMake (3.0+)
- A C compiler (`gcc`/`clang`)
- Python 3.10+
- Optional: `uv` for Python env/dependency management
  - Install: https://docs.astral.sh/uv/getting-started/installation/

## Python Dependencies

- Required for core examples: none (stdlib only)
- Optional for benchmarking: `numpy` (used by `usage_examples/vec_speedtest.py`)

## Quick Start

Build shared libraries:

```bash
./scripts/build.sh
```

Run examples:

```bash
python3 usage_examples/fib.py
python3 usage_examples/vec_test.py
```

Run benchmark (requires NumPy):

```bash
python3 usage_examples/vec_speedtest.py
```

## Using uv

Create/sync an environment without optional deps:

```bash
uv sync
```

Include benchmark dependency (`numpy`):

```bash
uv sync --extra benchmark
```

Run scripts through `uv`:

```bash
uv run python usage_examples/fib.py
uv run python usage_examples/vec_test.py
uv run python usage_examples/vec_speedtest.py
```

## Manual Build

If you prefer direct CMake commands:

```bash
cmake -S . -B build
cmake --build build -j
```

This produces:
- `build/libfibonacci.so`
- `build/libvec.so`
- Raw C executables in `build/`

## Notes

- Python examples load shared libs from `build/`.
- `usage_examples/fib.py` also supports a legacy local `./libfib.so` fallback.
