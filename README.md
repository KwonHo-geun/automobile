## 📘 AI 학습 정리

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

GitHub 사용법
✅ GitHub 계정 만드는 순서 (2025년 기준)
웹 브라우저 열기 크롬(Chrome), 엣지(Edge), 사파리(Safari) 중 편한 걸 사용하세요.

GitHub 웹사이트 접속 주소창에 아래 주소를 입력하고 Enter 누르세요: https://github.com

회원가입 시작하기 화면 오른쪽 위 또는 중간에 있는 Sign up 버튼 클릭

이메일 주소 입력 평소 자주 사용하는 이메일을 입력

비밀번호 만들기 영어 대문자, 소문자, 숫자, 특수문자를 섞어 안전하게! 예시: Git1234!hub

사용자 이름(Username) 정하기 나만의 고유한 이름을 지어요 (다른 사람이 쓰고 있으면 불가)

예시: jetsunmom, sungsookjang66 등
영어, 숫자, 하이픈(-) 가능 (띄어쓰기 ❌)
✅ Repository 만들기 순서
GitHub에 로그인 후 New Repository 클릭

new

Repository 이름 입력

Public/Private 선택

README.md 파일 생성 체크

Create repository 버튼 클릭

create_repository

Markdown 문법
Markdown 문법
🔰 1. 마크다운(Markdown)이란?
Markdown은 글을 쉽게 꾸미기 위한 문법이에요. HTML보다 간단하게 제목, 목록, 굵은 글씨, 링크, 코드블록 등을 작성할 수 있어요. GitHub에서는 README.md 파일을 통해 마크다운을 많이 사용합니다.

🛠️ 2. GitHub에서 마크다운 사용하려면?
GitHub 계정을 만들고
새 Repository를 만든 뒤
README.md 파일을 추가해서
마크다운 문법을 사용하여 내용을 입력하면 됩니다.
✍️ 3. 기본 마크다운 문법 정리
기능	문법	예시	결과
제목(Title)	#, ##, ###	## 내 프로젝트	내 프로젝트
굵게	**굵게**	**중요**	중요
기울임	*기울임*	*강조*	강조
목록	-, *	- 사과
- 배	● 사과
● 배
숫자 목록	1., 2.	1. 첫째
2. 둘째	1. 첫째
2. 둘째
링크	[이름](주소)	[구글](https://google.com)	구글
이미지	![이름](이미지주소)	![고양이](cat.jpg)	고양이
코드블록	```python	print("Hello")	코드박스
인라인 코드	`코드`	`a = 3`	a = 3
구분선	---	---	―――

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
[Python basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/docs/python3.md)

2. data structure / data sciencs
[데이터 구조 개요](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/data_structures.md)
[Pandas](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/pandas.md)
[Numpy](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/numpy.md)
[Matplotlib](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/Matplotlib.md)

3. Machine Learning
[Machine Learning Basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/ml_basic.md)
[모델 훈련 및 평가](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/ml_test.md)
4. OpenCV
[OpenCV Basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/OpenCV_basic.md)
[이미지 처리](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/image_test.md)

5. CNN(Convolution Neural Network
[CNN_Basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/CNN_basic.md)[
CNN_자율주행 관련 코드](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/cnn_test.md)

6. Ultralytics
[Ultralytics_Basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/Ultralytics_basic.md)
[YOLOv8](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/YOLOv8_test.md)
[YOLOv12](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/YOLOv12_test.md)
7. TensorRT vs PyTorch
[PyTorch_Basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/PyTorch_basic.md)
[TensorRT](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/TensorRT_test.md)
[YOLOv12](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/YOLOv12_test.md)

8. TAO Toolkit on RunPod
[TAO_사용법](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.TAO_install.md)
[TAO_Toolkit](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.TAO_Toolkit.md)

9. 칼만필터, CARLA, 경로 알고리즘
[kalman](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.kalman.md)
[CARLA_simulator](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.CARLA.md)

10. ADAS & (ADAS TensorRT vs PyTorch)
[adas_basic](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.adas_basic.md)
[TensorRT vs PyTorch 비교](https://github.com/jetsonmom/git_test_markdown_sample/blob/main/.vs.md)
