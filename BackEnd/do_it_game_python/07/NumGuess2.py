# 특정 범위의 숫자를 맞히는 게임입니다.
# 사용자는 숫자가 큰지 작은지 힌트를 얻습니다.
# 게임이 끝나면 몇 번 시도했는지를 알려 줍니다.

#라이브러리 불러오기
import random

#변수 정의하기
guesses = 0         #시도 횟수 추적하기
numMin = 1          #범위 시작 숫자
numMax = 100        #범위 끝 숫자
userInput = ""      #사용자 입력 저장하기
userGuess = 0       #사용자 입력 숫자로 저장하기

#무작위 숫자 생성하기
randNum = random.randrange(numMin, numMax+1)

#게임 설명하기
print(numMin, "와(과)", numMax, "사이의 숫자 하나를 정했습니다.")
print("이 숫자는 무엇일까요?")

#사용자가 맞힐 때까지 반복하기
while randNum != userGuess :
    #사용자 답 입력받기
    userInput = input("예상 숫자: ").strip()
    #입력한 것이 숫자인지 확인하기
    if not userInput.isnumeric() :
        #입력한 값이 숫자가 아니라면
        print(userInput, "이것은 숫자가 아닙니다!")
    else :
        # 입력한 값이 숫자라면 계속 진행
        # 시도 횟수 1회 늘리기
        guesses = guesses + 1
        # 입력한 값을 숫자로 변환하기
        userGuess = int(userInput)
        # 숫자 확인하기
        if userGuess < numMin or userGuess > numMax:
            print("{}은(는) {}와(과) {} 사이가 아닙니다."\
                  .format(userGuess, numMin, numMax))
        elif userGuess < randNum :
            print("너무 작습니다. 다시 입력하세요.")
        elif userGuess > randNum :
            print("너무 큽니다. 다시 입력하세요.")
        else :
            print("정답입니다! 시도 횟수: {}".format(guesses))

#끝날 때 출력할 메시지
print("즐거우셨나요? 또 만나요!")
