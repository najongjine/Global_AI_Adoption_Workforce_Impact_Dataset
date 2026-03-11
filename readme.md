Global AI Adoption & Workforce Impact Dataset
https://www.kaggle.com/datasets/mohankrishnathalla/global-ai-adoption-and-workforce-impact-dataset

* ai_company_adoption.csv -
About this file

Suggest Edits
ai_company_adoption.csv
Main dataset containing company-level observations across multiple years and quarters.

Each row represents a company survey observation capturing AI adoption behavior, workforce outcomes, operational changes, and governance practices.

Rows: 150,000
Columns: 43
{
response_id
Unique identifier for each observation record

company_id
Unique identifier for a company allowing panel data analysis across years

survey_year
Year in which the observation was recorded

quarter
Quarter of the year when the observation was recorded (Q1–Q4)

country
Country where the company operates

region
Geographic region of the country

industry
Industry sector of the company

company_size
Company size classification (Startup, SME, Enterprise)

num_employees
Total number of employees in the company

annual_revenue_usd_millions
Annual company revenue measured in USD millions

company_founding_year
Year the company was established

company_age
Number of years since the company was founded

company_age_group
Age category of the company (0–5, 6–15, 16–30, 30+ years)

ai_adoption_rate
Percentage level of AI adoption within the organization

ai_adoption_stage
AI adoption stage classification (none, pilot, partial, full)

years_using_ai
Number of years the company has been using AI technologies

ai_primary_tool
Primary AI tool or platform used by the company

num_ai_tools_used
Number of AI tools currently used by the company

ai_use_case
Primary business use case of AI within the company

ai_projects_active
Number of active AI projects currently running

ai_training_hours
Average AI-related employee training hours per year

ai_budget_percentage
Percentage of company budget allocated to AI initiatives

ai_maturity_score
Composite index representing overall AI capability maturity

ai_failure_rate
Percentage of AI projects that failed or were discontinued

ai_investment_per_employee
Estimated AI investment normalized per employee

regulatory_compliance_score
Score representing compliance with AI regulations

data_privacy_level
Level of organizational data privacy protection

ai_ethics_committee
Indicates whether the company has an AI ethics committee

ai_risk_management_score
Score reflecting maturity of AI risk management practices

remote_work_percentage
Percentage of workforce operating remotely

employee_satisfaction_score
Average employee satisfaction score

task_automation_rate
Percentage of operational tasks automated by AI

time_saved_per_week
Average hours saved per employee per week due to AI

productivity_change_percent
Percentage productivity improvement attributed to AI

jobs_displaced
Number of jobs displaced due to automation

jobs_created
Number of new jobs created due to AI adoption

reskilled_employees
Number of employees reskilled for AI-enabled roles

revenue_growth_percent
Revenue growth percentage linked to AI adoption

cost_reduction_percent
Percentage cost reduction due to AI implementation

innovation_score
Innovation capability index of the organization

customer_satisfaction
Customer satisfaction score

survey_source
Source from which the survey data was compiled

data_collection_method
Method used to collect or compile the data

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

========== [ 1. 데이터 미리보기 (head) ] ==========


========== [ 2. 데이터 기본 정보 (info) ] ==========



========== [ 3. 데이터 타입 (dtypes) ] ==========





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