import requests

# 1. 주소 설정
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

# 2. 업비트 서버에 요청 보내기
response = requests.get(url)

# 3. 받은 데이터 확인하기
if response.status_code == 200:
    data = response.json()
    # 업비트는 데이터를 리스트 [ ]에 담아 주므로 첫 번째 요소([0])를 꺼냅니다.
    price = data[0]['trade_price']
    print(f"현재 비트코인 시세: {price:,.0f}원")
else:
    print("데이터를 가져오는 데 실패했습니다.")