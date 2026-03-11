import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df = pd.read_csv('ai_company_adoption.csv')

# 수치형 주요 지표 선택
metrics = ['num_employees', 'annual_revenue_usd_millions', 'productivity_change_percent', 'ai_budget_percentage']

print("=== [Company Size별 기초 통계 비교] ===")
summary = df.groupby('company_size')[metrics].mean()
print(summary)

# 시각화 (각 규모별 분포 차이 확인)
plt.figure(figsize=(15, 10))

for i, metric in enumerate(metrics, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x='company_size', y=metric, data=df)
    plt.title(f'{metric} by Company Size')
    plt.yscale('log') if 'revenue' in metric or 'employees' in metric else None # 규모 차이가 크므로 로그 스케일 적용

plt.tight_layout()
plt.savefig('company_size_comparison.png')
print("\n시각화 결과가 'company_size_comparison.png'로 저장되었습니다.")
