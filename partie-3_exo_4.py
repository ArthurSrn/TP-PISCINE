def is_palindrome(chaine):
    # Verfication que la c'est une chaine de caractère
    if not isinstance(chaine, str):
        return TypeError("Ce n'est pas une chaîne de caractère")
    
    # Comparer la chaine en inversé
    return chaine == chaine[::-1]

# creation de la chaine 
chaine = "kayak"
is_a_palindrome = is_palindrome(chaine)
print(is_a_palindrome)
