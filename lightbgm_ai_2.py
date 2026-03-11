import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1단계: 데이터 로드 및 EDA (결측치 및 이상치 파악)
# ==========================================
print("=== [Step 1] Data Loading & EDA ===")
file_path = 'ai_company_adoption.csv'
df = pd.read_csv(file_path)

target = 'revenue_growth_percent'
base_features = ['productivity_change_percent', 'ai_adoption_rate']

# (1) 결측치 확인
print("\n[1-1] Missing Values Check:")
print(df[base_features + [target]].isnull().sum())

# (2) 이상치 확인 (IQR 방식)
print("\n[1-2] Outliers Detection (IQR Method):")
for col in base_features + [target]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
    print(f"- {col}: {outliers_count} outliers found")

# ==========================================
# 2단계: 명목 데이터 인코딩 (필요 시 수행)
# ==========================================
print("\n=== [Step 2] Nominal Encoding ===")
print("- Skip: Using only numerical features for this minimalist model.")

# ==========================================
# 3단계: 파생 변수 생성 및 다중공선성 확인
# ==========================================
print("\n=== [Step 3] Feature Engineering & Multicollinearity ===")
df['ai_interaction_score'] = df['ai_adoption_rate'] * df['productivity_change_percent']
features = base_features + ['ai_interaction_score']

# 다중공선성 확인 (상관계수 기반)
print("\n[3-1] Correlation Matrix:")
print(df[features].corr())

# ==========================================
# 4단계: 모델 학습 및 하이퍼파라미터 튜닝 (L1/L2 정규화 포함)
# ==========================================
print("\n=== [Step 4] Hyperparameter Tuning (L1/L2 Regularization) ===")
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_dist = {
    'num_leaves': [20, 31, 40, 50],
    'learning_rate': [0.01, 0.05, 0.1],
    'n_estimators': [500, 1000],
    'reg_alpha': [0.0, 0.1, 1.0],
    'reg_lambda': [0.0, 0.1, 1.0],
    'min_child_samples': [20, 30, 50]
}

print("- Finding best parameters...")
lgbm = lgb.LGBMRegressor(random_state=42, verbose=-1)
random_search = RandomizedSearchCV(lgbm, param_distributions=param_dist, n_iter=5, cv=3, random_state=42, n_jobs=-1)
random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_

# 최적 모델로 최종 학습 (Early Stopping)
best_model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    eval_metric='rmse',
    callbacks=[lgb.early_stopping(stopping_rounds=50), lgb.log_evaluation(period=0)]
)

# ==========================================
# 5단계: 모델 정확도 평가 (Train vs Test 비교)
# ==========================================
print("\n=== [Step 5] Model Evaluation (Train vs Test) ===")

def evaluate(model, X, y, label):
    pred = model.predict(X)
    mae = mean_absolute_error(y, pred)
    rmse = np.sqrt(mean_squared_error(y, pred))
    r2 = r2_score(y, pred)
    print(f"[{label}] MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}")

# Train 성능과 Test 성능을 비교하여 과적합 여부 확인
evaluate(best_model, X_train, y_train, "TRAIN")
evaluate(best_model, X_test, y_test, "TEST")

# ==========================================
# 6단계: 실제 모델 사용 예제 (Prediction Example)
# ==========================================
print("\n=== [Step 6] Practical Prediction Example ===")

# 가상의 새로운 기업 데이터 생성
new_data = pd.DataFrame({
    'productivity_change_percent': [15.5, 5.0],  # 생산성 변화율 (%)
    'ai_adoption_rate': [80.0, 30.0]             # AI 도입률 (%)
})

# 동일한 파생 변수 생성 필수
new_data['ai_interaction_score'] = new_data['ai_adoption_rate'] * new_data['productivity_change_percent']

# 예측 수행
prediction = best_model.predict(new_data)

print("Hypothetical Company Prediction:")
for i, pred in enumerate(prediction):
    prod = new_data.iloc[i]['productivity_change_percent']
    adopt = new_data.iloc[i]['ai_adoption_rate']
    print(f"Company {i+1} (Prod {prod}%, Adopt {adopt}%) -> Predicted Revenue Growth: {pred:.2f}%")

print("\nAll steps completed.")
