def dh(P,g,a,b):
    pa = (g**a) % P
    pb = (g**b) % P
    Ka = (pb**a) % P
    Kb = (pa**b) % P
    print("Pa = (",g,"**",a,") %", P," = ",pa)
    print("Pb = (",g,"**",b,") %", P," = ",pb)
    print("Ka = (",pb,"**",a,") %",P," = ",Ka)
    print("Kb = (",pa,"**",b,") %",P," = ",Kb)

def genD(E,phi) :
    D=1
    while (D * E) % phi != 1:
            D += 1
    return(D)

def RSA(P,Q,E):
    print("calcul de N : ")
    N = P*Q
    print("N = ",N)
    print("calcul de Phi : ")
    phi = (P-1)*(Q-1)
    print("phi = ",phi)
    print("trouver D")
    D = genD(E,phi)
    print('D = ',D)
    print("\n")
    print("Pour chiffré : text**",E,"%",N)
    print("Pour déchiffré : text**",D,"%",N)
    print("\n")
    print("les couple de clé :")
    print("clé publique :(",N,",",E,")")
    print("clé privée :(",N,",",D,")")