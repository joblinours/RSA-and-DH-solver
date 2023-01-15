def dh():
    P = int(input("Entrez P : "))
    g = int(input("Entrez g : "))
    a = int(input("Entrez a : "))
    b = int(input("Entrez b : "))
    pa = (g**a) % P
    pb = (g**b) % P
    Ka = (pb**a) % P
    Kb = (pa**b) % P
    print("Calcul de Pa & Pb")
    print("Pa = (",g,"**",a,") %", P," = ",pa)
    print("Pb = (",g,"**",b,") %", P," = ",pb)
    print("Calcul de la clé")
    print("Ka = (",pb,"**",a,") %",P," = ",Ka)
    print("Kb = (",pa,"**",b,") %",P," = ",Kb)
    print("Les deux clés sont ",Ka," et ",Kb)
    print("\n")

    
def genD(E,phi) :
    D=1
    while (D * E) % phi != 1:
            D += 1
    return(D)

def RSA():
    P = int(input("entrer P : "))
    Q = int(input("entrer Q : "))
    E = int(input("entrer E : "))
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
    print("\n")

    
def menu():
    print("Faire un choix entre Diffie-Hellman (1) RSA (2) ou fermer le soft (3)")
    choix = input("1 2 ou 3 : ")
    if (choix == "1"):
        dh()
        menu()
    elif (choix == "2"):
        print("calcul complet ou juste trouver D ? :")
        choix2 = input("a ou b :")
        if choix2 == "a" :
            RSA()
            menu()
        elif choix2 == "b" :
            e = int(input("entrer e : "))
            phi = int(input("entrer phi : "))
            print(genD(e,phi))
            print("\n")
            menu()
    elif (choix == "3"):
        print()
    else :
        print("Mais quelle bite, il sait meme pas lire. 1 2 ou 3 on t'as dis !")
        menu()
    

menu()