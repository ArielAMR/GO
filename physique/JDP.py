import math

def calculateur_teta(V0, D, H):
    g = 9.81

    teta_min_1 = 0
    teta_min_2 = math.pi / 2
    teta_min = (teta_min_1 + teta_min_2) / 2

    teta_max_1 = 0
    teta_max_2 = math.pi / 2
    teta_max = (teta_max_1 + teta_max_2) / 2


    y1 =  - (g * D**2) / (2 * V0**2 * math.cos(teta_min)**2) + D * math.tan(teta_min) + H
    y2 =  - (g * D**2) / (2 * V0**2 * math.cos(teta_max)**2) + D * math.tan(teta_max) + H

    hauteur_dedans_min = 1.1 + 0.03
    hauteur_dedans_max = 2.2 - 0.03


    while abs(y1 - hauteur_dedans_min) > 0.01:
        
        if y1 > hauteur_dedans_min:
            teta_min_2 = teta_min
        elif y1 < hauteur_dedans_min:
            teta_min_1 = teta_min

        teta_min = (teta_min_1 + teta_min_2) / 2
        y1 =  - (g * D**2) / (2 * V0**2 * math.cos(teta_min)**2) + D * math.tan(teta_min) + H


    while abs(y2 - hauteur_dedans_max) > 0.01:

        if y2 > hauteur_dedans_max:
            teta_max_2 = teta_max
        elif y2 < hauteur_dedans_max:
            teta_max_1 = teta_max

        teta_max = (teta_max_1 + teta_max_2) / 2
        y2 =  - (g * D**2) / (2 * V0**2 * math.cos(teta_max)**2) + D * math.tan(teta_max) + H

    return str(teta_min), str(teta_max), str(math.degrees(teta_min)), str(math.degrees(teta_max))

print(calculateur_teta(18.6, 28, 1))