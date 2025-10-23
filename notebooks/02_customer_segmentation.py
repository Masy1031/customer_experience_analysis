import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# データ読み込み
customer_full = pd.read_csv('../data/customer_full.csv')

# クラスタリング対象カラム
features = ['rides', 'app_logins', 'purchases', 'membership_years', 'total_points']
X = customer_full[features]

# スケーリング
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeansクラスタリング
kmeans = KMeans(n_clusters=4, random_state=42)
customer_full['cluster'] = kmeans.fit_predict(X_scaled)

# 各クラスタ特徴
print(customer_full.groupby('cluster')[features].mean())

# 可視化
sns.boxplot(x='cluster', y='rides', data=customer_full)
plt.title('Rides Distribution by Cluster')
plt.show()

# 保存
customer_full.to_csv('../data/customer_clustered.csv', index=False)
