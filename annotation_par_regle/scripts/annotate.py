from .syllabification import is_vowel

from typing import List
from pie_extended.cli.utils import get_tagger, get_model
from pie_extended.models.fro.imports import get_iterator_and_processor

# In case you need to download
do_download = False
if do_download:
    for dl in download("fro"):
        x = 1
#set_up
iterator, processor = get_iterator_and_processor()		
model_name = "fro"
tagger = get_tagger(model_name, batch_size=256, device="cuda", model_path=None)

def get_POS_tag(verse):
    output = tagger.tag_str(verse, iterator=iterator, processor=processor)
    POS_list  = [entry['POS'] for entry in output]
    lemma_list = [entry['lemma'] for entry in output]
    morph_list = [entry['morph'] for entry in output]
    #supprime les entrées comprenant une apostrophe car elles sont importantes pour le POS_tagging mais n'ont aucun intérêt pour l'annotation 
    apo_index = []
    for index, token in enumerate([entry['form'] for entry in output]):
        if "'" in token or "’" in token or "ʼ" in token:
            apo_index.append(index)
    for index in reversed(apo_index):
        del POS_list[index]
        del lemma_list[index]
        del morph_list[index]
    return POS_list, lemma_list, morph_list

def syllabed_to_verse(syllabed):
	verse_list = []
	for word_sep in syllabed:
		word = ''.join(word_sep) + ' '
		verse_list.append(word)
	verse = ''.join(verse_list)
	return verse

def is_tool_word(POS, lemma, morph):
	toolPOS = ['PRO', 'DET', 'PRE', 'CON', 'ETR', 'ABR', 'RED', 'OUT', 'ADV']
	maybeToolPOS= ['VER'] #toolword if lemma avoir or estre1 for verb and not toolword if morph ADV has DEGRE inside
	return (POS in toolPOS) or (POS in maybeToolPOS and (lemma in ['avoir', 'estre1'] or 'DEGRE' not in morph and POS == 'ADV'))

def is_weak(syl, POS):
	if len(syl) > 2 :
		return syl[-1] == 'e' or syl[-2:] == 'es' or (syl[-3:] == 'ent' and POS != 'ADV')
	elif len(syl) > 1:
		return syl[-1] == 'e' or syl[-2:] == 'es'
	else:
		return syl[-1] == 'e'

def annotate_step(syllabed, POS_list, lemma_list, morph_list):
	ano_verse = ''
	for i in range(len(syllabed)):
		if is_tool_word(POS_list[i][0:3], lemma_list[i], morph_list[i]):
			ano_verse = ano_verse + len(syllabed[i]) * 'w' 
		else:
			if is_weak(syllabed[i][-1], POS_list[i][0:3]):
				if len(syllabed[i]) == 1:
					   ano_verse = ano_verse + 'w'
				else:
					ano_verse = ano_verse + (len(syllabed[i]) - 2) * 'w' + 'Sw'
			else:
				ano_verse = ano_verse + (len(syllabed[i]) - 1) * 'w' + 'S'
		ano_verse = ano_verse + '.'
	return ano_verse[0:-1] #[0:-1] sert à ne pas afficher le dernier point

def find_dot_positions(input_string):
    positions = [i for i, char in enumerate(input_string) if char == '.']
    return positions

def correct_annotation(syllabed, ano_verse, POS): #POS du dernier mot du vers
	ano_verse = list(ano_verse)
	dots = find_dot_positions(ano_verse)
	if ano_verse[-1] == 'w':
		if is_weak(syllabed[-1][-1], POS):
			ano_verse[-1] = 'e'
	for i in range(len(dots)):
		dot_pos = dots[i]
		if ano_verse[dot_pos - 1] == 'w' :
			if len(syllabed[i]) > 1 and syllabed[i][-1][-1] == 'e' and is_vowel(syllabed[i+1][0][0]): #suppression du 'u' ou pas ?, à tester
				ano_verse[dot_pos - 1] = 'e'
	
	return "".join(ano_verse)	

def annotation(syllabed):
	verse = syllabed_to_verse(syllabed)
	POS_list, lemma_list, morph_list = get_POS_tag(verse)
	ano_verse = annotate_step(syllabed, POS_list, lemma_list, morph_list)
	ano_verse = correct_annotation(syllabed, ano_verse, POS_list[-1])
	return ano_verse
	
