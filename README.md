# URL 단축 서비스 프로젝트

## 프로젝트 소개

이 프로젝트는 FastAPI를 사용하여 URL 단축 서비스를 구현하였습니다. 사용자가 입력한 원본 URL을 단축하고, 단축된 URL을 통해 원본 URL로 리디렉션하는 기능을 제공합니다. 또한 Redis를 이용하여 각 단축 URL의 조회수를 관리하고, 조회수 통계 기능을 제공합니다.

## 데이터베이스 선택 이유

1. **MySQL 서버**: MySQL은 신뢰성 높은 관계형 데이터베이스로, 데이터의 일관성과 안정성을 보장할 수 있습니다. 이 프로젝트에서는 사용자의 원본 URL과 해당 URL에 대한 단축 URL 정보를 저장하기 위해 MySQL을 선택했습니다.

2. **Redis 서버**: Redis는 메모리 기반의 빠른 데이터베이스로, 단축 URL의 조회수를 실시간으로 관리하고 조회수 통계 기능을 제공하기 위해 선택했습니다.

## 설치 및 실행 방법

### 요구사항
- Python 3.7 이상
- MySQL 서버
- Redis 서버

## 설치 및 실행 방법

1. 환경 설정
   requirements.txt를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
2. 데이터베이스 설정
  app.database.py와 alembic.ini 파일에서 데이터베이스 연결 정보를 수정합니다.

3. 데이터베이스 마이그레이션
   ```bash
   alembic upgrade head
   ```

4 애플리케이션 실행
   ```bash
   uvicorn app.main:app --reload
   ```

5 API 문서 확인
  웹 브라우저에서 http://localhost:8000/docs로 접속하여 API 문서를 확인하고, API를 테스트할 수 있습니다.



