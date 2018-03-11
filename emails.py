import re

emails = '''
bluewitchproductions@gmail.com
mrSmart@university.edu
kuhn-321-doug@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
