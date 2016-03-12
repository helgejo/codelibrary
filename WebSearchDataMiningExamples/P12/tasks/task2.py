# Performing entity linking using DBpedia
# =======================================

# Task
# ------

# - Build a simple dictionary-based entity linker for a sample of entities.
#   * Given an input query, identify all the entity mentions in the query and list candidate entities
#     (i.e., entities that the mention might be referring to) for each mention.
# - Use the "primary" entity names from the `labels_en.nt` file.
# - Homework: extend the dictionary with redirect pages.

# Solution
# --------

from ntriples import *

DATA_DIR = "../data"

# Dictionary of entity name => URI mappings.
# Each entry is an entity name and the corresponding value is a list of entity URIs that have that name.
names = {}


# Create an entity name dictionary.
def create_dictionary(filename=DATA_DIR + "/labels_en.nt"):
    with open(filename) as f:
        for line in f:
            if line[0] != "#":  # skip comment lines
                (s, p, o) = nt_parse_line(line)
                # TODO store `o` as a name variant for entity `s`


# Link entities to a query.
def link_entities(query):
    terms = query.split(" ")
    # TODO Check each query N-gram (N consecutive terms) if it could be linked to an entity.


if __name__ == "__main__":
    create_dictionary()
    query = "parliament of the united kingdom of essex"
    link_entities(query)