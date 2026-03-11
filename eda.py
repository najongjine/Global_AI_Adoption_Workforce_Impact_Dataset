import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set aesthetic style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'Malgun Gothic' # For Korean characters if any
plt.rcParams['axes.unicode_minus'] = False

def run_eda(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    print("--- Loading Data ---")
    df = pd.read_csv(file_path)
    
    print("\n--- Basic Info ---")
    print(df.info())
    
    print("\n--- Summary Statistics ---")
    print(df.describe())
    
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # 1. AI Adoption by Industry
    plt.figure(figsize=(12, 6))
    if 'Industry' in df.columns:
        sns.countplot(data=df, y='Industry', order=df['Industry'].value_counts().index, palette='viridis')
        plt.title('Distribution of AI Adoption by Industry')
        plt.tight_layout()
        plt.savefig('eda_industry_distribution.png')
        print("Saved: eda_industry_distribution.png")

    # 2. Company Size vs Productivity Change
    plt.figure(figsize=(10, 6))
    if 'Company_Size' in df.columns and 'productivity_change_percent' in df.columns:
        sns.boxplot(data=df, x='Company_Size', y='productivity_change_percent', palette='Set2')
        plt.title('Productivity Change by Company Size')
        plt.tight_layout()
        plt.savefig('eda_productivity_by_size.png')
        print("Saved: eda_productivity_by_size.png")

    # 3. Correlation Heatmap
    plt.figure(figsize=(12, 10))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        sns.heatmap(numeric_df.corr(), annot=False, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap of Financial & Impact Metrics')
        plt.tight_layout()
        plt.savefig('eda_correlation_heatmap.png')
        print("Saved: eda_correlation_heatmap.png")

    # 4. Jobs Created vs Displaced
    plt.figure(figsize=(10, 6))
    if 'jobs_created' in df.columns and 'jobs_displaced' in df.columns:
        sns.scatterplot(data=df, x='jobs_displaced', y='jobs_created', alpha=0.5, color='blue')
        plt.title('Jobs Displaced vs Jobs Created')
        plt.tight_layout()
        plt.savefig('eda_jobs_impact.png')
        print("Saved: eda_jobs_impact.png")

    print("\nEDA completed. Visualizations saved as PNG files.")

if __name__ == "__main__":
    file_path = 'ai_company_adoption.csv'
    run_eda(file_path)
