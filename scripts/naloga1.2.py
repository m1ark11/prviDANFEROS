#! /usr/bin/python3

import yaml

with open("../log.txt", "r") as f:
    print(yaml.load(f.read()))