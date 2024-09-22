import re

cc_list = """
Ezra Koenig <ekoenig@vpwk.com>,
Rostam Badming <rbadmin@vpwk.com>,
Rostar Wadwin
Bostam Radlin
Chris Tomson <ctomson@vpwk.com>,
Bobbi Baio <bbaio@vpwk.com>
"""
if 'Rostam' in cc_list:
    print('Match')
else:
    print('None')

if re.search(r'Rostam', cc_list):
    print("Match for", re.search(r'Rostam', cc_list))

search_for_1 = r'[B, x]osta[r, m]'
search_in = re.search(search_for_1, cc_list)
findall_in = re.findall(search_for_1, cc_list)

if search_in:
    print("Match for:", search_in)

if findall_in:
    print("Found all:", findall_in)
