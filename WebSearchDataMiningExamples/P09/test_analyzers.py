# Testing different analyzers in Whoosh

from whoosh.analysis import *

text = "Hello there, I'm testing, this is a TEST"


def test(analyzer):
    for token in analyzer(text.decode()):  # input needs to be unicode text
        print "'" + token.text + "'",
    print  # newline

# KeywordAnalyzer: Parses whitespace- or comma-separated tokens.
test(KeywordAnalyzer())

# StandardAnalyzer: Composes a RegexTokenizer with a LowercaseFilter and StopFilter.
test(StandardAnalyzer())

# StemmingAnalyzer: Composes a RegexTokenizer with a lower case filter, a stop filter, and a stemming filter.
test(StemmingAnalyzer())

# You can compose a custom analyzer by combining tokenizers and filters together using the | character
# E.g., no lowercasing, stopword removal using a custom stopword list, and then stemming
my_analyzer = RegexTokenizer() | StopFilter(stoplist=["Hello", "TEST"]) | StemFilter()
test(my_analyzer)