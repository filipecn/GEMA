import urllib2
import re

from gemadb import Problem

for i in range(3):
	url =  "http://www.spoj.com/problems/classical/sort=0,start=" + str(i*50)
	response = urllib2.urlopen(url)
	html = response.read()

	REGEX = r'<tr class="problemrow">\n<td>(\d+)</td>\n.*\n<a href="/problems/(.*)/.*<b>(.*)</b>.*\n.*\n.*\n.*solutions.">(\d+).*\n.*problem.">([\d.]*)</a>'
	pattern = re.compile(REGEX, re.UNICODE)

	for match in pattern.finditer(html):
		p = Problem()
		p.judge = "spoj"
		p.judge_id = "%s" % match.group(2)
		p.name = "%s" % match.group(3)
		p.url = "http://www.spoj.com/problems/%s/" % match.group(2)
		p.users = "%s" % match.group(4)
		p.accepted = "%s" % match.group(5)
		p.dump()
