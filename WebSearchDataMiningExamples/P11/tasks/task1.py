# PageRank computation
# ====================

# Task
# ------

#  - Compute the PageRank scores for the given web graph.
#  - We assume that there are no rank sinks (pages with no outlinks).
#  - Use q=0.5

# Solution
# --------

from __future__ import division

# Graph: A->B, A->C, B->C, C->A
# (This is the graph from Task 1 of the exercise 20151103-Lecture-10-PageRank)

# Adjacency matrix of the graph
edges = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0]
]


def pagerank(edges, iterations=3, q=0.15):
    T = len(edges)  # total number of pages
    l = [sum(e) for e in edges]  # number of outgoing pages for each page
    pr = [1/T] * T  # initial PR values
    print "Iterarion 0", pr

    for it in range(iterations):
        pr_new = []  # new pagerank values

        for i in range(T):
            # TODO compute new PR value for page i
            pr_i = 0
            pr_new.append(pr_i)

        pr = pr_new
        print "Iterarion", (it+1), pr

if __name__ == "__main__":
    pagerank(edges, q=0.5)
