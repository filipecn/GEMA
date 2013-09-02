import urllib2
import urllib
import re, utils

#PROBLEM SET VOLUMES


html = urllib2.urlopen("http://icpc.baylor.edu/public/reservations/South-America-Brazil-First-Phase-2013").read()

REGEX = r'<span class="value"><span id="j_idt129:\d+:roexExName.*?>(.*?)<(.*?)Site: '
pattern = re.compile(REGEX, re.UNICODE | re.DOTALL)

for match in pattern.finditer(html):
	print match.group(1)
	uni_pattern = re.compile(r'data-ri=.*?gridcell">(.*?)<', re.UNICODE | re.DOTALL)
	count = {}
	lista = []
	for uni_match in uni_pattern.finditer(match.group(2)):
		lista.append(str(uni_match.group(1)))
		uni = count.get(str(uni_match.group(1)), -1)
		if uni == -1:
			count.setdefault(str(uni_match.group(1)), []).append(0)
	lista2 = [x for x in count.iteritems()]
	for key, value in lista2:
		print "%s %s" % (key, lista.count(str(key)))
	
