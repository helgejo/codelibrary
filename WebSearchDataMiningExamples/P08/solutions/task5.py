# Evaluate retrieval effectiveness
# ================================

# Task
# ------

# - The ground truth is in `data/cacm.rel`. The format is `queryID Q0 docID rel`
#   where `rel` is 1 if the document is relevant and 0 otherwise.
#   * This file contains only the relevant documents so the value will always be 1.
#     This means that everything that is not in this file counts as non-relevant.
# - Write a script that computes P@5, P@10, Average Precision, and Reciprocal Ranks
#   for each query as well as the averages over the entire query set for the output file generated in Task 4.

# Solution
# --------

from __future__ import division

gt_file = "../data/cacm.rel"  # ground truth file with relevance judgments
res_file = "../data/cacm.out"  # retrieval results file, i.e., output of batch retrieval
metrics = ["P5", "P10", "AP", "RR"]


# Load the ground truth file.
# It returns a dictionary with queryID as key and a list of relevant documents as value.
def load_gt(gt_file):
    gt = {}
    for line in open(gt_file, "r"):
        tmp = line.rstrip().split(" ")
        query_id = tmp[0]
        doc_id = tmp[2]
        rel = tmp[3]
        if int(rel) == 1:  # we only consider relevant documents
            if query_id not in gt:
                gt[query_id] = []
            gt[query_id].append(doc_id)
    return gt


# Load the retrieval results file.
# It returns a dictionary with queryID as key and a list of retrieved documents as value.
# We assume that the document in the file are ordered from more relevant the less relevant.
def load_res(run_file):
    res = {}
    for line in open(run_file, "r"):
        tmp = line.rstrip().split(" ")
        query_id = tmp[0]
        doc_id = tmp[2]
        # Note: we do not use the actual retrieval score, but we do assume that
        # the documents are ordered by descreasing order of relevance
        if query_id not in res:
            res[query_id] = []
        res[query_id].append(doc_id)
    return res


# Computes various evaluation metrics for a given query
def evaluate_query(gt, res):
    eval = {}
    for metric in metrics:
        eval[metric] = 0.0

    # We iterate through the returned results
    rel = 0  # relevant documents returned up till now
    for idx, doc_id in enumerate(res):
        rank = idx + 1  # this is just for our own convenience
        if doc_id in gt:  # relevant document retrieved
            rel += 1
            # mind that there might be less than 5 (10) results returned,
            # so we update P5 (P10) continuously
            if rank <= 5:
                eval['P5'] = rel / 5.0
            if rank <= 10:
                eval['P10'] = rel / 10.0
            # If this is the first relevant document encounter
            if rel == 1:
                eval['RR'] = 1.0 / rank
            # For AP we count precision after each relevant retrieved document
            eval['AP'] += rel / rank

    # We need to normalize AP by the total number of relevant documents (in the ground truth)
    eval['AP'] /= len(gt)

    return eval


# Evaluate a results file against a ground truth file.
def evaluate(gt_file, res_file):
    gt = load_gt(gt_file)
    res = load_res(res_file)

    eval = {}  # stores evaluation scores for each query and metric
    eval_avg = {}  # stores averaged evaluation scores for each metric

    # Evaluate each query in the ground truth
    for query_id in sorted(gt):
        # Note that there might not be results in the results file for the given query;
        # in such cases we take the results be an empty list (and we need to make sure we can
        # handle empty lists in `evaluate_query`).
        eval_q = evaluate_query(gt[query_id], res[query_id] if query_id in res else [])
        # Save the results
        eval[query_id] = eval_q
        for metric in eval_q:
            if metric not in eval_avg:
                eval_avg[metric] = 0
            eval_avg[metric] += eval_q[metric]

    # Compute averages
    for metric in eval_avg:
        eval_avg[metric] /= len(gt)

    # Print the results
    line = "-" * (10 + 9 * len(metrics))
    print "{:<10}".format("query_id"), ("{:>8}" * len(metrics)).format(*metrics)
    print line
    # Per-query results
    for query_id in sorted(eval):
        scores = [str(eval[query_id][metric])[:5] for metric in metrics]
        print "{:<10}".format(query_id), ("{:>8}" * len(metrics)).format(*scores)
    # Average results
    print line
    scores = [str(eval_avg[metric])[:5] for metric in metrics]
    print "{:<10}".format("Average"), ("{:>8}" * len(metrics)).format(*scores)


if __name__ == "__main__":
    evaluate(gt_file, res_file)