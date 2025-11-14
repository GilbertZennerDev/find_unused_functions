def findunusedfunctions(file):
    content = open(file, "r").read().splitlines()
    content = [line for line in content if '#' not in line]
    # the idea is to check whether every line which has a
    # def bla also has a line where only
    # bla()
    defs = [line for line in content if 'def ' in line]
    defs = [line.split()[1] for line in defs]
    defs = [part[:part.index('(')] for part in defs]
    func_calls = [line[:line.index('(')] for line in content if '(' in line and 'def' not in line]
    unused_funcs = [func for func in defs if func not in func_calls]
    print(defs, func_calls, unused_funcs)

if __name__ == "__main__": findunusedfunctions('testprogram.py')