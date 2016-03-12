from __future__ import division
from bs4 import BeautifulSoup
import os.path
import whoosh.index as index
from whoosh.fields import Schema,  TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from os import listdir
from os.path import isfile, join
from xml.dom import minidom
__author__ = 'HELGE BJORLAND'

index_dir = "../data/index2"
fname = "E:/Github/assignment-3/data/csiro-corpus/"
testname = "E:/Github/assignment-3/data/csiro-test/CSIRO001"

def get_Files(dir):
    onlyfiles = [dir + f for f in listdir(dir) if isfile(join(dir,f))]
    return onlyfiles

def parse_file(files):
    queries = []
    temp = ""
    docno = ""
    rd = False
    i = 1
    doccount = 0

    for file in files:
        print("Parsing file: " + str(i) + ". Total documents have reached: " + str(doccount))
        i += 1
        with open(file, 'r') as f:
            #FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
            output = f.read()
            #print type(output)
            for line in output.splitlines():
                FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
                line = FromRaw(line)

                if( line[:7] == "<DOCNO>"):
                    docno = line[7:24]
                    doccount += 1
                    #print docno

                if(line == "</DOC>"):
                    rd = False
                    #content[docno[-1]] = temp

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

    return queries

def init_ix():
    # We create the index schema.
    schema = Schema(id=ID(stored=True), title=TEXT, content=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    # Create the index directory
    ix = index.create_in(index_dir, schema)
    ix.close()

def parse_file2(files):
    queries = []
    temp = ""
    docno = ""
    rd = False
    i = 1
    doccount = 0

    init_ix()

    for file in files:
        print "Parsing file: " + str(i) + ". Total documents have reached: " + str(doccount)
        i += 1

        with open(file, 'r') as f:
            output = f.read()
            #print type(output)
            for line in output.splitlines():
                FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')
                line = FromRaw(line)

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

        create_index2(index_dir, queries)
        queries = []


def create_index2(dir, docs):
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

         try:
             name = doc['title'].decode()
         except(UnicodeEncodeError):
             name = "".decode()

         try:
             text = doc['content'].decode()
         except(UnicodeEncodeError):
             text = "".decode()

         writer.add_document(id=docID, title=name, content=text)
    # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit()
    ix.close()



def create_index_copy():
    # We create the index schema.
    schema = Schema(id=ID(stored=True), content=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    # The writer() method of the Index object returns an IndexWriter object that lets us add documents to the index.
    writer = ix.writer()

    xmldoc = minidom.parse(input_file)

    # Add documents to the index.
    for doc in xmldoc.getElementsByTagName("doc"):
        doc_id = doc.attributes['id'].value
        content = doc.firstChild.data
        print(doc_id)
        # Add document
        # Notes:
        # - Indexed text fields must be passed a unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
        writer.add_document(id=doc_id, content=content)

    # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit()

    ix.close()


def create_index(docs):
    # We create the index schema.
    schema = Schema(id=ID(stored=True), title=TEXT, content=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    # The writer() method of the Index object returns an IndexWriter object that lets us add documents to the index.
    writer = ix.writer()
    i = 1
    # Add documents to the index.
    for doc in docs:
         print("Indexing document: " + str(i))
         i += 1
        # Add document
        # Notes:
        # - Indexed text fields must be passed as unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
         try:
             docID = doc['id'].decode()
         except(UnicodeEncodeError):
             docID = "empty".decode()

         try:
             name = doc['title'].decode()
         except(UnicodeEncodeError):
             name = "".decode()

         try:
             text = doc['content'].decode()
         except(UnicodeEncodeError):
             text = "".decode()

         writer.add_document(id=docID, title=name, content=text)
        #
        #
        #writer.add_document(id=doc['id'], title=doc['title'], content=doc['content'])
        # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit()

    ix.close()

def read_index():
    # Check if index exists in `index_dir`
    if not index.exists_in(index_dir):
        print "Index does not exist"
        return None

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    # Number of documents the index contains
    print reader.doc_count()  # 4


    ix.close()

def parser_test(name):
    content = {}
    temp = ""
    docno = []
    rd = False
    with open(name) as f:
        for line in f:
            if(line == "</DOC>\n"):
                rd = False
                content[docno[-1]] = temp

                soup = BeautifulSoup(temp, 'html.parser')
                try:
                    title = soup.find('title').text
                except(AttributeError, KeyError):
                    title = ""
                #test = [text for text in soup.stripped_strings]
                print title
                #print(soup.prettify())
                #print(soup.get_text())
                temp = ""

            if(rd):
                temp = temp + line

            if( line[:7] == "<DOCNO>"):
                docno.append(line[7:24])
                print line[7:24]

            if(line == "</DOCHDR>\n"):
                rd = True

    #print content["CSIRO001-00304509"]

def index_creator():
    f = get_Files(fname)
    q = parse_file2(f)
    #create_index(q)

# Compute the TFIDF weight of a term
def tfidf(reader, term, count, length):
    tf = count / length
    idf = math.log(reader.doc_count() / reader.doc_frequency(default_field, term))
    return tf*idf

def retrieve_vsm(reader, query):
    # Preprocess the query in a naive way
    qterms = query.split()
    qt = Counter(qterms)

    N = reader.doc_count()  # number of documents
    scores = {}  # retrieval score for each doc
    doc_norm = {}  # score normalizer for each doc
    q_norm = 0  # normalizer for query (could be ignored)

    # for each query term t
    for t, cnt in qt.iteritems():

        # ignore terms not in the index
        if reader.frequency(default_field, t) == 0:
            #print "Query term", t, "ignored"
            continue

        # calculate w_t,q
        wtq = tfidf(reader, t, cnt, len(qterms))
        q_norm += wtq * wtq  # mind that the query normalizer could be ignored

        # for each doc in the posting list of t
        pr = reader.postings(default_field, t)
        while pr.is_active():
            docnum = pr.id()  # docnum is the internal (Whoosh) docID
            if docnum not in scores:
                scores[docnum] = 0
                doc_norm[docnum] = 0
            # term freq of t in doc
            freq = pr.value_as("frequency")
            doclen = reader.doc_field_length(docnum, default_field)
            wtd = tfidf(reader, t, freq, doclen)
            scores[docnum] += wtq * wtd
            doc_norm[docnum] += wtd * wtd
            pr.next()

    # `scores` at this points holds the counter of the cosine formula
    # we need to perform normslization dividing by sqrt(q_norm * doc_norm)
    for docnum, score in scores.iteritems():
        scores[docnum] = scores[docnum] / math.sqrt(q_norm * doc_norm[docnum])

    return scores

def scorer():

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    #TODO
    query = "algebraic language"

    # Retrieve documents using the vector space model
    res = retrieve_vsm(reader, query)

    for docnum in sorted(res, key=res.get, reverse=True)[:10]:
        # Look up our docID (stored field in the index)
        stored = reader.stored_fields(docnum)
        print stored['id'], res[docnum]  # doc id and score

    ix.close()

# Load queries from the query xml file
def load_queries():
    queries = []
    xmldoc = minidom.parse(query_file)
    for query in xmldoc.getElementsByTagName("query"):
        query_id = query.getElementsByTagName("number")[0].firstChild.nodeValue
        text = query.getElementsByTagName("text")[0].firstChild.nodeValue
        queries.append({'id': query_id, 'text': text})

    return queries

def score_to_file():

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    queries = load_queries()

    outfile = open(output_file, "w")

    for query in queries:
        print("Processing query number", query['id'])

        # Retrieve documents using the vector space model
        res = retrieve_vsm(reader, query['text'])

        # Output max 10 results
        for docnum in sorted(res, key=res.get, reverse=True)[:10]:
            # Look up our docID
            stored = reader.stored_fields(docnum)
            # Write `docID Q0 queryID score` into `data/cacm.out`
            outfile.write(query['id']+ " Q0 " + stored['id'] + " " + str(res[docnum]) + "\n")

    outfile.close()
    ix.close()

if __name__ == '__main__':
    #index_creator()
    read_index()


