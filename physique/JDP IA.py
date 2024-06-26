import math

def hits_target(V0, H, theta, D):
    g = 9.81  # Accélération gravitationnelle en m/s^2
    t = D / (V0 * math.cos(math.radians(theta)))
    y = H + V0 * math.sin(math.radians(theta)) * t - 0.5 * g * t**2
    return 1.1 <= y <= 2.2

def find_min_angle(V0, H, D):
    min_angle = None
    for theta in range(91):
        if hits_target(V0, H, theta, D):
            min_angle = theta
            break
    return min_angle

def find_max_angle(V0, H, D):
    max_angle = None
    for theta in range(90, -1, -1):
        if hits_target(V0, H, theta, D):
            max_angle = theta
            break
    return max_angle

# Exemple d'utilisation
V0 = 18.6  # vitesse initiale en m/s
H = 1  # hauteur initiale en m
D = 14  # distance en m

min_angle = find_min_angle(V0, H, D)
max_angle = find_max_angle(V0, H, D)


print(f"Angle minimum: {math.radians(min_angle)} degrés")
print(f"Angle maximum: {math.radians(max_angle)} degrés")
