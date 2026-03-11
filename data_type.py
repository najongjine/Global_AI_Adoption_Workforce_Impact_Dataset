import pandas as pd

# 데이터 로드
file_path = 'ai_company_adoption.csv'
df = pd.read_csv(file_path)

print("=== [1] Data Head (상위 5개 행) ===")
print(df.head())
print("\n")

print("=== [2] Data Info (데이터 요약 정보) ===")
df.info()
print("\n")

print("=== [3] Data Types (컬럼별 데이터 타입) ===")
print(df.dtypes)
print("\n")

print("=== [4] Missing Values (결측치 확인) ===")
print(df.isnull().sum())
print("\n")

print("=== [5] Outliers Detection (수치형 데이터 이상치 확인 - IQR 방식) ===")
# 수치형 컬럼만 선택
numeric_df = df.select_dtypes(include=['number'])

# IQR 방식을 이용한 이상치 개수 계산
outliers_summary = {}
for col in numeric_df.columns:
    Q1 = numeric_df[col].quantile(0.25)
    Q3 = numeric_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_count = ((numeric_df[col] < lower_bound) | (numeric_df[col] > upper_bound)).sum()
    outliers_summary[col] = outliers_count

# 결과 출력
outliers_df = pd.DataFrame(list(outliers_summary.items()), columns=['Column', 'Outliers_Count'])
print(outliers_df[outliers_df['Outliers_Count'] > 0]) # 이상치가 있는 컬럼만 출력
if outliers_df['Outliers_Count'].sum() == 0:
    print("이상치가 발견된 컬럼이 없습니다.")
