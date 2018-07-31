from numpy import matrix, pi, sqrt, array


def IBarA(mass, length):
    coeff = 1./12 * mass * length**2
    I = [[coeff, 0, 0], [0, 0, 0], [0, 0, coeff]]
    return matrix(I)

def IBarB(mass, length):
    coeff = 1./12 * mass * length**2
    I = [[0, 0, 0], [0, coeff, 0], [0, 0, coeff]]
    return matrix(I)

def parrallelAxisBar(mass, delta_x, delta_y, delta_z):
    xx = mass * (delta_y**2 + delta_z**2)
    yy = mass * (delta_x**2 + delta_z**2)
    zz = mass * (delta_y**2 + delta_x**2)
    xy = delta_x * delta_y * mass
    yx = xy
    yz = delta_y * delta_z * mass
    zy = yz
    zx = delta_z * delta_x * mass
    xz = zx
    P = [[xx, -xy, -xz], [-yx, yy, -yz], [-zx, -zy, zz]]
    return matrix(P)

I_A_cm = IBarA(5000, 20)
I_B_cm = IBarB(5000, 20)
I_A = I_A_cm + parrallelAxisBar(5000, -5, 5, 0)
I_B = I_B_cm + parrallelAxisBar(5000, 5, -5, 0)
I = I_A + I_B

one_revolution_in_radians = 2 * pi
one_revolution_in_seconds = 600.
omega = [one_revolution_in_radians / one_revolution_in_seconds, 0, 0]
stor_omega = [[0, -omega[2], omega[1]],
              [omega[2], 0, -omega[0]],
              [-omega[1], omega[0], 0]]
omega = matrix(omega)
stor_omega = matrix(stor_omega)
Moment = stor_omega * I * omega.transpose()
vector_Moment = array(Moment.getA1())
abs_Moment = sqrt(vector_Moment.dot(vector_Moment))
print("The magnitude of the couple exterted by the engines is: ", abs_Moment)