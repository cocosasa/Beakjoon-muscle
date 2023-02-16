N = int(input())

words = [input() for i in range(N)]
new_words = []

val_dict = {10**i:[] for i in range(8)}

for word in words :
    for i in range(len(word)) :
        val_dict[10**i].append(word[-i-1])
        
alpha_dict = {chr(65+i):0 for i in range(26)}

for val in val_dict.keys() :
    for al in val_dict[val] :
        alpha_dict[al] += val

sorteddict = sorted(alpha_dict.items(),key=lambda x: x[1])
new_dict = {}
for i in range(1,11):
    new_dict[sorteddict[-i][0]] = str(10-i)

for i in range(N) :
    newword = ''
    for c in words[i]:
        newword += new_dict[c]
    new_words.append(int(newword))
    
ans = sum(new_words)
print(ans)
    