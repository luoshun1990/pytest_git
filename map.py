#!/usr/bin/env python3

def fn(name):
	name=name[0].upper()+name[1:].lower()
	return name
L1 = ['adma','SFAF','qafSD']
L2 = list(map(fn,L1))
print(L2)

