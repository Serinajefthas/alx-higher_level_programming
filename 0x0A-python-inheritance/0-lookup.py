#!/usr/bin/python3
def lookup(obj):
    attributelist = dir(obj)
    attributelist = [att for att in attributelist if not att.startswith('_')]
    return attributelist
