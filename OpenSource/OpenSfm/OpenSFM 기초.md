# OpenSFM 기초

### OpenSFM 종속성 관련 라이브러리

- opencv
- python
- ceres slover
- setup.py

### 기본 실행 커맨드 opensfm_run_all 

실행시 OpenSFM이 기본적으로 제공하는 기능을 순차적으로 실행 시켜 준다.

커맨드 실행시 실행 하는 내여ㅑㄱ

- extract_metadata
- detect_features
- match_features
- create_tracks
- reconstruct
- mesh
- undistrort
- compute_depthMaps

#### extract_meta

Exif 메타 추출 CameraJosn 생성 및 exif_json 추출



#### detect features 

이미지 피처 계산

넘파이오 읽을수 있는 npzz 파일을 생성 및 출력 해당 파일에는 points,colors,세그먼트 정보 등 이 기입되어 있음

이미지.jpg.json파일 생성



#### match_features 

이미지 매칭 기능 매칭내역 match.json에 저장

매칭 값들 pickle 파일로 matches/ 폴더에 저장 함 .



#### create_tracks

트랙 생성 track.csv 생성 tracks.json 생성 매칭 내역 저장



#### recon_struct

SFM을 재구성 계산 GCP와 Track exit 기반 재구성



#### bundle

pass



#### mesh 

매쉬로 재구성

#### undistort

방사형 외곡이미지 변형 안함 ( 랜즈 왜곡 보정 X)



#### Compute_deptnmaps(맵 깊이 계산)

ply를 통한 산출물 생성 



#### compute_statitics

통계 값 계산 및 정리.

