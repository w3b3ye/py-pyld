# Deserialization using python and pickle
# Script to decode

import pickle
import base64
import sys

data = sys.argv[1]

print(pickle.loads(base64.b64decode(data)))
