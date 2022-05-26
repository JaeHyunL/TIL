# Docker Image Offline Running

폐쇄망 환경에서 도커 이미지를 다룰 때 가 있긴하다.

폐쇄망에서는 도커 허브가 연결되지않아 허브에있는 이미지를 당겨올 수 없다.

사내망에 있는 도커 저장소 말고는 사용할 수 없는것인가?

폐쇄망에서 도커 이미지를 사용해서 프로그램을 구축하는 방법을 아라보자

1. 온라인 환경에서 도커 이미지를 다운 받는다.

```jsx
docker pull kartoza/geoserver:2.20.2
```

1. 다운받은 이미지를 파일로 출력한다.

```jsx
docker save kartoza/geoserver:2.20.2 > $path/kartoza-geoserver.tar
```

1. 해당 파일을 offline server에 전송시키고 docker load 명령어로 이미지에 등록한다.

```jsx
docker load < kartoza/geoserver:2.20.2.tar
```

1. docker run 명령을 사용하여 컨테이너를 작동시키면 된다.

확실히 도커가 이미지로 관리하여서 오프라인 환경에서도 설치가 별 다른 어려움이 없다.