def decimal_vers_binaire(decimal):
    # Vérifier que l'entrée est un nombre entier positif
    if not isinstance(decimal, int) or decimal < 0:
        return ValueError("L'entrée doit être un nombre entier positif.")

    if decimal == 0:
            return "0"

    # Conversion en binaire
    binaire = ""
    while decimal > 0:
        binaire = str(decimal % 2) + binaire
        decimal //= 2

    
    return binaire
    

binaire = decimal_vers_binaire(62)
print(binaire)  # "111110"
