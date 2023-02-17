def conway_sequence(term, m):
    seq = [term]  # initialise la séquence avec le premier terme
    for i in range(m):
        next_term = ""  # initialise le terme suivant
        count = 1  # initialise le compteur de chiffres identiques
        for j in range(1, len(term)):
            if term[j] == term[j-1]: 
                count += 1  
            else: 
                next_term += str(count) + term[j-1]
                count = 1 
        next_term += str(count) + term[-1]  # ajouter le dernier chiffre au terme suivant
        seq.append(next_term)  
        term = next_term  
    return seq[1:]  


print(conway_sequence(term='2', m=7))