import maths as mt

def genererA(n):
    a = input()
    b = input()
    c = input()
    d = input()
    return [a, b, c, d]
def chiffre_de_hill(message, cle, ind,alphabet):
    n = len(alphabet)

    deter = (cle[0] * cle[3] - cle[1] * cle[2])%n

    try:
        inv_deter = [i for i in range(1,n) if (i*deter)%n == 1][0]
    except:
        return "Matrice cle non convenable"

    # Calcul de la matrice cle_b inverse de A modulo n

    cle_inverse = inverse_mod_n(cle, n inv_deter)
    if len(message) % 2 == 1:
        message += ' '

    #Résultat
    resultat = ''
    a, b, c, d = [cle, cle_inverse][ind]  # matrice de chiffrement ou déchiffrement

    for i in range(0, len(message), 2):
        m1, m2 = message[i:i + 2]  # 2 caractères
        p1, p2 = alphabet.index(m1), alphabet.index(m2)
        q1, q2 = (a * p1 + b * p2) % n, (c * p1 + d * p2) % n
        resultat += alphabet[q1] + alphabet[q2]
    return resultat

def determinant(A):
    # Déteminant de la matrice A (2x2)
    return (A[0] * A[3] - A[1] * A[2])


def tComatrice(A):
    # Transposée de la comatrice de la matrice A (2x2)
    return [A[3], -A[1], -A[2], A[0]]


def inverse_mod_n(A, n, invA):
    # Inverse de la matrice A (2x2) modulo n
    return [(invA * i) % n for i in tComatrice(A)]

def alphabet():
    # Définir votre alphabet : caractères autorisés
    alpha = ''
    alpha += u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    '''A Coder sur la plage ASCII : 32-126'''

    return alpha

alphab = alphabet()  # Alphabet autorisé
n = len(alphab)  # Nombre de caratères aautorisés
cle = [11, 11, 9, 10]  # Matrice clé (det(A) doit être premier avec n)
# print cle
