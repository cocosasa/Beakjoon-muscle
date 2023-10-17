def solve(n) :
    a,b,c,d,e,f = list(map(int,input().split()))

    numbers = [a,b,c,d,e,f]

    combi = []

    triple = []

    for i in [b,c,d,e] :
        combi.append(sum((a,i)))
    for i in [c,f,d] :
        combi.append(sum((b,i)))
    for i in [e,f] :
        combi.append(sum((c,i)))
    for i in [e,f] :
        combi.append(sum((d,i)))
    for i in [f] :
        combi.append(sum((e,i)))

    triple.append(sum((a,b,c)))
    triple.append(sum((b,f,c)))
    triple.append(sum((f,e,c)))
    triple.append(sum((e,a,c)))
    triple.append(sum((a,b,d)))
    triple.append(sum((b,f,d)))
    triple.append(sum((f,e,d)))
    triple.append(sum((e,a,d)))


    min_sum = min(combi)

    min_num = min(numbers)

    min_triple = min(triple)

    ans = 0

    if n == 1 :
        return sum(numbers)-max(numbers)
    if n == 2 :
        pass

    # 옆면의 면
    ans += (n-2) * (n-1) * min_num * 4
    # 윗면의 면
    ans += (n-2) * (n-2) * min_num

    # 옆면의 변 4개
    ans += (n-1) * min_sum * 4
    # 윗면의 변 4개
    ans += (n-2) * min_sum * 4

    # 윗모서리 4개
    ans += min_triple * 4


    return ans

n = int(input())

print(solve(n))
