#Martin Couture
#Explication du code : https://youtu.be/s8NXkh6ygPY

from math import sin, cos, tan, atan, atan2, radians

def distanceEllipse(lat1, long1, lat2, long2):
    global cos_sq_alpha, cos_2sigma_m, cos_sigma, sin_sigma, sigma
    a = 6378137.0  # Rayon de la terre
    f = 1 / 298.257223563  # Excentricité
    b = (1 - f) * a
    tolerance = 1e-12  # Tolérance de précision

    phi1, phi2 = lat1, lat2
    U1 = atan((1 - f) * tan(phi1))
    U2 = atan((1 - f) * tan(phi2))
    L1, L2 = long1, long2
    L = L2 - L1

    lambdaBase = L
    lambdaNouveau = 1

    #Itération jusqu'à la tolérance
    while not abs(lambdaNouveau - lambdaBase) <= tolerance:
        lambdaBase = lambdaNouveau
        t = pow((cos(U2) * sin(lambdaBase)),2)
        t += pow(cos(U1) * sin(U2) - sin(U1) * cos(U2) * cos(lambdaBase),2)
        sin_sigma = pow(t,0.5)
        cos_sigma = sin(U1) * sin(U2) + cos(U1) * cos(U2) * cos(lambdaBase)
        sigma = atan2(sin_sigma, cos_sigma)

        sin_alpha = cos(U1) * cos(U2) * sin(lambdaBase) / sin_sigma
        cos_sq_alpha = 1 - pow(sin_alpha,2)
        cos_2sigma_m = cos_sigma - 2 * sin(U1) * sin(U2) / cos_sq_alpha
        C = f * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha)) / 16

        t = sigma + C * sin_sigma * (cos_2sigma_m + C * cos_sigma * (-1 + 2 * cos_2sigma_m ** 2))
        lambdaNouveau = L + (1 - C) * f * sin_alpha * t


    u2 = cos_sq_alpha * ((pow(a,2) - pow(b,2)) / pow(b,2))
    A = 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))
    t = cos_2sigma_m + 0.25 * B * (cos_sigma * (-1 + 2 * cos_2sigma_m ** 2))
    t -= (B / 6) * cos_2sigma_m * (-3 + 4 * sin_sigma ** 2) * (-3 + 4 * cos_2sigma_m ** 2)
    delta_sigma = B * sin_sigma * t
    s = b * A * (sigma - delta_sigma)

    return s

print(distanceEllipse(radians(60),radians(-69),radians(60),radians(-68)))
