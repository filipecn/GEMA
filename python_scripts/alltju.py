import urllib2
import re

from gemadb import Problem

for i in range(31):
	html = urllib2.urlopen("http://acm.tju.edu.cn/toj/list%s.html" % str(i+1)).read()
	
	problem_regex = r'p\([0-9]+,[0-9]+,([0-9]+),"(.*?)",[0-9]+,([0-9]+),([0-9]+),"(.*?)"'
	problem_pattern = re.compile(problem_regex, re.UNICODE | re.DOTALL)
	
	for problem_match in problem_pattern.finditer(html):
		data = {
			'name': "%s" % unicode(problem_match.group(2), "ISO-8859-1"),
			'jid': "%s" % problem_match.group(1),
			'judge_id':'7', #id on gemadb
			'url': "http://acm.tju.edu.cn/toj/showp%s.html" % problem_match.group(1),
			'total_users': "%s" % problem_match.group(4),
			'accepted_users': "%d" % int(problem_match.group(3)),
			'total_submissions':-1,
			'accepted_submissions':-1,
			'description':'',
			'spoiler':'',
			'tag_ids':[]
		}
		p = Problem(data)
		if p.save():
			print "Problem %s saved " % data['jid']
		else:
			print "Problem %s NOT saved " % data['jid']
