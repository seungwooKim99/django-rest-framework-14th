# 1. NGINX란

- 웹 서버 소프트웨어다
- 가볍다
- 응용프로그램 서버로 요청을 보내는 리버스 프록시 역할
- HTML, CSS, JS, 이미지 같은 정적 파일 처리 HTTP 서버 역할
- 동시접속 처리에 특화되어 있다
- 비동기 처리 방식을 택한다

# 2. WSGI란

- 웹서버가 request를 Django같은 웹 프레임워크에 전달하는 호출 규약

Production 레벨에서는
WebServer(NGINX, APACHE) - Application Server(gunicorn, WSGI) - Django 같은 구조를 띈다

# 3. Docker

## What

도커는 컨테이너 기반의 오픈소스 가상화 플랫폼이다.

도커에는 다양한 개념들이 등장하는데, 가상화, VM, 컨테이너에 대해 아래 정리를 해 보았다.

## What +a (가상화, VM부터 컨테이너까지 정리)

### VM(Virtual Machine - 가상머신)

 가상 머신(Virtual Machine, VM)은 물리적 하드웨어 시스템(오프프레미스 또는 온프레미스에 위치)에 구축되어 자체 CPU, 메모리, 네트워크 인터페이스 및 스토리지를 갖추고 가상 컴퓨터 시스템으로 작동하는 가상 환경이다. 하이퍼바이저라 불리는 소프트웨어는 하드웨어에서 가상 머신의 리소스를 분리하고 적절히 프로비저닝하여 VM에서 사용할 수 있도록 한다. 소프트웨어 기반 컴퓨터라고 이해하면 된다.

