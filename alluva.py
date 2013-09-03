import urllib2
import urllib
import re

from gemadb import Problem

#PROBLEM SET VOLUMES

url =  "http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=1"
response = urllib2.urlopen(url)
html = response.read()

REGEX = r'<td><a href="(.*)">Volume'
pattern = re.compile(REGEX, re.UNICODE)

for match in pattern.finditer(html):
	url = re.sub(r'&amp;', '&', "%s" % (match.group(1)))
	print url
	problems_html = urllib2.urlopen("http://uva.onlinejudge.org/%s" % url).read()

	PROBLEM_REGEX = 'page=show_problem&amp;problem=(\d+)">(\d+)&nbsp;-&nbsp;(.*?)<.*?>\d+.*?>.*?%<.*?(\d+).*?>.*?sans-serif;">(.*?)%'
	problem_pattern = re.compile(PROBLEM_REGEX, re.UNICODE | re.DOTALL)
	
	for problem_match in problem_pattern.finditer(problems_html):
		p = Problem()
		p.judge = "uva"
		p.judge_id = "%s" % problem_match.group(2)
		p.name = "%s" % problem_match.group(3)
		p.url = "http://uva.onlinejudge.org/%s&page=show_problem&problem=%s" % (url, problem_match.group(1))
		p.users = "%s" % problem_match.group(4)
		p.accepted = "%s" % problem_match.group(5)
		p.dump()
