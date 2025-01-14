import numpy as np

def spline_b1(x):
    x_abs = np.abs(x)
    y = np.where(np.abs(x) <= 1, 1 - x_abs, 0)
    return y

def spline_b2(x):
    x_abs = np.abs(x)
    y = np.where(x_abs <= 0.5, 0.75 - np.square(x), 0)
    y = np.where((0.5 < x_abs) & (x_abs <= 1.5), np.square(1.5 - x_abs) * 0.5, y)
    y = np.where(x_abs < 1.5, y, 0)
    return y

def spline_b3(x):
    x_abs = np.abs(x)
    y = np.where(x_abs < 1, (2/3) - np.square(x_abs) + 0.5 * np.power(x_abs, 3), 0)
    y = np.where((1 <= x_abs) & (x_abs < 2), np.power(2 - x_abs, 3) / 6, y)
    y = np.where(x_abs < 2, y, 0)
    return y
