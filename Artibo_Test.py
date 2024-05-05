#장애물 인식 코드 -> 장애물 (20cm 거리 이내) 인식하면 우회전
n = 1
while n < 10:
    artibo_move("Go", 50, 1)
    
    #장애물 인식 후 True/False로 로봇에 표시
    obstacle = is_obstacle_detected()
    artibo_display_text(obstacle, 27)

    n = n + 1

    #장애물이 있으면 우회전 / 없으면 직진
    if obstacle == True:
        artibo_display_text("장애물 존재함", 27)
        artibo_move("Right", 100, 1)
    else:
        artibo_display_text("장애물 없음", 27)      
        artibo_move("Go", 100, 1)

#라인트레이서 코드 (테스트) → 어두울수록 값의 크기가 작아짐

RightValue = get_left_floor_sensor_value()
LeftValue = get_left_floor_sensor_value()

#검정색의 평균 명도값을 찾고 따라가는 알고리즘 제작해야 함
#카메라 화각이 아래 선까지 찍힌다면, 카메라가 그 선을 인식해서 따라가도록 할 수 있지 않을까..?