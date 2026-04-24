# 🪙Upbit-Coin-Price-Alerter  

업비트 API를 활용한 실시간 코인 시세 알림 시스템 (JAVA17, Spring Boot, MySQL, Python)

---

## 🏗️ 시스템 아키텍처 (Architecture)

본 프로젝트는 데이터 수집과 비즈니스 로직 처리를 분리한 구조로 설계되었습니다.

1. **Python (Data Collector)** - Upbit API(REST API)를 호출하여 실시간 시세를 JSON 형태로 수집합니다.
   - 가공된 데이터를 Java Spring Boot 서버로 전송합니다.

2. **Java Spring Boot (Backend)**
   - API 엔드포인트를 통해 시세 데이터를 수신합니다.
   - JDBC(Raw SQL)를 사용하여 MySQL에 저장된 사용자의 알림 설정가를 조회합니다.
   - 현재가와 설정가를 비교하여 알림 로직을 실행합니다.

3. **MySQL (Database)**
   - 사용자의 알림 타겟 가격 정보를 저장하고 관리합니다.

---

## 🛠️ 기술 스택 (Tech Stack)

**Backend:** Java 17, Spring Boot 3.x  

**Database:** MySQL 8.x  

**Script:** Python 3.x  

**DB Access:** JDBC (Plain SQL)  

---

## 📈 프로젝트 로드맵 (Roadmap)

**Step 1: Python** - Upbit API 연동 및 데이터 추출

**Step 2: MySQL** - 사용자 알림 설정 테이블 설계 및 생성

**Step 3: Java** - JDBC를 이용한 DB 연동 및 비교 로직 구현

**Step 4: 확장**
- 알림 대상 코인 추가 (BTC 외 2종 이상)
- 직접 작성한 SQL을 **JPA**로 전환해보기
- 기존에 REST API방식으로 받아오던 데이터를 WebSocket방식으로 바꾸어 대량의 데이터를 처리하는 시스템 구축
