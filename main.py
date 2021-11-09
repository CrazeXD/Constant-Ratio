import sys
import time

rows = int(input("Enter the number of rows in your table:\n"))
table = []
class getratio(object):
    def __init__(self, rows, table):
        self.rows = rows
        self.table = table
        for i in range(rows):
            self.currentrow = []
            self.x = int(input("Enter the x value:\n"))
            self.y = int(input("Enter the y value:\n"))
            self.currentrow.append(self.x)
            self.currentrow.append(self.y)
            table.append(self.currentrow)
    def findratios(self):
        self.changes = []
        for a in range(self.rows-1):
            if a==0:
                pass
            else:
                self.ychangecurrentrow = table[a][1]/table[a-1][1]
                self.xchangecurrentrow = table[a][0]/table[a-1][0]
                self.currentrow = self.ychangecurrentrow/self.xchangecurrentrow
                self.changes.append(self.currentrow)
        
    def checkratios(self):
        self.nochanges = self.rows-2
        for i in range(self.nochanges):
            for j in range(self.nochanges-i):
                if self.changes[i] == self.changes[j]:
                    pass
                else:
                    print("No common factor detected")
                    time.sleep(10)
                    sys.exit()
        return True

if __name__ == '__main__':
    obj = getratio(rows, table)
    obj.findratios()
    if obj.checkratios:
        print(f"Common Ratio = {obj.changes[0]}")