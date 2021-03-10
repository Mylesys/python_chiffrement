import random as rnd


# Définition PGDC
def pgcd(a, b):
    return a if b == 0 else pgcd(b, a % b)


# Génération matrice A 2x2
def genererA(n):
    while 1:
        a, b, c, d = [rnd.choice(range(1, n)) for i in range(4)]
        detA = (a * d - b * c) % n
        inv_detA = [i for i in range(1, n) if (i * detA) % n == 1]
        if len(inv_detA) == 1:
            break
    return [a, b, c, d]  # ,detA,inv_detA,divmod(detA*inv_detA[0],n)


def Hill(message, cle_a, ind, alphabet):
    # ind=0 pour chiffrer le message et 1 pour le déchiffrer
    # La matrice entière cle = [[a b], [c d]] peut être choisie arbitrairement
    # mais de manière à ce que det(A) = ab - cd soit un entier premier avec n
    # nombre de caractères autorisés de l'alphabet utilisé.'''
    # 1) Nombre de caractères autorisés
    n = len(alphabet)

    # 2) Vérification de la matrice cle
    # 2.1) Calcul du déterminant de la matrice cle modulo n
    detA = (cle_a[0] * cle_a[3] - cle_a[1] * cle_a[2]) % n
    # 2.2) Calcul de l'inverse de detA modulo n
    try:
        inv_detA = [i for i in range(1, n) if (i * detA) % n == 1][0]
    except:
        return "Matrice cle non convenable pour le chiffrement proposé ..."

        # 2.3) Calcul de la matrice cle_b inverse de A modulo n
    cle_b = inverse_mod_n(cle_a, n, inv_detA)

    # 2.4) Le nombre de caractères du message doit être pair
    if len(message) % 2 == 1:
        message += ' '

    # 3) Résultat du (dé)chiffrement)
    resultat = ''
    a, b, c, d = [cle_a, cle_b][ind]  # matrice de chiffrement ou déchiffrement

    for i in range(0, len(message), 2):
        m1, m2 = message[i:i + 2]  # 2 caractères
        p1, p2 = alphabet.index(m1), alphabet.index(m2)
        q1, q2 = (a * p1 + b * p2) % n, (c * p1 + d * p2) % n
        resultat += alphabet[q1] + alphabet[q2]
    return resultat


def determinant(A):
    ''' Déteminant de la matrice A (2x2)'''
    return (A[0] * A[3] - A[1] * A[2])


def tComatrice(A):
    ''' Transposée de la comatrice de la matrice A (2x2) '''
    return [A[3], -A[1], -A[2], A[0]]


def inverse_mod_n(A, n, invA):
    ''' Inverse de la matrice A (2x2) modulo n '''
    return [(invA * i) % n for i in tComatrice(A)]


def alphabet():
    ''' Définir votre alphabet : caractères autorisés '''
    alpha = ''
    # alpha+=u"abcdefghijklmnopqrstuvwxyz"
    alpha += u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # alpha+=u'0123456789'
    # alpha+="!#$%&'()*+,-./:;<=>?@[]^_`{|}~ "
    # alpha+='"'
    return alpha


alphab = alphabet()  # Alphabet autorisé
n = len(alphab)  # Nombre de caratères aautorisés
cle_a = [11, 11, 9, 10]  # Matrice clé (det(A) doit être premier avec n)
# print cle

message = str(input("Quelle est le message à chiffrer ?"))
message = message.upper()
print("Message d'origine :", message)
message_chiffre = Hill(message, cle_a, 0, alphab)

print("Message codé      :", message_chiffre)
message_chiffre = str(input("Quelle est le message à chiffrer ?"))
message_chiffre = message_chiffre.upper()
message_dechiffre = Hill(message_chiffre, cle_a, 1, alphab)
print("Message décodé    :", message_dechiffre)

