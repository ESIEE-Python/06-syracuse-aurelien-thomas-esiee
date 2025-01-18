#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    if n <= 0:
        raise ValueError("L'argument doit être un entier positif.")

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        print(f"Suite générée pour {n} : {sequence}")
    

    return sequence
    l = [ ]
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    
    return len(l) - 1

    n = 0
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    altitude_initiale = l[0]
    return sum(1 for valeur in l[1:] if valeur > altitude_initiale)

    n = 0
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    
    return max(l)
    
    n = 0
    return n


#### Fonction principale


def main():

    n = 7
    print(f"Calcul de la suite de Syracuse pour n = {n}")
    sequence = syracuse_l(n)
    print(f"Suite de Syracuse : {sequence}")

    temps_vol = temps_de_vol(sequence)
    print(f"Temps de vol : {temps_vol}")

    temps_altitude = temps_de_vol_en_altitude(sequence)
    print(f"Temps de vol en altitude : {temps_altitude}")

    altitude_max = altitude_maximale(sequence)
    print(f"Altitude maximale : {altitude_max}")

    # Génération du graphique de la suite
    syr_plot(sequence)
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()