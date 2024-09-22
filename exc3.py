import re

cc_list = """
Ezra Koenig <ekoenig@vpwk.com>,
Rostam Badming <rbadmin@vpwk.com>,
Chris Tomson <ctomson@vpwk.com>,
Bobbi Baio <bbaio@vpwk.com>
"""
if 'Rostam' in cc_list:
    print('Match')
else:
    print('None')

if re.search(r'Rostam', cc_list):
    print(re.search(r'Rostam', cc_list))
