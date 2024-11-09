## 함수 선언 부분 ##
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE - 1):
        return False
    elif (rear == SIZE - 1) and (front == -1):
        return True
    else:
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[front + 1]


def shift():
    global SIZE, queue, front, rear
    for i in range(front + 1, SIZE):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1


## 전역 변수 선언 부분 ##
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

enQueue('정국')
enQueue('뷔')
enQueue('지민')
enQueue('진')
enQueue('슈가')
print('대기 줄 상태 : ', queue)

for _ in range(SIZE):
    print(deQueue(), '님 식당에 들어감')
    # 좌에서 우로 한칸 씩 시프트 하는 함수 콜
    shift()
    print('대기 줄 상태 : ', queue)


## 메인 코드 부분 ##
if __name__ == "__main__":
    # select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 ==> ")
    # select = input("식당 영업 종료")


    # while (select != 'X' and select != 'x'):
    #     if select == 'I' or select == 'i':
    #         data = input("입력할 데이터 ==> ")
    #         enQueue(data)
    #         print("큐 상태 : ", queue)
    #     elif select == 'E' or select == 'e':
    #         data = deQueue()
    #         print("추출된 데이터 ==> ", data)
    #         print("큐 상태 : ", queue)
    #     elif select == 'V' or select == 'v':
    #         data = peek()
    #         print("확인된 데이터 ==> ", data)
    #         print("큐 상태 : ", queue)
    #     else:
    #         print("입력이 잘못됨")

        # print("식당 영업 종료")

    print("식당 영업 종료!")
