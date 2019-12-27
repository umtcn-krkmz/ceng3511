import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from numpy import genfromtxt
import sys,os
 
import glob
from PyPDF2 import PdfFileMerger
 
def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
 
    for path in input_paths:
        pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)
 


X = genfromtxt('data.csv',delimiter=',',skip_header=1)
colors = 11*["g","r","c","b","k","y","m"]
class K_Means:
    def __init__(self, k=11, tol=0.001, max_iter=900):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False

            if optimized:
                break

    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification







clf = K_Means(2)
clf.fit(X)
f=plt.figure()
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=10, linewidths=5)
        
plt.show()
f.savefig("plot1.pdf",bbox_inches='tight')


clf = K_Means(3)
clf.fit(X)
f=plt.figure()
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=10, linewidths=5)
        
plt.show()
f.savefig("plot2.pdf",bbox_inches='tight')


clf = K_Means(4)
clf.fit(X)
f=plt.figure()
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=10, linewidths=5)
        
plt.show()
f.savefig("plot3.pdf",bbox_inches='tight')


clf = K_Means(5)
clf.fit(X)
f=plt.figure()
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=10, linewidths=5)
        
plt.show()
f.savefig("plot4.pdf",bbox_inches='tight')

paths = glob.glob('*.pdf')
paths.sort()
merger('plot.pdf', paths)
os.remove("plot1.pdf")
os.remove("plot2.pdf")
os.remove("plot3.pdf")
os.remove("plot4.pdf")
