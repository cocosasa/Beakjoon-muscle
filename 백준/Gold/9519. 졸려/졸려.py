N = int(input())

word = input()
origin = word

word_list = [word]

word_len = len(word)
is_odd = word_len%2
half_len = word_len//2
if(is_odd) :   
    half_len += 1

count = 1

while count <= N : 
    start = word[::2]
    end = word[1::2][::-1]

    word = start+end
    word_list.append(word)
    if word == origin : 
        break
    count += 1
print(word_list[N%count])