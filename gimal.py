import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

data = pd.read_csv('happiness2019.csv')
data = data.dropna()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.iloc[:, 1:])

kmeans = KMeans(n_clusters=3, random_state=123, n_init=10)
data['cluster'] = kmeans.fit_predict(scaled_features)

our_country = "South Korea"
our_cluster = data.loc[data['Country name'] == our_country, 'cluster'].values[0]
same_cluster_countries = data[data['cluster'] == our_cluster].copy()

distances = cdist(scaled_features[data['cluster'] == our_cluster], 
                  scaled_features[data['Country name'] == our_country].reshape(1, -1), 
                  metric='euclidean').flatten()

same_cluster_countries = same_cluster_countries.assign(distance=distances)
nearest_country = same_cluster_countries[same_cluster_countries['Country name'] != our_country].sort_values(by='distance').iloc[0]['Country name']
print(nearest_country)
