S = input() # 단어 S 주어짐
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0] * 26

for i in S:
    if i in alphabet:
        idx_num = alphabet.index(i)
        answer[idx_num] += 1
print(*answer)
print(end=' ')