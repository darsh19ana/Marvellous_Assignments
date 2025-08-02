import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv("student-mat.csv", sep = ";")
print(df.head())

features = ["G1", "G2", "G3", "studytime", "failures", "absences"]
df_selected = df[features]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_selected)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Understand cluster characteristics
cluster_summary = df.groupby('cluster')[features].mean()
print("Cluster Averages:\n", cluster_summary)

# Map cluster labels (you may adjust based on cluster_summary)
# Suppose: Cluster 0 = Top performers, 1 = Average, 2 = Struggling
# You can re-map based on actual output
cluster_map = cluster_summary.mean(axis=1).sort_values(ascending=False).index
label_mapping = {cluster_map[0]: 'Top Performers', cluster_map[1]: 'Average Students', cluster_map[2]: 'Struggling Students'}
df['performance_category'] = df['cluster'].map(label_mapping)

print("\nCluster Label Counts:\n", df['performance_category'].value_counts())

# Visualize clusters using PCA (2D)
pca = PCA(n_components=2)
pca_components = pca.fit_transform(scaled_data)
df['pca1'] = pca_components[:, 0]
df['pca2'] = pca_components[:, 1]

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='performance_category', palette='Set2', s=80)
plt.title("Student Clusters based on Performance")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.show()

