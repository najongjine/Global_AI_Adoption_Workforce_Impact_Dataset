Global AI Adoption & Workforce Impact Dataset
https://www.kaggle.com/datasets/mohankrishnathalla/global-ai-adoption-and-workforce-impact-dataset

**"전 세계 기업들이 AI(인공지능)를 어떻게 도입하고 있고, 그게 실제 업무와 경영 성과에 어떤 영향을 주는지"*

* ai_company_adoption.csv -
About this file

Suggest Edits
ai_company_adoption.csv
Main dataset containing company-level observations across multiple years and quarters.

Each row represents a company survey observation capturing AI adoption behavior, workforce outcomes, operational changes, and governance practices.

Rows: 150,000
Columns: 43
{
1. 기본 정보 및 기업 프로필
response_id: 응답 고유 번호 (각 데이터 행의 신분증)
company_id: 기업 고유 번호 (여러 해에 걸친 데이터 분석 시 동일 기업을 식별하는 용도)
survey_year: 설문이 진행된 연도
quarter: 설문이 진행된 분기 (Q1~Q4)
country: 기업이 위치한 국가
region: 해당 국가가 속한 지역 (예: 아시아, 유럽 등)
industry: 산업 분야 (IT, 금융, 제조 등)
company_size: 기업 규모 규모 (스타트업, 중소기업, 대기업)
num_employees: 총 직원 수
annual_revenue_usd_millions: 연간 매출 (백만 달러 단위)
company_founding_year: 기업 설립 연도
company_age: 설립 후 경과된 햇수 (업력)
company_age_group: 업력 그룹 (0-5년, 6-15년, 16-30년, 30년 이상)

2. AI 도입 현황
ai_adoption_rate: 조직 내 AI 도입 수준 (백분율)
ai_adoption_stage: AI 도입 단계 (없음, 파일럿, 부분적, 완전한 도입)
years_using_ai: AI 기술 사용 기간
ai_primary_tool: 기업이 주로 사용하는 AI 도구
num_ai_tools_used: 현재 사용 중인 AI 도구 수
ai_use_case: AI의 주요 비즈니스 활용 사례
ai_projects_active: 현재 진행 중인 활성 AI 프로젝트 수
ai_training_hours: 연간 AI 관련 직원 교육 시간
ai_budget_percentage: AI 이니셔티브에 할당된 예산 비율
ai_maturity_score: 전반적인 AI 역량 성숙도 지수
ai_failure_rate: 실패하거나 중단된 AI 프로젝트 비율
ai_investment_per_employee: 직원 1인당 추정 AI 투자액

3. 규제 및 거버넌스
regulatory_compliance_score: AI 규정 준수 점수
data_privacy_level: 조직의 데이터 프라이버시 보호 수준
ai_ethics_committee: AI 윤리 위원회 유무
ai_risk_management_score: AI 위험 관리 관행 성숙도 점수

4. 업무 환경 및 생산성
remote_work_percentage: 원격 근무 직원 비율
employee_satisfaction_score: 직원 만족도 점수
task_automation_rate: AI로 자동화된 업무 비율
time_saved_per_week: AI로 인해 절약된 주당 평균 시간
productivity_change_percent: AI 도입으로 인한 생산성 변화율

5. 고용 및 인력 변화
jobs_displaced: 자동화로 인해 사라진 일자리 수
jobs_created: AI 도입으로 인해 새로 생긴 일자리 수
reskilled_employees: AI 관련 직무로 재교육받은 직원 수

6. 재무 성과 및 혁신
revenue_growth_percent: AI 도입과 연계된 매출 성장률
cost_reduction_percent: AI 구현으로 인한 비용 절감률
innovation_score: 조직의 혁신 역량 지수
customer_satisfaction: 고객 만족도 점수

7. 데이터 출처 및 수집 방식
survey_source: 설문 데이터가 수집된 출처
data_collection_method: 데이터 수집 또는 컴파일에 사용된 방법

}
* ai_industry_summary.csv - 
About this file

