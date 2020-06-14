from curve import curve
from edge import edge
# 3rd-party
import matplotlib.pyplot as plt
# Standard
from math import pi, sqrt, ceil
from cmath import exp
from time import sleep


def distance(pt1, pt2):
    '''
    pt1 et pt2 : tuples

    return distance(pt1, pt2)
    '''
    return sqrt(((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2).real)


def periode(pts):
    '''
    pts : liste de points (tuples)

    return périmètre de la courbe
    '''
    T = 0
    for i in range(len(pts)):
        T += distance(pts[i], pts[i - 1])
    return T


def geogebra(pts, T, N=20, p=0):
    '''
    pts : courbe : liste de points (tuples)
    T : période/périmètre de la courbe pts
    N : nombre de coefficients de fourier / nombre de cercle + 1
    p : module minimal de la partie réele des coefficients / rayon minimal des cercles

    print instructions de construction geogebra
    '''
    # Calcul des coefficients
    N //= 2
    coef = [c(k, pts, T) for k in range(-N, N + 1)]

    # Période
    print(f'Ne pas oublier t de période {ceil(T)} et show trace')

    # Centres des cercles
    print('C0  = 0 + 0ί')
    indexes = [0]
    for k in range(2 * N + 1):
        if abs(coef[k].real) > p:
            print(f'C{k+1} = C{indexes[-1]} + ({coef[k].real:.20f} + {coef[k].imag:.20f}ί) * exp({-(k - N)} / {T:.20f} * 2  * π * t * ί)')
            indexes.append(k + 1)

    # Cercles
    for k in range(1, len(indexes)):
        print(f'Circle(C{indexes[k - 1]}, C{indexes[k]})')


def equation(pts, T, N=20, p=0):
    '''
    pts : courbe : liste de points (tuples)
    T : période/périmètre de la courbe pts
    N : nombre de coefficients de fourier / nombre de cercle + 1
    p : module minimal de la partie réele des coefficients / rayon minimal des cercles

    print équation de l'épicycloïde
    '''
    N //= 2
    return ' + '.join([f'({c(k, pts, T).real:.20f} + {c(k, pts, T).imag:.20f}ί)' + f' * ℯ^(-ί * {2 * k / T * pi:.20f} * t)' if abs(c(k, pts, T).real) > p else 'a' for k in range(-N, N + 1)]).replace('a + ', '').replace('+ a', '')


def fourier_iter(ts, pts, T, N=20, p=0):
    '''
    ts : liste de valeurs pour t
    pts : courbe : liste de points (tuples)
    T : période/périmètre de la courbe pts
    N : nombre de coefficients de fourier / nombre de cercle + 1
    p : module minimal de la partie réele des coefficients / rayon minimal des cercles

    return liste points approximant la courbe
    '''
    N //= 2
    coef = [c(k, pts, T) for k in range(-N, N + 1)]
    return [sum([coef[k + N] * exp(complex(0, 2 * pi * k / T * t)) if abs(coef[k + N].real) > p else 0 for k in range(-N, N + 1)]) for t in ts]


def fourier(t, pts, T, N=20, p=0):
    '''
    t : paramètre de l'épicycloïde
    pts : courbe : liste de points (tuples)
    T : période/périmètre de la courbe pts
    N : nombre de coefficients de fourier / nombre de cercle + 1
    p : module minimal de la partie réele des coefficients / rayon minimal des cercles

    return liste points approximant la courbe
    '''
    N //= 2
    return sum(c(k, pts, T) * exp(complex(0, 2 * pi * k / T * t)) if abs(c(k, pts, T).real) > p else 0 for k in range(-N, N + 1))


def c(k, pts, T):
    '''
    k : indice du coefficient de fourier
    pts : courbe : liste de points (tuples)
    T : période/périmètre de la courbe pts

    return k-ième coefficient de fourier
    '''
    coefs = 0
    t = 0
    n = 0
    while t < T and n < len(pts):
        try:
            dt = distance(pts[n], pts[n + 1])
        except IndexError:
            dt = distance(pts[0], pts[-1])
        coefs += dt * exp(complex(0, -k * t * 2 * pi / T)) * complex(pts[n][0], pts[n][1])
        n += 1
        t += dt
    return coefs / T


if __name__ == '__main__':
    nb_cercles = 50
    rayon_minimal = 0
    path = 'ens.png'

    print("Détection d'un bord et des coordonnés de la courbe.")
    pts = curve(edge(path))

    print("Séparation des x et y.")
    ptsx = [pt[0] for pt in pts]
    ptsy = [pt[1] for pt in pts]

    print("Calcul de la période.")
    T = periode(pts)

    print("Échantillonage des ts.")
    p = 1  # précision
    ts = [t / p for t in range(ceil(T * p) + 1)]

    print("Calcul des affixes des pts de la série de fourier complexe de la courbe.")
    zs = fourier_iter(ts, pts, T, N=nb_cercles, p=rayon_minimal)

    print("Séparation des x et y.")
    xs = list(map(lambda z: z.real, zs))
    ys = list(map(lambda z: z.imag, zs))

    print("Affichage des courbes.")
    plt.subplot(2, 1, 1)
    plt.scatter(ptsx, ptsy, s=1)
    plt.subplot(2, 1, 2)
    plt.scatter(xs, ys, s=1)
    plt.show()

    # Pour s'assurer que la fenêtre du graphique est bien fermée.
    sleep(0.2)

    print("Affichage des instructions et de l'équation de l'épicycloïde.")
    geogebra(pts, T, nb_cercles, rayon_minimal)
    print(equation(pts, T, nb_cercles, rayon_minimal))

