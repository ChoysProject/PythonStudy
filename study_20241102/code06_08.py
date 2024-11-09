class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_full(self):
        return self.top >= self.size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, data):
        if self.is_full():
            print("스택이 꽉 찼습니다.")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("스택이 비었습니다.")
            return None
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("스택이 비었습니다.")
            return None
        return self.stack[self.top]

    def display(self):
        print("스택 상태: ", self.stack)

# 메인 코드 부분
if __name__ == "__main__":
    size = int(input("스택의 크기를 입력하세요 ==> "))
    stack = Stack(size)

    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        if select in ('X', 'x'):
            print("프로그램 종료!")
            break
        elif select in ('I', 'i'):
            data = input("입력할 데이터 ==> ")
            stack.push(data)
            stack.display()
        elif select in ('E', 'e'):
            data = stack.pop()
            print("추출된 데이터 ==> ", data)
            stack.display()
        elif select in ('V', 'v'):
            data = stack.peek()
            print("확인된 데이터 ==> ", data)
            stack.display()
        else:
            print("입력이 잘못됨")
            0.
            3000
            200 100 100 200