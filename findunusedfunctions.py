# the idea is to check whether every line which has a
	# def bla also has a line where only
	# bla()

import sys
from pathlib import Path

def get_all_filenames():
	return [str(name) for name in list(Path('.' + '/' + 'bla').rglob('*.py'))]

def giveContent(filename):
	try:
		content = open(filename, "r").read().splitlines()
		return [line for line in content if '#' not in line]
	except Exception as e:
		print(e);

def giveDefs(content):
	if content == None: return []
	defs = [line.split()[1] for line in content if 'def ' in line]
	return [part[:part.index('(')] for part in defs]

def giveFuncCalls(content):
	if content == None: return []
	return [line[:line.index('(')] for line in content if '(' in line and 'def' not in line]

def giveUnusedFuncs(defs, func_calls):
	return [func for func in defs if func not in func_calls]

def combine_files(files):
	combined = []
	arr = [giveContent(file) for file in files]
	for subarr in arr:
		for part in subarr:
			if len(part): combined.append(part)
	return combined

def find_unused_functions(content):
	unused_funcs = giveUnusedFuncs(giveDefs(content), giveFuncCalls(content))
	print("Unused Functions:", unused_funcs)

if __name__ == "__main__":
	ac = len(sys.argv)
	if ac < 2: find_unused_functions(combine_files(get_all_filenames())); exit()
	find_unused_functions(combine_files(sys.argv[1:]))