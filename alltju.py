import urllib2
import re

from gemadb import Problem

for i in range(31):
	html = urllib2.urlopen("http://acm.tju.edu.cn/toj/list%s.html" % str(i+1)).read()
	
	problem_regex = r'p\([0-9]+,[0-9]+,([0-9]+),"(.*?)",[0-9]+,[0-9]+,([0-9]+),"(.*?)"'
	problem_pattern = re.compile(problem_regex, re.UNICODE | re.DOTALL)
	
	for problem_match in problem_pattern.finditer(html):
		p = Problem()
		p.judge = "tju"
		p.judge_id = "%s" % problem_match.group(1)
		p.name = "%s" % problem_match.group(2)
		p.url = "http://acm.tju.edu.cn/toj/showp%s.html" % problem_match.group(1)
		p.users = "%s" % problem_match.group(3)
		p.accepted = "%s" % problem_match.group(4)
		p.dump()
