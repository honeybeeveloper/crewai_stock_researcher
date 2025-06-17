# 🧠 CrewAI 기반 주식 보유 결정 에이전트

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
│   └── websearch_tool.py     # 웹 수집 도구
│
├── crew.py
├── main.py                   
└── README.md
```

## 💼 output
```bash
financial_analysis.md
psychological_analysist.md
techinical_analysis.md
hedge_fund_manager.md
```
