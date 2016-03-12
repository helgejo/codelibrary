"""
Evaluation script.

Run:
    python eval.py file_ground_truth file_predictions

Where:
    - file_ground_truth is a file with a ground truth: one class label per line
    - file_predictions is a file with the predictions: one class label per line

@author: Krisztian Balog
"""

from __future__ import division

import sys


def eval(file_gt, file_predictions):
    """Perform evaluation."""

    # Load ground truth file and predictions file
    data_gt = [line.strip() for line in open(file_gt, 'r')]
    data_pred = [line.strip() for line in open(file_predictions, 'r')]

    correct = 0
    incorrect = 0
    total = 0
    for idx, label in enumerate(data_gt):
        # skip empty lines in the ground truth file; this should only happen at the very end of the file
        if len(label) > 0:
            total += 1
            if len(data_pred) > idx:
                if data_pred[idx] in ["<=50K", ">50K"]:
                    if data_pred[idx] == label:
                        correct += 1
                    else:
                        incorrect += 1
                else:
                    print "Error: Unrecognized or missing class label in prediction file (line " + str(idx+1) + ")"
                    return -1
            else:
                print "Error: Number of records mismatch (predictions missing)"
                return -1

    if total == 0:
        print "Error: Empty ground truth file"
        return -1

    print "Accuracy:   ", str(correct / total)[:6]  # max 3 digits
    print "Error rate: ", str(incorrect / total)[:6]  # max 3 digits
    return 0


def print_usage():
    print "Usage: python eval.py file_ground_truth file_predictions"
    sys.exit()


def main(argv):
    if len(argv) < 2:
        print_usage()

    eval(argv[0], argv[1])

if __name__ == '__main__':
    main(sys.argv[1:])
