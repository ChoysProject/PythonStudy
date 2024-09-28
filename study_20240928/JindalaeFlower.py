poet = '''
나 보기가 역겨워
가실 때에는
말없이 고이 보내 드리오리디.

양뱐에 약산
진달래꽃
아름 따다 가실 길에 뿌리오리다.

가시는 걸음걸음
놓인 그 꽃을
사뿐히 즈려 밟고 가시옵소서.

나 보기가 역겨워
가실 대에는
죽어도 아니 눈물 흘리오리다.
'''

dic1 = {}

for ch in poet:
    if ch.isalpha():
        if ch in dic1:
            dic1[ch] += 1
        else:
            dic1[ch] = 1

for i, j in dic1.items():
    print(i, ":", j)
