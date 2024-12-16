# 🍸 Cocktail DB: Data-driven Web Application for Cocktails

## 📖 프로젝트 소개
Cocktail DB는 다양한 칵테일 정보를 체계적으로 저장하고, 이를 활용하여 사용자에게 맞춤형 칵테일 추천, 레시피 제공, 필터링 기능 등을 제공하는 데이터 기반 웹 애플리케이션입니다.

### ✨ 주요 기능
- **칵테일 검색**: 재료, 카테고리, 알코올 함유량으로 검색
- **레시피 제공**: 칵테일 제조 과정 및 필요한 재료 확인
- **추천 시스템**: 사용 가능한 재료 기반 칵테일 추천
- **관리자 기능**: 새로운 칵테일, 재료, 카테고리, 태그 추가 및 관리

---

## 🏗️ 프로젝트 구조
```
/project-root  
├── DB
│   ├── ER-diagram.png       # ER 다이어그램 (png)  
│   ├── ER-diagram.svg       # ER 다이어그램 (svg)  
│   ├── DB-schema.png        # 데이터베이스 스키마 그림  
│   ├── SQL-schema-code.sql  # SQL 스키마 코드 (최종 데이터베이스 형태)  
│   └── cocktail-DB.db       # 데이터베이스 파일  
├── templates                
│   ├── add_cocktail.html    # 새로운 칵테일 추가 페이지
│   ├── cocktail_detail.html # 칵테일 상세 설명 페이지  
│   ├── edit_cocktail.html   # 기존 칵테일 정보 수정 페이지
│   └── index.html           # 메인 홈페이지  
├── app.py                   # flask 코드 파일  
└── README.MD                # 프로젝트 설명 문서  
```

---

## 🛠️ 기술 스택
- **Frontend**: HTML, (CSS)
- **Backend**: Flask (Python)
- **Database**: SQLite

---

## 🚀 시작하기
### 1️⃣ 로컬 환경에서 실행하기
1. **레포지토리 클론**
    ```bash
    git clone https://github.com/atomicNum29/Cocktail-DB.git
    cd cocktail-db
    ```

2. **의존성 설정**
    - Python 가상환경 생성 및 활성화  
	  맥 또는 리눅스
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
	  윈도우
	  ```bash
      python -m venv venv
      source venv/Scripts/activate
      ```
    - 필요한 모듈 설치
      ```bash
      pip install flask
      ```

3. **서버 실행**
    - 실행
      ```bash
	  python app.py
	  ```

4. **애플리케이션 접속**
    - 웹 브라우저에서 `http://127.0.0.1:5000` 접속

---

## 📧 문의
- 개발자: 박시우
- 이메일: atomicw63.546@gmail.com
