def find_dot_positions(input_string):
    positions = [i for i, char in enumerate(input_string) if char == '.']
    return positions

def correct_annotation(syllabed, annotated):
	annotated = list(annotated)
	dot_annotated = find_dot_positions(annotated)
	dot_syllabed = find_dot_positions(syllabed)
	if annotated[-1] == 'w' and len(syllabed[-1]) > 1:
		if (syllabed[-1] == 'e' or syllabed[-2:] == 'es' or (syllabed[-3:] == 'ent' and syllabed[-4:] != 'ment')): #prends en compte les terminsaisons de verbe en 'ent' en excluant les adverbes finissant par "ment"
			annotated[-1] = 'e'
	for i_a, i_s in zip(dot_annotated, dot_syllabed):
		if annotated[i_a - 1] == 'w':
			if (syllabed[i_s - 1] == 'e' and syllabed[i_s+2] in ['a', 'à', 'e', 'é', 'è', 'i', 'o']): #exclue le u car la syllabe n'est pas élidée quand c'est un v
				annotated[i_a - 1] = 'e'
	return "".join(annotated)
