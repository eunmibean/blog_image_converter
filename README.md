# Blog Image Converter

블로그용 이미지에 텍스트를 삽입하는 CLI 도구입니다.

## 기능

- **메인 이미지 생성**: 배경 이미지에 제목과 부제목을 스타일링하여 삽입
- **Before/After 이미지 생성**: "작업 전", "작업 후" 라벨이 포함된 비교 이미지 생성
- **랜덤 지역명 생성**: 서울, 경기, 인천 지역의 동 이름을 랜덤으로 선택하여 텍스트 파일 생성

## 설치

```bash
# 가상환경 생성 및 활성화
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
# myenv\Scripts\activate  # Windows

# 필요한 패키지 설치
pip install Pillow
```

## 사용법

```bash
python image_editor_cli.py
```

메인이미지로 사용할 사진 파일 이름은:  1.jpeg 
작업 전 이미지로 사용할 사진 파일 이름은:  2.jpeg 
작업 후 이미지로 사용할 사진 파일 이름은:  3.jpeg 
바꾼 후에 같은 폴더에 넣어놓는다.

실행 후 제목을 입력하면 다음 파일들이 생성됩니다:
- `main.jpeg` - 메인 이미지
- `작업 전.jpeg` - Before 이미지
- `작업 후.jpeg` - After 이미지
- `random_dong.txt` - 랜덤 지역명 목록

### 입력 예시

```
제목 입력하기!!! (줄바꾸기는 \n 넣기)): 욕실 타일\n시공 완료
```

## 프로젝트 구조

```
blog_image_converter/
├── image_editor_cli.py    # 메인 스크립트
├── 1.jpeg                 # 메인 이미지 배경
├── 2.jpeg                 # Before 이미지 배경
├── 3.jpeg                 # After 이미지 배경
├── dong_list/             # 지역명 데이터
│   ├── seoul.txt
│   ├── gyeonggido.txt
│   └── incheon.txt
└── ttf/                   # 폰트 파일
    ├── Hakgyoansim Allimjang TTF B.ttf
    └── Hakgyoansim_TteokbokkiB.ttf
```

## 요구사항

- Python 3.x
- Pillow
