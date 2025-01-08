def make_list(f_name1, f_name2):
    list1 = []
    list2 = []

    # Ouvrir le premier fichier et lire les lignes
    with open(f_name1, 'r') as file1:
        for line in file1:
            list1.append(line.strip())  # Utiliser strip() pour enlever les caractères de nouvelle ligne

    # Ouvrir le deuxième fichier et lire les lignes
    with open(f_name2, 'r') as file2:
        for line in file2:
            list2.append(line.strip())  # Utiliser strip() pour enlever les caractères de nouvelle ligne

    return list1, list2

def compare(list1, list2):
    v = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            v += 1
        else:
            print(f"Ligne {i+1} de la liste 1: {list1[i]}")
            print(f"Ligne {i+1} de la liste 2: {list2[i]}")
            user_input = input("Les lignes sont différentes. Tapez 'o' pour continuer ou 'n' pour passer à la ligne suivante: ")
            if user_input.lower() == 'o':
                v += 1
    return v / len(list1)


#f_name1 = "temoin_claude.txt"
f_name1 = "test_file.txt"
f_name2 = "test_controle.txt"
list_ai, list_control = make_list(f_name1, f_name2)
print("Taux de confiance = ", compare(list_ai, list_control))
