import urllib

class Problem:
    def __init__(self):
        pass
    
    def dump(self):
    	print "%s %s %s %s %s %s" % (self.judge, self.judge_id, self.name, self.url, self.users, self.accepted)

    def save(self):
        problem = { 'judge':self.judge, 'name':self.name, 'judge_id':self.judge_id,
            'judge_users':self.users, 'judge_accepted':self.accepted, 'url':self.url }

        params = urllib.urlencode(problem)
        f = urllib.urlopen("http://base-gema.rhcloud.com/problems", params)

        return f.getcode() == 200
