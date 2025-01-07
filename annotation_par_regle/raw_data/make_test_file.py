def annotate_file(input_file, output_file):
    """
    Fonction pour lire un fichier, demander à l'utilisateur de noter l'annotation pour chaque ligne,
    et écrire les annotations dans un fichier de sortie.

    :param input_file: Le fichier à lire.
    :param output_file: Le fichier dans lequel enregistrer les annotations.
    """
    with open(input_file, 'r', encoding = "utf-8") as in_file, open(output_file, 'w', encoding = "utf-8") as out_file:
        for line in in_file:
            print(f"Ligne: {line.strip()}")
            annotation = input("Veuillez entrer l'annotation pour cette ligne: ")
            out_file.write(f"{annotation}\n")

# Exemple d'utilisation
input_file = "test_file.txt"
output_file = "test_controle.txt"
annotate_file(input_file, output_file)