Suggest Edits
ai_industry_summary.csv
Aggregated industry-level metrics derived from the main dataset to support quick benchmarking and comparative analysis.

Rows: 9
Columns: 8

* country_ai_index.csv -
About this file

Suggest Edits
country_ai_index.csv
Country-level indicators representing digital infrastructure, economic conditions, and AI ecosystem maturity.

Rows: 30
Columns: 8


----------------------------

=== [1] Data Head (상위 5개 행) ===
   response_id  company_id  survey_year quarter country  ... cost_reduction_percent innovation_score customer_satisfaction              survey_source  data_collection_method
0            1  COMP-00001         2023      Q1   Italy  ...                   9.45               53                  5.20                 WEF Survey              API Scrape
1            2  COMP-00001         2023      Q2   Italy  ...                   0.00               51                  6.98            McKinsey Report         Phone Interview
2            3  COMP-00001         2023      Q3   Italy  ...                   9.74               40                  4.12  Internal Corporate Survey    Research Compilation
3            4  COMP-00001         2023      Q4   Italy  ...                   0.00               51                  5.72  Internal Corporate Survey    Research Compilation
4            5  COMP-00001         2024      Q1   Italy  ...                   9.02               43                  6.31            McKinsey Report    Research Compilation

[5 rows x 43 columns]


=== [2] Data Info (데이터 요약 정보) ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150000 entries, 0 to 149999
Data columns (total 43 columns):
 #   Column                       Non-Null Count   Dtype
---  ------                       --------------   -----
 0   response_id                  150000 non-null  int64
 1   company_id                   150000 non-null  object
 2   survey_year                  150000 non-null  int64
 3   quarter                      150000 non-null  object
 4   country                      150000 non-null  object
 5   region                       150000 non-null  object
 6   industry                     150000 non-null  object
 7   company_size                 150000 non-null  object
 8   num_employees                150000 non-null  int64
 9   annual_revenue_usd_millions  150000 non-null  float64
 10  company_founding_year        150000 non-null  int64
 11  company_age                  150000 non-null  int64
 12  company_age_group            150000 non-null  object
 13  ai_adoption_rate             150000 non-null  float64
 14  ai_adoption_stage            150000 non-null  object
 15  years_using_ai               150000 non-null  int64
 16  ai_primary_tool              150000 non-null  object
 17  num_ai_tools_used            150000 non-null  int64
 18  ai_use_case                  150000 non-null  object
 19  ai_projects_active           150000 non-null  int64
 20  ai_training_hours            150000 non-null  float64
 21  ai_budget_percentage         150000 non-null  float64
 22  ai_maturity_score            150000 non-null  float64
 23  ai_failure_rate              150000 non-null  float64
 24  ai_investment_per_employee   150000 non-null  float64
 25  regulatory_compliance_score  150000 non-null  int64
 26  data_privacy_level           150000 non-null  object
 27  ai_ethics_committee          150000 non-null  object
 28  ai_risk_management_score     150000 non-null  int64
 29  remote_work_percentage       150000 non-null  float64
 30  employee_satisfaction_score  150000 non-null  float64
 31  task_automation_rate         150000 non-null  float64
 32  time_saved_per_week          150000 non-null  float64
 33  productivity_change_percent  150000 non-null  float64
 34  jobs_displaced               150000 non-null  int64
 35  jobs_created                 150000 non-null  int64
 36  reskilled_employees          150000 non-null  int64
 37  revenue_growth_percent       150000 non-null  float64
 38  cost_reduction_percent       150000 non-null  float64
 39  innovation_score             150000 non-null  int64
 40  customer_satisfaction        150000 non-null  float64
 41  survey_source                150000 non-null  object
 42  data_collection_method       150000 non-null  object
dtypes: float64(15), int64(14), object(14)
memory usage: 49.2+ MB


