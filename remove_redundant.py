# logic to effectively cut off redundant elements in an array

k = 0
for i in a:
	if i in a[:k]:
		a.remove(i)
	k = k+1
