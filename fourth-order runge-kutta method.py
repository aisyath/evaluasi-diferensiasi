# Main or "Driver" Program
def main():
    # Assign values for n number of equations,
    # yi initial values of n dependent variables,
    # xi initial value independent variable, xf final value independent variable,
    # dx calculation step size, xout output interval
    n = 2
    yi = [1.0, 0.0]
    xi = 0.0
    xf = 5.0
    dx = 0.1
    xout = 1.0
    x = xi
    m = 0
    xpm = x

    results = []

    for i in range(n):
        ypi_m = yi[i]
        yi[i] = ypi_m

    while True:
        xend = x + xout
        if xend > xf:
            xend = xf
        h = dx
        integrator(x, yi, n, h, xend)
        m += 1
        xpm = x
        results.append((x, yi[:]))
        if x >= xf:
            break

    display_results(results)

# Routine to Take One Output Step
def integrator(x, y, n, h, xend):
    while True:
        if (xend - x) < h:
            h = xend - x
        rk4(x, y, n, h)
        if x >= xend:
            break

# Fourth-Order RK Method for a System of ODEs
def rk4(x, y, n, h):
    k1 = derivs(x, y)

    ym = [0.0] * n
    for i in range(n):
        ym[i] = y[i] + k1[i] * h / 2

    k2 = derivs(x + h / 2, ym)

    for i in range(n):
        ym[i] = y[i] + k2[i] * h / 2

    k3 = derivs(x + h / 2, ym)

    for i in range(n):
        ym[i] = y[i] + k3[i] * h

    k4 = derivs(x + h, ym)

    for i in range(n):
        slope = (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
        y[i] = y[i] + slope * h

    x = x + h

# Routine to Determine Derivatives
def derivs(x, y):
    dy1 = y[0] + 2 * y[1]
    dy2 = -3 * y[0] + y[1]
    return [dy1, dy2]

# Display Results
def display_results(results):
    print("Results of ODE Integration:")
    print("   x        y1       y2")
    for x, y in results:
        print(f"{x:.4f}   {y[0]:.4f}   {y[1]:.4f}")

# Example usage
if __name__ == "__main__":
    main()
