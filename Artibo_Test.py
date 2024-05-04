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
