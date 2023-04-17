FROM ubuntu:22.04

# base pkg
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    wget \
    unzip \
    vim \
    zip \
    locales \
    libxcb1 \
    libfftw3-3 \
    libxmu6 \
    libxcomposite-dev \
    imagemagick && \
    locale-gen en_US.UTF-8


# 타임존, 인코딩
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
ENV TZ=KST-9
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install python
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip
# Version targeting
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
RUN update-alternatives --install /usr/bin/python python3 /usr/bin/python3.11 2

# 경희대 알고리즘 파이썬 버전 타겟팅을 위한 apt 추가설치.
# RUN apt-get install -y autoconf \
#     automake \
#     bzip2 \
#     dpkg-dev \
#     file \
#     g++ \
#     gcc \
#     libbz2-dev \
#     libc6-dev \
#     libcurl4-openssl-dev \
#     libdb-dev \
#     libevent-dev \
#     libffi-dev \
#     libgdbm-dev \
#     libgeoip-dev \
#     libglib2.0-dev \
#     libgmp-dev \
#     libjpeg-dev \
#     libkrb5-dev \
#     liblzma-dev \
#     libmagickcore-dev \
#     libmagickwand-dev \
#     libncurses5-dev \
#     libncursesw5-dev \
#     libpng-dev \
#     libpq-dev \
#     libreadline-dev \
#     libsqlite3-dev \
#     libssl-dev \
#     libtool \
#     libwebp-dev \
#     libxml2-dev \
#     libxslt-dev \
#     libyaml-dev \
#     make \
#     patch \
#     xz-utils 
    # zlib1g-dev 



# RUN wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz -P /tmp

# RUN tar -xzf /tmp/Python-3.6.8.tgz -C  /tmp
# WORKDIR /tmp/Python-3.6.8
# RUN ./configure --enable-optimizations  -with-lto  --with-pydebug
# RUN make -j 8  # adjust for number of your CPU cores
# RUN make altinstall


# permission denied 방지.
RUN umask 000
COPY . /src/boss
RUN chmod a+x /src/boss/script
WORKDIR /src/boss

# install python package
RUN ["python3.11", "-m", "pip", "install", "-r", "requirements.txt"]
RUN ["python3.11", "-m", "pip", "install", "-e", "."]


# GDAL Install 관련 .
RUN apt-get -y update
RUN apt-get install -y gdal-bin
RUN apt-get install -y libgdal-dev
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN python3.11 -m pip install GDAL


# Dev
CMD [ "python3.11", "-m", "uvicorn", "app.main:app",  "--reload", "--host=0.0.0.0", "--port=30001"]
