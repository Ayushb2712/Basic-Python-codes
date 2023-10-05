import re

r1=re.compile('[A-Z][a-z]+ \d+, \d+')
for dates in open(fp):
    print(r1.findall(dates))