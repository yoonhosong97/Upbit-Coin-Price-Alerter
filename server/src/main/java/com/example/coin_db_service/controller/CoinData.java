package com.example.coin_db_service.controller;

public class CoinData {

    // 코인이름
    private String market;

    // 코인의 현재가
    private double tradePrice;

    public String getMarket(){
        return this.market;
    }

    public Double getTradePrice(){
        return this.tradePrice;
    }

    
}
