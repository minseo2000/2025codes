import mss

with mss.mss() as sct:
    screenshot = sct.shot(output="screenshot.png")

print("스크린샷이 저장되었습니다: screenshot.png")
