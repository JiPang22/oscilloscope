import numpy as np
import sounddevice as sd
import keyboard  # 키 입력 감지 라이브러리

# 설정
frequency = 1850
# 사인파 주파수 (Hz)


fs = 20 * frequency  # 샘플링 속도 (Hz)


# 사인파 생성
t = np.linspace(0, 1, fs, endpoint=False)  # 1초 길이의 시간 벡터
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # 사인파 (-1 ~ 1)

# 상태 변수
is_playing = False  # 사운드 재생 여부
is_running = True  # 프로그램 실행 여부

# 사인파 주기 출력
print(f"사인파 주기 (T): {1e3 / frequency:.6f} ms")

print("=== 사운드 제어 프로그램 ===")
print("Space: 사운드 재생/정지")
#  print("Esc: 프로그램 종료")

# 메인 루프
while is_running:
    try:
        if keyboard.is_pressed('space'):  # Space 키로 재생/정지 토글
            if not is_playing:
                sd.play(sine_wave, fs, loop=True)  # 사인파 무한 재생
                print("사운드 재생 시작...")
                is_playing = True
            else:
                sd.stop()  # 재생 중지
                print("사운드 재생 중지...")
                is_playing = False
            keyboard.wait('space')  # 키가 떼어질 때까지 대기

        # if keyboard.is_pressed('esc'):  # Esc 키로 프로그램 종료
        #     print("프로그램 종료...")
        #     is_running = False
        #     if is_playing:
        #         sd.stop()  # 종료 시 재생 중지

    except Exception as e:
        print(f"오류 발생: {e}")
        break
