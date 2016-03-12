# Naive NTriples parsing utilities


# Parse NTriple line and return a list with a triple
def nt_parse_line(line):
    # we just strip the " ." ending from each line, i.e., the last 2 characters
    return line.rstrip()[0:-2].split(" ", 2)


# Extract the name part of a URI. From "<http://.../xxx>" it returns "xxx" (part after the last /).
def nt_get_uri_name(uri):
    return uri.split("/")[-1][:-1]


if __name__ == "__main__":
    ntriple = '<http://dbpedia.org/resource/Academy_Award_for_Best_Production_Design> <http://www.w3.org/2000/01/rdf-schema#label> "Academy Award for Best Production Design"@en . '
    print nt_parse_line(ntriple)
