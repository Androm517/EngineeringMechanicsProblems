from numpy import sqrt, sin, cos, pi, arcsin


m = 2.
l = 1.
I = 1./12. * m * l**2

b = m * (l/2.)**2 + I
d = -m * 9.81 * l / 2.
w1 = sqrt(-2 * d/b)
print("Before impact")
print(f'w1 is {w1}')

h = -(w1/2)**2 * 0.5 * b/d
thetha4 = arcsin(h)
print(f'Angle relative to the horizon is {thetha4} radians or {thetha4 * 180 / pi} degrees')