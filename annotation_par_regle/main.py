#modules maison
import scripts.tools as st

#modules python à télécharger
from pathlib import Path

#fonctions maison
from scripts.clean_data import clean_files #no argument, need folder raw_data and clean_data
from scripts.clean_annotation import correct_annotation #arguments: syllabed, annotated
from scripts.syllabification import divide_verse_into_syllables #argument: verse
from scripts.annotate import annotation #arg

st.nouveau_dossier("clean_data")
st.nouveau_dossier("annotated_data")
clean_files()

#print(divide_verse_into_syllables('quoi quel qualité quais laquais est'))

for p in Path('./clean_data/').glob('*.txt') :
	print(p)
	filename = "./annotated_data/" + str(p)[11:len(str(p))]
	content = st.file_to_lines(str(p))
	st.new_empty_file(filename)
	for line in content:
		s_verse = divide_verse_into_syllables(line)
		ano_verse = annotation(s_verse)
		with open(filename, 'a', encoding="utf-8") as f:
			f.write(ano_verse + '\n')