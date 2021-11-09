from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.metrics import silhouette_score 
from numpy import genfromtxt
from yellowbrick.cluster import SilhouetteVisualizer, silhouette
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as shc
from nltk.cluster import KMeansClusterer, euclidean_distance, cosine_distance

data = genfromtxt('ttd.csv', delimiter = '\t')
clusterer = KMeansClusterer(4, euclidean_distance)
clusters = clusterer.cluster(data, True, trace=True)

score = silhouette_score(data, clusters, metric='euclidean')
print('Silhouette Score: %.3f' % score)

#visualizer = SilhouetteVisualizer(clusters, colors='yellowbrick')
#visualizer.fit(data)
#visualizer.show()

LabelList = open('titles.txt', 'r')
LabelList.close()
plt.figure(figsize=(10, 7))
plt.title("Dendogram")
dend = shc.dendrogram(shc.linkage(data, method='ward'))
plt.show()
