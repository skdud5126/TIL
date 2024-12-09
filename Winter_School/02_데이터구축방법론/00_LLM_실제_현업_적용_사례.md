# LLM과 실제 현업 적용 사례

### Index

- Large Language Models

- Industrial Applications of LLM

---

### `Large Language Models`

- History of (Large) Language Models

  ![alt text](images/image_00.png)

---

#### **Transfomer ( 2017.06 )**

- 내부에 인코더(ex. 문장이 들어왔을때 컴퓨터가 잘 이해할 수 있게 하는 역할) 파트와 디코더(ex. 사람들이 잘 이해할 수 있게 답변을 생성해주는 역할) 파트가 존재하며 이 둘 사이를 이어주는 연결고리가 존재

  ![alt text](images/image_01.png)

ps) 추가 논문 - Attention is all you need

#### Trnasformer의 개괄적 구조

- (오리지널 버전에서는 여섯개의 인코더와 여섯개의 디코더를 사용)

  ![alt text](images/image_02.png)

---

#### **B**idirectional **E**ncoder **R**epresentations from **T**ransformer(BERT) (2018.10)

- Transformer의 인코더 구조만 사용

- 번역 모델이 아닌 범용 모델이므로 대용량의 코퍼스를 사용하여 두 가지 과업을 학습

  - Masked language model(MLM) : bidirectional pre-training for language representations

  - Next sentence prediction (NSP)

    ![alt text](images/image_03.png)

  - 사전 학습된 BERT는 이후 단순한 출력 레이어를 추가하는 것만으로도 다양한 자연어처리 과업에서 SOTA 성능을 달성

---

### **B**idirectional and **A**uto-**R**egressive **T**ransformer(BART) (2019.10)

- Original Transformer는 기계 번역을 위해 제안됨

  - Source-target의 paired dataset을 통한 superviesed learning 방식

- BART 아이디어 : Transformer 구조를 사용해서 self-supervised learning을 학습하는 방법

  - 입력 token을 단순 masking하는 것이 아니라 corruption 시켜서 사용하는 방법

  ![alt text](images/image_04.png)

---

#### Exploring the Limits of **T**ransfer Learning with a Unified **T**ext-**t**o-**T**ext **T**ransformer(T5) (2019.10)

- 모든 언어 문제를 text-to-text format으로 변환하는 통합된 프레임워크 unified framework

- 기본적인 구조는 Original Transformer의 구조를 그대로 따름

  - 차이점 : Layer Normalization, Position Embedding

  ![alt text](images/image_05.png)

---

#### **G**enerative **P**re-**T**raining of a Language Model(GPT-1) (2018.06)

- 비지도 학습 기반의 사전 학습

- Transformer의 디코더 (12 Layers)만 사용한 언어 모델

- 사전 학습 objective : Language Modeling (Auto-Regressive)
  - 주어진 token sequence를 바탕으로 next token 예측

    ![alt text](images/image_06.png)

---

#### GPT-2(2019.02)

- Fine-tuning 없이 zero-shot으로 downstream task를 풀 수 있는 방법은 없을까?

  - 직접 구축한 대량의 데이터셋을 이용하여 더 많은 parameters로 구성된 무델을 설계

  - Zero-shot inference : 대용량 데이터로 모델을 사전 학습하면 downstream task에 관한 정보를 배우게 됨 (Input에 task에 대한 지시사항(prompt)를 추가하면 zero-shot으로 정답 생성 가능)

- GPT-1 과 GPT-2의 차이점?

  - GPT-1의 구조를 확장시켜 더 많은 데이터를 이용해 잘 학습시킨 모델

  - GPT-2의 토큰 개수 : 1024개(GPT-1은 512개)

    ![alt text](images/image_07.png)