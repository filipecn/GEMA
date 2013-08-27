import urllib

class Problem:
    def __init__(self):
        pass

    def save(self):
        problem = { 'judge':self.judge, 'name':self.name, 'judge_id':self.judge_id,
            'judge_difficulty':self.difficulty, 'url':self.url }

        params = urllib.urlencode(problem)
        f = urllib.urlopen("http://base-gema.rhcloud.com/problems", params)

        return f.getcode() == 200
