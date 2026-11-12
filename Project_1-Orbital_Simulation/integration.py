import math

# Physical constants
RE = 1.5e11
rS = 7.0e8
MS = 2.0e30
G = 6.67e-11


def simpson(f, a, b, N):
    total = 0.0
    start = float(a)
    step = float(b - a) / N

    for i in range(N):
        total += (
            f(start + step * i)
            + 4 * f(start + step * (i + 0.5))
            + f(start + step * (i + 1))
        ) * step / 6.0

    return total


def integrand(x, v0):
    if x == 0.0 and v0 == 0.0:
        return 2.0 * RE / math.sqrt(2.0 * G * MS)

    R = RE - x * x

    return 2.0 * x / math.sqrt(
        v0 * v0 + 2.0 * G * MS * (1.0 / R - 1.0 / RE)
    )


# Integration parameters
N = 10000
a = 0.0
b = math.sqrt(RE - rS)

# Calculate fall times
for v0 in [0.0, 10.0, 1000.0]:
    t = simpson(lambda x: integrand(x, v0), a, b, N)
    print(f"Initial velocity: {v0} m/s")
    print(f"Fall time: {t:.2f} seconds ({t / 86400.0:.4f} days)\n")
