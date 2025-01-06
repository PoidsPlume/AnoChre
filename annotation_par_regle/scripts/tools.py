import os

def nouveau_dossier(path_name):
    newpath = path_name 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def file_to_lines(filename):
	lines = []
	with open(filename, 'r', encoding="utf-8") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def new_empty_file(filename):
    with open(filename, 'w+', encoding="utf-8") as f:
        f.write("")
