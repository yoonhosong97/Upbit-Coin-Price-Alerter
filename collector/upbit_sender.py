import requests

# 1. 주소 설정
UPBIT_URL = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
JAVA_URL = "http://localhost:8080/api/coin/update"

# 2. 자바 서버로 데이터 보내기

def fetch_and_send():
    
    try:
        response = requests.get(UPBIT_URL)
        if(response.status_code == 200):
            data = response.json()

            try:
                res = requests.post(JAVA_URL, json=data)
                print(f"[전송] 데이터 보냄 / 자바 응답: {res.text}")
            except Exception as e:
                print(f"[에러] 자바 서버 연결 확인: {e}")
    except KeyboardInterrupt:
        print("중단됨")

if __name__ == "__main__":
    fetch_and_send()
    
                



        

'''
[받은 데이터 확인하고 그 중 필요한 데이터 출력해보기]

if response.status_code == 200: # 정상응답

    # 응답 데이터를 JSON형식으로 파싱해서 변수에 저장
    data = response.json() 

    # data리스트 0번에 trade_price에 해당하는 값을 price에 저장
    price = data[0]['trade_price'] 
    
    print(f"현재 비트코인 시세: {price:,.0f}원")
    
else:
    print("데이터를 가져오는 데 실패했습니다.")

'''
