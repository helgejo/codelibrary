from __future__ import division
from bs4 import BeautifulSoup
import os
from xml.dom import minidom
import codecs
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hac
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
#from sklearn import preprocessing


__author__ = 'HELGE BJORLAND'

#input_dir = "E:/Github/ass2data/training"
#output_dir = "E:/Github/1337zmbi-assignment-2/training.test"

input_dir = "E:/Github/ass2data/test"
output_dir = "E:/Github/1337zmbi-assignment-2/output"

def loadNameFile(name):
    xmldoc = minidom.parse(input_dir + "/" + name + "/" + name + ".xml")
    itemlist = xmldoc.getElementsByTagName("corpus")
    #personName.append(itemlist[0].attributes['search_string'].value)
    itemlist = xmldoc.getElementsByTagName('doc')
    docs = [[s.attributes['rank'].value, 0, ""] for s in itemlist]
    return docs

def getNames(input_dir):
    names = []
    # For each name in the directory
    for name in os.listdir(input_dir):
        names += [name]
    return names

def getText(input_dir, name, docs):
    #dir = input_dir + "/" + person_name + "/docs/"
    for doc in docs:
        # First get the correct file number
        number = str(doc[0])
        #print doc[0]
        if len(number)==1:
            number = "00" + number
        else:
            number = "0" + number

        file_path = input_dir + "/" + name + "/docs/" + number + ".html"
        if not os.path.isfile(file_path):
            #set as discarded if it does not exist
            doc[1] = "discarded"
        else:
            #open each html document
            html = codecs.open(file_path, 'r').read()
            FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
            html = FromRaw(html)
            #parse the document
            soup = BeautifulSoup(html, "html.parser")

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out

            #get only text and add to array
            text = soup.get_text()
            text = tokenize(text)
            #text = tokenize_and_stem(text)
            doc[2] = text
    return docs

def tokenize(text):
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

def vectorize(txtArray):
    #define vectorizer parameters
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=2000000,
                                     min_df=0.2, stop_words='english',
                                     use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

    tfidf_matrix = tfidf_vectorizer.fit_transform(txtArray) #fit the vectorizer
    #terms = tfidf_vectorizer.get_feature_names()
    #print terms
    dist = 1 - cosine_similarity(tfidf_matrix)
    return dist

def tokenize_and_stem(text):
     # adopted from http://brandonrose.org/clustering
     # load nltk's English stopwords as variable called 'stopwords'
    stopwords = nltk.corpus.stopwords.words('english')
    stemmer = SnowballStemmer("english")

    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    #stems = [stemmer.stem(t) for t in filtered_tokens]
    stems = '\n'.join(stemmer.stem(t) for t in filtered_tokens)
    return stems

def clust(docs, met, metr):
    cv = CountVectorizer(stop_words="english")

    txtArray = []
    for doc in docs:
        txtArray.append(doc[2])
    #print txtArray
    # Learns the vocabulary and returns the Document-term matrix
    counts = cv.fit_transform(txtArray)
    # Document-term matrix
    dtm = counts.toarray()

    #dtm = vectorize(txtArray)
    #dtm = preprocessing.scale(dtm)
    z = hac.linkage(dtm, method=met, metric=metr)
    #z = hac.linkage(dtm, method=met)

    return z

def cutTree(z, threshold, crit):
    try:
        z = np.clip(z,0,9999999)
        tree = hac.fcluster(z, threshold, criterion = crit)
        return tree
    except ValueError, e:
        print("cutTree: %s" % str(e))
        tree = hac.fcluster(z, 50, criterion = "euclidean")
        print "negative values in matrix"
        return tree

def addClusters(docs, tree):
    i = 0
    for cluster in tree.T:
        docs[i][1] = cluster
        i+=1

def getClusterList(docs):
    ClusterList = defaultdict(list)
    for doc in docs:
        cluster = doc[1]
        #print "GetClusterList cluster: " + str(cluster)

        if cluster in ClusterList:
            ClusterList[cluster].append(doc[0])
        else:
            ClusterList[cluster] = [doc[0]]
    return ClusterList

def plotdend(z):
    plt.clf()
    plt.title("HAC " + "single" + " linkage")
    hac.dendrogram(z,
               color_threshold=1,
               labels=range(len(z)),
               show_leaf_counts=True)
    plt.show()

def printClusters(clusterlist):
    id = 0
    for cluster, rank in clusterlist.iteritems():
        print "Cluster nr: " + str(cluster)
        for i in rank:
            print "  -> rank: " + i
        id +=1

def writexml(clusterlist, person_name, output_dir):
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + person_name + '">"\n'
    footer = '</clustering>\n'
    out = open(output_dir + "/" + person_name + ".clust.xml", 'w')
    out.write(header)
    #for idx,d in enumerate(docs):
    id = 0
    for cluster, rank in clusterlist.iteritems():
        #print "Cluster nr: " + str(cluster)
        out.write('\t<entity id="' + str(cluster) + '">\n')
        for i in rank:
            #print "rank: " + i
            out.write('\t\t<doc rank="' + i + '" />\n')
        out.write('\t</entity>\n')
        id +=1
    out.write(footer)
    out.close()

def main():
    names = getNames(input_dir)
    #print names
    for name in names:
        print name
        docs = loadNameFile(name)
        docs = getText(input_dir, name, docs)
        z = clust(docs, "single", "cosine")
        tree = cutTree(z, 0.6, "distance")
        addClusters(docs, tree)
        clusterList = getClusterList(docs)
        #printClusters(clusterList)
        writexml(clusterList, name, output_dir)

if __name__ == '__main__':
    main()

#TESTING NOTES

# 0.8
# Purity:         0.564
# Inv.purity:     0.906
# F-measure:      0.695


# 0.4
# Purity:         0.576
# Inv.purity:     0.906
# F-measure:      0.704

#test
#0.1 = 0.666, 0.3 = 0.698, 0.2 = 0.680, 0.4 = 0.727, 0.5 = 0.75, 0.6= 0.756, 0.7 = 0.708

#f = 0.743
        # z = clust(docs, "single", "cosine")
        # tree = cutTree(z, 0.85, "distance")


#f = 0.684
        # z = clust(docs, "single", "euclidean")
        # tree = cutTree(z, 100, "distance")

#f = 0.678
        # z = clust(docs, "single", "euclidean")
        # tree = cutTree(z, 85, "distance")

#eval.py "E:/Github/1337zmbi-assignment-2/training.gt" "E:/Github/1337zmbi-assignment-2/training.test"
#f = 0.675
        # z = clust(docs, "single", "euclidean")
        # tree = cutTree(z, 75, "distance")

#f = 0.651
#z = clust(docs, "single", "euclidean")
#tree = cutTree(z, 30, "maxclust")