=== [3] Data Types (컬럼별 데이터 타입) ===
response_id                      int64
company_id                      object
survey_year                      int64
quarter                         object
country                         object
region                          object
industry                        object
company_size                    object
num_employees                    int64
annual_revenue_usd_millions    float64
company_founding_year            int64
company_age                      int64
company_age_group               object
ai_adoption_rate               float64
ai_adoption_stage               object
years_using_ai                   int64
ai_primary_tool                 object
num_ai_tools_used                int64
ai_use_case                     object
ai_projects_active               int64
ai_training_hours              float64
ai_budget_percentage           float64
ai_maturity_score              float64
ai_failure_rate                float64
ai_investment_per_employee     float64
regulatory_compliance_score      int64
data_privacy_level              object
ai_ethics_committee             object
ai_risk_management_score         int64
remote_work_percentage         float64
employee_satisfaction_score    float64
task_automation_rate           float64
time_saved_per_week            float64
productivity_change_percent    float64
jobs_displaced                   int64
jobs_created                     int64
reskilled_employees              int64
revenue_growth_percent         float64
cost_reduction_percent         float64
innovation_score                 int64
customer_satisfaction          float64
survey_source                   object
data_collection_method          object
dtype: object


=== [4] Missing Values (결측치 확인) ===
response_id                    0
company_id                     0
survey_year                    0
quarter                        0
country                        0
region                         0
industry                       0
company_size                   0
num_employees                  0
annual_revenue_usd_millions    0
company_founding_year          0
company_age                    0
company_age_group              0
ai_adoption_rate               0
ai_adoption_stage              0
years_using_ai                 0
ai_primary_tool                0
num_ai_tools_used              0
ai_use_case                    0
ai_projects_active             0
ai_training_hours              0
ai_budget_percentage           0
ai_maturity_score              0
ai_failure_rate                0
ai_investment_per_employee     0
regulatory_compliance_score    0
data_privacy_level             0
ai_ethics_committee            0
ai_risk_management_score       0
remote_work_percentage         0
employee_satisfaction_score    0
task_automation_rate           0
time_saved_per_week            0
productivity_change_percent    0
jobs_displaced                 0
jobs_created                   0
reskilled_employees            0
revenue_growth_percent         0
cost_reduction_percent         0
innovation_score               0
customer_satisfaction          0
survey_source                  0
data_collection_method         0
dtype: int64


=== [5] Outliers Detection (수치형 데이터 이상치 확인 - IQR 방식) ===
                         Column  Outliers_Count
2                 num_employees           27894
3   annual_revenue_usd_millions           27947
6              ai_adoption_rate             504
8             num_ai_tools_used            1587
9            ai_projects_active             353
10            ai_training_hours             528
11         ai_budget_percentage             644
12            ai_maturity_score             582
13              ai_failure_rate             249
14   ai_investment_per_employee           12098
15  regulatory_compliance_score             706
16     ai_risk_management_score             269
17       remote_work_percentage             850
18  employee_satisfaction_score             963
19         task_automation_rate             511
20          time_saved_per_week             526
21  productivity_change_percent             529
22               jobs_displaced           26622
23                 jobs_created           27697
24          reskilled_employees           26980
25       revenue_growth_percent             538
26       cost_reduction_percent             519
27             innovation_score             443
28        customer_satisfaction             862

이 데이터셋은 아주 작은 스타트업부터 초거대 기업까지 전 세계의 다양한 기업들을 포함하고 있기 때문에, 통계적으로 "이상치"로 분류되는 거대 기업들의 데이터가 많이 포함되어 있는 것으로 보입니다. 이는 데이터 오류라기보다는 분석 대상의 규모 차이가 매우 크다는 것을 의미합니다.

Q: 오... 그러면 학습시킬때 회사 규모에 따라서 학습 시켜야한다는거야?
학습 전략 실험 결과가 나왔습니다!

결론부터 말씀드리면, **"모든 데이터를 합쳐서 하나의 모델로 학습시키되, 회사 규모 정보를 피처(Feature)로 넣어주는 방식"**이 각 규모별로 모델을 따로 만드는 것보다 성능이 조금 더 좋았습니다.

