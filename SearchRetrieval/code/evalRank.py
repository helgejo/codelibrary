from eval import main
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

__author__ = 'HELGJO'


gt = "../data/qrels.txt"
output = "../output/baseline.out"

def score_file_to_object(score_file):
    obj = {}
    for line in open(score_file, "r"):
        tmp = line.rstrip().split(" ")
        query_id = float(tmp[0])
        score = float(tmp[1])
        obj[query_id] = score
    return obj

def plot_graph_scores(score_files):
    plt.figure()
    legend = []
    for score_file in score_files:
        score_file_obj = score_file_to_object(score_file)
        # sorted_dict = sorted(score_file_obj, key=lambda key: score_file_obj[key])
        x = list(score_file_obj.keys())
        y = list(score_file_obj.values())
        plt.plot(x, y)
        legend.append('y = {0}'.format(score_file))
    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(legend, "Scores", prop=fontP)
    plt.ylabel('Score')
    plt.xlabel('Query ID')
    plt.title('Scores')
    plt.show()

def plot_score_difference(score_file1, score_file2):
    plt.figure()
    legend = []
    score_file1_obj = score_file_to_object(score_file1)
    score_file2_obj = score_file_to_object(score_file2)
    # sorted_dict = sorted(score_file_obj, key=lambda key: score_file_obj[key])
    x = list(score_file1_obj.keys())
    y1 = list(score_file1_obj.values())
    y2 = list(score_file2_obj.values())
    y = list(np.array(y2) - np.array(y1))
    plt.plot(x, y)
    plt.axhline(0, color='black')
    legend.append('y = Comparing {0} against {1}'.format(score_file2, score_file1))
    fontP = FontProperties()
    fontP.set_size('small')
    plt.legend(legend, "title", prop=fontP)
    plt.ylabel('Score difference')
    plt.xlabel('Query ID')
    plt.title('Scores')
    plt.show()

if __name__ == '__main__':
    tobeEval = [gt, output]
    main(tobeEval)
    # score_files = ['../output/baseline_tfidf_score.out', '../output/baseline_bm25_score.out']
    # plot_graph(score_files)
    # plot_score_difference(score_files[0], score_files[1])
    # python eval.py data/qrels.txt output/baseline.out