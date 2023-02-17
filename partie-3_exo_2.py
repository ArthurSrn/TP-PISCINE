class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

def somme_maximale(arbre):
    def somme_maximale_rec(noeud):
        if not noeud:
            return 0
        gauche_somme_maximale = somme_maximale_rec(noeud.gauche)
        droite_somme_maximale = somme_maximale_rec(noeud.droit)
        valeur = noeud.valeur if noeud.valeur > 0 else 0
        somme = gauche_somme_maximale + droite_somme_maximale + valeur
        if somme < valeur:
            return valeur
        else:
            return somme
    
    somme = somme_maximale_rec(arbre)
    return somme if somme > 0 else 0
