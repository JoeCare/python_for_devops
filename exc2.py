# with open("file.txt", "x") as file_x:
#     file_w = file_x.write(str(fib_sequence))

with open("file.txt", "r") as file_r:
    file_r = file_r.read()

print(len(file_r))

text = '''
export STAGE=DEV
export USER_ID=user-124
export CLUSTER_ID=klust-321'''

with open('.envrc', 'w') as envrc:
    envrc.write(text)

import json
import os
import pathlib

path = pathlib.Path('/home/gjwer/docs/py_for_devops/file.txt')
print(path.read_text())
path_w = pathlib.Path('/home/gjwer/docs/py_for_devops/file_w.txt')
path_w.write_text("LOG:DEBUG")
print(path_w.read_text())

policy = {
    "Version": "2017-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": "service-prefix:action-name",
        "Resource": "*",
        "Condition": {
            "DateGreaterThan": {"aws:CurrentTime": "2020-10-10T00:00:00Z"},
            "DateLessThan": {"awsCurrentTime": "2022-12-12T23:59:52Z"}
            }
    }
}

