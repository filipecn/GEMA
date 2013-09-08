import urllib2
import json

from gemadb import Problem

page = urllib2.urlopen("http://uhunt.felix-halim.net/api/p").read()

problems = json.loads(page)

for problem in problems[1000:]:
	data = {
		'name': "%s" % problem[2],
		'jid': "%s" % problem[0],
		'judge_id':'9', #id on gemadb
		'url': "http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=%s" % problem[0],
		'total_users':-1,
		'accepted_users': -1,
		'total_submissions':sum(problem[10:19]),
		'accepted_submissions':problem[18],
		'description':'',
		'spoiler':'',
		'tag_ids':[]
	}
	p = Problem(data)
	if p.save():
		print "Problem %s saved " % data['jid']
	else:
		print "Problem %s NOT saved " % data['jid']

