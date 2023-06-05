from mininumpy import Vector

size = 3
a = Vector(size)
b = Vector(size)
a.fill(1)
b.fill(2)

c = a.add(b)
print(f"a + b: {c}")

c = a.sub(b)
print(f"a - b: {c}")

print(f"Sum: {a.sum()}")
