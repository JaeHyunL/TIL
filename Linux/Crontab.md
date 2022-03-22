# Crontab

### 크론탭이란 

리눅스 상에서 커맨드를 예약실행하는 명령어

### Crontab 커맨드
> usage:  crontab [-u user] file

    crontab [ -u user ] [ -i ] { -e | -l | -r }
            (default operation is replace, per 1003.2)
    -e      (edit user's crontab)
    -l      (list user's crontab)
    -r      (delete user's crontab)
    -i      (prompt before deleting user's crontab)

crontab -e 옵션을 통해 에디터 모드를 켜줍니다.
아래와 같이 콘솔 창을 볼 수 있음. 크론 표현식을 기반으로 작성 함

> "*" (asterisk) 는 모든 시간에 실행한다는 것을 의미 

순서대로 (분) (시) (일) (요일) (주) 해당 스크립트. 순서대로 시간을 설정해 줄 수 있음
<img src="https://user-images.githubusercontent.com/48937399/159390287-21e834af-b2b7-412e-aca4-68d2962dcdca.png">

### 크론 표현식 기호

● * : 모든 값을 뜻합니다.

● ? : 특정한 값이 없음을 뜻합니다. 

● - : 범위를 뜻합니다. (예) 월요일에서 수요일까지는 MON-WED로 표현

● , : 특별한 값일 때만 동작 (예) 월,수,금 MON,WED,FRI 

● / : 시작시간 / 단위  (예) 0분부터 매 5분 0/5

● L : 일에서 사용하면 마지막 일, 요일에서는 마지막 요일(토요일)

● W : 가장 가까운 평일 (예) 15W는 15일에서 가장 가까운 평일 (월 ~ 금)을 찾음

● # : 몇째주의 무슨 요일을 표현 (예) 3#2 : 2번째주 수요일


### 크론 표현식 예시

- 5 8-20/3 * * * : 매일 08시 ~ 20시 사이 3시간 간격으로 05분에 실행

- 0,10 17 * * 0,2,3 : 매주 일, 화, 수요일 17시 00분과 17시 10분에 실행

- 0 15 10 15 * ? : 매달 15일 오전 10시:15분에 실행
  0 15 10 ? * 6L : 매월 마지막 금요일 오전 10시 15에



기타 크론탭 실행시 에러 크론탭은 vim 혹은 vi 기반으로 택스트를 편집해야 하므로 해당 리눅스 콘솔에 vim 또는 nano 등이 설치 되어 있어야 함.

<img src="https://user-images.githubusercontent.com/48937399/159389976-e2828827-e5a7-403f-a41d-561c6f6825ac.png">
