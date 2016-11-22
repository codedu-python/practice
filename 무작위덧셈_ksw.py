import random
print('문제는 총 10문제이고, 한 문제당 10점입니다.')

right = 0
def addition_test(i, a, b):
    try:
        answer = int(input('{}번문제: {} + {} = ?\n'.format(i, a, b)))
        return answer
    except:
        answer = addition_test(i, a, b)
        return answer

for i in range(1,11):
    a = random.randint(10,99)
    b = random.randint(10,99)
    answer = addition_test(i, a, b)
    if answer == a + b:
        print('정답입니다.\n')
        right = right + 1
    else:
        print('오답입니다.\n')

score = right*10
print('%d점 입니다.' %(score))
