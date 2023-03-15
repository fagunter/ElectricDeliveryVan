import numpy as np


def get_rolling_resistance(f_r, M, g, alpha):
    """Computes the vehicle rolling resistance using the rolling resistance coefficient [-], mass [kg],
    gravitational acceleration [m/s^2] and gradient angle [degrees]"""
    return f_r * M * g * np.cos(alpha)


def get_drag(rho, A_f, C_d, V, V_w):
    """Computes the aerodynamic drag using the air density [kg/m^3], frontal area [m^2], drag coefficient [-],
    vehicle speed [m/s] and wind speed in vehicle direction [m/s]"""
    return 0.5 * rho * A_f * C_d * (V - V_w) ** 2


def get_gradient_resistance(M, g, alpha):
    """Computes the gradient resistance using the mass [kg], gravitational acceleration [m/s^2] and
    gradient angle [degrees]"""
    return M * g * np.sin(alpha)


def get_vehicle_forces(f_r, M, g, alpha, rho, A_f, C_d, V, V_w):
    return get_rolling_resistance(f_r, M, g, np.deg2rad(alpha)) + get_drag(rho, A_f, C_d, V, V_w) \
        + get_gradient_resistance(M, g, np.deg2rad(alpha))


print(get_vehicle_forces(0.1, 3000, 9.81, 30, 1.225, 3.35, 0.3, 50, 0))
