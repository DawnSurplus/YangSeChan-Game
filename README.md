# 양세찬 게임을 통한 최적의 프롬프트 찾기

<br/>

## 📖 목차
### 1. 프로젝트 개요
### 2. 양세찬 게임 (콜 마이 네임)
### 3. 게임 구현
### 4. 프로젝트 개선점
### 5. 한 줄 회고평평
<br/>



## 🔖 프로젝트 개요
- 프로젝트 제목 : 양세찬 게임을 통한 최적의 프롬프트 찾기

- 설명 : 런닝맨의 '양세찬 게임(콜 마이 네임)' 규칙을 기반으로 AI와 사람이 번갈아 질문/답변/캐릭터 추론을 하며, LLM 프롬프트 엔지니어링을 실습할 수 있는 웹 기반 게임

- 특징
    > 1. 실시간 AI와의 추론/질문/정답 맞추기
    > 2. 다양한 Prompt Engineering 및 Test 지원
    > 3. 직관적 UI와 로그/설정 분리

<br/>

### 🛠 기술 스택
![Python](https://img.shields.io/badge/Language-Python-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-yellow)
![Ollama](https://img.shields.io/badge/Ollama-EEVE_Korean_10.8B_v1.0-brown)

<br/>

### 🗓️ WBS
- 개발기간 : 4/18 ~ 4/24

![wbs](/img/wbs.png)

---

<br/><br/><br/>



## 👲 양세찬 게임 (콜 마이 네임)
![rule](/img/rule.png)

### ✅ 게임 규칙
1. 자리 / 순서 정하기
    - User 먼저 진행
2. 주제 선정 및 캐릭터 할당
    - 주제 : 연예인, 영화/드라마 인물, 위인, 캐릭터)
    - 각 플레이어에게 랜덤으로 캐릭터가 할당 (본인은 자신의 캐릭터를 모름)
3. 질문 / 답변
    - 자신의 차례가 되면 AI에게 본인의 캐릭터를 추론할 수 있는 질문 가능
    - 질문을 받은 플레이어는 '예/아니오/단답형'으로 답변
4. 정답 맞추기
    - 질문 후, 본인이 정답을 맞출 기회를 가짐
    - 정답이면 게임 종료, 아니면 다음 플레이어로 턴 이동
5. AI 차례
    - AI도 동일
    - AI 질문 → 유저가 답변 → AI가 정답 추측
6. 종료 조건
    - 누군가 자신의 캐릭터를 맞추면 즉시 게임 종료.
---

<br/><br/><br/>



## 🎲 게임 구현
- ### https://e0ed3f70a3eb1b44e3.gradio.live

### 1. UI 구성
- Game Section
![ui](/img/ui_1.png)

- Setting Section
![ui](/img/ui_2.png)

### 2. 게임 시작
1. 주제 선택
2. 플레이어 수 선택
3. <게임시작>
![ui](/img/sequence.png)

### 3. 게임 Flow
- Player 수 2명 설정 (User, AI)
- 게임 시작 >> 사용자(-> AI) 질문 >> 사용자 답변 >> AI(-> 사용자) 질문 >> AI(-> AI) 캐릭터 유추 >> AI 답변 >> 사용자(-> AI) 질문 >> ...반복 >> 누군가 정답 혹은 20라운드 후 게임종료

### 4. 게임 설정
- Parameter
  - Temperature : 출력의 무작위성(창의성) 조절
    - range : [0 ~ 1]
    - default=0.3
- Prompt
  - stop 옵션 지원 : 모델이 특정 토큰을 생성할 때, 응답 생성을 중단하고 출력
    - `["<|im_start|>", "<|im_end|>", "<|eot_id|>"]` 적용
  - System Prompt : AI 모델 공통 system role 설정 관련
    - 객체 생성 시, 처음 한 번만 적용
  - Question Prompt : AI 모델이 자신의 캐릭터를 추측하기 위해 다른 플레이어에게 할 질문 관련 Prompt
    - 변수 지원
      - `{topic}` : 주제 (ex. 연예인, 드라마/영화 인물, 등)
  - Answer Prompt : 상대 플레이어 질문에 대한 AI 모델의 답 관련 Prompt
    - 변수 지원
      - `{topic}` : 주제 (ex. 연예인, 드라마/영화 인물, 등)
      - `{question}` : 상대 플레이어의 질문
      - `{character}` : 상대 플레이어의 캐릭터
  - Guess Prompt : AI 모델이 자신의 캐릭터를 유추하기 위한 Prompt
    - 변수 지원
      - `{topic}` : 주제 (ex. 연예인, 드라마/영화 인물, 등)

### 5. 게임 결과
#### 1. 기본 Setting 적용
![result](/img/result1.png)
![result](/img/result2.png)

#### 2. Temperature 및 Prompt 변경
![result](/img/result3.png)
![result](/img/result4.png)

---

<br/><br/><br/>



## 👨‍🔧 프로젝트 문제 및 개선점
- 사용자가 전달한 질문에 대해서는 일부 수행 가능하나, AI가 직접 본인의 캐릭터에 대한 질의나 유추하는 부분의 성능이 떨어짐

### 1. 다양한 LLM 모델 지원
- 현재는 EEVE 단일 LLM만 지원
- llama 또는 gpt 모델 등을 선택할 수 있도록 하여 다양한 모델에 따른 Prompt Test 및 모델 성능 Test 가능

### 2. 프롬프트 및 Option Parameter 확장
- 현재 한정된 프롬프트 및 Temperature Option 한 개만 적용
- top_k, top_p, max_tokens 등 다양한 Option을 확장하여 모델 별 Test 가능

<br/>

## 🏦 한 줄 회고평

> Ollama EEVE 모델의 성능이 좋지 않아 결과가 좋지 않았지만, Prompt Engineering 및 파라미터 값 조절을 다양하게 시도해 봄으로써 효과와 한계를 체감하는 계기가 되었다.