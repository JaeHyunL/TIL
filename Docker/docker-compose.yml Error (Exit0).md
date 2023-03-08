# docker-compose



docker-compose

Dockerfile cmd 제거 후 command 실행 시.

```sh
ERROR: for main-backend  Cannot start service main-backend: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "uvicorn app.main:app --reload --host=0.0.0.0 --port=30001": executable file not found in $PATH: unknown
ERROR: Encountered errors while bringing up the project.

```



<body>

정확한 원인은 모르겠으나. Docker file에 CMD 부분을 제거했을 경우 Exit 0 (정상 적으로 코드 수행완료) 기타 명령어나 커맨드로 강제적으로 프로그램이 종료되지 않게 유지하더라도 위 와 같은 에러가 발생함(PATH ERROR) 따라서 docker-compose.yml 에 CMD가 중복 적용되더라도 무시하고 실행 함.

</body>