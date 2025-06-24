## 목차
1. [프로젝트 소개](#프로젝트-소개)
2. [구성도](#구성도)
3. [기술 스택](#기술-스택)
4. [설치 방법](#설치-방법)
5. [기본 회로도 - 추가예정](#기본-회로도)
6. [코드 예시 - 추가예정](#코드-예시)
7. [코랩 연동](#코렙-연동)
8. [GitHub](#Github) 
9. [MarkDown](#MarkDown)
10. [배운 내용](#배운-내용)


## 프로젝트 소개

Python Library를 활용한 Car IMAGE Detection 프로그램 개발

---

## 구성도

아키텍쳐 요약

---


## 기술 스택

모델 - YOLOv12 Transfor Learning

임베디드 보드 - Jetson Orin Nano

Programming Language - Python3, C++(GPU)

---

## 설치 방법

#Python Library install
```
pip install pyserial
pip install opencv-python
```

## 코랩 연동

1. 코랩 로그인 이후 -> 파일-> Github사본 저장 -> github 로그인 이후 연동
2. 연동 이후 repo지정 이후, repo이름으로 저장 


## GitHub

1. Github 로그인 - https://github.com 에서 로그인
2. 프로필 사진, 소개글 추가
3. Github웹에선 Create repository를 눌러 내 첫 프로젝트 만들기
4. linux.ver Github repo create
```
sudo apt update && sudo apt install gh
gh auth login
gh repo create [reponame] [-v]

```
5. 기존 디렉토리
```
cd my-projectfoler
git init #이미 Git이 설치되어있다는 기준으로

git add [filename] or [.]
git commit -m "Initial commit"

gh repo create --personal --private --source=. --remote=origin --push #private
gh repo create --personal --public --source=. --remote=origin --push #personal
```

## MarkDown

1. 글자 크기 조정

# H1 제목
## H2 제목
### H3 제목
#### H4 제목
##### H5 제목
###### H6 제목

2. 텍스트 서식

3. 순서 없는 목록

- 항목 1
- 항목 2
 - 하위 항목 2.1
 - 하위 항목 2.2

4. 체크박스 목록

- [ ] 미완료 작업
- [x] 완료된 작업

5. 인용문

> 이것은 인용문입니다.
> 여러 줄로 작성 가능합니다.
>> 중첩 인용문

6. 다이어그램

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
7. 이미지
![image](https://github.com/user-attachments/assets/dd444ae9-c57a-4d13-b63a-a4e6c7515df8)

10. 배운 내용
1. About Python3
Python basic
2. data structure / data sciencs
데이터 구조 개요
Pandas
Numpy
Matplotlib
3. Machine Learning
Machine Learning Basic
모델 훈련 및 평가
4. OpenCV
OpenCV Basic
이미지 처리
5. CNN(Convolution Neural Network
CNN_Basic
CNN_자율주행 관련 코드
6. Ultralytics
Ultralytics_Basic
YOLOv8
YOLOv12
7. TensorRT vs PyTorch
PyTorch_Basic
TensorRT
YOLOv12
8. TAO Toolkit on RunPod
TAO_사용법
TAO_Toolkit
9. 칼만필터, CARLA, 경로 알고리즘
kalman
CARLA_simulator
10. ADAS & (ADAS TensorRT vs PyTorch)
adas_basic
TensorRT vs PyTorch 비교
