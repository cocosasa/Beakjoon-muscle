string = input()

tailwords = []

for i in range(len(string)) :
    tailwords.append(string[i:])

tailwords.sort()
for s in tailwords : 
    print(s)