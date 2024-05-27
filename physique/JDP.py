import math

def rentre_ou_pas(V0, D, H):
    g = 9.81
    teta_min = math.pi/2
    y = -(g*D**2)/(V0**2*math.cos(teta_min)**2)+math.tan(teta_min)*D
    while abs(y-H)>0.1:
        y = -(g*D**2)/(V0**2*math.cos(teta_min)**2)+math.tan(teta_min)*D
        if y>H:
            teta_min+=teta_min/2
        if y<H:
            teta_min-=teta_min/2
    print(math.degrees(teta_min))

rentre_ou_pas(18.6,14,1.23)