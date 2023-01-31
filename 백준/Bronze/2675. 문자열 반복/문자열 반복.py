T = int(input())
for test_case in range(1,T+1) :
    N , s_in = input().split()
    N = int(N)
    for c in s_in :
        print(c*N,end='')
    print('')
