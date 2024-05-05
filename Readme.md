# Artibo 

## 1. Obstacle Checking Algorithm

Artibo Body Front Sensor가 장애물 (20cm 이내) 인식하고, 장애물이 있다면 우회전한다.

## 2. Line Tracer Algorithm

### Case 1

Artibo Head Camera 로 검정색 테이프를 인식하고 검정색을 따라 움직인다

*조건
- Artibo Head Camera의 화각이 아래까지 찍히는 가?
- Artibo가 검정색 테이프를 인식할 수 있는가?

### Case 2

Artibo Body Bottom Sensor가 검정색의 평균 명도값을 인식하고 따라 움직인다

*조건 
- 평균 명도값을 구할 수 있는가?
- 검정색 테이프(또는 매직)의 명도가 일정한가?
- 오른쪽 센서와 왼쪽 센서 값 중 어떤 센서를 이용할 것인가?

### Case 3

Case 1과 Case 2의 기술을 결합한다

*조건
- Case 1과 Case 2의 조건을 모두 충족함

