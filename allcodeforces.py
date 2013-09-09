import urllib2
import re

from gemadb import Problem

tagsdic = {}
tagsf = open('tagslist', 'r+').read()
tagpattern = re.compile(r'(\d+),(.*?)\n', re.UNICODE | re.DOTALL)

for tagmatch in tagpattern.finditer(tagsf):
	tagsdic[str(tagmatch.group(2)).lower()] = int(tagmatch.group(1))

print tagsdic

for i in range(1):
	html = urllib2.urlopen("http://codeforces.com/contests/page/" + str(i+1)).read()
	
	contests_html = re.search(r'Contest history(.*)', html, re.UNICODE | re.DOTALL)
	contest_regex = r'data-contestId="(\d+)".*?<td>[\n|\r| ]*(.*?)<br/>.*?nbsp;x(\d+)'
	contest_pattern = re.compile(contest_regex, re.UNICODE | re.DOTALL)
	
	for contest_match in contest_pattern.finditer(contests_html.group(1)):
		print "%s %s %s" % (contest_match.group(1), contest_match.group(2), contest_match.group(3))
		
		contest_html = urllib2.urlopen("http://codeforces.com/contest/%s" % (contest_match.group(1))).read()
		problem_regex = r"/contest/"+re.escape(contest_match.group(1))+r'/problem/(.*?)".*?problem.*?>(.*?)<.*?nbsp;(x\d+|.)'
		problem_pattern = re.compile(problem_regex, re.UNICODE | re.DOTALL)
		
		for problem_match in problem_pattern.finditer(contest_html):
			print "%s %s %s" % (problem_match.group(1), problem_match.group(2), problem_match.group(3))
			problem_html = urllib2.urlopen("http://codeforces.com/contest/%s/problem/%s" % (contest_match.group(1),problem_match.group(1))).read()
			
			print "http://codeforces.com/contest/%s/problem/%s" % (contest_match.group(1),problem_match.group(1))
			tags_html = re.search(r"Problem tags(.*?)addTagForm", problem_html, re.UNICODE | re.DOTALL)
			tag_regex = r'<span class="tag-box".*?>.*?([a-z])(.*?)[\r|\n]'
			tag_pattern = re.compile(tag_regex, re.UNICODE | re.DOTALL)
			
			tagslist = []
			for tag_match in tag_pattern.finditer(tags_html.group(1)):
				print "%s%s" % (tag_match.group(1), tag_match.group(2))
				print tagslist.append(tagsdic["%s%s" % (tag_match.group(1), tag_match.group(2))])

			data = {
				'name': "%s" % problem_match.group(2),
				'jid': "%s" % "asd",
				'judge_id':'1', #id on gemadb
				'url': "http://codeforces.com/contest/%s/problem/%s" % (contest_match.group(1),problem_match.group(1)),
				'total_users':contest_match.group(3),
				'accepted_users': problem_match.group(3),
				'total_submissions':-1,
				'accepted_submissions':-1,
				'description':'',
				'spoiler':'',
				'tag_ids':tagslist
			}
			p = Problem(data)
			print p
			#if p.save():
			#	print "Problem %s saved " % data['jid']
			#else:
			#	print "Problem %s NOT saved " % data['jid']
