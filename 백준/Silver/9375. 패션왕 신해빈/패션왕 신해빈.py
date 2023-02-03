T = int(input())

for tc in range(T) :
    N = int(input())        

    dic = {}
    for i in range(N) :
        name , a = (input().split())
        if dic.get(a) == None :
            dic[a] = {name,}
        else :
            dic[a].add(name)
            
    ans = 1
    for item in dic.values() :
        ans *= len(item)+1

    
    ans -= 1
    print(ans)
    