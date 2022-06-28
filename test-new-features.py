import lief
import ember
import ember.featuresjson as featuresjson
import json
import sys

path = str(sys.argv[1])
#print(f'path is: ', path)
#f = open('libcurl.parse.formatted.new')
f = open(path)
lief_data = json.load(f)

fe = featuresjson.PEFeatureExtractor()
features = fe.raw_features(lief_data)
print(json.dumps(features))
