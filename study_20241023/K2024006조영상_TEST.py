# 전화번호 추가
def add_data(name, number):
    katok.append((name, number))

def delete_data(name):
    for i in range(len(katok)):
        if katok[i][0] == name:
            del katok[i]
            print(f"{name}의 데이터가 삭제되었습니다.")
            return
    print(f"{name}의 데이터가 존재하지 않습니다.")

def search_data(name):
    for entry in katok:
        if entry[0] == name:
            print(entry[1])  # 전화번호만 출력
            return
    print(f"{name}의 데이터가 존재하지 않습니다.")

## 전역 변수 선언 부분 ##
select = -1
katok = []

## 메인 코드 부분 ##
if __name__ == "__main__":

    while (select != 4):
        select = int(input("** 선택하세요(1: 추가, 2: 삭제, 3: 검색, 4: 종료)--> "))

        if (select == 1):
            data = input("추가할 이름--> ")
            phoneNum = input("추가할 전화번호 --> ")
            add_data(data, phoneNum)
            print(katok)  # katok 리스트 출력
        elif (select == 2):
            name = input("삭제할 이름--> ")
            delete_data(name)
            print(katok)  # katok 리스트 출력
        elif (select == 3):
            name = input("검색할 이름--> ")
            search_data(name)
        elif (select == 4):
            print("프로그램을 종료합니다.")
            print(katok)  # katok 리스트 출력
            break
        else:
            print("1~4 중 하나를 입력하세요.")