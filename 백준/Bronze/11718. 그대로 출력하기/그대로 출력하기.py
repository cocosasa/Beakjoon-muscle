# 입력 받기
lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

# 입력 그대로 출력하기
for line in lines:
    print(line)