# the idea is to check whether every line which has a
	# def bla also has a line where only
	# bla()

import sys
from pathlib import Path

def get_all_filenames(folder):
	return [str(name) for name in list(Path(folder).rglob('*.py'))]

def giveContent(filename):
	try:
		content = open(filename, "r").read().splitlines()
		return [line for line in content if '#' not in line]
	except Exception as e:
		print(e);

def giveDefs(content):
	if content == None: return []
	defs = [line.split()[1] for line in content if 'def' in line]
	defs = [line for line in defs if '(' in line]
	return [part[:part.index('(')] for part in defs]

#need to improve the code for bla(bla(bla()))

def chk_chrs_in_line(line, chrs):
	for c in chrs:
		if c in line: return c
	return False

def cut_line(line):
	chrs = "(["
	line_funcs = []
	while chk_chrs_in_line(line, chrs):
			if '(' in line: c = '('
			if '[' in line: c = '['
			func_call = line[:line.find(c)]
			line = line[line.find(c) + 1 :]
			if 'def ' in func_call: break
			line_funcs.append(func_call)
	return line_funcs

def giveFuncCalls(content):
	if content == None: return []
	all_func_calls = []
	for line in content: all_func_calls += cut_line(line)
	return [call.strip() for call in all_func_calls]

def giveUnusedFuncs(defs, func_calls):
	return [func for func in defs if func not in func_calls]

def combine_files(files):
	combined = []
	arr = [giveContent(file) for file in files]
	for subarr in arr:
		if subarr == None: continue
		for part in subarr:
			if part == None: continue
			if len(part): combined.append(part)
	return combined

def find_unused_functions(content):
	print('All func definitions:', giveDefs(content))
	print('All func calls:', giveFuncCalls(content))
	unused_funcs = giveUnusedFuncs(giveDefs(content), giveFuncCalls(content))
	if not len(unused_funcs): print("No unused functions!"); exit()
	print(f"{len(unused_funcs)} Unused Functions:")
	for func in unused_funcs: print(func)
	return unused_funcs

if __name__ == "__main__":
	ac = len(sys.argv)
	if ac == 3 and sys.argv[1] == '-f': find_unused_functions(combine_files(get_all_filenames(sys.argv[2]))); exit()
	find_unused_functions(combine_files(sys.argv[1:]))