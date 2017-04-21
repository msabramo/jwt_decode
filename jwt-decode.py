#!/usr/bin/env python3

import json
import sys

import jwt


if len(sys.argv) >= 2:
    encoded_jwt = sys.argv[1]
else:
    encoded_jwt = sys.stdin.read().rstrip()

# @todo: Add ability verify JWT signature
decoded_jwt = jwt.decode(encoded_jwt, verify=False)
print(json.dumps(decoded_jwt, indent=4))
