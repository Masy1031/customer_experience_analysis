# 顧客体験分析ポートフォリオ

## 概要
本リポジトリは、顧客体験（Customer Experience）向上のための分析プロセスを再現したポートフォリオです。  
SaaS・交通・小売・サブスクリプション事業などのデータを想定し、以下のステップで構成されています。

1. **顧客データの理解と前処理**  
   - 顧客属性や利用ログの集計・特徴量化  
2. **顧客セグメンテーション（クラスタリング）と示唆出し**  
   - RFM類似の要素＋利用傾向からクラスタリング  
3. **ダッシュボード用データ設計**  
   - BI/可視化ツール（Looker Studio, Tableau等）連携を想定した設計  

全データは架空生成データを用いており、実際の企業データを安全に模擬できる構成です。

## 🧩 ディレクトリ構成
````
customer_experience_analysis/
├── scripts/ # データ生成・補助スクリプト
├── data/ # 顧客データ・利用ログ（自動生成）
├── notebooks/ # 各分析段階のNotebook
├── app/ # ダッシュボード出力用データ
└── README.md # 本ファイル

````

## ⚙️ セットアップ手順

### 1️⃣ リポジトリをクローン
```bash
git clone https://github.com/USERNAME/customer_experience_analysis.git
cd customer_experience_analysis
```

### 2️⃣ 仮想環境セットアップ
```python
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ 架空データ生成
```python
python scripts/generate_customer_data.py

```
### 4️⃣ 分析ノートブック実行
```bash
jupyter notebook

```

#### Notebook の順番：
- 01_customer_analysis.py：データ理解・前処理
- 02_customer_segmentation.py：クラスタリング・示唆出し
- 03_customer_dashboard.py：ダッシュボード用データ整形

## 📊 使用技術
- Python 3.10+
- pandas / numpy
- scikit-learn
- matplotlib / seaborn
- Jupyter Notebook

## 📘 目的・期待するアウトプット
- 顧客群ごとの特徴理解（例：リピーター・離反予備群）
- KMeans によるクラスタリング結果の可視化
- BI ダッシュボード用のデータ整形・出力

## 🧮 今後の拡張例
- LTV（顧客生涯価値）推定
- 離反予測モデル構築
- Streamlit / Dash による可視化アプリ作成

## ✅ このテンプレの特徴
- 実務想定の分析フローを段階分けして明示
- データ生成〜前処理〜クラスタリング〜BI出力までを1リポジトリで完結
- READMEを整えておけば、採用担当・エンジニア・データ職向けポートフォリオとして即利用可能