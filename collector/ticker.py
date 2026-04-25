import requests

# 1. 주소 설정
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

# 2. 설정한 url에 있는 데이터들 response에 받아옴
response = requests.get(url)

# 3. 받은 데이터 확인하고 그 중 필요한 데이터 출력해보기
if response.status_code == 200: # 정상응답
    data = response.json() # 응답 데이터를 JSON형식으로 파싱해서 변수에 저장
    price = data[0]['trade_price'] # 만약 2개의 코인정보를 가져오는 url을 사용하면 List의 0번과 1번에 저장됨
    print(f"현재 비트코인 시세: {price:,.0f}원")
    
else:
    print("데이터를 가져오는 데 실패했습니다.")