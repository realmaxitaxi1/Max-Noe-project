import tkinter as POPPA

class plankTracker:
    def __init__(self):
        self.plankList = list()
        self.BIGDADDY = POPPA.Tk()
        self.BIGDADDY.title('POPPA')
    def makeDaddy(self):
        self.BIGDADDY.mainloop()
    def setup(self):
        readFile = open('storedPlankTimes.txt','r')

        for i in readFile.readlines():
            t,d = i.strip('\n').split(', ')
            self.plankList.append((t, d))
        readFile.close()
    #collect data
    def collectData(self):
        plankTime = input('What plank time did you get?')
        plankDate = input('What was the date?')
        self.plankList.append((plankTime,plankDate))
        print(self.plankList)

    #store data
    def storeData(self):
        openFile = open('storedPlankTimes.txt','w')
        for i,j in self.plankList:
            openFile.write(f'{i}, {j}\n')
        openFile.close()

#2:30, 4/5
#2:45, 4/7

#test comment jaja

if __name__ == '__main__':
    print('hello world')
    track = plankTracker()
    track.makeDaddy()