from __future__ import division
from bs4 import BeautifulSoup
import os.path
import whoosh.index as index
from whoosh.fields import Schema, TEXT, ID
from os import listdir
from os.path import isfile, join
from whoosh.analysis import *

__author__ = 'HELGE BJORLAND'

index_dir = "../data/index3"
fname = "../data/csiro-corpus/"

def get_Files(dir):
    onlyfiles = [dir + f for f in listdir(dir) if isfile(join(dir,f))]
    return onlyfiles

def init_ix():
    # We create the index schema.
    schema = Schema(id=ID(stored=True), title=TEXT(stored=True), content=TEXT(analyzer=StemmingAnalyzer()))

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    # Create the index directory
    ix = index.create_in(index_dir, schema)
    ix.close()

def parse_file(files):
    queries = []
    temp = ""
    docno = ""
    rd = False
    i = 1
    doccount = 0

    init_ix()

    for file in files:
        print("Parsing file: " + str(i) + ". Total documents have reached: " + str(doccount))
        i += 1

        with open(file, 'r', encoding='utf8', errors='ignore') as f:
            output = f.read()
            #print type(output)
            for line in output.splitlines():
                # FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
                # line = FromRaw(line)

                if( line[:7] == "<DOCNO>"):
                    docno = line[7:24]
                    doccount += 1
                    #print docno

                if(line == "</DOC>"):
                    rd = False

                    soup = BeautifulSoup(temp, 'html.parser')
                    try:
                        title = soup.find('title').text
                        #print title
                    except(AttributeError, KeyError):
                        title = ""

                    text = ""
                    for txt in soup.stripped_strings:
                        text = text + txt + " "
                    queries.append({'id': docno, 'title': title, 'content': text})
                    temp = ""
                    #print text

                if(rd):
                    temp = temp + line

                if(line == "</DOCHDR>"):
                    rd = True

        create_index(index_dir, queries)
        queries = []

def create_index(dir, docs):
    ix = index.open_dir(dir)
    writer = ix.writer()
    #i = 1
    # Add documents to the index.
    for doc in docs:
         #print "Indexing document: " + str(i)
         #i += 1
        # Add document
        # Notes:
        # - Indexed text fields must be passed as unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
         try:
             docID = doc['id'].decode()
         except(UnicodeEncodeError):
             docID = "empty".decode()
         except(AttributeError):
             docID = doc['id']

         try:
             name = doc['title'].decode()
         except(UnicodeEncodeError):
             name = "".decode()
         except(AttributeError):
             name = doc['title']

         try:
             text = doc['content'].decode()
         except(UnicodeEncodeError):
             text = "".decode()
         except(AttributeError):
             text = doc['content']

         writer.add_document(id=docID, title=name, content=text)
    # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit(merge=False)
    ix.close()

def index_creator():
    f = get_Files(fname)
    parse_file(f)

    # re-instantiate the writer
    ix = index.open_dir(index_dir)
    writer = ix.writer()

    # do an optimized commit for the remaining records
    print("Starting the merging and optimizing...")
    writer.commit(optimize=True)
    ix.close()
    print("Done.")

if __name__ == '__main__':
    index_creator()
