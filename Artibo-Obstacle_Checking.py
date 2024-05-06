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

    #10번 반복해야 하는데.

#테스트할 때, 거리 늘려가면서 하고 천장 향하게도 해봤는데..


