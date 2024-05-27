import math

def rentre_ou_pas(V0, D, H):
    g = 9.81
    teta_min = 180
    y = 1
    while abs(y-H)>0.01:
        y = -(g*D**2)/(V0**2*math.cos(teta_min)**2)+math.tan(teta_min)*D
        if y>H:
            teta_min+=teta_min/2
        if y<H:
            teta_min-=teta_min/2
    print(teta_min)

rentre_ou_pas(18.6,14,1.23)