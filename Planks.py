print("hello word")

readFile = open('storedPlankTimes.txt','r')
plankList = list()

for i in readFile.readlines():
    t,d = i.strip('\n').split(', ')
    plankList.append((t, d))

#collect data
plankTime = input('What plank time did you get?')
plankDate = input('What was the date?')
plankList.append((plankTime,plankDate))
print(plankList)

#store data
openFile = open('storedPlankTimes.txt','w')
for i,j in plankList:
    openFile.write(f'{i}, {j}\n')
openFile.close()

#2:30, 4/5
#2:45, 4/7