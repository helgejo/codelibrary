# PageRank computation
# ====================

# Task
# ------

#  - Compute the PageRank scores for the given web graph.
#  - The graph contains rank sinks (pages with no outlinks) -- deal with them!
#  - Use q=0.15

# Solution
# --------

from __future__ import division

# Graph: 1->2, 1->3, 3->1, 3->2, 3->5, 4->5, 4->6, 5->4, 5->6, 6->4
# (This is the graph from Task 2 of the exercise 20151103-Lecture-10-PageRank)

# Adjacency matrix of the graph
edges = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0],
]


def pagerank(edges, iterations=3, q=0.15):
    T = len(edges)  # total number of pages
    l = [sum(e) for e in edges]  # number of outgoing pages for each page
    pr = [1/T] * T  # initial PR values
    print "Iterarion 0", pr

    for it in range(iterations):
        pr_new = []  # new pagerank values

        for i in range(T):
            # compute new PR value for page i
            pr_i = q / T
            for j in range(T):
                # if page i is pointed by page j
                if edges[j][i] > 0:
                    pr_i += (1-q) * pr[j] / l[j]
            pr_new.append(pr_i)

        pr = pr_new
        print "Iterarion", (it+1), pr, " Sum:", sum(pr)

if __name__ == "__main__":
    pagerank(edges)
