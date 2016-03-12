__author__ = 'HELGJO'

#tuples are immutable so need to go with different structure
test = [[1,5,"this is an example"],[2,3,"test 2"]]
#print test[0][2]
from collections import defaultdict
a = defaultdict(list)



#a = {}

a["test"] = [1, 4, 6]
a["shit"] = [56,3]

for key in a:
    a[key].append(99)

print a

# a["test"] = a.get("test").append(65)
# print a["test"]
# for cluster, key in a.iteritems():
#     print cluster
#     #print a[cluster]
#     for i in key:
#         print i
# list2 = "10"
# if len(list2)==1:
#     list2 = "00" + list2
# else:
#     list2 = "0" + list2