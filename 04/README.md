# Machine Learning Practice

scikit-learn과 PyTorch를 활용하여 고전 머신러닝부터 딥러닝까지 단계적으로 구현한 프로젝트.

---

## 노트북 구성

| 노트북 | 과제 | 내용 |
|---|---|---|
| notebook1 | 1 ~ 4번 | 데이터 분할, K-NN, 분류 알고리즘 비교, 데이터 증강 |
| notebook2 | 5 ~ 7번 | 활성화 함수, MLP, CNN |

---

## 과제별 내용

### 과제 1 — 데이터셋 분할

`make_classification`으로 생성한 가상 이진 분류 데이터를 Train / Validation / Test로 3분할.  
`train_test_split()`을 두 번 사용하여 구현.

```
Train      : 600개 (60%)
Validation : 200개 (20%)
Test       : 200개 (20%)
```

---

### 과제 2 — K-NN

K-Nearest Neighbors 알고리즘으로 이진 분류 수행.

| K | Validation 정확도 |
|---|---|
| 3 | 94.0% |
| 5 | - |

- **Test 정확도: 91.5%**
- 결정 경계: 구불구불한 비선형 경계

---

### 과제 3 — 분류 알고리즘 비교

Perceptron, SVM, Random Forest, Naive Bayes 4가지 알고리즘을 동일한 데이터로 비교.

| 알고리즘 | Train | Validation | Test |
|---|---|---|---|
| Perceptron | 74.17% | 71.50% | 79.00% |
| SVM (rbf) | 87.83% | 90.00% | 90.50% |
| Random Forest | 100.00% | 93.00% | 92.00% |
| Naive Bayes | 85.00% | 88.50% | 89.00% |

**혼동 행렬 비교 (Test 기준)**

| 알고리즘 | TN | FP | FN | TP |
|---|---|---|---|---|
| Perceptron | 54 | 41 | 1 | 104 |
| SVM | 93 | 2 | 17 | 88 |
| Random Forest | 91 | 4 | 12 | 93 |
| Naive Bayes | 93 | 2 | 20 | 85 |

---

### 과제 4 — 데이터 증강 (Data Augmentation)

동일한 데이터에 데이터 증강 적용 후 전후 성능 비교.

---

### 과제 5 — 활성화 함수 직접 구현

라이브러리 없이 numpy로 4가지 활성화 함수를 직접 구현 및 시각화.

```python
def step_function(x):
    return np.where(x > 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
```

| 함수 | 출력 범위 | 기울기 소실 | 주요 사용처 |
|---|---|---|---|
| Step | 0 또는 1 | 항상 소실 | 거의 안 씀 |
| Sigmoid | 0 ~ 1 | 있음 | 출력층 (이진 분류) |
| ReLU | 0 ~ ∞ | 없음 (양수) | 은닉층 기본값 |
| Tanh | -1 ~ 1 | 있음 (덜함) | 은닉층, RNN |

---

### 과제 6 — MLP (다층 퍼셉트론)

`make_moons` 비선형 데이터로 PyTorch MLP 설계 및 학습.

**모델 구조**
```
입력 (2) → Linear(2→16) → ReLU → Linear(16→8) → ReLU → Linear(8→1) → Sigmoid → 출력
총 파라미터: 193개
```

**학습 설정**
- Optimizer: Adam (lr=0.001)
- Epochs: 1000

**결과**

| 데이터 | 정확도 |
|---|---|
| Train | 97.83% |
| Validation | 97.00% |
| Test | 96.00% |

---

### 과제 7 — CNN 이미지 분류

MNIST 손글씨 숫자 데이터셋으로 CNN 설계 및 학습.

**데이터**
```
클래스  : 10개 (숫자 0~9)
이미지  : 28×28 픽셀 (흑백)
Train   : 60,000개
Test    : 10,000개
```

**모델 구조**
```
입력 (1, 28, 28)
→ Conv2d(1→32) + ReLU + MaxPool → (32, 14, 14)
→ Conv2d(32→64) + ReLU + MaxPool → (64, 7, 7)
→ Flatten → (3136,)
→ Linear(3136→128) + ReLU
→ Linear(128→10)
→ 출력 (클래스 10개)
```

**학습 설정**
- Optimizer: Adam (lr=0.001)
- Epochs: 5

**결과**

| Epoch | Loss | Train 정확도 |
|---|---|---|
| 1 | 0.1692 | 94.84% |
| 2 | 0.0485 | 98.52% |
| 3 | 0.0334 | 98.99% |
| 4 | 0.0239 | 99.23% |
| 5 | 0.0189 | 99.40% |

- **Test 정확도: 98.87%**

---

## 기술 스택

| 분류 | 라이브러리 |
|---|---|
| 데이터 생성 | scikit-learn (make_classification, make_moons) |
| 고전 머신러닝 | scikit-learn (KNN, SVM, RandomForest, NaiveBayes, Perceptron) |
| 딥러닝 | PyTorch |
| 데이터 처리 | numpy, pandas |
| 시각화 | matplotlib |
