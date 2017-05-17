# CTA200H 2017 Problem Set 1, Question 4
# Jack Hong and Bill Kong

import matplotlib.pyplot as plt
import numpy as np

N = 300  # linear pixels
L = 100  # iterations


def mandelbrot(a, l):
    z = 0
    for i in range(l):
        if abs(z) < 2:
            z = z ** 2 + a
        else:
            return 1
    return 0


vals = np.empty([N, N])
xv = np.linspace(-2, 2, N)
yv = np.linspace(-2, 2, N)
cv = xv + 1j * yv

for i in range(N):
    for j in range(N):
        c = xv[i] + yv[j] * 1j
        vals[i, j] = mandelbrot(c, L)

fig = plt.figure()
plt.imshow(vals, cmap="gist_gray")

plt.title("Mandelbrot Set")
plt.colorbar()


def mandelbrot2(a, l):
    z = 0
    for i in range(l):
        if abs(z) < 2:
            z = z ** 2 + a
        else:
            # return 1.0-float(i)/L
            return i
    return 0


vals = np.empty([N, N])
xv = np.linspace(-.5, .5, N)
yv = np.linspace(0, 1, N)
cv = xv + 1j * yv

for i in range(N):
    for j in range(N):
        c = xv[i] + yv[j] * 1j
        vals[i, j] = mandelbrot2(c, L)

plt.figure()
plt.imshow(vals, cmap="jet")
plt.title("Mandelbrot Set")
plt.colorbar()


def mandelbrot2(a, l):
    z = 0
    for i in range(l):
        if abs(z) < 2:
            z = z ** 2 + a
        else:
            # return 1.0-float(i)/L
            return i
    return 0


vals = np.empty([N, N])
xv = np.linspace(-2, 2, N)
yv = np.linspace(-2, 2, N)
cv = xv + 1j * yv

for i in range(N):
    for j in range(N):
        c = xv[i] + yv[j] * 1j
        vals[i, j] = mandelbrot2(c, L)

plt.figure()
plt.imshow(vals, cmap="jet")
plt.title("Mandelbrot Set")
plt.colorbar()

plt.show()
