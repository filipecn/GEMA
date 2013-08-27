import urllib2
import re

for i in range(5):
	html = urllib2.urlopen("http://acm.tju.edu.cn/toj/list%s.html" % str(i+1)).read()
	
	problem_regex = r'p\([0-9]+,[0-9]+,([0-9]+),"(.*?)",[0-9]+,([0-9]+),([0-9]+),'
	problem_pattern = re.compile(problem_regex, re.UNICODE | re.DOTALL)
	
	for problem_match in problem_pattern.finditer(html):
		print "%s %s %s %s" % (problem_match.group(1), problem_match.group(2), problem_match.group(3), problem_match.group(4))
