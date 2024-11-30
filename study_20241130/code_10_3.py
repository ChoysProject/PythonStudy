def addNumber(num1, num2):
    if num2 <= num1:
        return 1
    return num1 + addNumber(num1, num1 + 1)


n1 = int(input('숫자1 -->'))
n2 = int(input('숫자2 -->'))

print(addNumber(n1, n2))
