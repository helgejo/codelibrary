"""
Evaluation script.

Run:
    python eval.py dir_ground_truth dir_predictions

Where:
    - dir_ground_truth is a directory with a ground truth files (*.clust.xml)
    - dir_predictions is a directory with the predicted clusterings (*.clust.xml)

"""

from __future__ import division

import os
import sys


def eval(dir_gt, dir_predictions):
    """Perform evaluation."""

    sum_pur = 0
    sum_ipur = 0
    names = 0

    print "%-30s\t%s\t%s" % ("Name", "Pur.", "Inv.pur")
    print "-" * 47

    # For each name in the ground truth directory
    for name in os.listdir(dir_gt):
        # parameterize scorer
        cmd = "java -cp weps_scorer.jar es.nlp.uned.weps.evaluation.Scorer " \
              + dir_gt + "/" + name + " " \
              + dir_predictions + "/" + name
        # call scorer and save output line-by-line
        tmp = os.popen(cmd).read().split("\n")
        # extract purity value
        pur = float(tmp[-3][22:])
        sum_pur += pur
        # extract inv. purity value
        ipur = float(tmp[-2][22:])
        sum_ipur += ipur
        names += 1

        print "%-30s\t%.3f\t%.3f" % (name, pur, ipur)

    print "-" * 47
    avg_pur = sum_pur / names
    print "%-15s\t%.3f" % ("Purity:", avg_pur)
    avg_ipur = sum_ipur / names
    print "%-15s\t%.3f" % ("Inv.purity:", avg_ipur)
    print "%-15s\t%.3f" % ("F-measure:", 1 / (0.5 * (1/avg_pur) + 0.5 * (1/avg_ipur)))


def main(argv):

    if not os.path.isfile("weps_scorer.jar"):
        print "ERROR: weps_scorer.jar not found!"
        sys.exit()

    if len(argv) < 2:
        print "Usage: python eval.py dir_ground_truth dir_predictions"
        sys.exit()

    eval(argv[0], argv[1])

if __name__ == '__main__':
    main(sys.argv[1:])
