import urllib2
import re

from gemadb import Problem

for i in range(1):
	html = urllib2.urlopen("http://acm.tju.edu.cn/toj/list%s.html" % str(i+1)).read()
	
	problem_regex = r'p\([0-9]+,[0-9]+,([0-9]+),"(.*?)",[0-9]+,([0-9]+),([0-9]+),'
	problem_pattern = re.compile(problem_regex, re.UNICODE | re.DOTALL)
	
	for problem_match in problem_pattern.finditer(html):
		print "%s %s %s %s" % (problem_match.group(1), problem_match.group(2), problem_match.group(3), problem_match.group(4))
		p = Problem()
		p.judge = "tju"
		p.name = "%s" % problem_match.group(2)
		p.judge_id = "%s" % problem_match.group(1)
		p.judge_difficulty = "0"
