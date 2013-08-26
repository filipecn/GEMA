import urllib2
import re

for i in range(1):
	html = urllib2.urlopen("http://codeforces.com/contests/page/" + str(i+1)).read()
	
	contests_html = re.search(r'Contest history(.*)', html, re.UNICODE | re.DOTALL)
	contest_regex = r'data-contestId="(\d+)".*?<td>[\n|\r| ]*(.*?)<br/>.*?nbsp;x(\d+)'
	contest_pattern = re.compile(contest_regex, re.UNICODE | re.DOTALL)
	for contest_match in contest_pattern.finditer(contests_html.group(1)):
			print "%s %s %s" % (contest_match.group(1), contest_match.group(2), contest_match.group(3))
			"http://codeforces.com/contest/%s" % (contest_match.group(1))
