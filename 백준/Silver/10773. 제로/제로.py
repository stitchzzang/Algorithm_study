K = int(input())
total = []
for k in range(1, K+1):
    money = int(input())
    if money != 0 :
        total.append(money)
    elif money == 0 and len(total) != 0 :
        total.pop()
total_money = len(total)
if total_money == 0:
    print(0)
else :
    total_money = sum(total)
    print(total_money)