import sys  
import random

def run_game():
    
    try:
        max_range = int(sys.argv[1])  # 첫 번째 인자: 최대 숫자 범위
        lives = int(sys.argv[2])      # 두 번째 인자: 제한 기회 횟수
    except (IndexError, ValueError):
        # IndexError: 숫자를 안 적었을 때 / ValueError: 글자를 적었을 때 발생하는 에러를 방지
        print("❌ 실행 방법이 올바르지 않습니다.")
        print("💡 사용법: python3 game.py [범위] [기회]")
        print("💻 예시: python3 game.py 1000 5")
        return

    # 입력받은 변수를 기반으로 게임 설정
    target_number = random.randint(1, max_range)  
    score = 100
    
    print("========================================")
    print("         [ 숫자 맞추기 게임 ]")
    print(f"  1부터 {max_range} 사이의 숫자를 맞추는 게임입니다.")
    print(f"  총 {lives}번의 기회가 주어집니다.")
    print("========================================")

    # 게임 루프 시작
    while lives > 0:
        print(f"\n남은 기회: {lives}")
        user_input = input("숫자를 입력하세요 (종료하려면 q): ")

        # 'q' 입력 시 프로그램 종료
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            return

        # 숫자가 아닌 오타를 입력했을 때 예외 처리
        if not user_input.isdigit():
            print("오류: 숫자만 입력 가능합니다.")
            continue

        guess = int(user_input)

        # UP / DOWN 판정 로직
        if guess == target_number:
            print("----------------------------------------")
            print(f"정답입니다. 숫자는 {target_number}였습니다.")
            print(f"최종 점수: {score}점")
            print("----------------------------------------")
            break
        elif guess < target_number:
            print("결과: UP (더 큰 숫자를 입력하세요)")
        else:
            print("결과: DOWN (더 작은 숫자를 입력하세요)")

        # 틀릴 때마다 기회와 점수 차감
        lives -= 1
        score -= 10

        # 기회를 모두 소진했을 때 게임 오버
        if lives == 0:
            print("\n----------------------------------------")
            print("게임 오버 (기회를 모두 사용하셨습니다)")
            print(f"정답은 {target_number}였습니다.")
            print("----------------------------------------")

if __name__ == "__main__":
    run_game()