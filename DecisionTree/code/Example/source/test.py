from dtree import *
from id3 import *
import sys


def get_file():
    """
    Tries to extract a filename from the command line.  If none is present, it
    prompts the user for a filename and tries to open the file.  If the file 
    exists, it returns it, otherwise it prints an error message and ends
    execution. 
    """
    # Get the name of the data file and load it into 
    if len(sys.argv) < 2:
        # Ask the user for the name of the file
        print "Filename: ", 
        filename = sys.stdin.readline().strip()
    else:
        filename = sys.argv[1]

    try:
        fin = open(filename, "rU")
    except IOError:
        print "Error: The file '%s' was not found on this system." % filename
        sys.exit(0)
    print fin
    return fin

def run_test(fin):
    """
    This function creates a list of exmaples data (used to learn the d-tree)
    and a list of samples (for classification by the d-tree) from the
    designated file.  It then creates the d-tree and uses it to classify the
    samples.  It prints the classification of each record in the samples list
    and returns the d-tree.
    """
    # Create a list of all the lines in the data file
    lines = [line.strip() for line in fin.readlines()]
    print lines
    # Remove the attributes from the list of lines and create a list of
    # the attributes.
    lines.reverse()
    print lines
    attributes = [attr.strip() for attr in lines.pop().split(";")]
    print attributes[-1]
    target_attr = attributes[-1]
    lines.reverse()
    print attributes
    print target_attr

    # Create a list of the data in the data file
    data = []
    for line in lines:
        data.append(dict(zip(attributes,[datum.strip() for datum in line.split(";")])))

    print data
    # Copy the data list into the examples list for testing
    examples = data[:]
    print examples
    # Create the decision tree
    tree = create_decision_tree(data, attributes, target_attr, gain)

    # Classify the records in the examples list
    classification = classify(tree, examples)

    # Print out the classification for each record
    for item in classification:
        print item

    return tree

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object.  
    """
    if type(tree) == dict:
        print "%s%s" % (str, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (str, item)
            print_tree(tree.values()[0][item], str + "\t")
    else:
        print "%s\t->\t%s" % (str, tree)


if __name__ == "__main__":
    fin = get_file()
    print "------------------------\n"
    print "--   Classification   --\n"
    print "------------------------\n"
    print "\n"    
    tree = run_test(fin)
    print "\n"
    print "------------------------\n"
    print "--   Decision Tree    --\n"
    print "------------------------\n"
    print "\n"
    print_tree(tree, "")
    fin.close()
