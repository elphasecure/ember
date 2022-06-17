import lief
import ember
import json

lief_data = json.loads('tool_versions.exe.parse.formatted')

fe = ember.featuresjson.PEFeatureExtractor()
features = fe.raw_features(lief_data)
print(json.dumps(features))
