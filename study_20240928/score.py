scoreList = []
score1 = int(input("점수 입력 : "))
score2 = int(input("점수 입력 : "))
score3 = int(input("점수 입력 : "))
score4 = int(input("점수 입력 : "))
score5 = int(input("점수 입력 : "))

scoreList = [score1, score2, score3, score4, score5]

avg = 0
student = 0

for i in range(0, len(scoreList)):
    avg += scoreList[i]
print(avg/len(scoreList))

avg = avg/len(scoreList)

for i in range(0, len(scoreList)):
    if scoreList[i] >= avg:
        student += 1


print('평균 이상인 학생 수 : %d' % student)