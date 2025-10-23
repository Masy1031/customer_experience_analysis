import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# データ読み込み
customer_data = pd.read_csv('../data/customer_data.csv')
usage_log = pd.read_csv('../data/usage_log.csv')

# 利用ログ集計
usage_summary = usage_log.groupby('customer_id').agg({
    'rides': 'sum',
    'app_logins': 'sum',
    'purchases': 'sum'
}).reset_index()

# 顧客データ結合
customer_full = pd.merge(customer_data, usage_summary, on='customer_id', how='left').fillna(0)

# 基礎統計
print(customer_full.describe())

# 可視化
sns.pairplot(customer_full[['rides', 'app_logins', 'purchases', 'membership_years']])
plt.show()

# 保存
customer_full.to_csv('../data/customer_full.csv', index=False)
