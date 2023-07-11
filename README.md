# 은행 사기계좌 탐지 분류분석 프로젝트

### 수행기간 : 2023.04.20 ~ 2023.05.03

## 주제
사기 거래에 이용되는 계좌의 특징을 분석하여 정상거래계좌 인지 사기이용계좌 인지를 구분하는 모델을 생성

## 팀원
<ul>
  <li>남기태 - <a href="https://github.com/krkoki">krkoki</a></li>
  <li>박상춘 - <a href="https://github.com/sangchun1">sangchun1</a></li>
</ul>

## 데이터 출처
Kaggle : [Bank Account Fraud Dataset Suite (NeurIPS 2022)](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022?select=Base.csv)
 - 32개의 컬럼과 100만개의 데이터로 구성 : 정상 계좌는 998,971건 & 사기에 이용된 계좌는 11,029건

## 수행방법 및 절차
#### 1. 데이터 전처리
  - 불필요한 컬럼 삭제
  - 결측치 제거
  - 범주형 변수 변환(OneHot-Encoding)
  - 언더샘플링
    - 언더샘플링으로 정상건수 735491 건을 사기건수 6871 건으로 동일하게 맞춤
  - 후진제거법
    - statsmodels 로지스틱 회귀분석 알고리즘의 요약을 확인하고 유의하지 않다고 판단한 변수들을 제거

#### 2. 모델 학습
  - 학습한 모델은 총 7개
    - 로지스틱 회귀분석
    - 의사결정나무
    - 랜덤포레스트
    - 서포트벡터머신
    - K최근접이웃
    - 인공신경망
      - MLPClassifier
      - KerasClassifier
 - 모든 모델은 3회 교차검증을 통해 최적의 파라미터를 구하고, 각 알고리즘별 모델의 정확도, 정밀도, 재현율, f1-score, AUC를 구함

#### 3. 웹서비스 구현
| 홈페이지 |
| --- |
| <div align="center"><img src="https://github.com/sangchun1/nba_salary/assets/121409511/5e263a50-ce00-4d81-8ae4-9250ce8a2836" width=70%/></div> |

| 결과 페이지 |
| --- |
| <div align="center"><img src="https://github.com/sangchun1/nba_salary/assets/121409511/0ce229b8-59ce-44b4-be31-87f7d555197b" width=70%/></div>|

| 상세결과 페이지 |
| --- |
| <div align="center"><img src="https://github.com/sangchun1/nba_salary/assets/121409511/d20a0414-9cfc-4e1f-9c64-0402c758b03e" width=70%/></div>|

## 결과
#### 모델 평가
<img src="https://github.com/sangchun1/nba_salary/assets/121409511/1229b2d9-c6c2-4747-9051-54c1fa7ad0fc" width=70%/>
<img src="https://github.com/sangchun1/nba_salary/assets/121409511/2c181b45-2f15-4e78-94dd-c54d5f372072" width=70%/>

#### 결론
최적의 알고리즘 :
  1. 인공신경망(Keras) : 정확도가 제일 높으며 F1-Score와 AUC는 두번째로 높음
  2. 인공신경망(Scikit-learn) : 정확도는 3-4번으로 높지만 F1-Score외 AUC가 제일 높음

## 향후계획
 - 모든 알고리즘의 ROC-Curve가 한눈에 보여지게 시각화
 - 웹으로 구현한 사이트 꾸미기
 - 하이퍼 파라미터 값을 더욱 세밀하게 조절하여 알고리즘별  최적의 성능을 찾기

## 사용한 언어, 라이브러리 및 프레임워크
#### 언어
<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
</div>

#### 라이브러리
<div align="left">
  <img src="https://img.shields.io/badge/Keras-FF0000?style=flat-square&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/SciPy-%230C55A5.svg?style=flat-square&logo=scipy&logoColor=%white"/>
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/statsmodels-3f51b5?style=flat-square&logo=statsmodels&logoColor=white"/>
</div>
<div align="left">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=flat-square&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-F2F2F2?style=flat-square&logo=Matplotlib&logoColor=black"/>
</div>

#### 프레임워크
<div align="left">
  <img src="https://img.shields.io/badge/conda-342B029.svg?&style=flat-square&logo=anaconda&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
</div>
