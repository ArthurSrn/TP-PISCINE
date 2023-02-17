# on souhaite créer une structure de données qui représente une carte routière comprenant des villes reliées par des routes
# la structure de données doit être capable de prendre en compte la distance entre deux villes et les temps de trajet en fonction de la vitesse des distances et de la vitesse moyenne sur les routes

# Écrivez une fonction qui prend en entrée deux villes et renvoie le temps minimum nécessaire pour se déplacer d'une ville à l'autre en utilisant la structure de données. La fonction doit gérer les cas où aucun chemin n'existe entre les deux villes en renvoyant un message d'erreur approprié.

class RoadMap:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        # ajouter une ville au graphe avec une liste vide de routes sortantes
        self.graph[city] = []

    def add_road(self, source, dest, distance, speed_limit):
        # calculer le temps de trajet en fonction de la vitesse moyenne
        time = distance / speed_limit

        # ajouter une route sortante à la ville source avec la ville destination et les poids distance et temps
        self.graph[source].append((dest, distance, time))

    def get_distance(self, source, dest):
        # retourner la distance entre deux villes adjacentes
        for road in self.graph[source]:
            if road[0] == dest:
                return road[1]

        # si les villes ne sont pas adjacentes, retourner None
        return "Erreur: les deux villes ne sont pas adjacentes"

    def get_time(self, source, dest):
        # retourner le temps de trajet entre deux villes adjacentes
        for road in self.graph[source]:
            if road[0] == dest:
                return road[2]

        # si les villes ne sont pas adjacentes, retourner None
        return "Erreur: les deux villes ne sont pas adjacentes"


# voici un exemple d'utilisation de la classe RoadMap
# on crée une carte routière
road_map = RoadMap()

# on ajoute des villes à la carte
road_map.add_city("A")
road_map.add_city("B")
road_map.add_city("C")
road_map.add_city("D")
road_map.add_city("E")
road_map.add_city("F")

# on ajoute des routes à la carte
road_map.add_road("A", "B", 10, 50)
road_map.add_road("A", "C", 20, 50)
road_map.add_road("B", "D", 30, 50)
road_map.add_road("B", "E", 40, 50)
road_map.add_road("C", "F", 50, 50)
road_map.add_road("D", "F", 60, 50)

# on affiche la distance entre deux villes adjacentes
print(road_map.get_distance("A", "B"))
print(road_map.get_distance("B", "D"))
print(road_map.get_distance("C", "F"))

# on affiche le temps de trajet entre deux villes adjacentes
print(road_map.get_time("A", "B"))
print(road_map.get_time("B", "D"))
print(road_map.get_time("C", "F"))

# on affiche la distance entre deux villes non adjacentes (message d'erreur attendu)
print(road_map.get_distance("A", "D"))
