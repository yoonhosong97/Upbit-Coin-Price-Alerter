package com.example.coin_db_service.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
public class CoinController {

    @PostMapping("/api/coin/update")
    public String receiveData(@RequestBody List<CoinData> data) {
        
        if(data != null && !data.isEmpty()){
            CoinData coin = data.get(0);

            System.out.println("---- 데이터 수신 시작 ----");
            System.out.println("코인이름: "+ coin.getMarket());
            System.out.println("현재가: " + coin.getTradePrice());
            System.out.println("---- 데이터 수신 완료 ----");

            return "자바 서버가 데이터를 잘 받았습니다";
        }
        
        return "데이터가 비었습니다";        
    }
}
