#장애물 인식 코드 -> 장애물 (20cm 거리 이내) 인식하면 우회전
while True:
    artibo_move("Go", 50, 1)
    
    #장애물 인식 후 True/False로 로봇에 표시
    obstacle = is_obstacle_detected()
    artibo_display_text(obstacle, 27)

    #장애물이 있으면 우회전 / 없으면 직진
    if obstacle == True:
        artibo_display_text("장애물 존재함", 27)
        artibo_move("Right", 100, 1)
        break
    else:
        artibo_display_text("장애물 없음", 27)      
        artibo_move("Go", 100, 1)
        break

#라인트레이서 코드 (테스트) → 어두울수록 값의 크기가 작아짐

RightValue = get_left_floor_sensor_value()
LeftValue = get_left_floor_sensor_value()

