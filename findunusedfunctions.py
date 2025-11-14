# the idea is to check whether every line which has a
    # def bla also has a line where only
    # bla()

def giveContent(filename):
    content = open(filename, "r").read().splitlines()
    return [line for line in content if '#' not in line]

def giveDefs(content):
    defs = [line.split()[1] for line in content if 'def ' in line]
    return [part[:part.index('(')] for part in defs]

def giveFuncCalls(content):
    return [line[:line.index('(')] for line in content if '(' in line and 'def' not in line]

def giveUnusedFuncs(defs, func_calls):
    return [func for func in defs if func not in func_calls]

def findunusedfunctions(filename):
    content = giveContent(filename)
    unused_funcs = giveUnusedFuncs(giveDefs(content), giveFuncCalls(content))
    print("Unused Functions:", unused_funcs)

if __name__ == "__main__": findunusedfunctions('testprogram.py')