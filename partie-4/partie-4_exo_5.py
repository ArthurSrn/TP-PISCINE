# Exercice 5: Liste d'emplois

# Créez une fonction qui prend en entrée une liste de dictionnaires représentant des emplois et un input utilisateur. Chaque dictionnaire contient les clés 'id', 'title', 'description' et 'qualifications'.

# 'id' est un identificateur unique pour chaque emploi
# 'title' est le titre de l'emploi,
# 'description' est une description de l'emploi
# 'qualifications' est une liste de qualifications requises

# La fonction doit renvoyer une liste contenant les emplois correspondant au terme récupéré par l’input utilisateur, et présent dans au moins une valeur du dictionnaire.


def search_jobs(jobs, term):
    result = []
    for job in jobs:
        for value in job.values():
            if isinstance(value, str) and term in value:
                result.append(job)
                break
    return result


jobs = [
    {
        'id': 1,
        'title': 'Ingénieur logiciel',
        'description': 'Conception et développement de logiciels pour des applications web',
        'qualifications': ['Bac+5 en informatique', 'Expérience en développement web', 'Maîtrise de Python, Java et SQL']
    },
    {
        'id': 2,
        'title': 'Développeur front-end',
        'description': 'Développement d\'interfaces utilisateur pour des applications web',
        'qualifications': ['Bac+2 en informatique', 'Expérience en développement front-end', 'Maîtrise de HTML, CSS et JavaScript']
    },
    {
        'id': 3,
        'title': 'Analyste financier',
        'description': 'Analyse des données financières et préparation de rapports pour la direction',
        'qualifications': ['Bac+5 en finance', 'Expérience en analyse financière', 'Maîtrise de Microsoft Excel']
    },
    {
        'id': 4,
        'title': 'Analyste des ressources humaines',
        'description': 'Gestion des ressources humaines et recrutement de nouveaux employés',
        'qualifications': ['Bac+3 en ressources humaines', 'Expérience en gestion des ressources humaines', 'Bonne communication et compétences interpersonnelles']
    }
]

term = 'Analyste'

matching_jobs = search_jobs(jobs, term)


for job in matching_jobs:
    print(job['title'])
