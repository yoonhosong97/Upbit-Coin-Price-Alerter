package com.example.coin_db_service.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CoinController {

    @PostMapping("/api/coin/update")
    public String receiveData(@RequestBody CoinData data) {
        
        System.out.println("---- 데이터 수신 시작 ----");
        System.out.println("코인이름: "+ data.getMarket());
        System.out.println("현재가: " + data.getTradePrice());
        System.out.println("---- 데이터 수신 완료 ----");
    }

}