(출처 : [https://www.redhat.com/ko/topics/virtualization/what-is-a-virtual-machine](https://www.redhat.com/ko/topics/virtualization/what-is-a-virtual-machine))

### Hypervisor 기반의 Virtualization

 가상화를 관리하는 소프트웨어(주로 Hypervisor)를 사용하여 하나의 물리적 머신에서 가상 머신(VM)을 만드는 프로세스.

![vm](./img/vm.png)

(출처: [https://www.youtube.com/watch?v=bn-KfziRfiE](https://www.youtube.com/watch?v=bn-KfziRfiE))

 위에서 보는 것처럼 물리적 서버나 Host 위에서 Hypervisor라는 소프트웨어가 실행된다. Hypervisor는 두가지가 있다.

1. Type1
    - 물리적 서버의 리소스를 풀링하여 사용자의 가상환경에 바로 할당한다
    - 물리적 서버 상단에 바로 설치된다
    - 베어 메탈 하이퍼바이저(Bare Metal Hypervisor) 라고도 불린다
    - 가장 안전하고 대기시간이 짧으며 시중에 가장 많이 나와있다
    - VMware ESXi, Microsoft Hyper-V, 오픈소스 KVM 등
2. Type2
    - 물리적 서버와 하이퍼바이저 사이에 Host OS Layer가 있다
    - Oracle VirtualBox, VMware Workstation 등

 하이퍼바이저가 설치되었으면 그 위에 여러개의 VM을 구축할 수 있다. 하이퍼바이저는 이렇게 구축된 VM에 할당된 리소스를 관리한다. VM은 독립적이기 때문에 서로다른 운영체제를 실행할 수 있다. 또한 완전히 다른 머신의 하이퍼바이저 위로 VM을 이전할 수도 있다. 가상화 기술은 역사가 깊은 오래된 기술이지만, 클라우드 컴퓨팅 기술의 핵심이다.

![vm](./img/vm2.png)

### [가상화의 예시]

 가상화를 이용하면 서버를 통합(Server Consolidation) 하고 서버의 자원을 최대한으로 활용함으로써 서버 급증 문제(Server Proliferation Problem)를 해결할 수 있다.

 예를 들어, 용도가 다른 3개의 물리 서버가 있다고 가정하자. 1개는 메일서버이고, 다른 1개는 웹 서버이고, 다른 1개는 내무 레거시 애플리케이션을 실행하는 서버이다. 각 서버는 잠재적인 실행 용량의 30%만 사용되고 있지만, 내부 운영을 위해 레거시 애플리케이션이 계속 필요하므로, 레거시 애플리케이션과 이를 호스팅하는 또 다른 3번째 서버를 유지해야 한다.

![https://blog.kakaocdn.net/dn/bUkVOV/btqILMqOZLY/x27CXTABQeNmd1wOoSCfN0/img.png](https://blog.kakaocdn.net/dn/bUkVOV/btqILMqOZLY/x27CXTABQeNmd1wOoSCfN0/img.png)

 전통적으로 1개의 서버에 설치된 1개의 OS 위에 1개의 태스크를 수행하도록 하는 것이 더 쉽고 안정적인 경우가 많다. 하지만 이러한 경우 각각의 서버가 자원을 최대한으로 활용하지 않기 때문에 서버 전력비가 비효율적으로 발생하며, 각각의 서버가 서로 다른 공간에 위치하므로 공간 대여 비용도 발생하는 등 각각의 서버를 최대한으로 활용하지 못하고 있다.

 그러나 가상화를 사용하면 기존의 메일 서버를 2개로 분리하여 1개의 서버로는 메일을 처리하고, 1개의 서버로는 레거시 애플리케이션을 마이그레이션 할 수 있다.

![https://blog.kakaocdn.net/dn/RMYsg/btqIJaZPAFa/j2kOd1Lkw34Q7nBd3kntu0/img.png](https://blog.kakaocdn.net/dn/RMYsg/btqIJaZPAFa/j2kOd1Lkw34Q7nBd3kntu0/img.png)

 또한 메일서버를 만약 3개로 분리한다면, 메일 서버의 자원을 최대한으로 활용하고, 남은 2개의 서버는 다른 태스크를 처리하거나 사용을 중지하여 냉각 및 유지 관리 비용을 줄일 수 있다.

 출처

- [https://mangkyu.tistory.com/86](https://mangkyu.tistory.com/86)
- [https://www.redhat.com/ko/topics/virtualization/what-is-virtualization](https://www.redhat.com/ko/topics/virtualization/what-is-virtualization)
- [https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900](https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900)

### Container 기반의 Virtualization

 가상 머신(VM)은 하드웨어 스택을 가상화한다. 컨테이너(Container)는 이와 달리 운영체제 수준에서 가상화를 하여 여러개의 컨테이너들이 OS 커널에서 직접 구동한다. 컨테이너는 Hypervisor을 이용하는 VM 기반의 가상화보다 훨씬 가볍고 OS 커널을 공유하며, 시작이 훨씬 빠르고 OS 전체 부팅보다 메모리를 훨씬 적게 차지한다. OS 커널 단에서 프로세스를 격리하여 자원을 할당하게 되는데, 자세한 내용은 아래를 참조하면 된다.

 

> 컨테이너는 어느 날 갑자기 혜성처럼 등장한 가상화 기술은 아닙니다. 리눅스 기반 시스템에서 프로세스 간 격리를 위해 사용하던 기술들을 조합하여 발전시킨 것이라고 볼 수 있는데요. chroot와 네임 스페이스, cgroup을 조합한 형태인 LXC(Linux Container)에서부터 컨테이너 가상화 기술이 본격적으로 발전 했습니다.이 세 요소를 알고 있다면 OS 커널 단에서 프로세스를 어떻게 격리하여 자원을 할당하는지 파악할 수 있고, 컨테이너 가상화를 이해하기 수월합니다.  - chroot: 특정 디렉토리를 루트(최상위 디렉토리)로 인식하게끔 하는 명령어- 네임 스페이스: 리눅스 시스템 자원을 묶어 프로세스에 할당하는 방식으로, 하나의 프로세스 자원을 관리하는 기능- cgroup: CPU, 메모리 등 프로세스 그룹의 시스템 자원 사용량을 관리하여 특정 애플리케이션이 자원을 과다하게 사용하는 것을 제한먼저 chroot를 통해 특정 파일 디렉토리가 최상위 계정(Root)으로 인식되도록 한 후, cgroup과 네임스페이스를 통해 특정 프로세스에 자원을 할당하고 제어하는 방식입니다.
> 

![https://post-phinf.pstatic.net/MjAxOTA2MTlfMjg0/MDAxNTYwOTMzMTgxMjcy.UK_NuxaYPHZDsv2boTwscAnirxRl93Q1LClp3un2_VIg.9nCwumh6Iszz7WuVF2HXFOF7eyqUz1ywpnMATJrcOZUg.PNG/image.png?type=w1200](https://post-phinf.pstatic.net/MjAxOTA2MTlfMjg0/MDAxNTYwOTMzMTgxMjcy.UK_NuxaYPHZDsv2boTwscAnirxRl93Q1LClp3un2_VIg.9nCwumh6Iszz7WuVF2HXFOF7eyqUz1ywpnMATJrcOZUg.PNG/image.png?type=w1200)

![https://lh6.googleusercontent.com/zM8Atdm0jDl7ZIPSBGLfM_c-Y0_J30fw_AlUoZo65ytYGP-p-GKO4xQTNfCKQh0G9PdP1-W6-METGsMF96gZaCi64kuEVJm7tuY_TjrGDy3gL8JjSd1Hhlj96qJI-DJUV0IEbAvv](https://lh6.googleusercontent.com/zM8Atdm0jDl7ZIPSBGLfM_c-Y0_J30fw_AlUoZo65ytYGP-p-GKO4xQTNfCKQh0G9PdP1-W6-METGsMF96gZaCi64kuEVJm7tuY_TjrGDy3gL8JjSd1Hhlj96qJI-DJUV0IEbAvv)

> 이처럼 격리된 고유 영역에서 할당된 자원을 이용해 애플리케이션을 실행하는 것을 의미하는 컨테이너는 애플리케이션의 실행에 필요한 라이브러리와 바이너리, 기타 구성 파일을 ‘**이미지**’ 단위로 빌드하여 패키지로 배포합니다.실행에 필요한 모든 환경이 준비되어 있으므로 어떤 환경에서도 애플리케이션을 오류 없이 동작시킬 수 있는 것이 가장 큰 특징입니다.
> 

(참조: [https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900](https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900))

### VM vs Container

![https://lh6.googleusercontent.com/HWd2a3foV81WcdrNub4Q_B265GamwqAFSniZyLqErj9yzsnQWvPqkKMbKExaSEpJLm9L_qCItPSv7kUWL26AcXU9BZprZikZV0D76bTSU7hSYLyR2AuHj_ZioNJX6NgkTHDyhCiM](https://lh6.googleusercontent.com/HWd2a3foV81WcdrNub4Q_B265GamwqAFSniZyLqErj9yzsnQWvPqkKMbKExaSEpJLm9L_qCItPSv7kUWL26AcXU9BZprZikZV0D76bTSU7hSYLyR2AuHj_ZioNJX6NgkTHDyhCiM)

(참조: [https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900](https://post.naver.com/viewer/postView.nhn?memberNo=2521903&volumeNo=21385900))

 일단 컨테이너는 VM과 비교해서 하이퍼바이저, 게스트 OS가 필요하지 않아 훨씬 가볍다. VM은 보통 수 GB에 해당하고, 실행과정은 'VM을 띄우고 → 자원 할당 하고 → 게스트 OS 부팅하고 → 어플리케이션 실행'으로 느리다. 컨테이너는 어플리케이션 실행패키지인 '이미지'만 있으면 되므로 훨씬 빠르고 가볍다.

다음은 표로 가상화 와 컨테이너를 비교해 보았다.

|종류|하이퍼 바이저 형 가상화|컨테이너 형 가상화|
|---|---|---|
|시작시간|몇 분|몇 초|
|이미지 크기|수 GB ~ 수백 GB|~ 수백 MB|
|Guest OS|Windows/Linux 등 다양한 선택 가능|호스트 OS 와 동일한 OS|
|이식성|대부분 가상 이미지에 대한 변환이 필요함|컨테이너 이미지 그대로 사용 가능|
|데이터 관리|VM 내부또는 연결된 스토리지에 저장|컨테이너 내부에 있는 데이터는 종료시 소멸되며, 필요에 따라 스토리지를 이용하여 저장|
|Guest OS 와의 관계|Guest OS는 하드웨어(가상)로 인식|Host OS를 커널 수준으로 분리하여 OS를 가상화 형태로 사용하여 필요에 따라 호스트와 리소스 공유 가능|


(참고: [http://www.opennaru.com/cloud/virtualization-vs-container/](http://www.opennaru.com/cloud/virtualization-vs-container/))

 결론 : 컨테이너를 관리하는 가상환경 플랫폼인 ‘도커(Docker)’를 이용하면, 컨테이너를 쉽게 생성하고 배포할 수 있다.

## Why

- 다양한 OS 환경에서 같은 개발-배포 환경을 만들어준다.
- 개발-배포 환경을 이미지 형태로 저장하고, 이를 바탕으로 컨테이너를 띄워 배포하므로 배포가 용이하고 매우 빠르다

## How

다음은 Dockerfile의 예시이다.

```docker
FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# dependencies for psycopg2-binary
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /app/
```

도커파일을 작성하는 문법은 상당히 직관적이고 간단하다. 필요한 패키지를 설치하고, 코드를 copy하는 등 서버 환경을 구축하기 위한 명령어들을 정의할 수 있다.

정의한 dockerfile은 docker build 명령어를 통해 이미지로 만들 수 있다. 아래는 로컬환경에서 확인한 도커 이미지들이다.

![스크린샷 2021-09-30 오후 11.26.18.png](./img/docker1.png)

이후, 만들어진 이미지를 기반으로 docker run 명령어를 통해 컨테이너를 띄울 수 있다. 

![스크린샷 2021-09-30 오후 11.27.35.png](./img/docker2.png)

# 4. docker-compose

## What

docker-compose란 docker 이미지 기반 다중 컨테이너를 정의하고 공유할 수 있는 툴이다.

## Why

도커 이미지를 빌드하고, 다양한 컨테이너로 띄우기 위한 과정을 줄일 수 있다. 이게 무슨 말인가 하면 docker로 이미지를 빌드하고, 그 이미지를 기반으로 container를 띄우기 위해서는 장황한 옵션과 함께 커맨드로 입력을 해줘야한다. 호스트 os와 컨테이너의 마운트 작업을 하고, 포트포워딩을 하고, 환경변수 값을 넘겨주고 등등... 매번 컨테이너를 띄울 때마다 상당히 번거로운 작업을 반복하게 된다. 컨테이너를 수시로 지웠다 다시 생성해야 하는 상황이라면, 이런 반복적인 작업이 반갑지는 않을 것이다. docker-compose는 이 작업들을 미리 정의해두기 때문에 문제점을 해결할 수 있다.

## How

Docker는 Dockerfile을 통해 이미지를 빌드하지만, docker-compose는 docker-compose.yml 파일을 통해 실행된다. 다음은 docker-compose.yml 파일의 예시이다.

```docker
version: '3'
services:

  db:
    container_name: db
    image: mariadb:latest
    restart: always
    environment:
      MYSQL_ROOT_HOST: '%'
      MYSQL_ROOT_PASSWORD: mysql
    expose:
      - 3306
    ports:
      - "3307:3306"
    env_file:
      - .env
    volumes:
      - dbdata:/var/lib/mysql

  web:
    container_name: web
    build: .
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    environment:
      MYSQL_ROOT_PASSWORD: mysql
      DATABASE_NAME: mysql
      DATABASE_USER: 'root'
      DATABASE_PASSWORD: mysql
      DATABASE_PORT: 3306
      DATABASE_HOST: db
      DJANGO_SETTINGS_MODULE: django-rest-framework-14th.settings.dev
    restart: always
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db
volumes:
  app:
  dbdata:
```

docker-compose.yml 파일도 상당히 직관적이고 작성하기 쉽다. service 하단에 db, web 두가지가 정의되어 있다. db, web은 Dockerfile 이미지를 기반으로 생성될 container이다. db, web 서비스 하단에 정의되어 있는 것들을 간단히 확인해보자.

- environment : docker run 옵션 중 -e 에 해당된다.
- image : 사용할 도커 이미지를 정의한다.
- build : docker build 명령을 실행할 디렉토리 경로다.
- ports : docker run 옵션 중 -p에 해당되며, 포트포워딩을 설정할 수 있다.

이 외에도 다양한 docker build 옵션을 docker-compose.yml 파일을 통해 정의할 수 있다.

# 5. Github Action

## What

Github 저장소를 기반으로 Runners 라는 환경에서, 개발 Workflow를 자동화 할 수 있는 도구이다

## Why

개발을 하며 변경사항을 반영하여 빌드하고, 테스트하고, 배포하는 등 모든 과정을 개발자가 직접 하지 않고 손쉽게 자동화를 하기 때문에 사용된다.

아래 상황을 예시로 Github Action을 왜 쓰는지 알아보자.

> 웹 애플리케이션 개발을 완료하여 AWS EC2 우분투 서버에 배포하려고 한다. 처음 인스턴스를 생성하고 서버로 들어가보면 정말 아무것도 없다. 배포를 위해 필요한 패키지들을 설치하고, 배포환경을 구축 한다. 드디어 git pull 또는, docker로 배포할 경우 docker pull 로 소스코드 혹은 이미지를 받아와 배포를 진행한다. 처음부터 상당히 손이 많이 가는데, 이후에 여러명과 개발을 진행하며 기능이 추가되었다. master 브랜치에 반영된 새로운 기능들을 배포판에도 업데이트를 해줘야하는데, 당장은 서버로 들어가 새로운 코드로 갱신해주는 방법 밖에 없다.
> 

단순 반복작업 때문에 생산성이 떨어지는 경험을 할 수 있다. 여러 사람과 함께 개발을 하며 갱신된 master 브랜치의 내용으로 자동 배포되면 얼마나 좋을까? 바로 이것을 Github action이 해결해준다.

## How

전체적인 프로세스는 다음과 같다

1. 프로젝트 레파지토리에 .github/workflows/deploy.yml 을 생성한다
2. deploy.yml 에는 git push 나 pull request 같은 이벤트 발생시 어떤 일을 할 지 정의한다
3. 실제로 트리거 이벤트(push, pr)을 발생시켰을 때, github action 탭에서 액션을 확인할 수 있다.

deploy.yml은 다음과 같은 구조를 가진다.

```yaml
name: ~~~
on: [push]
jobs:

  build:
    name: ~~~
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@master

		- name: create env file
      run: |
        touch .env
        echo "${{ secrets.ENV_VARS }}" >> .env
```

- 어떤 이벤트에 반응하여 액션을 수행할지 적어준다 → on: [push] (push에 대해 반응)
- 최소 한 개 이상의 job을 정의하며, 안에는 여러개의 step으로 구성된다
- 각 step 안에서 커맨드를 실행하거나, Github 마켓플레이스에 공유된 Action을 가져와 수행한다.
- "checkout"에 해당하는 step은 "actions/checkout@master"라는 action을 가져와 수행한다.
- "create env file"에 해당하는 step은 run에 정의된 커맨드들을 수행한다.

![스크린샷 2021-09-30 오후 10.57.25.png](./img/githubaction.png)

이 때, secrets.ENV_VARS는 Github Secret 탭에서 미리 정의한 변수이다. 보안상의 이유로 소스코드 형태 그대로 올릴 수 없기 때문에 이와 같이 처리했다.

아래는 스터디에 사용된 deploy.yml 코드이다

```yaml
name: Deploy to EC2
on: [push]
jobs:

  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@master

    - name: create env file
      run: |
        touch .env
        echo "${{ secrets.ENV_VARS }}" >> .env

    - name: create remote directory
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ubuntu
        key: ${{ secrets.KEY }}
        script: mkdir -p /home/ubuntu/srv/ubuntu

    - name: copy source via ssh key
      uses: burnett01/rsync-deployments@4.1
      with:
        switches: -avzr --delete
        remote_path: /home/ubuntu/srv/ubuntu/
        remote_host: ${{ secrets.HOST }}
        remote_user: ubuntu
        remote_key: ${{ secrets.KEY }}

    - name: executing remote ssh commands using password
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ubuntu
        key: ${{ secrets.KEY }}
        script: |
          sh /home/ubuntu/srv/ubuntu/config/scripts/deploy.sh
```

step 별로 어떤 액션을 하는지 알아보자

1. checkout : 깃헙 코드를 GitHub runners 인스턴스에 올린다
2. create env file : secrets 탭에 정의한 ENV_VARS으로 .env 파일을 생성한다
3. create remote directory : ec2 서버 /home/ubuntu/srv/ubuntu 디렉토리를 구축한다
4. copy source via ssh key : rsync로 runners 내부의 파일(깃헙 코드 + .env)를 ec2 인스턴스로 동기화한다
5. executing remote ssh commands using password : [deploy.sh](http://deploy.sh)를 실행한다
(deploy.sh는 ec2서버에 docker, docker-compose를 설치하기 위한 스크립트다)