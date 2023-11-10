import random

def lotto():
    lotto_numbers = []
    a = 0
    while a < 6:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)
            a += 1
    lotto_numbers.sort()
    print(f"생성된 로또 번호는 {lotto_numbers}입니다.")

lotto()

