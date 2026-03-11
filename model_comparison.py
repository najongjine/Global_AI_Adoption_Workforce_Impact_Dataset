import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

# 1. 데이터 로드
print("Loading data...")
df = pd.read_csv('ai_company_adoption.csv')

# 2. 전처리: 로그 스케일링
print("Preprocessing: Applying Log Scaling...")
df['num_employees_log'] = np.log1p(df['num_employees'])
df['annual_revenue_log'] = np.log1p(df['annual_revenue_usd_millions'])

# 3. 피처 선택 (수치형 + 범주형 일부)
# 타겟: 생산성 변화율 (productivity_change_percent)
features = [
    'num_employees_log', 'annual_revenue_log', 'ai_adoption_rate', 
    'years_using_ai', 'num_ai_tools_used', 'ai_budget_percentage',
    'ai_maturity_score', 'industry'
]
target = 'productivity_change_percent'

# 범주형 변수(industry) 인코딩
le = LabelEncoder()
df['industry_encoded'] = le.fit_transform(df['industry'])
features_for_model = [f if f != 'industry' else 'industry_encoded' for f in features]

# ---------------------------------------------------------
# [Approach 1] General Model (모든 규모 통합 + company_size 피처 포함)
# ---------------------------------------------------------
print("\n[Approach 1] Training General Model...")
X_gen = df[features_for_model + ['company_size']]
# company_size 인코딩
X_gen = pd.get_dummies(X_gen, columns=['company_size'])
y_gen = df[target]

X_train, X_test, y_train, y_test = train_test_split(X_gen, y_gen, test_size=0.2, random_state=42)

gen_model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
gen_model.fit(X_train, y_train)
y_pred = gen_model.predict(X_test)

gen_mae = mean_absolute_error(y_test, y_pred)
gen_r2 = r2_score(y_test, y_pred)
print(f"General Model - MAE: {gen_mae:.4f}, R2: {gen_r2:.4f}")

# ---------------------------------------------------------
# [Approach 2] Segmented Models (규모별 분리 학습)
# ---------------------------------------------------------
print("\n[Approach 2] Training Segmented Models...")
results_seg = {}

for size in df['company_size'].unique():
    print(f"Training model for size: {size}...")
    df_size = df[df['company_size'] == size]
    
    X_seg = df_size[features_for_model]
    y_seg = df_size[target]
    
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_seg, y_seg, test_size=0.2, random_state=42)
    
    seg_model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
    seg_model.fit(X_train_s, y_train_s)
    y_pred_s = seg_model.predict(X_test_s)
    
    mae_s = mean_absolute_error(y_test_s, y_pred_s)
    r2_s = r2_score(y_test_s, y_pred_s)
    results_seg[size] = {'MAE': mae_s, 'R2': r2_s}
    print(f" - {size} Model - MAE: {mae_s:.4f}, R2: {r2_s:.4f}")

# ---------------------------------------------------------
# 결과 비교 출력
# ---------------------------------------------------------
print("\n=== [Final Comparison] ===")
print(f"General Model overall MAE: {gen_mae:.4f}")
avg_seg_mae = np.mean([res['MAE'] for res in results_seg.values()])
print(f"Segmented Models average MAE: {avg_seg_mae:.4f}")

if avg_seg_mae < gen_mae:
    print("\n결론: 규모별 분리 학습(Segmented)이 더 정밀한 예측을 보여줍니다.")
else:
    print("\n결론: 하나의 통합 모델(General)이 더 안정적인 성능을 보여줍니다.")
