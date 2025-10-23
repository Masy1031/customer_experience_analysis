import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# データ読み込み
customer_clustered = pd.read_csv('../data/customer_clustered.csv')

# 集計データ作成
dashboard_data = customer_clustered.groupby('cluster').agg({
    'rides': 'mean',
    'app_logins': 'mean',
    'purchases': 'mean',
    'membership_years': 'mean'
}).reset_index()

# 保存
dashboard_data.to_csv('../app/dashboard_prototype.csv', index=False)
print("✅ Dashboard data exported to app/dashboard_prototype.csv")

# 簡易可視化
sns.heatmap(dashboard_data.set_index('cluster'), annot=True, cmap='Blues')
plt.title("Cluster Summary Dashboard")
plt.show()
