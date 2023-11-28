import numpy as np

def backward_difference(x, y):
    if x.size < 2 or y.size < 2:
        raise ValueError("'x' and 'y' arrays must have 2 values or more.")
    if x.size != y.size:
        raise ValueError("'x' and 'y' must have the same size.")

    dy = np.zeros_like(y)
    for i in range(0, x.size):
        if i == 0:
            hx = x[i + 1] - x[i]
            dy[i] = (y[i + 1] - y[i]) / hx
        elif i == x.size - 1:
            hx = x[i] - x[i - 1]
            dy[i] = (y[i] - y[i - 1]) / hx
        else:
            hx = x[i + 1] - x[i]
            dy[i] = (y[i + 1] - y[i]) / hx

    return dy

def three_point(x, y):
    if x.size < 3 or y.size < 3:
        raise ValueError("'x' and 'y' arrays must have 3 values or more.")

    dy = np.zeros_like(y)
    hx = x[1] - x[0]
    for i in range(0, y.size - 1):
        dy[i] = (y[i + 1] - y[i]) / hx

    return dy

def five_point(x, y):
    if x.size < 5 or y.size < 5:
        raise ValueError("'x' and 'y' arrays must have 5 values or more.")
    if x.size != y.size:
        raise ValueError("'x' and 'y' must have the same size.")

    dy = np.zeros_like(y)
    hx = x[1] - x[0]
    for i in range(2, x.size - 2):
        dy[i] = (y[i - 2] - 8 * y[i - 1] + 8 * y[i + 1] - y[i + 2]) / (12 * hx)

    return dy

# Examples
print("1.1. Backward Difference:")
x_bd = np.array([0.0, 0.2, 0.41])
y_bd = np.array([0.00000, 0.74140, 1.37181])
result_bd = backward_difference(x_bd, y_bd)
print(result_bd)

print("\n1.2. Three-Point:")
x_tp = np.array([1.2, 1.3, 1.4])
y_tp = np.array([9.025013, 11.02318, 13.46374, 16.44465])
result_tp = three_point(x_tp, y_tp)
print(result_tp)

print("\n1.3. Five-Point:")
x_fp = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
y_fp = np.array([-1.709847, -0.9160143, -1.373823, -1.119214, -0.7470223])
result_fp = five_point(x_fp, y_fp)
print(result_fp)
