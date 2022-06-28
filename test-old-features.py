import lief
import ember
import json
import sys

bs = []
#with open('tool_versions.exe', 'rb') as f:
path = str(sys.argv[1])
with open(path, 'rb') as f:
    b = f.read(1)
    while b:
        bs.append(ord(b))
        b = f.read(1)

fe = ember.features.PEFeatureExtractor()
features = fe.raw_features(bytes(bs))
print(json.dumps(features))
