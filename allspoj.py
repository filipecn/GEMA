import urllib2
import re

for i in range(3):
	url =  "http://www.spoj.com/problems/classical/sort=0,start=" + str(i*50)
	response = urllib2.urlopen(url)
	html = response.read()

	REGEX = r'<tr class="problemrow">\n<td>(\d+)</td>\n.*\n<a href="/problems/(.*)/.*<b>(.*)</b>.*\n.*\n.*\n.*solutions.">(\d+).*\n.*problem.">([\d.]*)</a>'
	pattern = re.compile(REGEX, re.UNICODE)

	for match in pattern.finditer(html):
		print "%s %s %s %s %s" % (match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
