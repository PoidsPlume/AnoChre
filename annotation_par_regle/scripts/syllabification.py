def is_vowel(letter):
	vowels = [
	'a', 'A', 'á', 'Á', 'à', 'À', 'â', 'Â', 'ä', 'Ä', 'ã', 'Ã', 'å', 'Å', 'æ', 'Æ',
	'e', 'E', 'é', 'É', 'è', 'È', 'ê', 'Ê', 'ë', 'Ë', 'ė', 'Ė', 'ę', 'Ę', 'ě', 'Ě',
	'i', 'I', 'í', 'Í', 'ì', 'Ì', 'î', 'Î', 'ï', 'Ï', 'ĩ', 'Ĩ', 'į', 'Į', 'ī', 'Ī',
	'o', 'O', 'ó', 'Ó', 'ò', 'Ò', 'ô', 'Ô', 'ö', 'Ö', 'õ', 'Õ', 'ø', 'Ø', 'œ', 'Œ',
	'u', 'U', 'ú', 'Ú', 'ù', 'Ù', 'û', 'Û', 'ü', 'Ü', 'ũ', 'Ũ', 'ų', 'Ų', 'ū', 'Ū',
	'y', 'Y', 'ý', 'Ý', 'ÿ', 'Ÿ', 'ŷ', 'Ŷ'
	]
	return letter in vowels

def is_consonant(letter):
	consonant = [
	'b', 'B', 'c', 'C', 'ç', 'Ç', 'č', 'Č', 'ć', 'Ć',
	'd', 'D', 'ď', 'Ď', 'đ', 'Đ',
	'f', 'F',
	'g', 'G', 'ğ', 'Ğ',
	'h', 'H', 'ħ', 'Ħ',
	'j', 'J',
	'k', 'K', 'ĸ', 'Ĺ',
	'l', 'L', 'ł', 'Ł', 'ļ', 'Ļ', 'ľ', 'Ľ',
	'm', 'M',
	'n', 'N', 'ń', 'Ń', 'ň', 'Ň', 'ņ', 'Ņ', 'ñ', 'Ñ',
	'p', 'P',
	'q', 'Q',
	'r', 'R', 'ŕ', 'Ŕ', 'ř', 'Ř',
	's', 'S', 'ś', 'Ś', 'š', 'Š', 'ş', 'Ş',
	't', 'T', 'ť', 'Ť', 'ţ', 'Ţ',
	'v', 'V',
	'w', 'W', 'ŵ', 'Ŵ',
	'x', 'X',
	'z', 'Z', 'ź', 'Ź', 'ż', 'Ż', 'ž', 'Ž'
	]
	return letter in consonant

def is_neutral(char):
	return char in [ "’",  "'",  "ʼ" ]

def is_diphtong(letters):
	diphtongues = [
	'ai', 'au', 'ei', 'eu', 'oi', 'ou', 'ua', 'ui', 'uo', 'ìi', 'íi'
	]
	return letters in diphtongues

def is_diphtong_e(letters):
	diphtongues = [
	'ie', 'ue', 'oe', 'io'
	]
	return letters in diphtongues

def divide_word_into_syllables(word):
	syllables = []
	syllable = ""
	i = 0
	while i < len(word):
		#ajoute les lettres à la syllabe tant que ce sont des consonnes, si une syllabe n'a pas de voyelle à la fin, la rattache à la syllabe précédente
		if is_consonant(word[i]):
			syllable = syllable + word[i]
			if i == len(word) - 1 and len(syllables) > 0:
				for letter in syllable:
					had_vowel = is_vowel(letter)
					if had_vowel:
						break
				if had_vowel:
					syllables.append(syllable)
				else:
					syllables[-1] = syllables[-1] + syllable
			i = i + 1
		#gestion des voyelles
		elif is_vowel(word[i]):
			#gestion des diphtongues
			if i + 1 < len(word):
				if is_diphtong(word[i:i+2]) or is_neutral(word[i+1]):
					syllable = syllable + word[i:i+2]
					i = i + 2
				elif i + 2 < len(word):
					#ne considère pas les diphtongues terminant par un e comme un diphtong pour garder la prononciation du e final
					if is_diphtong_e(word[i:i+2]): #and is_consonant(word[i+2]): 
						syllable = syllable + word[i:i+2]
						i = i + 2
					else:
						syllable = syllable + word[i]
						i = i + 1
				else:
					syllable = syllable + word[i]
					i = i + 1
					
			else:	
				syllable = syllable + word[i]
				i = i + 1
			syllables.append(syllable)
			syllable = ""
		elif is_neutral(word[i]):
			syllable = syllable + word[i]
			i = i + 1
		#gestion des caractères inconnus
		else:
			#print(f"Le caractère '{word[i]}' est inconnu\nMot traité: {word}\nEtat de la syllabe: {syllable}")
			#user_input = input("Tapez '0' pour supprimer le caractère, '1' pour l'ajouter à la syllabe en cours, '2' pour commencer une nouvelle syllabe par ce caractère\n")
			#if user_input == '1':
			#	syllable = syllable + word[i]
		#	elif user_input == '2':
		#		syllables.append(syllable)
		#		syllable = word[i]
			i = i + 1
	
	#gestion qu
	if len(syllables) > 1:
		for i in range(len(syllables) - 1):
			if syllables[i][0:2] == 'qu' and is_vowel(syllables[i+1][0]): #and (is_diphtong(syllables[i][-1] + syllables[i+1][0]) or is_diphtong_e(syllables[i][-1] + syllables[i+1][0])):
				syllables[i] = syllables[i] + syllables[i+1][0]
				syllables[i+1] = syllables[i+1][1:len(syllables[i+1])]
		
	
	# A FAIRE -> gestion de la coupure des verbes qui finissent par 'uent' ou 'ient' ou 'oent'
	
	#répartition des consonnes correctement entre les syllabes
	i = 1
	while i < len(syllables):
		if len(syllables[i]) > 2:
			if is_consonant(syllables[i][0]) and is_consonant(syllables[i][1]) and not syllables[i][0:2] == 'ch':
				syllables[i-1] = syllables[i-1] + syllables[i][0]
				syllables[i] = syllables[i][1:len(syllables[i])]
		i = i + 1
	
	for i in range(len(syllables))[1:len(syllables)]:
		had_vowel = []
		for letter in syllables[i]:
			had_vowel.append(is_vowel(letter))
		if True not in had_vowel:
			syllables[i-1] = syllables[i-1] + syllables[i]
			syllables[i] = '' 
					
	
	if '' in syllables:
		syllables.remove('')
		
	return syllables

def divide_verse_into_syllables(verse):
	words = verse.split()
	syllables = []
	for word in words:
		syllables.append(divide_word_into_syllables(word))
	return syllables
