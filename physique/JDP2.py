import math

def rentre_ou_pas(V0, D, H):
    g = 9.81
    teta_min = 0
    teta_max = math.pi / 2
    epsilon = 0.001
    y = 1

    while abs(y - H) > epsilon:
        teta = (teta_min + teta_max) / 2
        y =  - (g * D**2) / (2 * V0**2 * math.cos(teta)**2) + D * math.tan(teta)

        if y > H:
            teta_max = teta
        else:
            teta_min = teta

    print(math.degrees(teta))

rentre_ou_pas(18.6, 14, 1.23)