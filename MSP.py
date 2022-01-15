def primefactors(n: int):
    factors = []
   #Le but est de rendre n impair, tant qu'il est pair on affiche ajoute 2 au tableau
    while n % 2 == 0:
      factors.append(2),
      n = int(n / 2)
    
   #Les diviseurs vont de pairs, on s'arrete donc à srqt(n)+1 (voir https://math.stackexchange.com/questions/3875424/sieve-of-eratosthenes-why-can-we-stop-at-the-sqrt-n)
    for i in range(3,int(n**0.5)+1,2):
     
      while (n % i == 0):
         factors.append(i)
         n = int(n / i)
    
    #Si il reste encore un nombre n > 2 c'est qu'il est un facteur du nombre.
    if n > 2:
      factors.append(n)
      
    return factors

#Cette fonction génère toutes les possibilités de somme via les facteurs
def genp(ac:int):
    factors = primefactors(ac)
    tableauDeToutesLesPossibilités = []
    tableau1 = factors.copy()
    tableau2 = []
    for i in range(0,len(factors)-1):
        tableau2.append(tableau1[0])
        tableau1.pop(0)
        n1 = 1
        n2 = 1
        for i in range(0,len(tableau1)):
            n1 = tableau1[i] * n1
        for i in range(0,len(tableau2)):
            n2 = tableau2[i] * n2
        tableauDeToutesLesPossibilités.append([n1, n2])
    return tableauDeToutesLesPossibilités

# Test de M et P pour voir si m+p = b
def MSP(ac:int, b:int):
    posibilities = genp(ac)
    for i in range(0,len(posibilities)):
        m = posibilities[i][0]
        p = posibilities[i][1]
        if m + p == b:
            return [m,p]
        elif -m + p == b:
            return [-m,p]
        elif m + -p == b:
            return [m,-p]
        elif -m + -p == b:
            return [-m,-p]
    return "Aucun m et p valable."  