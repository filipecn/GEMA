import urllib2
import re

last_week = open('lastweek', 'r+').read()

pattern = re.compile(r'(.*?)[ |\t]*?(\d+)', re.UNICODE)

lastweek = {}

for match in pattern.finditer(last_week):
	lastweek.setdefault(str(match.group(1)), []).append(int(match.group(2)))

html = urllib2.urlopen("http://gema.herokuapp.com/ranking").read()

contestant_pattern = re.compile(r'<td>(.*?)</td>.*?<td>(\d+)<', re.UNICODE | re.DOTALL)

score = {}
for contestant_match in contestant_pattern.finditer(html):
	lastweekcount = lastweek.get(str(contestant_match.group(1)), -1)
	if lastweekcount != -1:
		score.setdefault(str(contestant_match.group(1)), []).append(int(contestant_match.group(2)) - int(lastweekcount[0]))

sorted = [x for x in score.iteritems()]
sorted.sort(key=lambda x: x[1])

sorted.reverse()
for key, value in sorted:
	print "%s%s" % (key, value)
