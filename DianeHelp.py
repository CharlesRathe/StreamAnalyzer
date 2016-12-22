import re

string = 'https:\/\/t.co\/E5FlddUsRm'
regex = r'https:\\/\\/t\.co\\/\w{10}'
r = re.compile(regex)
m = re.search(regex, string)

print(m)