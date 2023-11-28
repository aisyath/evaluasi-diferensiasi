import numpy as np

# Driver Program
def driver(xi, xf, yi):
    maxstep = 100
    h = 0.5
    tiny = 1.0e-30
    eps = 0.00005

    print(xi, yi)
    x = xi
    y = yi
    h = h
    istep = 0

    results = []  # To store results

    while True:
        if istep >= maxstep or (x + h) > xf:
            break

        istep += 1
        dy = derivs(x, y)
        yscal = np.abs(y) + np.abs(h * dy) + tiny

        if (x + h) > xf:
            h = xf - x

        if x + h < xf:
            h = xf - x

        adapt(x, y, dy, h, yscal, eps)

        results.append((x, y.copy()))  # Store the results
        display_results(x, y)

    display_results(x, y)  # Display the final result

# Adaptive Step Routine
def adapt(x, y, dy, htry, yscal, eps):
    safety = 0.9
    econ = 1.89e-4

    htry = htry
    ytemp = np.zeros_like(y)  # Initialize ytemp here
    yerr = np.zeros_like(y)   # Initialize yerr here
    while True:
        rkck(y, dy, x, htry, ytemp, yerr)
        emax = np.max(np.abs(yerr / yscal / eps))

        if emax <= 1.0:
            break

        htemp = safety * htry * emax**(-0.25)
        h = max(abs(htemp), 0.25 * abs(htry))
        xnew = x + h

        if xnew == x:
            print("Error: Step size underflow.")
            break

    if emax > econ:
        hnxt = safety * htry * emax**(-0.2)
    else:
        hnxt = 4.0 * htry

    x = x + htry  # Update x with the original step size
    y = ytemp.copy()

# Routine to Determine Derivatives
def derivs(x, y):
    # Replace with the actual calculation of derivatives for your system
    dy = 2 * x  # Example derivative for a single variable
    return dy

# RKCK method for adaptive step size
def rkck(y, dy, x, h, yout, yerr):
    a2 = 0.2
    a3 = 0.3
    a4 = 0.6
    a5 = 1.0
    a6 = 0.875

    b21 = 0.2
    b31 = 0.075
    b32 = 0.225
    b41 = 0.3
    b42 = -0.9
    b43 = 1.2
    b51 = -11.0 / 54.0
    b52 = 2.5
    b53 = -70.0 / 27.0
    b54 = 35.0 / 27.0
    b61 = 1631.0 / 55296.0
    b62 = 175.0 / 512.0
    b63 = 575.0 / 13824.0
    b64 = 44275.0 / 110592.0
    b65 = 253.0 / 4096.0

    c1 = 37.0 / 378.0
    c3 = 250.0 / 621.0
    c4 = 125.0 / 594.0
    c6 = 512.0 / 1771.0

    dc1 = c1 - 2825.0 / 27648.0
    dc3 = c3 - 18575.0 / 48384.0
    dc4 = c4 - 13525.0 / 55296.0
    dc5 = -277.0 / 14336.0
    dc6 = c6 - 0.25

    ytemp = y + h * b21 * dy
    dyt = derivs(x + a2 * h, ytemp)
    ytemp = y + h * (b31 * dy + b32 * dyt)
    dyt = derivs(x + a3 * h, ytemp)
    ytemp = y + h * (b41 * dy + b42 * dyt)
    dyt = derivs(x + a4 * h, ytemp)
    ytemp = y + h * (b51 * dy + b52 * dyt)
    dyt = derivs(x + a5 * h, ytemp)
    ytemp = y + h * (b61 * dy + b62 * dyt)
    dyt = derivs(x + a6 * h, ytemp)

    yout = y + h * (c1 * dy + c3 * dyt + c4 * derivs(x + a4 * h, ytemp) + c6 * derivs(x + a6 * h, ytemp))
    yerr = h * (dc1 * dy + dc3 * dyt + dc4 * derivs(x + a4 * h, ytemp) + dc5 * derivs(x + a5 * h, ytemp) + dc6 * derivs(x + a6 * h, ytemp))
    ytemp = y + h * (c1 * dy + c3 * dyt + c4 * derivs(x + a4 * h, ytemp) + c6 * derivs(x + a6 * h, ytemp))

# Display Results
def display_results(x, y):
    print(f"Result at x = {x:.4f}: y = {y[0]:.4f}")

# Example usage
if __name__ == "__main__":
    driver(xi=0.0, xf=2.0, yi=np.array([1.0]))
