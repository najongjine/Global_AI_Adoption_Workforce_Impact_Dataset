import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 로드
print("Loading data...")
file_path = 'ai_company_adoption.csv'
df = pd.read_csv(file_path)

# 2. 피처 선택 (Feature Selection)
# 타겟 변수
target = 'revenue_growth_percent'

# 범주형 변수 (Categorical Features)
cat_features = [
    'industry', 'region', 'company_size', 'ai_adoption_stage', 
    'ai_primary_tool', 'ai_use_case', 'data_privacy_level', 'ai_ethics_committee'
]

# 수치형 변수 (Numerical Features)
num_features = [
    'company_age', 'num_employees', 'annual_revenue_usd_millions', 
    'ai_adoption_rate', 'years_using_ai', 'num_ai_tools_used', 
    'ai_projects_active', 'ai_training_hours', 'ai_budget_percentage', 
    'ai_maturity_score', 'ai_investment_per_employee', 'task_automation_rate', 
    'productivity_change_percent', 'cost_reduction_percent', 'innovation_score', 
    'customer_satisfaction', 'employee_satisfaction_score', 'reskilled_employees'
]

features = cat_features + num_features

# 3. 전처리
print("Preprocessing...")
X = df[features].copy()
y = df[target]

# LightGBM의 범주형 데이터 처리를 위해 dtype 변경
for col in cat_features:
    X[col] = X[col].astype('category')

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 모델 생성 및 학습
print("Training LightGBM model...")
model = lgb.LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.05,
    num_leaves=31,
    random_state=42,
    importance_type='gain'
)

model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    eval_metric='rmse',
    categorical_feature=cat_features,
    callbacks=[lgb.early_stopping(stopping_rounds=50), lgb.log_evaluation(period=100)]
)

# 5. 평가
print("\n=== Model Evaluation ===")
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")

# 6. 피처 중요도 시각화
plt.figure(figsize=(12, 10))
lgb.plot_importance(model, max_num_features=20, importance_type='gain', figsize=(12, 8))
plt.title("Feature Importance (Gain)")
plt.tight_layout()
plt.savefig('feature_importance.png')
print("\nFeature importance plot saved as 'feature_importance.png'")

# 결과 요약 저장 (Walkthrough 업데이트용)
with open('results_summary.txt', 'w') as f:
    f.write(f"MAE: {mae:.4f}\n")
    f.write(f"RMSE: {rmse:.4f}\n")
    f.write(f"R2: {r2:.4f}\n")
