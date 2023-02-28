A = input()
B = input()
A = '0' + A
B = '0' + B
len_A = len(A)
len_B = len(B)
LCS = [[0]*(len_B) for _ in range(len_A)]

for i in range(len_A) :
    for j in range(len_B) :
        if i == 0 or j == 0:  # 마진 설정
            LCS[i][j] = 0
        elif A[i] == B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
print(LCS[-1][-1])