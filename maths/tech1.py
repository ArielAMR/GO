def E(n):
    e=1

    factorielle = 1
    for i in range(1,n):
        factorielle*=i
        e+=1/factorielle
    print(e)

E(4)