## gitlab /root 디렉토리 용량 관련 (502 ERROR)

/root 디렉토리 용량이 가득 참 . no Space Device 문제로 정상적인 서비스 불가능
해결 방법
/var/lib/docker/volumes/gitlab_data/_data/backups/repositories/* 용량을 여분 디스크로 move
백업 커맨드 이용 후 백업 정보 내용들을 해싱 처리하여 여러 파일로 분산 함.
다만 현재 용량이 100% 가 넘어가므로 백업을 한다 하더라도 정상적으로 백업 되는지는 의문