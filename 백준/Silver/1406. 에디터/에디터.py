import sys

left_stack = list(sys.stdin.readline().strip())  # 초기 문자열
right_stack = []
n = int(sys.stdin.readline())  # 명령 개수

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'L':  # 왼쪽 이동
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command[0] == 'D':  # 오른쪽 이동
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command[0] == 'B':  # 문자 삭제
        if left_stack:
            left_stack.pop()

    elif command[0] == 'P':  # 문자 삽입
        left_stack.append(command[1])

# 결과 출력 (left_stack + right_stack 역순)
print(''.join(left_stack + right_stack[::-1]))
	