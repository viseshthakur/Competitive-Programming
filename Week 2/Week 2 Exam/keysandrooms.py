def keysandrooms(listofkeys):
	l=len(listofkeys)
	list2=[]
	for i in range(l-1):
		list2.extend(listofkeys[i])
		if i+1 in list2:
			flag=True
		else: 
			return False
	if flag is True:
		return True
	else:
		return False

print(keysandrooms([[1],[0,2],[3]]))
print(keysandrooms([[1,3],[3,0,1],[2],[0]]))
print(keysandrooms([[1,2,3],[0],[0],[0]]))
print(keysandrooms( [[1], [0,2,4], [1,3,4], [2], [1,2]] ))
print(keysandrooms( [[1], [2,3], [1,2], [4], [1], [5]] ))
print(keysandrooms([[1], [2], [3], [4], [2]]))
print(keysandrooms( [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]] ))
