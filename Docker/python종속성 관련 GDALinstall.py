# 파이썬 종속성 문제를 일으켜 라이브러리가 설치 안될스 Ex) Gdal


### target Version 지정.

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
RUN update-alternatives --install /usr/bin/python python3 /usr/bin/python3.11 2
# GDAL Install 

# RUN add-apt-repository ppa:ubuntugis/ppa
RUN apt-get -y update
RUN apt-get install -y gdal-bin
RUN apt-get install -y libgdal-dev
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN python3.11 -m pip install GDAL
