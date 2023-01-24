N = int(input())
words = set()
for i in range(N) :
	words.add(input())
words = list(words)
words.sort()
words.sort(key = lambda x : len(x) )
for word in words :
	print(word)