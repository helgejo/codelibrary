"""
Generate baseline clusterings
"""

import os
from xml.dom import minidom

input_dir = "training"
output_dir = "training.bl"


def baseline(name):
    xmldoc = minidom.parse(input_dir + "/" + name + "/" + name + ".xml")
    itemlist = xmldoc.getElementsByTagName("corpus")
    person_name = itemlist[0].attributes['search_string'].value
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + person_name + '">"\n'
    footer = '</clustering>\n'

    itemlist = xmldoc.getElementsByTagName('doc')
    docs = [s.attributes['rank'].value for s in itemlist]

    # All-in-one
    out_aio = open(output_dir + "/all-in-one/" + name + ".clust.xml", 'w')
    out_aio.write(header)
    out_aio.write('\t<entity id="0">\n')
    for d in docs:
        out_aio.write('\t\t<doc rank="' + d + '" />\n')
    out_aio.write('\t</entity>\n')
    out_aio.write(footer)
    out_aio.close()

    # One-in-one
    out_oio = open(output_dir + "/one-in-one/" + name + ".clust.xml", 'w')
    out_oio.write(header)
    for idx,d in enumerate(docs):
        out_oio.write('\t<entity id="' + str(idx) + '">\n')
        out_oio.write('\t\t<doc rank="' + d + '" />\n')
        out_oio.write('\t</entity>\n')
    out_oio.write(footer)
    out_oio.close()


for name in os.listdir(input_dir):
    baseline(name)
