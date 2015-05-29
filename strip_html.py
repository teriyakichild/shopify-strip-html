from HTMLParser import HTMLParser
import csv
import re
import sys
 
 
if len(sys.argv) < 3:
    print 'Usage: python {0} <file-in> <file-out>'.format(sys.argv[0])
 
filein = sys.argv[1]
fileout = sys.argv[2]
 
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
 
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
 
 
allthethings = []
with open(filein, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        row[2] = re.sub('[ \n]{3,40}', '\n', strip_tags(row[2]))
        allthethings.append(row)
 
with open(fileout, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in allthethings:
        writer.writerow(row)
