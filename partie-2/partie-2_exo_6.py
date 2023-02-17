dict = [{
        'nom': 'Clan Asano',
        'membres': 50,
        'chef': 'Yashiteru'
        },
        {
        'nom': 'Clan Hiroshima',
        'membres': 40,
        'chef': 'Narikata'

        },
        {
        'nom': 'Clan Munetsune',
        'membres': 35,
        'chef': 'Shigeakira'
        }
        ]

# on souhaite afficher le nombre de clans
print(len(dict))

# on souhaite le clan avec le plus de membres
print(max(dict, key=lambda x: x['membres']))

# on souhaite intervertir les valeurs des clés "nom" et "chef" pour chaque clan
for clan in dict:
    clan['nom'], clan['chef'] = clan['chef'], clan['nom']

print(dict)
