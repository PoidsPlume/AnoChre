#modules maison
import scripts.tools as st

#modules python à télécharger
from pathlib import Path

#fonctions maison
from scripts.clean_data import clean_files #no argument, need folder raw_data and clean_data
from scripts.clean_annotation import correct_annotation #arguments: syllabed, annotated
from scripts.syllabification import divide_verse_into_syllables #argument: verse

st.nouveau_dossier("clean_data")
clean_files()

#print(divide_verse_into_syllables('quoi quel qualité quais laquais est'))

for p in Path('clean_data/').glob('*.txt'):
	content = st.file_to_lines(str(p))
	syllabed = []
	for line in content:
		s_verse = divide_verse_into_syllables(line.lower())
		syllabed.append(s_verse)
		print(syllabed)		