📊 실험 결과 (평균 절대 오차 - MAE)
통합 모델 (General): 3.0086
규모별 분리 모델 (Segmented): 3.0557 (평균값) 결과값이 낮을수록 예측이 정확합니다.
💡 왜 통합 모델이 더 좋을까요?
데이터 양의 이점: 15만 개의 전체 데이터를 활용할 때 모델이 더 일반적인 패턴을 잘 학습합니다.
규모 정보 활용: 모델이 "대기업 데이터"와 "스타트업 데이터"의 차이를 스스로 학습하면서도, 공통적인 비즈니스 로직(예: AI 도구 수가 많으면 생산성이 오른다 등)을 공유할 수 있기 때문입니다.
✅ 최종 추천 가이드
num_employees와 annual_revenue는 **로그 변환(Log Scaling)**을 해서 값의 격차를 줄인 뒤 사용하세요.
하나의 모델을 쓰시되, company_size를 꼭 피처로 포함해 주세요.
상세한 분석 과정과 코드는 

walkthrough.md
에서 확인하실 수 있습니다. 분석용 코드는 model_comparison.py에 정리해 두었습니다! 🚀


----------------------------------



💡 LightGBM 최적화 5단계 전처리 파이프라인
- 1단계: 결측치 및 이상치 파악 (가장 먼저 수행)

모델에 데이터를 넣거나 변환하기 전에 가장 먼저 해야 하는 작업입니다.

대출 데이터의 경우 나이가 144살이거나, 직장 경력이 나이보다 많은 논리적 오류(이상치)를 찾아내어 제거하거나 평균값 등으로 대체합니다.

- 2단계: 명목 데이터 인코딩 👉 [수정] 원핫 인코딩 대신 라벨 인코딩 / Category 타입 변환

중요: LightGBM은 트리(Tree) 기반 모델 중에서도 범주형 변수를 가장 잘 다루는 모델입니다. 원핫 인코딩을 하면 데이터의 차원이 불필요하게 늘어나고 0이 너무 많아져(Sparse) 오히려 학습 속도와 성능이 떨어집니다.

해결책: '자가', '전세', '월세' 같은 텍스트 데이터를 0, 1, 2 같은 단순 정수로 바꾸는 라벨 인코딩(Label Encoding)을 하거나, Pandas에서 데이터 타입을 category로 변환만 해두면 됩니다. LightGBM이 알아서 최적의 기준으로 분류합니다.

- 3단계: 파생 변수 생성 및 다중공선성 확인

선형 회귀 모델과 달리 트리 모델은 다중공선성에 매우 강하므로, 굳이 다중공선성이 높다고 해서 변수를 무조건 기계적으로 삭제할 필요는 없습니다.

다만, 대출금액과 연소득을 활용해 이미 소득 대비 대출 비율이라는 더 좋은 변수가 있다면 중복되는 원본 변수들을 정리해 주는 것이 모델을 가볍게 만들고 나중에 결과를 해석할 때 유리합니다.

- 4단계: 모델 학습 및 하이퍼파라미터 튜닝 (L1/L2 정규화 포함)

전처리가 끝난 데이터를 모델에 넣고 학습합니다. 이때 과적합(Overfitting)을 막기 위해 말씀하신 reg_alpha(L1), reg_lambda(L2) 값을 부여합니다.

장착하고 계신 RTX 3060 8GB의 GPU 가속 환경(device='gpu')을 활용하면, 이 단계에서 트리의 깊이(max_depth)나 학습률(learning_rate) 같은 다양한 파라미터 조합을 수십 번씩 반복 테스트하더라도 순식간에 최적의 값을 찾아낼 수 있습니다.

- 5단계: 학습 후 중요도 분석(SHAP) 및 변수 최종 제거

1차 학습 결과를 바탕으로 변수 중요도(Feature Importance)나 SHAP Value를 뽑아봅니다.

모델의 예측에 거의 기여하지 않는 하위 10~20%의 변수들을 과감히 쳐내고, 남은 '진짜 중요한 변수'들만 가지고 다시 4단계로 돌아가 최종 모델을 훈련시킵니다.