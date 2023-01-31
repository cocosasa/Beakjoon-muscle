strin = input()

for i in range(26) :
	if chr(i+97) in strin :
		print(strin.index(chr(i+97)),end=' ')
	else :
		print(-1,end=' ')