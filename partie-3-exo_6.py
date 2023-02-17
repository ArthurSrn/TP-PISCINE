def parentheses_equilibrium(expression):
    # Vérifier si la chaîne est vide
   
    if expression=='' :
        print("La chaîne est vide.")
    else :
        print("La chaîne n'est pas vide.")
    

    # Utiliser une pile pour vérifier l'équilibre des parenthèses
    stack = []
    for parenthese in expression:
        if parenthese == '(':
            stack.append(parenthese)
        elif parenthese == ')':
            if not stack:
                return False
            stack.pop()
    
    # Vérifier si toutes les parenthèses ont été fermées
    return len(stack) == 0


print(parentheses_equilibrium("((3 + 4) * 5)"))