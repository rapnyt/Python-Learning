list1 = list(range(110,600,20))
list2 = []


for i in range(len(list1)):
	for j in range(len(list1)):
		list2.append([list1[i],list1[j],False])

for i in range(len(list2)):
    print(list2[i])