##OpenCV 정리
📌 OpenCV란?
**OpenCV(Open Source Computer Vision Library)**는 컴퓨터 비전 및 이미지 처리 분야에서 널리 사용되는 오픈소스 라이브러리입니다. 실시간 영상 처리, 객체 인식, 머신러닝 등 다양한 기능을 제공합니다.

🏗️ 주요 특징
다양한 언어 지원: Python, C++, Java 등

플랫폼 호환성: Windows, Linux, macOS, Android, iOS

방대한 함수 제공: 이미지/영상 처리, 특징 추출, 머신러닝, 딥러닝 등

🛠️ 설치 방법
Python에서 설치
```
pip install opencv-python
```
C++에서 설치
공식 홈페이지에서 바이너리 다운로드 또는 소스 빌드

🖼️ 주요 기능별 예제
1. 이미지 읽기, 저장, 표시
```
python
import cv2
```

# 이미지 읽기
```
img = cv2.imread('image.jpg')
```
# 이미지 표시
```
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# 이미지 저장
```
cv2.imwrite('output.jpg', img)
```

2. 이미지 전처리
python
# 그레이스케일 변환
```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
# 크기 조정
```
resized = cv2.resize(img, (224, 224))
```

# 블러 처리
```
blur = cv2.GaussianBlur(img, (5, 5), 0)
```
3. 에지 검출 (Canny)
python
```
edges = cv2.Canny(gray, 50, 150)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

4. 도형 그리기
python
```
# 선 그리기
cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 2)


# 원 그리기
cv2.circle(img, (50, 50), 20, (0, 255, 0), -1)

# 사각형 그리기
cv2.rectangle(img, (10, 10), (60, 60), (0, 0, 255), 3)
5. 허프 변환을 이용한 직선 검출
python
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=100, maxLineGap=50)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
```

🧩 주요 모듈
모듈명	설명
core	기본 데이터 구조, 수학 함수
imgproc	이미지 처리(필터, 변환 등)
highgui	GUI 창, 이미지/비디오 입출력
features2d	특징점 검출, 매칭
objdetect	객체 검출(얼굴, 사람 등)
video	동영상 처리, 추적
ml	머신러닝
dnn	딥러닝 프레임워크 연동
📚 참고 자료
OpenCV 공식 문서

OpenCV-Python Tutorials

OpenCV GitHub

📝 활용 예시
자율주행 자동차: 차선 인식, 표지판 인식

얼굴 인식, 객체 추적

OCR(문자 인식)

영상 필터, 증강현실(AR)

💡 Tip
OpenCV는 Numpy와 함께 사용하면 이미지 배열 연산이 매우 편리합니다.

실시간 웹캠 처리도 간단하게 구현 가능!

이 문서를 README.md로 저장하면 GitHub 저
