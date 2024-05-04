#장애물 인식 코드 -> 장애물 인식하면 오른쪽으로 회전
while True:
    artibo_move("Go", 50, 1)
    
    obstacle = is_obstacle_detected()
    artibo_display_text(obstacle, 27)

    if obstacle == True:
        artibo_display_text("장애물 존재함", 27)
        artibo_move("Right", 100, 1)
        break
    else:
        artibo_display_text("장애물 없음", 27)      
        artibo_move("Go", 100, 1)
        break

#라인트레이서 코드 (테스트) -> 오른쪽 센서 기준값 (어두운 색일수록 값이 작음)

RightValue = get_left_floor_sensor_value()
LeftValue = get_left_floor_sensor_value()

if RightValue < LeftValue:
    artibo_move("Go", 10, 1)
elif RightValue > LeftValue:
    artibo_move("Right", 90, 1)
else:
    artibo_move("stop", 100, 1)
