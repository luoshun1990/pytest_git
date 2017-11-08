#!/usr/bin/env python3

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
	return t[0].lower()

print('by_name:')
L2 = sorted(L,key=by_name)
print(L2)

def by_score(t):
	return t[1]

L3 = sorted(L,key=by_score,reverse=True)

print('by_score')

print(L3)

