import pandas as pd
import numpy as np

np.random.seed(42)

# 顧客数
n_customers = 500

# 顧客基本情報
customer_data = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'age': np.random.randint(18, 70, size=n_customers),
    'gender': np.random.choice(['M', 'F'], size=n_customers),
    'membership_years': np.random.randint(1, 10, size=n_customers),
    'total_points': np.random.randint(0, 10000, size=n_customers)
})

# 利用ログ
usage_log = pd.DataFrame({
    'customer_id': np.random.choice(customer_data['customer_id'], size=2000),
    'month': np.random.randint(1, 13, size=2000),
    'rides': np.random.poisson(lam=10, size=2000),
    'app_logins': np.random.poisson(lam=5, size=2000),
    'purchases': np.random.randint(0, 5, size=2000)
})

# CSV出力
customer_data.to_csv('data/customer_data.csv', index=False)
usage_log.to_csv('data/usage_log.csv', index=False)
print("✅ Customer data and usage logs generated.")
