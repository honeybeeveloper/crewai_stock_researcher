# CrewAI 기반 주식 보유 결정 에이전트

## 📌 프로젝트 개요

본 프로젝트는 [CrewAI](https://docs.crewai.com/)를 활용하여 여러 개의 전문 에이전트들이 협업을 통해 **주식 보유 여부를 판단**하도록 설계된 시스템입니다.  
특히 이 프로젝트는 **뉴스 감정 분석 도구(Sentiment Analysis Tool)** 를 추가하여, 최근 뉴스의 8가지의 감정이 주식 결정에 반영 되도록 구성되었습니다.

---

## 🚀 주요 기능

- **에이전트 기반 역할 분담**  
  - 각 에이전트는 특정 역할(자료 수집가, 재무 분석가, 기술 분석가, 감정 분석가 등)을 수행 하며 협업을 통해 판단을 내립니다.
  
- **뉴스 감정 분석 도구 통합**
  - 뉴스 데이터를 기반으로 텍스트 감정을 분석합니다.
  - 주가와 직접적인 관련이 있는 뉴스만 필터링하여 반영합니다.
  
- **보유/매도/매수 결정 로직**
  - 재무 지표, 기술적 분석, 뉴스 감정 분석 결과를 종합하여 결정합니다.
  
- **유연한 프롬프트 기반 사용자 질의**
  - 사용자는 종목명 또는 기업명을 입력하면 에이전트가 팀을 구성하여 종합 판단을 제공합니다.

---

## 🛠️ 사용 기술

- **[CrewAI](https://crewai.com)**
- **OpenAI**

---

## 📂 프로젝트 구조

```bash
📁 stock-conclusion/
│
├── config/
│   ├── agents.yaml
│   ├── tasks.yaml
│
├── tools/
│   ├── sentimentanalysis_tool.py       # 감정 분석 도구
│   └── websearch_tool.py               # 웹 수집 도구
│   └── balancesheet_tool.py            # 재무 상태 수집 도구
│   └── gathernews_tool.py              # 뉴스 수집 도구
│   └── insidertransaction_tool.py      # 내부자 거래 수집 도구
│   └── stockprice_tool.py              # 주가 수집 도구
│   └── incomestatement_tool.py         # 손익 수집 도구
│
├── crew.py
├── main.py                   
└── README.md
```

## 💼 output Example

### 1. financial_analysis.md
```
The Trade Desk Financial Overview: 
The Trade Desk has shown consistent growth in revenue over the past years, with a strong operating profit margin. 
The balance sheet indicates a healthy financial position with significant equity and working capital. 
Insider transactions show a mix of stock purchases and sales, reflecting varying sentiments among insiders.

Projected Operating Profit Margin: 
The projected operating profit margin for The Trade Desk in two years from now is subject to market conditions, competition, and the company's ability to leverage AI and adtech trends effectively. 
It is recommended to monitor industry trends and company performance closely for a more precise projection.

Expected Performance: 
The Trade Desk's focus on AI, expansion into new markets like CTV, and strategic partnerships position it well for potential growth. 
However, competitive threats and market dynamics should be carefully considered when evaluating the company's expected performance in the coming years.
```

### 2. technical_analysis.md
```
Technical Analysis Report: The Trade Desk (TTD)

Overview
The Trade Desk (TTD) stock has shown fluctuations in price over the recent trading sessions. The stock opened at $74.20 on 19th May 2025 and surged to a high of $78.03 on 29th May 2025. However, it experienced some pullbacks as well.

Current Trend
The current trend of TTD stock is characterized by volatility, with both upward and downward price movements observed in the recent period.

Support and Resistance Levels
- Support Levels: 
  - Initial support around $68.93 (13th June 2025).
  - Stronger support at $66.82 (16th June 2025).

- Resistance Levels:
  - Immediate resistance near $78.03 (29th May 2025).
  - Further resistance at $76.52 (4th June 2025).

Entry Points
Potential entry points for traders may be considered near the support levels to capitalize on potential rebounds.

Price Targets
- Short-term Price Target: $76.52
- Medium-term Price Target: $78.50

Key Technical Indicators
The key technical indicators, such as moving averages, Relative Strength Index (RSI), and volume levels, should be monitored closely to assess the stock's future price movements.
This technical analysis provides a snapshot of recent price action and potential areas of interest for traders in The Trade Desk (TTD) stock.
---

Please note that stock price movements are subject to market volatility and external factors that may influence trading decisions.
```

### 3. sentiment_analysis.md
```
Based on the expert opinions and sentiment analysis, The Trade Desk appears to be positively perceived due to its strategic moves in the adtech industry, AI focus, and partnerships. 
The recent stock repurchases and partnerships have contributed to a positive sentiment, indicating growing interest and potential attention from investors and the public. 
The company's expansion into new markets and the positive outlook on adtech spending further suggest a favorable perception and increased attention towards The Trade Desk in the near future.
```

### 4. stock_decision.md
```
Based on the comprehensive analysis of The Trade Desk (TTD) stock, I recommend a BUY decision with a strong rationale to support this recommendation.

Rationale for Buying The Trade Desk (TTD) Stock:
Financial Performance: 
The Trade Desk has demonstrated consistent revenue growth, strong operating profit margins, and a healthy financial position indicated by its balance sheet metrics. 
These positive financial indicators suggest the company's ability to generate value for investors.

Technical Analysis: 
Despite recent price fluctuations, the stock has shown resilience with potential support levels at 66.82. 
The current trend of volatility presents an opportunity for traders to enter near support levels and capitalize on potential rebounds.

Price Targets: 
The short-term price target of 78.50 provide a positive outlook for potential price appreciation, aligning with the upward trajectory of the stock.

Industry Positioning: 
The Trade Desk's strategic focus on AI, expansion into new markets like CTV, and formation of key partnerships position it well for future growth opportunities. 
The company's initiatives to stay ahead in the adtech industry underscore its competitive strength.

Sentiment Analysis: 
Positive sentiment surrounding The Trade Desk is evident from recent stock repurchases, strategic partnerships, and the company's expansion into new markets. 
This favorable sentiment indicates growing interest from investors and the public, supporting the potential for increased stock value.

In conclusion, considering the strong financial performance, positive technical indicators, strategic positioning in the industry, and favorable sentiment, I recommend BUYING The Trade Desk (TTD) stock. 
Investors are advised to monitor key technical indicators and market conditions for timely entry and potential capitalization on the stock's growth opportunities.
```


