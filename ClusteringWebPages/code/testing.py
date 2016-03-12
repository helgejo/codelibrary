
from __future__ import division
import urllib2
from bs4 import BeautifulSoup
import numpy
import os
from xml.dom import minidom
import sys
import codecs
import textmining
import math
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as hac
from scipy.spatial.distance import *
import pylab as pl

__author__ = 'HELGJO'
input_dir = "E:/Github/ass2data/training"
output_dir = "../training.out"

def baseline(name):
    xmldoc = minidom.parse(input_dir + "/" + name + "/" + name + ".xml")
    itemlist = xmldoc.getElementsByTagName("corpus")
    person_name = itemlist[0].attributes['search_string'].value
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + person_name + '">"\n'
    footer = '</clustering>\n'

    itemlist = xmldoc.getElementsByTagName('doc')
    docs = [s.attributes['rank'].value for s in itemlist]

    # All-in-one
   # out_aio = open(output_dir + "/all-in-one/" + name + ".clust.xml", 'w')
   # out_aio.write(header)
    #out_aio.write('\t<entity id="0">\n')
  #  for d in docs:
  #      out_aio.write('\t\t<doc rank="' + d + '" />\n')
   # out_aio.write('\t</entity>\n')
   # out_aio.write(footer)
 #   out_aio.close()

    # One-in-one
    out_oio = open(output_dir + "/one-in-one/" + name + ".clust.xml", 'w')
    out_oio.write(header)
    for idx,d in enumerate(docs):
        out_oio.write('\t<entity id="' + str(idx) + '">\n')
        out_oio.write('\t\t<doc rank="' + d + '" />\n')
        out_oio.write('\t</entity>\n')
    out_oio.write(footer)
    out_oio.close()

# Compute the cosine similarity of two term vectors
def cosine(tv1, tv2):
    # tv1 and tv2 must have the same length
    if len(tv1) != len(tv2):
        print "Error: term vectors must have the same length!"
        return -1

    cnt = sum1 = sum2 = 0
    for i in range(len(tv1)):
        cnt += tv1[i] * tv2[i]
        sum1 += tv1[i] * tv1[i]
        sum2 += tv2[i] * tv2[i]

    print cnt
    print sum1
    print sum2

    return 0 if sum1 * sum2 == 0 else cnt / math.sqrt(sum1 * sum2)
#for name in os.listdir(input_dir):
#    baseline(name)
name = "Abby_Watkins"
#baseline(name)

f=codecs.open(input_dir + "/" + name + "/docs/" +"001.html", 'r')
g=codecs.open(input_dir + "/" + name + "/docs/" +"002.html", 'r')
h=codecs.open(input_dir + "/" + name + "/docs/" +"003.html", 'r')
i=codecs.open(input_dir + "/" + name + "/docs/" +"004.html", 'r')

soup = BeautifulSoup(f, "html.parser")
soup2 = BeautifulSoup(g, "html.parser")
soup3 = BeautifulSoup(h, "html.parser")
soup4 = BeautifulSoup(i, "html.parser")



doc = soup.get_text()
doc2 = soup2.get_text()
doc3 = soup3.get_text()
doc4 = soup4.get_text()

#print doc
#print(doc)

docs = [doc, doc2, doc3, doc4]


cv = CountVectorizer(stop_words="english")
#print(cv)
# Learns the vocabulary and returns the Document-term matrix
counts = cv.fit_transform(docs)

#print counts
# Vocabulary
#print cv.vocabulary_

# Document-term matrix
dtm = counts.toarray()
print dtm
#print cosine(dtm[0], dtm[1])
#print counts

z = hac.linkage(dtm, method="single", metric="cosine")
plt.clf()
plt.title("HAC " + "single" + " linkage")
hac.dendrogram(z,
           color_threshold=1,
           labels=range(len(docs)),
           show_leaf_counts=True)
#plt.show()

#print hac.leaves_list(z)
#print hac.num_obs_linkage(z)
t = hac.to_tree(z)

test = hac.fcluster(z, 0.7, criterion = "distance")
print test.T
print test.T[0]
print test.T[1]
print test.T[2]
print test.T[3]

#cn = hac.ClusterNode()
#root = ?
#ids = root.pre_order(lambda x: x.id)

#print ids
# dm = pdist(dtm, metric="cosine")
# print 'Distance matrix computed. Length:', len(dm)
# hc = hac.linkage(dm, method="single")
# print 'Hierarchical clustering completed.'
#
# distances = numpy.unique(dm)
#
# #xs = pp_run_num_clusters(hc, distances)
# xs = len(numpy.unique(hac.fcluster(hc, distances, criterion='distance')))
# ys = [y for y in distances]
#
# hac.dendrogram(hc,
#     leaf_label_func=lambda x: dtm.index[x],
#     color_threshold=1)
# f = pl.gcf()
# f.get_axes()[0].axhline(y=1, linestyle='--', color='red')
# f.autofmt_xdate()
# f.set_size_inches(16, 6)
# f.show()
#
# fig = pl.figure()
# ax = fig.add_subplot(111)
# ax.plot(xs, ys)
# ax.axhline(y=1, linestyle='--', color='red')
# fig.set_size_inches(16, 6)
# fig.show()