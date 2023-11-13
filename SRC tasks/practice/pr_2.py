list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergeList = [ ]
	
while 0 != len(list1) + len(list2):
	if len(list1) == 0:
		for i in list2:
			mergeList.append(i)
			list2.remove(i)
	elif len(list2) == 0:
		for i in list1:
			mergeList.append(i)
			list1.remove(i)
	elif  list1[0] <= list2[0]:
		mergeList.append(list1[0])
		list1.remove(list1[0])
	elif list2[0] <= list1[0]:
		mergeList.append(list2[0])
		list2.remove(list2[0])
		
print(mergeList)	
