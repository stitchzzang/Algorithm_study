room_num = input()
answer = [0] * 10
for i in range(len(room_num)):
    num = int(room_num[i])
    if num == 6 or num == 9:
        if answer[6] <= answer[9]: # 6, 9는 더 작은 인덱스 번째를 증가시켜줌 / 편의상 낮은 인덱스를 증가
            answer[6] += 1 # 6이 더 작으면 6 개수를 증가
        else:
            answer[9] += 1 # 9가 더 작으면 9 개수를 증가
    else:
        answer[num] += 1

print(max(answer)) # 인덱스를 증가시키는 과정이 끝난 후 리스트에서 최댓값을 출력