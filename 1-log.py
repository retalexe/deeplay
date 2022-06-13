import re

sid_reg = "sid=/(.+?)\/&"
ip = "10.1.192.38"
sidlist = []

with open('log.txt', encoding='utf-8') as file:

    for line in file:
        if line.find(ip) != -1:
            m = re.search(sid_reg,line)
            sidlist.append(m.group(1))
sidlist.sort()
print('\n'.join(sidlist))
