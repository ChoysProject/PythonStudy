
student1 = {'학번' :"K2024006", "이름" : "조영상", "학과" : "소프트웨어학과", '학번':"K2024"}

## 딕셔널리는 중복이 제거가 된다.

print(student1)



student1 = {'학번' :"K2024006", "이름" : "조영상", "학과" : "소프트웨어학과"}

print(student1.get('학번'))
print(student1.get("나이"))


student1 = {'학번' :"K2024006", "이름" : "조영상", "학과" : "소프트웨어학과"}

if '나이' in student1:
    print(student1.get('나이'))
else:
    student1['나이'] = 24
    print(student1.get('나이'))



for i,j in student1.items():
    print(i,j)

### 딕셔널리 에서는 values 는 value 값만 keys 는 키값만 items 는 키밸류를 둘다 가져온다고 생각  하면된다.

### 세트는 디셔널리에서 키들만 가져오는거라고 생각하면된다. 키값이기에 중복은 허용하지 않는다.
### set은 딕셔널리처럼 {} 중괄호를 사용하는데
### set(list) 를 하면 중복값이 제거가 되버린다.

### 튜플
### 소괄호 () 인데
### 읽기만 가능하고 최초에 생성 함ㄴ 변경이 불가하다.








