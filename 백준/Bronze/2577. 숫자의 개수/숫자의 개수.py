A = int(input())
B = int(input())
C = int(input())

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = [0] * 10 # 정답 출력할 배열 생성 / 한줄씩 출력은 마지막에 하면 됨

multiple = A * B * C
mtp = str(multiple) # 곱한 숫자 문자열로 저장

for i in mtp: # 문자열 탐색
    # if i in number: # 숫자 배열에 들어있냐 ?
    idx = number.index(i) # 인덱스 번호 확인 후 저장
    answer[idx] += 1 # 해당 인덱스 번호의 숫자 개수 만큼 하나씩 누적합
for j in range(len(answer)):
    print(answer[j]) # answer 배열 한줄씩 띄워서 출력