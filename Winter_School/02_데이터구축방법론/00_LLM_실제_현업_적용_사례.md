# LLM과 실제 현업 적용 사례

### Index

- Large Language Models

- Industrial Applications of LLM

---

### `Large Language Models`

- History of (Large) Language Models

  ![alt text](images/image_00.png)

#### **Transfomer ( 2017.06 )**

- 내부에 인코더(ex. 문장이 들어왔을때 컴퓨터가 잘 이해할 수 있게 하는 역할) 파트와 디코더(ex. 사람들이 잘 이해할 수 있게 답변을 생성해주는 역할) 파트가 존재하며 이 둘 사이를 이어주는 연결고리가 존재

  ![alt text](images/image_01.png)

ps) 추가 논문 - Attention is all you need

#### Trnasformer의 개괄적 구조

- (오리지널 버전에서는 여섯개의 인코더와 여섯개의 디코더를 사용)

  ![alt text](images/image_02.png)

#### **B**idirectional **E**ncoder **R**epresentations from **T**ransformer(BERT) (2018.10)

- Transformer의 인코더 구조만 사용

- 번역 모델이 아닌 범용 모델이므로 대용량의 코퍼스를 사용하여 두 가지 과업을 학습

  - Masked language model(MLM) : bidirectional pre-training for language representations

  - Next sentence prediction (NSP)

    ![alt text](images/image_03.png)

  - 사전 학습된 BERT는 이후 단순한 출력 레이어를 추가하는 것만으로도 다양한 자연어처리 과업에서 SOTA 성능을 달성


