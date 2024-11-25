# Problem 3

def hash_function(x, a, b, p, w):
    return ((a * x + b) % p) % w

def count_min_sketch(a, b, p, w, stream):
    d = len(a)
    sketch = [[0] * w for _ in range(d)]
    for x in stream:
        for i in range(d):
            idx = hash_function(x, a[i], b[i], p, w)
            sketch[i][idx] += 1
    return sketch

def increment(sketch, x, a, b, p, w):
    d = len(a)
    for i in range(d):
        idx = hash_function(x, a[i], b[i], p, w)
        sketch[i][idx] += 1

def query(sketch, x, a, b, p, w):
    d = len(a)
    counts = []
    for i in range(d):
        idx = hash_function(x, a[i], b[i], p, w)
        counts.append(sketch[i][idx])
    return min(counts)