import numpy as np

f = open('../datasets/UN4col.csv')
X = np.loadtxt(f)
f.close()

from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

K = range(1,10)
km = [kmeans(X,k) for k in K] # kmeans with each k (1-10)
centroids = [cent for cent,var in km] # cluster of centroids

D_k = [cdist(X, cent, 'euclidean') for cent in centroids] # find the distance

cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/X.shape[0] for d in dist]  

kIdx = 2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, avgWithinSS, 'b*-')
ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, 
      markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
tt = plt.title('Elbow for K-Means clustering')

plt.show()

from sklearn.cluster import KMeans
km = KMeans(3, init='k-means++') # initialize
km.fit(X)
c = km.predict(X) # classify into three clusters

import kmeans as mykm
(pl0,pl1,pl2) = mykm.plot_clusters(X,c,3,2) # column 3 GDP, vs column 2 infant mortality. Note indexing is 0 based
plt.show((pl0,pl1,pl2))