import operator

trains = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5),
	  		('토마스', 4), ('헨리', 7), ('에드워드', 3), ('에밀리', 8),
			('퍼시', 5), ('고든', 13)]
trainDict = {}

for train in trains:
	name = train[0]
	weight = train[1]

	if name in trainDict:
		trainDict[name] += weight
	else:
		trainDict[name] = weight
trainList = sorted(trainDict.items(), key = operator.itemgetter(1), reverse = True)
totalRank, currentRank = 0, 0
for i in range(0, len(trainList)):
	totalRank += 1
	if i > 0 and trainList[i][1] == trainList[i-1][1]:
		pass
	else:
		currentRank = totalRank
	print("%d %s %d" % (currentRank, trainList[i][0], trainList[i][1]))
	
