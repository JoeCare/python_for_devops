import re

cc_list = """
Ezra Koenig <ekoenig@vpwk.com>,
Rostam Badming <rbadming@vpwk.com>,
Rostar Vadin <rwadwin@vpwk.com>,
Bostam Radlin <bradlin@vpwk.com>,
Chris Tomson <ctomson@vpwk.com>,
Bobbi Baio <bbaio@vpwk.com>,
Bartosz Bartosz <bartosz_bartosz3qp@vpwk.pl>,
Rafal Termos <r.termos97@vpwk.pl>
"""

if 'Rostam' in cc_list:
    print('Match')
else:
    print('None')

if re.search(r'Rostam', cc_list):
    print("Match for", re.search(r'Rostam', cc_list))

search_for_1 = r'[B, R]osta[r, m]'
search_for_mail = r'[A-Za-z0-9._]+@[a-z]+\.+[a-z]{2,3}' 
search_in = re.search(search_for_1, cc_list)
findall_1 = re.findall(search_for_1, cc_list)
findall_mail = re.findall(search_for_mail, cc_list)

if search_in:
    print("Match for:", search_in)

if findall_1:
    print("Found all:", findall_1)

print(findall_mail)

print(re.findall(r'\.\w{2,4}', cc_list))
print(re.findall(r'\w+\@\w+\.\w{2,4}', cc_list))
print(re.findall(r'[A-Za-z0-9._]+\@\w+\.\w{2,4}', cc_list))
print(re.findall(r'([A-Za-z0-9._]+)\@(\w+)\.(\w{2,4})', cc_list))

print(re.search(r'([A-Za-z0-9._]+)\@(\w+)\.(\w{2,4})', cc_list).group(1))

search_group = re.search(r'(?P<nazwa>[A-Za-z0-9._]+)\@(?P<SLD>\w+)\.(?P<PLD>\w{2,4})', cc_list)
findall_groups = re.findall(r'(?P<nazwa>[A-Za-z0-9._]+)\@(?P<SLD>\w+)\.(?P<PLD>\w{2,4})', cc_list)
finditer = re.finditer(r'([A-Za-z0-9._]+)\@(\w+)\.(\w{2,4})', cc_list)

# print(search_group, search_group.group('nazwa'), search_group.group('SLD'), search_group.group('PLD'))
print(findall_groups)
names = [x[0] for x in findall_groups]
print(names)
print(finditer, [next(finditer) for x in finditer])

finditer_groups = re.finditer(r'(?P<nazwa>[A-Za-z0-9._]+)\@(?P<SLD>\w+)\.(?P<PLD>\w{2,4})', cc_list)
print([x.groupdict() for x in finditer_groups])
