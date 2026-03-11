import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# 데이터 로드
df = pd.read_csv('ai_company_adoption.csv')

# 피처 정의
all_features = [
    'industry', 'region', 'company_size', 'ai_adoption_stage', 
    'ai_primary_tool', 'ai_use_case', 'data_privacy_level', 'ai_ethics_committee',
    'company_age', 'num_employees', 'annual_revenue_usd_millions', 
    'ai_adoption_rate', 'years_using_ai', 'num_ai_tools_used', 
    'ai_projects_active', 'ai_training_hours', 'ai_budget_percentage', 
    'ai_maturity_score', 'ai_investment_per_employee', 'task_automation_rate', 
    'productivity_change_percent', 'cost_reduction_percent', 'innovation_score', 
    'customer_satisfaction', 'employee_satisfaction_score', 'reskilled_employees'
]
top_2_features = ['productivity_change_percent', 'ai_adoption_rate']
cat_features = ['industry', 'region', 'company_size', 'ai_adoption_stage', 'ai_primary_tool', 'ai_use_case', 'data_privacy_level', 'ai_ethics_committee']

def train_and_eval(name, features, categorical=None):
    X = df[features].copy()
    y = df['revenue_growth_percent']
    
    if categorical:
        for col in categorical:
            if col in X.columns:
                X[col] = X[col].astype('category')
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = lgb.LGBMRegressor(n_estimators=500, learning_rate=0.05, random_state=42, verbose=-1)
    model.fit(X_train, y_train, categorical_feature=[c for c in categorical if c in features] if categorical else None)
    
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    return name, r2, mae

results = []
results.append(train_and_eval("Full Model (26 Features)", all_features, cat_features))
results.append(train_and_eval("Top 2 Only (Productivity, Adoption)", top_2_features, []))

print("\n=== Model Comparison Results ===")
print(f"{'Model Name':<40} | {'R2 Score':<10} | {'MAE':<10}")
print("-" * 65)
for name, r2, mae in results:
    print(f"{name:<40} | {r2:<10.4f} | {mae:<10.4f}")
