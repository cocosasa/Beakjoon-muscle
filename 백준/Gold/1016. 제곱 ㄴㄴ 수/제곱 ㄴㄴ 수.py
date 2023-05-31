def era_prime(N):
    A = [0 for _ in range(N - _min)]
    for i in range(2, int(_max**0.5)+1):
        temp = i*i
        start_index = _min//temp * temp
        for j in range(start_index, N, temp):
            if j < _min:
                continue
            A[j - _min] = 1
    return A

_min, _max = map(int, input().split())

p = era_prime(_max+1)
ans = 0
for n in  p :
    if not n :
        ans += 1

print(ans)

