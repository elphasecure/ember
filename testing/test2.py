import lief
import ember
import ember.featuresjson as featuresjson
import json

#f = open('tool_versions.exe.parse.formatted')
f = open('libcurl.parse.formatted.new')
lief_data = json.load(f)

fe = featuresjson.PEFeatureExtractor()
features = fe.raw_features(lief_data)
print(json.dumps(features))
