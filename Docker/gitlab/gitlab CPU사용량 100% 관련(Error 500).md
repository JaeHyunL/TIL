깃랩 CPU 사용량 관련 

## 문제 1.

깃 랩 서버 재부팅시 .vscode 프로세스가 실행 됨 
해당 프로세스가 CPU 및 메모리를 최대한 잡아 먹음.

임시 해결방법
1) .vscode kill -9 PID 제거 방법 

해결 방법
vscode systemctl 서비스 시작 제어, 혹은 삭제. 
vscode가 필요한 이유가 있는지 알아봐야 함.

## 문제 2.
kthreaddw Cpu 사용량 증가.

https://gitlab.com/gitlab-org/gitlab/-/issues/344888 이슈 발생.

https://gitlab.com/gitlab-org/gitlab/-/merge_requests/73715 이 후 버전사용 권장.

임시 해결방법
1) docker restart로 재시작.
