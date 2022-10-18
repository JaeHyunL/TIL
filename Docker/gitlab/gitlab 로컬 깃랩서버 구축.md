# Gitlab 도커 구동

gitlab 자체는 도커에 공식적으로 이미지를 지원한다
[ https://hub.docker.com/r/gitlab/gitlab-ce ]

Cli 

```bash
docker pull gitlab/gitlab-ce:15.4.2-ce.0  # 이미지를당겨온다.

export GITLAB_HOME=/srv/gitlab # 환경변수 등록


docker run --detach \
--hostname gitlab.example.com \
--publish 443:443 --publish 80:80 --publish 22:22 \
--name gitlab \
--restart always \
--volume $GITLAB_HOME/config:/etc/gitlab \
--volume $GITLAB_HOME/logs:/var/log/gitlab \
--volume $GITLAB_HOME/data:/var/opt/gitlab \
--shm-size 256m \
gitlab/gitlab-ce:15.4.2-ce.0  # 도커 이미지를 구동한다.
```

```bash
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password # 깃랩 도커 패스워드를 출력한다.
```

로그인 및 접속테스트 하면 완료 관리자 계정: root / password

도커 컴포즈로 처리하기 .

```yml
version: '3.6'
services:
  web:
    image: 'gitlab/gitlab-ee:latest'
    restart: always
    hostname: 'gitlab.example.com'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.example.com'
        # Add any other gitlab.rb configuration here, each on its own line
    ports:
      - '80:80'
      - '443:443'
      - '22:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'
```

```sh
docker-compose up -d  # 커맨드실행.
```