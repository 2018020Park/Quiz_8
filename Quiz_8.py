import random

lotto = []
a = 0

while a < 6:
    number = random.randint(1, 45)
    if number not in lotto:
        lotto.append(number)
    a += 1
lotto.sort()

print(f"생성된 로또 번호는 {lotto}입니다.")
