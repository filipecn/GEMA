import urllib2
import re

from gemadb import Problem

html = urllib2.urlopen("http://br.spoj.com/problems/main/").read()
main_html = re.search(r'problemas</a><br>(.*?)search', html, re.UNICODE | re.DOTALL)

categories_pattern = re.compile(r'"/problems/(.*?)"', re.UNICODE | re.DOTALL)

for category_match in categories_pattern.finditer(main_html.group(1)):
	print "%s" % category_match.group(1)
	category_url = "http://br.spoj.com/problems/%s/" % category_match.group(1) 

while proximo

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
