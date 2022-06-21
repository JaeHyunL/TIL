# Docker network hostName

도커 네트워크 사용 중 네트워크 안에 접속되어있는 컨테이너 경우 

도커 내부에서 ip 대신 hostName으로 사용 접근할 경우가 있다.

이 때 network 상애서 포트를 어디로 포워딩 하든 간에

상관없이 도커 컨테이너 내부에서 작동하므로 hostName 자체에 있는 포트로 접근하면 된다.

