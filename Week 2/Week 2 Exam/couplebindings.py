def couples(i):
	if i % 2 == 0:
		return i + 1
	else:
		return i - 1
def swappingofcouples(persons):
	cnt = 0
	for x in range(0, len(persons), 2):
		other = couples(persons[x])
		if persons[x + 1] != other:
			exch(other, x + 1, persons)
			cnt += 1
	print(str(persons) + " " + str(cnt))

def exch(p1, p2, persons):
	a = persons.index(p1)
	persons[a], persons[p2] = persons[p2], persons[a]

swappingofcouples([1, 3, 4, 0, 2, 5])
swappingofcouples([3, 2, 0, 1])
# swaps([3,30,50,90,16,91,65,18,61,58])
# swaps( [3,1,5,4,6,2] )
swappingofcouples([1,0])
