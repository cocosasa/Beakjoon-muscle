from sys import stdin,stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for i in M:
    stdout.write('1\n') if i in N else stdout.write('0\n')