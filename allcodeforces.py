import urllib2
import re

for i in range(1):
	contests_html = urllib2.urlopen("http://codeforces.com/contests/page/" + str(i+1)).read()
	skip_regex = r'Contest history'
	contest_regex = r'data-contestId="(\d+)".*?<td>[\n|\r| ]*(.*?)<br/>(.*?)'#nbsp;x(\d+)'

	contest_pattern = re.compile(contest_regex, re.UNICODE | re.DOTALL)
	skip = 2
	for contest_match in contest_pattern.finditer(contests_html):
		if skip > 2 :
			print "%s %s %s" % (contest_match.group(1), contest_match.group(2), contest_match.group(3))
		skip += 1



