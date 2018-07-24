import numpy as np

def func(thetha, R):
    rad_neg_30 = -30. * np.pi / 180.
    o = thetha
    A = -R * np.sin(rad_neg_30)
    B = 10 * np.sin(o)
    C = R * np.cos(rad_neg_30) / (10 * np.cos(o))
    D = 9.81 / (10 * np.cos(o))
    return A + B * C - D * np.power(C, 2)

def func2(thetha, R):
    radians = -60. * np.pi / 180.
    ax = 9.81 * np.cos(radians)
    vx0 = 10 * np.cos(thetha)
    t = 2 * 10 * np.sin(thetha) / (9.81 * np.sin(radians))
    return ax * np.power(t, 2) / 2. + vx0 * t - R