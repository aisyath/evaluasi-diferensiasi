# Simple Heun without Corrector
def heun(x, y, h):
    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    dy2dx = derivs(x + h, ye)
    slope = 0.5 * (dy1dx + dy2dx)
    ynew = y + slope * h
    x += h
    return x, ynew

# Midpoint Method
def midpoint(x, y, h):
    dydx = derivs(x, y)
    ym = y + dydx * (h / 2)
    dymdx = derivs(x + h/2, ym)
    ynew = y + dymdx * h
    x += h
    return x, ynew

# Heun with Corrector
def heun_with_corrector(x, y, h):
    es = 0.01
    maxit = 20
    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    iter = 0

    while True:
        ye_old = ye
        dy2dx = derivs(x + h, ye)
        slope = 0.5 * (dy1dx + dy2dx)
        ye = y + slope * h
        iter += 1
        ea = abs((ye - ye_old) / ye) * 100

        if ea < es or iter >= maxit:
            break

    ynew = ye
    x += h
    return x, ynew

# Derivative Calculation (Replace with your actual implementation)
def derivs(x, y):
    # Replace the following line with the actual calculation for the derivative
    dydx = 2 * x  # Example derivative calculation, replace with actual formula
    return dydx

# Example usage
x, y = 0.0, 1.0
h = 0.1

# Simple Heun without Corrector
x, y = heun(x, y, h)
print("Simple Heun without Corrector:", x, y)

# Midpoint Method
x, y = midpoint(x, y, h)
print("Midpoint Method:", x, y)

# Heun with Corrector
x, y = heun_with_corrector(x, y, h)
print("Heun with Corrector:", x, y)