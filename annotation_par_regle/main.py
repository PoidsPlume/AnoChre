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

print(divide_verse_into_syllables('quoi quel qualité quais laquais'))

#for p in Path('clean_data/').glob('*.txt'):
#	content = st.file_to_lines(str(p))
#	print(content)
#	syllabed = ''
#	for line in content:
#		s_verse = divide_verse_into_syllables(line)
#		print(s_verse)
		#txt_verse = ''
		#for j in range(len(s_verse)):
		#	word = s_verse[j]
		#	for i in range(len(word)):
		#		if i != len(word) - 1:
		#			txt_verse = txt_verse + word[i] + '-'
		#		else:
		#			txt_verse = txt_verse + word[i]
		#	print(txt_verse)
				